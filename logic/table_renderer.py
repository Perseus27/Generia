from bb_renderer import BB_Renderer

class Table_Renderer:

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input):
        self.yaml_input = yaml_input;
        self.html_output = ""


    def get_output(self):
        self.format_to_html()
        return self.html_output




    def format_to_html(self):
        result = f"""
<div class="rendered-table">
    <h3 id="{self.yaml_input.get("id")}">{self.BB_HELPER.process(self.yaml_input.get("name"))}</h3>
    <table class="{self.yaml_input.get("table_type")} rendered-table-inner">
        {self.build_header(self.yaml_input)}
        {self.build_content(self.yaml_input)}
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
        

    def build_content(self, input_array):
        result = ""
        for x in input_array.get("items"):
            result += "<tr>"
            for subitem in x:
                result += "<td>"+self.BB_HELPER.process(str(x.get(subitem)))+"</td>"
            result += "</tr>"
        return result