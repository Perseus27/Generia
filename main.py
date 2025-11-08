## `main.py`
import pathlib
import yaml
from html import escape
from markupsafe import Markup
import bbcode as _bb

# Helper: format ability scores as small boxes
_DEF_ABIL_ORDER = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

import re
import bbcode as _bb

_LINE_WRAP_RE = re.compile(r'(?<!\n)\n(?!\n)')  # a single \n not part of \n\n
_CODE_BLOCK_RE = re.compile(r'\[code\](.*?)\[/code\]', re.DOTALL | re.IGNORECASE)
# --- WA preprocessor ---
_H_RE = re.compile(r"\[h(\d)(?:\|([^\]]+))?\](.*?)\[/h\1\]", re.DOTALL)
_URL_COLON_RE = re.compile(r"\[url:([^\]]+)\](.*?)\[/url\]", re.DOTALL)
_SECTION_COLON_RE = re.compile(r"\[section:([^\]]+)\]", re.IGNORECASE)
_CONTAINER_COLON_RE = re.compile(r"\[container:([^\]]+)\]", re.IGNORECASE)

def _bruteforce_section(text: str) -> str:
    text = _SECTION_COLON_RE.sub(lambda m: f"<span class='{_slugify_class(m.group(1))} section'>", text)
    text = text.replace("[/section]", "</span>")
    return text
def _bruteforce_container(text: str) -> str:
    text = _CONTAINER_COLON_RE.sub(lambda m: f"<div class='{_slugify_class(m.group(1))} container'>", text)
    text = text.replace("[/container]", "</div>")
    return text


def _slugify_class(name: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "-", name.strip().lower())

def _protect(code):
    return code.group(0).replace('\n', '\uE000')  # sentinel for restoring

def _normalize_newlines(text: str) -> str:
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # temporarily protect [code]...[/code] blocks
    text = _CODE_BLOCK_RE.sub(_protect, text)
    # collapse single wraps to a space; preserve paragraph breaks (\n\n)
    text = _LINE_WRAP_RE.sub(' ', text)
    # restore code block newlines
    return text.replace('\uE000', '\n')

def _normalize_sections(text: str) -> str:
    # [section:foo] → [section=foo]   (foo → css-safe)
    return _SECTION_COLON_RE.sub(lambda m: f"[section={_slugify_class(m.group(1))}]", text)

def _normalize_containers(text: str) -> str:
    # [container:spell-content] → [container=spell-content]
    return _CONTAINER_COLON_RE.sub(lambda m: f"[container={_slugify_class(m.group(1))}]", text)

def _normalize_all(text: str) -> str:
    #text = _normalize_sections(text)
    #text = _normalize_containers(text)
    text = _normalize_newlines(text)
    return text
    

_SIMPLE_MAP = {
    '[ul]': '<ul>', '[/ul]': '</ul>',
    '[ol]': '<ol>', '[/ol]': '</ol>',
    '[li]': '<li>', '[/li]': '</li>',
    '[table]': "<table class='wa-table'>", '[/table]': '</table>',
    '[tr]': '<tr>', '[/tr]': '</tr>',
    '[th]': '<th>', '[/th]': '</th>',
    '[td]': '<td>', '[/td]': '</td>',
    #'[br]': '<br/>', '[hr]': '<hr/>'
}

def _wa_process_urls(text: str) -> str:
    def _url_sub(m):
        href, label = m.group(1).strip(), m.group(2)
        if not href.startswith(('http://', 'https://', '#', '/')):
            href = '/' + href
        return f"[url={href}]{label}[/url]"
    text = _URL_COLON_RE.sub(_url_sub, text)
    return text

def _wa_preprocess(text: str) -> str:
    
    def _h_sub(m):
        level, anchor, title = m.group(1), (m.group(2) or '').strip(), m.group(3)
        return f"<h{level} id='{anchor}'>{title}</h{level}>" if anchor else f"<h{level}>{title}</h{level}>"
    text = _H_RE.sub(_h_sub, text)

    # Lists, tables, <br/>, <hr/>
    for k, v in _SIMPLE_MAP.items():
        text = text.replace(k, v)
    return text




