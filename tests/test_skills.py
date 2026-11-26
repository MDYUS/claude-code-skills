import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import install
from validate import validate
class Tests(unittest.TestCase):
    def test_catalog(self):
        self.assertEqual(validate(), 50)
    def test_install_and_protect(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(install(d, ["debugging"]), 1)
            self.assertTrue((Path(d) / ".claude/skills/debugging/references/checklist.md").is_file())
            with self.assertRaises(FileExistsError):
                install(d, ["debugging"])
    def test_dry_run(self):
        with tempfile.TemporaryDirectory() as d:
            install(d, ["seo"], True)
            self.assertFalse((Path(d) / ".claude").exists())
    def test_invalid(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                install(d, ["../bad"])
