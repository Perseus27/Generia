from bb_renderer import BB_Renderer

class Class_Renderer:

    BB_HELPER = BB_Renderer()

    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.autolinker = autolinker

    def get_output_main(self):
        return self.BB_HELPER.process(self.format_class_main(self.yaml_input))

    def get_output_card(self):
        return self.BB_HELPER.process(self.format_class_card(self.yaml_input))
    

    def format_class_main(self,c):
        caster_info = c.get("spellcaster_info", False)
        perks = c.get("perks")
        actions = c.get("actions")
        proficiencies = c.get("proficiencies")
        prof_civilian = proficiencies.get("civilian")
        starter_set = c.get("starter_set", [])
        # class header
        result = f"[h1]{c.get('name')}[/h1]"
        # spellcaster info
        if caster_info:
            result += f"[container:class-main-caster-info]{caster_info}[/container]"
        # description
        result += f"[container:class-main-description]{c.get('description')}[/container]"
        # info
        result += f"[container:class-main-info]"
        ## prerequisites
        result += f"[h4]Prerequisites[/h4]"
        result += f"{self.format_list_comma(c.get('prerequisites'), to_link='class')}"
        ## subclasses
        result += f"[h4]Subclasses[/h4]"
        result += f"{self.format_list_comma(c.get('subclasses'), to_link='class')}"
        # close info
        result += "[/container]"
        # body
        result += f"[container:class-main-body]"
        ## perks
        result += f"[container:class-main-perks]"
        result += f"[h3]Perks[/h3]"
        ### combat
        result += f"[container:class-main-sub50]"
        result += f"[h4]Combat[/h4]"
        result += f"{self.build_ul_li_with_autolink(perks.get('combat'), 'perk')}"
        result += "[/container]"
        ### magic
        result += f"[container:class-main-sub50]"
        result += f"[h4]Magic[/h4]"
        result += f"{self.build_ul_li_with_autolink(perks.get('magic'), 'perk')}"
        result += "[/container]"
        ## close perks
        result += "[/container]"
        ## actions
        result += f"[container:class-main-actions]"
        result += f"[h3]Actions[/h3]"
        ### skills
        result += f"[container:class-main-sub50]"
        result += f"[h4]Skills[/h4]"
        result += f"{self.build_ul_li_with_autolink(actions.get('skills'), 'skill')}"
        result += "[/container]"
        ### spells
        result += f"[container:class-main-sub50]"
        result += f"[h4]Spells[/h4]"
        result += f"{self.build_ul_li_with_autolink(actions.get('spells'), 'spell')}"
        result += "[/container]"
        ## close actions
        result += "[/container]"
        ## proficiencies
        result += f"[container:class-main-proficiencies]"
        result += f"[h3]Proficiencies[/h3]"
        ### weapon
        if len(prof_civilian):
            result += f"[container:class-main-sub33]"
        else:
            result += f"[container:class-main-sub50]"
        result += f"[h4]Weapons[/h4]"
        result += f"{self.build_ul_li(proficiencies.get('weapons'))}"
        result += "[/container]"
        ### spellcasting
        if len(prof_civilian):
            result += f"[container:class-main-sub33]"
        else:
            result += f"[container:class-main-sub50]"
        result += f"[h4]Spellcasting[/h4]"
        result += f"{self.build_ul_li(proficiencies.get('magic'))}"
        result += "[/container]"
        ### civilian?
        if len(prof_civilian):
            result += f"[container:class-main-sub33]"
            result += f"[h4]Civilian[/h4]"
            result += f"{self.build_ul_li(proficiencies.get('civilian'))}"
            result += "[/container]"
        ## close proficiencies
        result += "[/container]"
        # close body
        result += "[/container]"
        # STARTER SET ???
        if len(starter_set):
            result += f"[container:class-main-starter]"
            result += f"[h2]Starter Set[/h2]"
            result += f"{self.build_ul_li(starter_set)}"
            result += "[/container]"
        return result
        

    def format_class_card(self, c):
        result = f"[container:class-card]"
        # header
        result += f"[container:class-card-header][h2][url:{c.get('prefix')}/{c.get('id')}]{c.get('name')}[/url][/h2][/container]"
        # body
        result += f"[container:class-card-body]"
        # description
        result += f"[container:class-card-description]{c.get('description')}[/container]"
        # info
        result += f"[container:class-card-info]"
        # prerequisites
        result += f"[h4]Prerequisites[/h4]{self.format_list_comma(c.get('prerequisites'), to_link='class')}"
        # subclasses
        result += f"[h4]Subclasses[/h4]{self.format_list_comma(c.get('subclasses'), to_link='class')}"
        # close info
        result += "[/container]"
        return result
    

    def format_list_br(self, list, to_link=False):
        result = ""
        first = True
        for i in list:
            if first:
                first = False
            else:
                result += "[br]"
            if to_link:
                link = False
                if to_link == "class":
                    link = self.autolinker.link_class(i)
                if link:
                    result += f"[url:{link}]{i}[/url]"
                else:
                    result += i
            else:
                result += i
        return result

    def format_list_comma(self, list, to_link=False):
        result = ""
        first = True
        for i in list:
            if first:
                first = False
            else:
                result += ", "
            if to_link:
                link = False
                if to_link == "class":
                    link = self.autolinker.link_class(i)
                if link:
                    result += f"[url:{link}]{i}[/url]"
                else:
                    result += i
            else:
                result += i
        return result
    
    def build_ul_li(self, input_list):
        list_start = "[ul]"
        list_end = "[/ul]"
        result = list_start
        if len(input_list):
            for x in input_list:
                if len(x):
                    if isinstance(x, list):
                        result += f"[li]{x[0]} [i]({x[1]})[/i][/li]"
                    else:
                        result += f"[li]{x}[/li]"
                else:
                    result += "[li][/li]"        
        else:
            result += "[li][/li]"
        result += list_end
        return result
    

    def build_ul_li_with_autolink(self, input_list, link_type):
        list_start = "[ul]"
        list_end = "[/ul]"
        result = list_start
        if len(input_list):
            for x in input_list:
                if len(x):
                    if isinstance(x, list):
                        to_link = x[0]
                    else:
                        to_link = x
                    if link_type == "perk":
                        link = self.autolinker.link_perk(to_link)
                    elif link_type == "skill":
                        link = self.autolinker.link_skill(to_link)
                    elif link_type == "spell":
                        link = self.autolinker.link_spell(to_link)
                    if isinstance(x, list):
                        if link:
                            result += f"[li][url:{link}]{x[0]}[/url] [i]({x[1]})[/i][/li]"
                        else:
                            result += f"{x[0]} {x[1]}"
                    else:
                        if link:
                            result += f"[li][url:{link}]{x}[/url][/li]"
                        else:
                            result += f"[li]{x}[/li]"
                else:
                    result += "[li][/li]"
        else:
            result += "[li][/li]"
        result += list_end
        return result