def define_env(env):
    project_root = pathlib.Path(env.project_dir)
    docs_root = project_root / "docs"

    # --- Statblock helpers ---
    def _read_yaml(rel_path: str):
        full = docs_root / rel_path
        if not full.exists():
            raise FileNotFoundError(f"YAML not found: {rel_path}")
        return yaml.safe_load(full.read_text(encoding="utf-8"))

    @env.macro
    def creature(path: str):
        """Render a creature statblock from a YAML file under docs/.
        Usage in Markdown: {{ creature('data/creatures/goblin.yaml') }}
        """
        d = _read_yaml(path)
        # Safe accessors
        def g(key, default=""):
            return d.get(key, default) or default

        abil = d.get("abilities", {})
        # Preserve order with default ordering
        ordered = [abil.get(k, "-") for k in _DEF_ABIL_ORDER]
        abil_html = "".join(
            f"<div class='ability'><div class='label'>{k}</div><div class='score'>{escape(str(v))}</div></div>"
            for k, v in zip(_DEF_ABIL_ORDER, ordered)
        )

        def entries(section):
            out = []
            for item in d.get(section, []) or []:
                name = escape(str(item.get("name", "")))
                text = escape(str(item.get("text", "")))
                out.append(f"<div class='entry'><strong>{name}.</strong> {text}</div>")
            return "".join(out)

        skills = ", ".join(map(escape, g("skills", [])))

        html = f"""
<div class="statblock" role="note">
  <div class="header">
    <h2>{escape(g('name'))}</h2>
    <div class="meta">{escape(g('size'))} {escape(g('type'))}{', ' + escape(g('alignment')) if g('alignment') else ''}</div>
  </div>
  <hr/>
  <div class="row"><strong>AC</strong> {escape(str(g('ac')))} &nbsp; <strong>HP</strong> {escape(str(g('hp')))} &nbsp; <strong>Speed</strong> {escape(g('speed'))}</div>
  <div class="abilities">{abil_html}</div>
  <hr/>
  {f"<div class='row'><strong>Skills</strong> {skills}</div>" if skills else ''}
  {f"<div class='row'><strong>Senses</strong> {escape(g('senses'))}</div>" if g('senses') else ''}
  {f"<div class='row'><strong>Languages</strong> {escape(g('languages'))}</div>" if g('languages') else ''}
  {f"<div class='row'><strong>Challenge</strong> {escape(str(g('cr')))}</div>" if g('cr') else ''}
  <hr/>
  {f"<div class='section'><h3>Traits</h3>{entries('traits')}</div>" if d.get('traits') else ''}
  {f"<div class='section'><h3>Actions</h3>{entries('actions')}</div>" if d.get('actions') else ''}
  {f"<div class='section'><h3>Reactions</h3>{entries('reactions')}</div>" if d.get('reactions') else ''}
  {f"<div class='section'><h3>Legendary Actions</h3>{entries('legendary_actions')}</div>" if d.get('legendary_actions') else ''}
</div>
"""
        return html

    # --- BBCode helpers ---
    _parser = _bb.Parser(replace_links=False, newline='')
    _parser.add_simple_formatter('br', '<br>', standalone=True)

    @env.macro
    def bb(text: str):
        return _parser.format(_wa_preprocess(text))

    @env.macro
    def bb_from_file(path: str):
        p = docs_root / path
        text = p.read_text(encoding='utf-8')
        text = _normalize_all(text)
        text = _wa_process_urls(text)
        text = _parser.format(text)
        text = _bruteforce_section(text)
        text = _bruteforce_container(text)
        text = _wa_preprocess(text)
        #text = text.replace("<br/>", "")
        return text


    @env.macro
    def read_text(path: str):
        """Return raw text from a file under docs/ (no conversion)."""
        p = docs_root / path
        return p.read_text(encoding="utf-8")