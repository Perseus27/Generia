from bb_renderer import BB_Renderer

class Spell_Renderer:

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input):
        self.yaml_input = yaml_input
        self.html_output = ""


    def get_output(self):
        self.format_to_html()
        return self.html_output
    
    def format_to_html(self):
        self.html_output = self.BB_HELPER.process(self.format_all())
    
    def format_all(self):
        y = self.yaml_input
        id_ap = y.get("id_appendix")
        x = y.get("is_exclusive", False)
        if x:
            return f"""
[h1|Tier{id_ap}]Tier {id_ap}[/h1]
{self.format_spells_from_category(y.get('exclusive', False))}
            """        
        result = f"""
[h1|Tier{id_ap}]Tier {id_ap}[/h1]
[h2|Offensive{id_ap}]Offensive[/h2]
{self.format_spells_from_category(y.get('offensive', False))}
[h2|Defensive{id_ap}]Defensive[/h2]
{self.format_spells_from_category(y.get('defensive', False))}
[h2|Utility{id_ap}]Utility[/h2]
{self.format_spells_from_category(y.get('utility', False))}
[h2|Ritual{id_ap}]Ritual[/h2]
{self.format_spells_from_category(y.get('ritual', False))}
        """
        return result
    

    def format_spells_from_category(self, category):
        if not category:
            return "–"
        result = ""
        for i in category:
            if i.get("is_subheader", False):
                result += self.format_subheader(i)
            else:
                result += self.format_spell(i)
        return result

    def format_subheader(self, subheader):
        return f"[h3|{subheader.get('id')}]{subheader.get('name')}[/h3]"

    def format_spell(self, spell):
        ###
        header = f"[container:spell][h2|{spell.get('id')}]{spell.get('name')}[/h2][container:spell-content]"
        ### left column
        columnleft = f"[container:spell-columnleft]{self.format_list_br(spell.get('tags'))}[/container]"
        ### center column
        columncenter = f"[container:spell-columncenter][section:spell-casttype]{self.format_list_br(spell.get('type'))}[/section]"
        # check for material
        material = spell.get("material", False)
        if material:
            columncenter += f"[br][b]Material:[/b][br]{self.format_list_br(material)}"
        # check for cost
        cost = spell.get("cost", False)
        if cost:
            columncenter += f"[br][b]Cost: {self.format_list_comma(cost)}[/b]"
        # check for cast time
        cast_time = spell.get("cast_time", False)
        if cast_time:
            columncenter += f"[br][b]Cast:[/b] {cast_time}"
        columncenter +=  f"[br]{spell.get('description', 'DESCRIPTION ERROR')}"
        columncenter += f"[/container]"
        ### right column
        columnright = f"[container:spell-columnright][container:spell-effect]"
        columnright += f"[b]EFFECT:[/b][br]{spell.get('effect', 'EFFECT ERROR')}"
        effect10 = spell.get("effect10", False)
        if effect10:
            columnright += f"[br][b]EFFECT+10:[/b][br]{effect10}"
        saved = spell.get("saved", False)
        if saved:
            columnright += f"[br][b]SAVED:[/b][br]{saved}"
        saved10 = spell.get("saved10", False)
        if saved10:
            columnright += f"[br][b]SAVED+10:[/b][br]{saved10}"
        columnright += f"[/container][/container]"
        ###
        footer = f"[/container][/container]"
        spell_bb = header + columnleft + columncenter + columnright + footer
        return spell_bb
    

    def format_list_br(self, list):
        result = ""
        first = True
        for i in list:
            if first:
                first = False
            else:
                result += "[br]"
            result += i
        return result
    
    def format_list_comma(self, list):
        result = ""
        first = True
        for i in list:
            if first:
                first = False
            else:
                result += ", "
            result += i
        return result

