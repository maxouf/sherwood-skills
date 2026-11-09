#!/usr/bin/env python3
"""Build ClawHub-format copies of the skills and publish them.

ClawHub wants `version` and `metadata.openclaw` in the frontmatter and refuses a
`license` line (every published skill is MIT-0). The copies are written to a
temporary folder; the repository files stay spec-compliant.

Usage: tools/clawhub.py [--publish] [--version 1.0.1] [--changelog "text"]
Needs: `npx -y clawhub@latest login` done once on the machine.
"""
import argparse, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

def frontmatter(name, desc, version):
    return f"""name: {name}
{desc}
version: {version}
metadata:
  openclaw:
    requires:
      env:
        - APIFY_TOKEN
      anyBins:
        - apify
        - curl
    primaryEnv: APIFY_TOKEN
    envVars:
      - name: APIFY_TOKEN
        required: true
        description: Apify API token (free account at apify.com); the Actors are billed per result on that account.
    homepage: https://github.com/maxouf/sherwood-skills/tree/main/skills/{name}"""

def build(out, version):
    names = []
    for n in sorted(os.listdir(SKILLS)):
        src = os.path.join(SKILLS, n, "SKILL.md")
        if not os.path.exists(src):
            continue
        s = open(src, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", s, re.S)
        fm, body = m.group(1), m.group(2)
        desc = re.search(r"^description:.*?(?=^\w+:|\Z)", fm, re.M | re.S).group(0).rstrip("\n")
        dst = os.path.join(out, n)
        shutil.copytree(os.path.join(SKILLS, n), dst, ignore=shutil.ignore_patterns(".clawhub"))
        open(os.path.join(dst, "SKILL.md"), "w", encoding="utf-8").write("---\n" + frontmatter(n, desc, version) + "\n---\n" + body)
        names.append(n)
    return names

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--publish", action="store_true")
    ap.add_argument("--version", default="1.0.0")
    ap.add_argument("--changelog", default="Task guide; the Sherwood Apify Actor is one of the tools compared. Source github.com/maxouf/sherwood-skills")
    a = ap.parse_args()
    out = tempfile.mkdtemp(prefix="clawhub-")
    names = build(out, a.version)
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    print(f"{len(names)} copies in {out}")
    for n in names:
        cmd = ["npx", "-y", "clawhub@latest", "skill", "publish", os.path.join(out, n), "--slug", n,
               "--version", a.version, "--tags", "latest", "--source-repo", "maxouf/sherwood-skills",
               "--source-commit", sha, "--source-ref", "main", "--source-path", f"skills/{n}", "--changelog", a.changelog]
        if a.publish:
            r = subprocess.run(cmd, capture_output=True, text=True)
            print(n, ":", (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else r.returncode)
        else:
            print(" ".join(cmd))

if __name__ == "__main__":
    main()
