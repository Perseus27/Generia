from bb_renderer import BB_Renderer

from list_builder import List_Builder

class Table_Renderer:

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.autolinker = autolinker
        self.list_builder = List_Builder(autolinker)


    def get_output(self):
        return self.format_to_html()

    def get_price_table(self):
        return self.format_price_table()

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
        
        return result
    
    def format_price_table(self):
        result = f"""
<div class="rendered-table rendered-table-50">
    <h3 id="{self.yaml_input.get("id")}">{self.BB_HELPER.process(self.yaml_input.get("name"))}</h3>
    <table class="price-table rendered-table-inner">
        {self.build_price_table()}
    </table>
</div>
        """
        return result

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
                    result += "<td>"+self.BB_HELPER.process(self.list_builder.build_list(x.get(subitem), to_link="skill", list_type="comma"))+"</td>"
                elif subitem == "tags":
                    result += "<td>"+self.BB_HELPER.process(self.list_builder.build_list(x.get(subitem), to_link="tag", list_type="comma"))+"</td>"
                else:
                    result += "<td>"+self.BB_HELPER.process(str(x.get(subitem)))+"</td>"
            result += "</tr>"
        return result
    

    def build_price_table(self):
        # Build Header
        result = "<tr>"
        result += "<th>Name</th>"
        result += "<th>Price</th>"
        result += "<th>Rarity</th>"
        result += "</tr>"
        for x in self.yaml_input.get("items"):
            result += "<tr>"
            name = x.get("name")
            price = x.get("price", "–")
            rarity = x.get("rarity", "–")
            result += f"<td>{name}</td>"
            result += f"<td>{price}</td>"
            result += f"<td>{rarity}</td>"
            result += "</tr>"
        return result

        
