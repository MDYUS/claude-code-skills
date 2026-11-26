import argparse
import shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def install(project, names=None, dry_run=False):
    available = {p.name: p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file()}
    selected = list(dict.fromkeys(names or sorted(available)))
    if any(n not in available for n in selected):
        raise ValueError("Unknown skill")
    dest = Path(project).resolve() / ".claude" / "skills"
    plan = [(available[n], dest / n) for n in selected]
    if any(p.exists() or p.is_symlink() for _, p in plan):
        raise FileExistsError("Existing skill directory: no changes made")
    for src, dst in plan:
        print(("Would install " if dry_run else "Installing ") + str(dst))
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst)
    return len(plan)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--project", required=True)
    p.add_argument("--skills", nargs="+")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    try:
        install(args.project, args.skills, args.dry_run)
    except (OSError, ValueError) as e:
        p.exit(1, str(e) + "\n")
