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
        is_tier1 = c.get("prefix") == "class1"
        caster_info = c.get("spellcaster_info", False)
        perks = c.get("perks")
        actions = c.get("actions")
        proficiencies = c.get("proficiencies")
        prof_civilian = proficiencies.get("civilian", [])
        starter_set = c.get("starter_set", [])
        # class header
        result = f"[container:class-main]"
        result += f"[h1]{c.get('name')}[/h1]"
        # spellcaster info
        if caster_info:
            result += f"[container:class-main-caster-info]{caster_info}[/container]"
        # info
        result += f"[container:class-main-info]"
        ## description
        result += f"[h2]Description[/h2]"
        result += f"[container:class-main-description]{c.get('description')}[/container]"
        ## prerequisites
        result += f"[container:class-main-subinfo]"
        result += f"[h4]Prerequisites[/h4]"
        result += f"{self.format_list_comma(c.get('prerequisites'), to_link='class')}"
        ## subclasses
        result += f"[h4]Subclasses[/h4]"
        result += f"{self.format_list_comma(c.get('subclasses'), to_link='class')}"
        result += f"[/container]"
        # close info
        result += f"[/container]"
        result += f"[hr]"
        # body
        result += f"[container:class-main-body]"
        ## perks
        result += f"[h2]Perks[/h2]"
        result += f"[container:class-main-body-category]"
        ### combat
        result += f"[container:class-main-sub50]"
        result += f"[h4]Combat[/h4]"
        result += f"{self.build_ul_li_with_autolink(perks.get('combat'), 'perk')}"
        result += "[/container]"
        ### magic
        result += f"[container:class-main-sub50]"
        result += f"[h4]Magic[/h4]"
        result += f"{self.build_ul_li_with_autolink(perks.get('magic'), 'perk')}"
        result += f"[/container]"
        ## close perks
        result += f"[/container]"
        result += f"[hr]"
        ## actions
        result += f"[h2]Actions[/h2]"
        result += f"[container:class-main-body-category]"
        ### skills
        result += f"[container:class-main-sub50]"
        result += f"[h4]Skills[/h4]"
        result += f"{self.build_ul_li_with_autolink(actions.get('skills'), 'skill')}"
        result += f"[/container]"
        ### spells
        result += f"[container:class-main-sub50]"
        result += f"[h4]Spells[/h4]"
        result += f"{self.build_ul_li_with_autolink(actions.get('spells'), 'spell')}"
        result += f"[/container]"
        ## close actions
        result += f"[/container]"
        result += f"[hr]"
        ## proficiencies
        result += f"[h2]Proficiencies[/h2]"
        result += f"[container:class-main-body-category]"
        ### weapon
        if is_tier1:
            result += f"[container:class-main-sub33]"
        else:
            result += f"[container:class-main-sub50]"
        result += f"[h4]Weapons[/h4]"
        result += f"{self.build_ul_li(proficiencies.get('weapons'))}"
        result += f"[/container]"
        ### spellcasting
        if is_tier1:
            result += f"[container:class-main-sub33]"
        else:
            result += f"[container:class-main-sub50]"
        result += f"[h4]Spellcasting[/h4]"
        result += f"{self.build_ul_li(proficiencies.get('magic'))}"
        result += f"[/container]"
        ### civilian?
        if is_tier1:
            result += f"[container:class-main-sub33]"
            result += f"[h4]Civilian[/h4]"
            result += f"{self.build_ul_li(proficiencies.get('civilian'))}"
            result += f"[/container]"
        ## close proficiencies
        result += f"[/container]"
        result += f"[hr]"
        # close body
        result += f"[/container]"
        # STARTER SET ???
        if is_tier1:
            result += f"[hr]"
            result += f"[container:class-main-starter]"
            result += f"[h2]Starter Set[/h2]"
            result += f"{self.build_ul_li(starter_set)}"
            result += f"[/container]"
        # close class-main
        result += f"[/container]"
        return result
        

    def format_class_card(self, c):
        cid = c.get("id")
        result = f"[container:class-card]"
        # header
        result += f"[container:class-card-header][h2|{cid}][url:{c.get('prefix')}/{cid}]{c.get('name')}[/url][/h2][/container]"
        # body
        result += f"[container:class-card-body]"
        # description
        result += f"[container:class-card-description][h4]Description[/h4]{c.get('description')}[/container]"
        # info
        result += f"[container:class-card-info]"
        # prerequisites
        result += f"[h4]Prerequisites[/h4]{self.format_list_comma(c.get('prerequisites'), to_link='class-overview')}"
        # subclasses
        result += f"[h4]Subclasses[/h4]{self.format_list_comma(c.get('subclasses'), to_link='class-overview')}"
        # close info
        result += f"[/container]"
        # close body
        result += f"[/container]"
        #close card
        result += f"[/container]"
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
                elif to_link == "class-overview":
                    link = self.autolinker.link_class(i, overview=True)
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