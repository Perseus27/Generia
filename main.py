import pathlib
import yaml

import sys
sys.path.append("logic")

from test_renderer import Test_Renderer
from character_renderer import Character_Renderer
from creature_renderer import Creature_Renderer
from table_renderer import Table_Renderer
from bb_renderer import BB_Renderer

_BB_HELPER = BB_Renderer()

def define_env(env):
    project_root = pathlib.Path(env.project_dir)
    docs_root = project_root / "docs"

    def _read_yaml(rel_path: str):
        full = docs_root / rel_path
        if not full.exists():
            raise FileNotFoundError(f"YAML not found: {rel_path}")
        return yaml.safe_load(full.read_text(encoding="utf-8"))
    
    @env.macro
    def character(path: str):
        yaml_content = _read_yaml(path)
        return Character_Renderer(yaml_content).get_output()

    @env.macro
    def creature(path: str):
        yaml_content = _read_yaml(path)
        return Creature_Renderer(yaml_content).get_output()        
    
    @env.macro
    def table(path: str):
        yaml_content = _read_yaml(path)
        return Table_Renderer(yaml_content).get_output()

    @env.macro
    def test_block(path: str):
        yaml_content = _read_yaml(path)
        return Test_Renderer(yaml_content).get_output()

    @env.macro
    def bb(text: str):
        return _BB_HELPER.bb_parser.format(_BB_HELPER.bb_postprocess(text))

    @env.macro
    def bb_from_file(path: str):
        p = docs_root / path
        text = p.read_text(encoding='utf-8')
        text = _BB_HELPER.process(text)
        return text


    @env.macro
    def read_text(path: str):
        p = docs_root / path
        return p.read_text(encoding="utf-8")