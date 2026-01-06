from bb_renderer import BB_Renderer

from list_builder import List_Builder

class Perk_Renderer:

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.autolinker = autolinker
        self.list_builder = List_Builder(autolinker)


    def get_output(self):
        return self.format_to_html()
    
    def format_to_html(self):
        return self.BB_HELPER.process(self.format_all(self.yaml_input.get("content")))    

    def format_all(self, perk_yaml):
        if not perk_yaml:
            return "–"
        result = ""
        for i in perk_yaml:
            if i.get("is_subheader", False):
                result += self.format_subheader(i)
            else:
                result += self.format_perk(i)
        return result

    def format_subheader(self, subheader):
        return f"[h3|{subheader.get('id')}]{subheader.get('name')}[/h3]"

    def format_perk(self, perk):
        ###
        perk_bb = f"[container:perk][h2|{perk.get('id')}]{perk.get('name')}[/h2]"
        # sp cost
        perk_bb += f"[b][i]SP Cost:[/i][/b] {perk.get('sp-cost')}"
        # requirements
        perk_bb += f"[br][b]Requirements:[/b][br]{perk.get('requirements')}"
        # description
        perk_bb += f"[br][b]Description:[/b][br]{perk.get('description')}"
        # end
        perk_bb += f"[/container]"
        return perk_bb

