from bb_renderer import BB_Renderer

class Skill_Renderer:

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
        x = y.get("is_exclusive", False)
        if x:
            return f"""
[h2|TierII]Tier II[/h2]
{self.format_skills_from_category(y.get('tier2', False))}
[hr]
[h2|TierIII]Tier III[/h2]
{self.format_skills_from_category(y.get('tier3', False))}
        """
        return f"""
[h2|Offensive]Offensive[/h2]
{self.format_skills_from_category(y.get('offensive', False))}
[hr]
[h2|Utility]Utility[/h2]
{self.format_skills_from_category(y.get('utility', False))}
[hr]
[h2|Reaction]Reaction[/h2]
{self.format_skills_from_category(y.get('reaction', False))}
        """
    

    def format_skills_from_category(self, category):
        if not category:
            return "–"
        result = ""
        for i in category:
            if i.get("is_subheader", False):
                result += self.format_subheader(i)
            else:
                result += self.format_skill(i)
        return result

    def format_subheader(self, subheader):
        return f"[h3|{subheader.get('id')}]{subheader.get('name')}[/h3]"

    def format_skill(self, skill):
        ###
        header = f"[container:skill][h2|{skill.get('id')}]{skill.get('name')}[/h2][container:skill-content]"
        ### left column
        columnleft = f"[container:skill-columnleft]{self.format_list_br(skill.get('tags'))}[/container]"
        ### right column
        columnright = f"[container:skill-columnright]"
        skill_type = skill.get("type", False)
        if skill_type:
            columnright += f"[container:skill-type]{self.format_list_br(skill_type)}[/container]"
        cost = skill.get("cost", False)
        if cost:
            columnright += f"[container:skill-cost][b]Cost:[/b] {self.format_list_comma(cost)}[/container]"
        if skill_type or cost:
            columnright += f"[hr]"
        columnright += f"{skill.get('description', 'DESCRIPTION ERROR')}"
        effect10 = skill.get("effect10", False)
        if effect10:
            columnright += f"[br][b]EFFECT+10:[/b] {effect10}"
        saved = skill.get("saved", False)
        if saved:
            columnright += f"[br][b]SAVED:[/b] {saved}"
        saved10 = skill.get("saved10", False)
        if saved10:
            columnright += f"[br][b]SAVED+10:[/b] {saved10}"
        columnright += f"[/container]"
        ###
        footer = f"[/container][/container]"
        skill_bb = header + columnleft + columnright + footer
        return skill_bb
    

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