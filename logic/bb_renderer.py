import re
import bbcode as bb

class BB_Renderer:
    def __init__(self):
        self.H_RE = re.compile(r"\[h(\d)(?:\|([^\]]+))?\](.*?)\[/h\1\]", re.DOTALL)
        self.URL_COLON_RE = re.compile(r"\[url:([^\]]+)\](.*?)\[/url\]", re.DOTALL)
        self.SECTION_COLON_RE = re.compile(r"\[section:([^\]]+)\]", re.IGNORECASE)
        self.CONTAINER_COLON_RE = re.compile(r"\[container:([^\]]+)\]", re.IGNORECASE)
        self.SIMPLE_MAP = {
            '[ul]': '<ul>', '[/ul]': '</ul>',
            '[ol]': '<ol>', '[/ol]': '</ol>',
            '[li]': '<li>', '[/li]': '</li>',
            '[table]': "<table class='table'>", '[/table]': '</table>',
            '[tr]': '<tr>', '[/tr]': '</tr>',
            '[th]': '<th>', '[/th]': '</th>',
            '[td]': '<td>', '[/td]': '</td>'
        }
        self.SHORT_LINKS = {
            'values'    :   '/generia/rules/basic/values',
            'def'       :   '/generia/rules/basic/definitions',
            'core'      :   '/generia/rules/basic/core-mechanics',
            'actions'   :   '/generia/rules/basic/universal-actions',
            'status'    :   '/generia/rules/combat/status-effects',
            'wounds'    :   '/generia/rules/combat/wounds',
            'dmgtype'   :   '/generia/rules/combat/damage-types',
            'species'   :   '/generia/rules/misc/species',
            'skills1'   :   '/generia/character/skills/skills-tier-i',
            'skills2'   :   '/generia/character/skills/skills-tier-ii',
            'skills3'   :   '/generia/character/skills/skills-tier-iii',
            'skillsX'   :   '/generia/character/skills/skills-exclusive',
            'perksC'    :   '/generia/character/perks/perks-combat',
            'perksXC'   :   '/generia/character/perks/perks-combat-exclusive',
            'perksM'    :   '/generia/character/perks/perks-magic',
            'perksXM'   :   '/generia/character/perks/perks-magic-exclusive',
            'perksD'    :   '/generia/character/perks/perks-divine',
            'acolyteS'  :   '/generia/character/spellcasting-traditions/acolyte/acolyte-spells',
            'alchemistS':   '/generia/character/spellcasting-traditions/alchemist/alchemist-spells',
            'bardS'     :   '/generia/character/spellcasting-traditions/bard/bard-spells',
            'druidS'    :   '/generia/character/spellcasting-traditions/druid/druid-spells',
            'noxS'      :   '/generia/character/spellcasting-traditions/nox/nox-spells',
            'shamanS'   :   '/generia/character/spellcasting-traditions/shaman/shaman-spells',
            'sorcererS' :   '/generia/character/spellcasting-traditions/sorcerer/sorcerer-spells',
            'hermetics' :   '/generia/character/spellcasting-traditions/wizard/wizard-spells-hermetics',
            'kinetics'  :   '/generia/character/spellcasting-traditions/wizard/wizard-spells-kinetics',
            'meteorics' :   '/generia/character/spellcasting-traditions/wizard/wizard-spells-meteorics',
            'thermics'  :   '/generia/character/spellcasting-traditions/wizard/wizard-spells-thermics',
            'wizardX'   :   '/generia/character/spellcasting-traditions/wizard/wizard-spells-exclusive',
            'class1'    :   '/generia/character/classes/tier-i',
            'class2'    :   '/generia/character/classes/tier-ii',
            'class3'    :   '/generia/character/classes/tier-iii',
            'eqtags'    :   '/generia/rules/equipment/equipment-tags',
            'skillsW'   :   '/generia/rules/equipment/weapon-skills',
            'armor'     :   '/generia/equipment/armor',
            'weapons'   :   '/generia/equipment/weapons',
        }
        
        self.bb_parser = bb.Parser(replace_links=False, newline='', url_template="<a href='{href}'>{text}</a>")
        self.bb_parser.add_simple_formatter('br', '<br>', standalone=True)

    def process(self, text: str) -> str:
        text = self.process_urls(text)
        text = self.bb_parser.format(text)
        text = self.bruteforce_container(text)
        text = self.bruteforce_section(text)
        text = self.bb_postprocess(text)
        return text

    def bruteforce_section(self, text: str) -> str:
        text = self.SECTION_COLON_RE.sub(lambda m: f"<span class='{m.group(1)} section'>", text)
        text = text.replace("[/section]", "</span>")
        return text
    def bruteforce_container(self, text: str) -> str:
        text = self.CONTAINER_COLON_RE.sub(lambda m: f"<div class='{m.group(1)} container'>", text)
        text = text.replace("[/container]", "</div>")
        return text
    
    def process_urls(self, text: str) -> str:
        def url_sub(m):
            href, label = m.group(1).strip(), m.group(2)
            for k, v in self.SHORT_LINKS.items():
                if href.startswith(k):
                    href = href.replace(k, v, 1)
            return f"[url={href}]{label}[/url]"
        text = self.URL_COLON_RE.sub(url_sub, text)
        return text
    

    def bb_postprocess(self, text: str) -> str:
    
        def h_sub(m):
            level, anchor, title = m.group(1), (m.group(2) or '').strip(), m.group(3)
            return f"<h{level} id='{anchor}'>{title}</h{level}>" if anchor else f"<h{level}>{title}</h{level}>"
        text = self.H_RE.sub(h_sub, text)

        # Lists, tables, <br/>, <hr/>
        for k, v in self.SIMPLE_MAP.items():
            text = text.replace(k, v)
        return text
