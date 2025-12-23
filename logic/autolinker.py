import yaml
from pathlib import Path

class Autolinker:

    DATA_DIR = Path.cwd() / "docs" / "data"
    CLASS_DIR = DATA_DIR / "classes"
    PERK_DIR = DATA_DIR / "perks"
    SKILL_DIR = DATA_DIR / "skills"
    SPELL_DIR = DATA_DIR / "spells"
    TAG_DIR = DATA_DIR / "tags"

    def __init__(self):
        self.class_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.CLASS_DIR.rglob("*.yaml"))
        ]
        self.perk_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.PERK_DIR.rglob("*.yaml"))
        ]
        self.skill_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.SKILL_DIR.rglob("*.yaml"))
        ]
        self.spell_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.SPELL_DIR.rglob("*.yaml"))
        ]
        self.tag_yamls = [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(self.TAG_DIR.rglob("*.yaml"))
        ]

    def link_class(self, x, overview=False):
        for c in self.class_yamls:
            if c.get("name") == x or x in c.get("alias", []):
                if overview:
                    return f"#{c.get('id')}"
                else:
                    return f"{c.get('prefix')}/{c.get('id')}"
        return False
    
    def link_perk(self, x):
        for y in self.perk_yamls:
            prefix = y.get("prefix")
            for p in self.get_all_perks_from_file(y):
                name = p.get("name")
                if name == x or x in p.get("alias", []):
                    return f"{prefix}#{p.get('id', name)}"
        return False

    def link_skill(self, x):
        for y in self.skill_yamls:
            prefix = y.get("prefix")
            for subcat in self.get_all_skills_from_file(y):
                for i in subcat:
                    name = i.get("name")
                    if name == x or x in i.get("alias", []):
                        return f"{prefix}#{i.get('id', name)}"
        return False

    def link_spell(self, x):
        for y in self.spell_yamls:
            prefix = y.get("prefix")
            for subcat in self.get_all_spells_from_file(y):
                for i in subcat:
                    name = i.get("name")
                    if name == x or x in i.get("alias", []):
                        return f"{prefix}#{i.get('id', name)}"
        return False
    
    def link_tag(self, x):
        for y in self.tag_yamls:
            prefix = y.get("prefix")
            for p in self.get_all_tags_from_file(y):
                name = p.get("name")
                if name == x or x in p.get("alias", []):
                    return f"{prefix}#{p.get('id', name)}"
        return False
    



    
    def get_all_perks_from_file(self, f):
        return f.get("content", [])
    
    def get_all_skills_from_file(self, f):
        all = [f.get("offensive", False), 
                  f.get("utility", False), 
                  f.get("reaction", False),
                  f.get("tier2", False),
                  f.get("tier3", False),
                  f.get("content", False)]
        result = [x for x in all if x]
        return result
    
    def get_all_spells_from_file(self, f):
        all = [f.get("offensive", False), 
                  f.get("defensive", False), 
                  f.get("utility", False), 
                  f.get("ritual", False),
                  f.get("exclusive", False)]
        result = [x for x in all if x]
        return result
    
    def get_all_tags_from_file(self, f):
        return f.get("content", [])
    
