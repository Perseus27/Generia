import pathlib
import yaml

import sys
sys.path.append("logic")

from character_renderer import Character_Renderer
from creature_renderer import Creature_Renderer
from class_renderer import Class_Renderer
from table_renderer import Table_Renderer
from perk_renderer import Perk_Renderer
from skill_renderer import Skill_Renderer
from spell_renderer import Spell_Renderer
from autolinker import Autolinker
from bb_renderer import BB_Renderer

_BB_HELPER = BB_Renderer()

def define_env(env):
    project_root = pathlib.Path(env.project_dir)
    docs_root = project_root / "docs"
    autolinker = Autolinker()

    def _read_yaml(rel_path: str):
        full = docs_root / rel_path
        if not full.exists():
            raise FileNotFoundError(f"YAML not found: {rel_path}")
        return yaml.safe_load(full.read_text(encoding="utf-8"))
    
    @env.macro
    def doc_env():
        return {name:getattr(env, name) for name in dir(env) if not name.startswith('_')}
    
    @env.macro
    def test_autolinker(spellname: str):
        return Test_Renderer().autolink_test(spellname)
    
    @env.macro
    def character(path: str):
        yaml_content = _read_yaml(path)
        return Character_Renderer(yaml_content, autolinker).get_output()

    @env.macro
    def creature(path: str):
        yaml_content = _read_yaml(path)
        return Creature_Renderer(yaml_content, autolinker).get_output()
    
    @env.macro
    def class_main(path: str):
        yaml_content = _read_yaml(path)
        return Class_Renderer(yaml_content, autolinker).get_output_main()
    
    @env.macro
    def class_card(path: str):
        yaml_content = _read_yaml(path)
        return Class_Renderer(yaml_content, autolinker).get_output_card()
    
    @env.macro
    def table(path: str):
        yaml_content = _read_yaml(path)
        return Table_Renderer(yaml_content, autolinker).get_output()
    
    @env.macro
    def perks(path: str):
        yaml_content = _read_yaml(path)
        return Perk_Renderer(yaml_content).get_output()
    
    @env.macro
    def skills(path: str):
        yaml_content = _read_yaml(path)
        return Skill_Renderer(yaml_content).get_output()
    
    @env.macro
    def spells(path: str):
        yaml_content = _read_yaml(path)
        return Spell_Renderer(yaml_content).get_output()

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