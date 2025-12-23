from bb_renderer import BB_Renderer

class Table_Renderer:

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.html_output = ""
        self.autolinker = autolinker


    def get_output(self):
        self.format_to_html()
        return self.html_output




    def format_to_html(self):
        include_fields = []
        for x in self.yaml_input.get("headers"):
            include_fields.append(x.lower().replace(".", ""))
        result = f"""
<div class="rendered-table">
    <h3 id="{self.yaml_input.get("id")}">{self.BB_HELPER.process(self.yaml_input.get("name"))}</h3>
    <table class="{self.yaml_input.get("table_type")} rendered-table-inner">
        {self.build_header(self.yaml_input)}
        {self.build_content(self.yaml_input, include_fields)}
    </table>
</div>
        """
        
        self.html_output = result

    def build_header(self, input_array):
        result = "<tr>"
        for x in input_array.get("headers"):
            result += "<th>"+self.BB_HELPER.process(str(x))+"</th>"
        result += "</tr>"
        return result
        

    def build_content(self, input_array, include_fields):
        result = ""
        for x in input_array.get("items"):
            result += "<tr>"
            for subitem in x:
                if subitem not in include_fields:
                    continue
                if subitem == "damage":
                    result += "<td>"+self.BB_HELPER.process(f"[section:clr-roll]{str(x.get(subitem))}[/section]")+"</td>"
                elif subitem == "skill":
                    result += "<td>"+self.BB_HELPER.process(self.format_list_comma(x.get(subitem), to_link="skill"))+"</td>"
                elif subitem == "tags":
                    result += "<td>"+self.BB_HELPER.process(self.format_list_comma(x.get(subitem), to_link="tag"))+"</td>"
                else:
                    result += "<td>"+self.BB_HELPER.process(str(x.get(subitem)))+"</td>"
            result += "</tr>"
        return result

    def format_list_comma(self, input_list, to_link=False):
        result = ""
        first = True
        if not isinstance(input_list, list):
            input_list = [input_list]
        for i in input_list:
            list_flag = False
            if first:
                first = False
            else:
                result += ", "
            if isinstance(i, list):
                first_part = i[0]
                second_part = i[1]
                i = first_part
                list_flag = True
            if to_link:
                link = False
                if to_link == "tag":
                    link = self.autolinker.link_tag(i)
                elif to_link == "skill":
                    link = self.autolinker.link_skill(i)
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
        return result