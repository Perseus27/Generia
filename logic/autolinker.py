import yaml
from pathlib import Path

class Autolinker:

    DATA_DIR = Path.cwd() / "docs" / "data"
    PERK_DIR = DATA_DIR / "perks"
    SKILL_DIR = DATA_DIR / "skills"
    SPELL_DIR = DATA_DIR / "spells"

    def __init__(self):
        self.spell_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.SPELL_DIR.rglob("*.yaml"))
        ]

    def link_spells(self, x):
        for y in self.spell_yamls:
            prefix = y.get("prefix")
            for subcat in self.get_all_spells_from_file(y):
                for i in subcat:
                    if i.get("name") == x:
                        return f"{prefix}#{i.get("id")}"
        return "SpellLinkError"
    
    def get_all_spells_from_file(self, f):
        all = [f.get("offensive", False), 
                  f.get("defensive", False), 
                  f.get("utility", False), 
                  f.get("ritual", False),
                  f.get("exclusive", False)]
        result = [x for x in all if x]
        return result