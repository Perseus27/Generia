import yaml
from pathlib import Path

class Autolinker:

    DATA_DIR = Path.cwd() / "docs" / "data"
    PERK_DIR = DATA_DIR / "perks"
    SKILL_DIR = DATA_DIR / "skills"
    SPELL_DIR = DATA_DIR / "spells"

    def __init__(self):
        self.perk_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.PERK_DIR.rglob("*.yaml"))
        ]
        self.spell_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.SPELL_DIR.rglob("*.yaml"))
        ]
    
    def link_perk(self, x):
        for y in self.perk_yamls:
            prefix = y.get("prefix")
            for p in self.get_all_perks_from_file(y):
                if p.get("name") == x or x in p.get("alias", []):
                    return f"{prefix}#{p.get('id')}"
        return False

    def link_spell(self, x):
        for y in self.spell_yamls:
            prefix = y.get("prefix")
            for subcat in self.get_all_spells_from_file(y):
                for i in subcat:
                    if i.get("name") == x or x in i.get("alias", []):
                        return f"{prefix}#{i.get('id')}"
        return False
    
    def get_all_perks_from_file(self, f):
        return f.get("content", [])
    
    def get_all_spells_from_file(self, f):
        all = [f.get("offensive", False), 
                  f.get("defensive", False), 
                  f.get("utility", False), 
                  f.get("ritual", False),
                  f.get("exclusive", False)]
        result = [x for x in all if x]
        return result
    
