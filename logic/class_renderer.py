from bb_renderer import BB_Renderer

class Class_Renderer:

    BB_HELPER = BB_Renderer()

    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.autolinker = autolinker

    def get_output_card(self):
        return self.BB_HELPER.process(self.format_class_card(self.yaml_input))



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
        result += f"[h4]Prerequisites[/h4]{self.format_list_comma(c.get('prerequisites'), to_link="class")}"
        # subclasses
        result += f"[h4]Subclasses[/h4]{self.format_list_comma(c.get('subclasses'), to_link="class")}"
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