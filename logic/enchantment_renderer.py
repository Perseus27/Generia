from bb_renderer import BB_Renderer

from list_builder import List_Builder

class Enchantment_Renderer:

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.autolinker = autolinker
        self.list_builder = List_Builder(autolinker)


    def get_output(self):
        return self.format_to_html()
    
    def format_to_html(self):
        return self.BB_HELPER.process(self.format_all(self.yaml_input.get("content")))    

    def format_all(self, ench_list):
        result = ""
        for i in ench_list:
            result += self.format_ench(i)
        return result

    def format_ench(self, ench):
        ###
        ench_bb = f"[container:enchantment][h2|{ench.get('id')}]{ench.get('name')}[/h2]"
        # medium
        ench_bb += f"[b]Medium:[/b][br][section:clr-enchantment-medium]{self.list_builder.build_list(ench.get('medium'), list_type='comma')}[/section]"
        # description
        ench_bb += f"[br][b]Description:[/b][br]{ench.get('description')}"
        # attunement?
        att = ench.get('attunement', False)
        if att:
            ench_bb += f"[br][b]Attunement:[/b] [section:clr-malus]{att}[/section]"
        # end
        ench_bb += f"[/container]"
        return ench_bb

