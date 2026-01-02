class List_Builder:
    def __init__(self, autolinker):
        self.autolinker = autolinker


    def build_list(self, input_list, to_link = False, list_type = "ul"): # br, comma, li, commabr
        result = ""
        if list_type == "ul":
            result += "[ul]"
        first = True
        for i in input_list:
            list_flag = False
            if list_type == "ul":
                result += "[li]"
            else:
                if first:
                    first = False
                else:
                    if list_type in ["comma", "commabr"]:
                        result += ", "
                    if list_type in ["br", "commabr"]:
                        result += "[br]"
            if isinstance(i, list):
                first_part = i[0]
                second_part = i[1]
                i = first_part
                list_flag = True
            if to_link:
                link = self.get_link(i, to_link)
                if link:
                    if list_flag:
                        result += f"[url:{link}]{first_part}[/url] {second_part}"
                    else:
                        result += f"[url:{link}]{i}[/url]"
                else:
                    if list_flag:
                        result += f"{first_part} {second_part}"
                    else:
                        result += i                    
            else:
                result += i
            if list_type == "ul":
                result += "[/li]"
        if list_type == "ul":
            result += "[/ul]"
        return result
    


    def get_link(self, s, to_link):
        link = False
        if to_link == "class":
            link = self.autolinker.link_class(s)
        elif to_link == "perk":
            link = self.autolinker.link_perk(s)
        elif to_link == "skill":
            link = self.autolinker.link_skill(s)
        elif to_link == "spell":
            link = self.autolinker.link_spell(s)
        elif to_link == "tag":
            link = self.autolinker.link_tag(s)
        return link