from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
def validate():
    names = []
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        name = p.parent.name
        s = p.read_text(encoding="utf-8")
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
        assert s.startswith("---\nname: " + name + "\n")
        assert "description:" in s.split("---", 2)[1]
        if name == "website-forge":
            assert "## 5. Execute verification" in s
            for ref in ("design.md", "implementation.md", "verification.md"):
                assert (p.parent / "references" / ref).is_file()
                assert f"references/{ref}" in s
        else:
            assert "## Verification" in s
            assert (p.parent / "references/checklist.md").is_file()
        assert (ROOT / "site/skills" / name / "index.html").is_file()
        assert f"skills/{name}/SKILL.md" in (ROOT / "SKILLS_GUIDE.md").read_text()
        names.append(name)
    assert len(names) == 51
    print(f"Validated {len(names)} skills")
    return len(names)
if __name__ == "__main__":
    validate()
