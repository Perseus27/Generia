import yaml
from pathlib import Path

class Autolinker:

    DATA_DIR = Path.cwd() / "docs" / "data" / "util"
    PERK_PATH = DATA_DIR / "perk-links.yaml"
    SKILL_PATH = DATA_DIR / "skill-links.yaml"
    SPELL_PATH = DATA_DIR / "spell-links.yaml"

    def __init__(self):
        self.perk_yaml = yaml.safe_load(self.PERK_PATH.read_text())
        self.skill_yaml = yaml.safe_load(self.SKILL_PATH.read_text())
        self.spell_yaml = yaml.safe_load(self.SPELL_PATH.read_text())

    def link_spells(self, x):
        return