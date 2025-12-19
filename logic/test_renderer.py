from bb_renderer import BB_Renderer
import bbcode as _bb
import pathlib

class Test_Renderer:
    
    ATTRIBUTE_ORDER = ["CON", "STR", "DEX", "INT", "WIL", "PER"]
    VALUE_ORDER = ["EN", "MP", "MPR", "WL", "WT", "TN", "MS"]
    ARMOR_ORDER = ["head", "torso", "arms", "legs", "md", "enc"]

    BB_HELPER = BB_Renderer()
    
    def __init__(self):
       pass


    def get_cwd(self):
        return pathlib.Path.cwd() / "docs" / "data" / "test" / "test.yaml"