from bb_renderer import BB_Renderer

class Character_Renderer:
    
    ATTRIBUTE_ORDER = ["CON", "STR", "DEX", "INT", "WIL", "PER"]
    VALUE_ORDER = ["EN", "MP", "MPR", "WL", "WT", "TN", "MS"]
    ARMOR_ORDER = ["head", "torso", "arms", "legs", "md", "enc"]
    DEFAULT_HITZONES = ["Head", "Torso", "Arms", "Legs"]

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input
        self.html_output = ""
        self.autolinker = autolinker


    def get_output(self):
        self.format_to_html()
        return self.html_output

    def format_attributes(self):
        all_attributes = self.yaml_input.get("attributes", {})
        a = [all_attributes.get(x) for x in self.ATTRIBUTE_ORDER]
        attr_bb = f"""
[table][tr][td][b]CON[/b][/td]
[td]{a[0][0]} [{a[0][1]}][/td]
[/tr]
[tr][td][b]STR[/b][/td]
[td]{a[1][0]} [{a[1][1]}][/td]
[/tr]
[tr][td][b]DEX[/b][/td]
[td]{a[2][0]} [{a[2][1]}][/td]
[/tr]
[tr][td][b]INT[/b][/td]
[td]{a[3][0]} [{a[3][1]}][/td]
[/tr]
[tr][td][b]WIL[/b][/td]
[td]{a[4][0]} [{a[4][1]}][/td]
[/tr]
[tr][td][b]PER[/b][/td]
[td]{a[5][0]} [{a[5][1]}][/td]
[/tr][/table]
        """
        return self.BB_HELPER.process(attr_bb)
    
    def format_values(self):
        all_values = self.yaml_input.get("values", {})
        a = [all_values.get(x) for x in self.VALUE_ORDER]
        values_bb = f"""
[table][tr][td][b]EN[/b][/td]
[td]{a[0]}[/td]
[/tr]
[tr][td][b]MP|R[/b][/td]
[td]{a[1]}|{a[2]}[/td]
[/tr]
[tr][td][b]WL[/b][/td]
[td]{a[3]}[/td]
[/tr]
[tr][td][b]WT[/b][/td]
[td]{a[4]}[/td]
[/tr]
[tr][td][b]TN[/b][/td]
[td]{a[5]}[/td]
[/tr]
[tr][td][b]MS[/b][/td]
[td]{a[6]}[/td]
[/tr][/table]
        """
        return self.BB_HELPER.process(values_bb)
    
    def format_armor(self):
        hit_zones = self.yaml_input.get("custom-hitzones", self.DEFAULT_HITZONES)
        all_armor = self.yaml_input.get("armor", {})
        a = [all_armor.get(x) for x in self.ARMOR_ORDER]
        armor_bb = f"""
[table][tr][td][b]{hit_zones[0]}[/b][/td]
[td]{a[0]}[/td]
[/tr]
[tr][td][b]{hit_zones[1]}[/b][/td]
[td]{a[1]}[/td]
[/tr]
[tr][td][b]{hit_zones[2]}[/b][/td]
[td]{a[2]}[/td]
[/tr]
[tr][td][b]{hit_zones[3]}[/b][/td]
[td]{a[3]}[/td]
[/tr]
[tr][td][b]MD[/b][/td]
[td]{a[4]}[/td]
[/tr]
[tr][td][b]Enc.[/b][/td]
[td]{a[5]}[/td]
[/tr][/table]
        """
        return self.BB_HELPER.process(armor_bb)
    
    def format_info(self):
        i = self.yaml_input.get("info", {})
        species = i.get("species")
        size = i.get("size")
        class_list = self.format_list_comma(i.get("classes"), to_link="class")
        tag_list = self.format_list_comma(i.get("tags"), to_link="tag")
        info_bb = f"""
[table][tr][td][b]Species:[/b][/td]
[td][url:{self.autolinker.link_perk(species)}]{species}[/url][/td]
[/tr]
[tr][td][b]Level:[/b][/td]
[td]{i.get("level")}[/td]
[/tr]
[tr][td][b]Size:[/b][/td]
[td][url:{self.autolinker.link_tag(size)}]{size}[/url][/td]
[/tr]
[/table]
[container:chara-info-container]
[br]
[b]Classes:[/b]
[br]{class_list}
[br]
[br][b]Tags:[/b]
[br]{tag_list}
[/container]
        """
        return self.BB_HELPER.process(info_bb)
    
    def format_notes(self):
        return self.BB_HELPER.process(self.yaml_input.get("notes"))

    def format_items(self):
        all_items = self.yaml_input.get("inventory")
        weapons = self.build_list_of_items_of_category(all_items.get("weapons"))
        armor = self.build_list_of_items_of_category(all_items.get("armor"))
        misc = self.build_list_of_items_of_category(all_items.get("misc"))
        items_formatted = {"weapons" : self.BB_HELPER.process(weapons), "armor" : self.BB_HELPER.process(armor), "misc" : self.BB_HELPER.process(misc)}
        return items_formatted

    def format_proficiencies(self):
        all_proficiencies = self.yaml_input.get("proficiencies")
        magic = self.build_list_from_list(all_proficiencies.get("magic"))
        weapons = self.build_list_from_list(all_proficiencies.get("weapons"))
        civilian = self.build_list_from_list(all_proficiencies.get("civilian"))
        proficiencies_formatted = {"magic" : self.BB_HELPER.process(magic), "weapons" : self.BB_HELPER.process(weapons), "civilian" : self.BB_HELPER.process(civilian)}
        return proficiencies_formatted
    
    def format_actions(self):
        all_actions = self.yaml_input.get("actions")
        skills = self.build_list_with_autolink(all_actions.get("skills"), "skill")
        spells = self.build_list_with_autolink(all_actions.get("spells"), "spell")
        rituals = self.build_list_with_autolink(all_actions.get("rituals"), "spell")
        actions_formatted = {"skills" : self.BB_HELPER.process(skills), "spells" : self.BB_HELPER.process(spells), "rituals" : self.BB_HELPER.process(rituals)}
        return actions_formatted

    def format_perks(self):
        all_perks = self.yaml_input.get("perks")
        special_perks_bb = self.build_list_with_autolink(all_perks.get("special"), "perk")
        combat_perks_bb = self.build_list_with_autolink(all_perks.get("combat"), "perk")
        magic_perks_bb = self.build_list_with_autolink(all_perks.get("magic"), "perk")
        perks_formatted = {"special" : self.BB_HELPER.process(special_perks_bb), "combat" : self.BB_HELPER.process(combat_perks_bb), "magic" : self.BB_HELPER.process(magic_perks_bb)}
        return perks_formatted

    def format_to_html(self):
        item_list = self.format_items()
        prof_list = self.format_proficiencies()
        act_list = self.format_actions()
        perk_list = self.format_perks()
        result = f"""
<div class="chara-block">
    <div class="chara-toprow">
        <h3 id="{self.yaml_input.get("id")}">{self.yaml_input.get("name")}</h3>
    </div>
    <div class="chara-content-head">
        <div class="chara-general">
            <h6>General</h6>
            <div class="chara-value-table">
                <span class="chara-table-title">Attributes</span>
                {self.format_attributes()}
            </div>
            <div class="chara-value-table">
                <span class="chara-table-title">Values</span>
                {self.format_values()}
            </div>
            <div class="chara-value-table">
                <span class="chara-table-title">Armor</span>
                {self.format_armor()}
            </div>
        </div>
        <div class="chara-general">
            <h6>Info</h6>
            <div class="chara-info">
                {self.format_info()}
            </div>
            <div class="chara-notes">
                {self.format_notes()}
            </div>
        </div>
    </div>
    <div class="chara-content-body">
        <div class="chara-content-tile">
            <h6>Inventory</h6>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Weapons</span>
                {item_list.get("weapons")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Armor</span>
                {item_list.get("armor")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Misc.</span>
                {item_list.get("misc")}
            </div>
        </div>
        <div class="chara-content-tile">
            <h6>Actions</h6>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Skills</span>
                {act_list.get("skills")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Spells</span>
                {act_list.get("spells")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Rituals</span>
                {act_list.get("rituals")}
            </div>
        </div>
        <div class="chara-content-tile">
            <h6>Proficiencies</h6>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Weapons</span>
                {prof_list.get("weapons")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Magic</span>
                {prof_list.get("magic")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Civilian</span>
                {prof_list.get("civilian")}
            </div>
        </div>
        <div class="chara-content-tile">
            <h6>Perks</h6>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Special</span>
                {perk_list.get("special")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Combat</span>
                {perk_list.get("combat")}
            </div>
            <div class="chara-content-subtile">
                <span class="chara-subtile-title">Magic</span>
                {perk_list.get("magic")}
            </div>
        </div>
    </div>
</div>
        """
        #result = self.format_attributes()
        self.html_output = result


    def build_list_from_list(self, input_list, autolink = False):
        list_start = "[ul]"
        list_end = "[/ul]"
        result = list_start
        if len(input_list):
            for x in input_list:
                link = False
                if autolink == "perk":
                    pass
                elif autolink == "skill":
                    pass
                elif autolink == "spell":
                    link = self.autolinker.link_spell(x)
                if link:
                    result += "[li][url:"+link+"]"+x+"[/url][/li]"
                else:
                    result += "[li]"+x+"[/li]"
        else:
            result += "[li][/li]"
        result += list_end
        return result
    
    def build_list_of_items_of_category(self, input_category):
        list_start = "[ul]"
        list_end = "[/ul]"
        #return input_category
        result = list_start
        if len(input_category):
            for x in input_category:
                result += "[li]"
                first = True
                for subitem in x:
                    if first:
                        first = False
                    else:
                        result += "[br]  "
                    result += x.get(subitem)
                result += "[/li]"
        else:
            result += "[li][/li]"
        result += list_end
        return result
    

    def build_list_with_autolink(self, input_list, link_type):
        list_start = "[ul]"
        list_end = "[/ul]"
        result = list_start
        if len(input_list):
            for x in input_list:
                if isinstance(x, list):
                    to_link = x[0]
                else:
                    to_link = x
                if link_type == "perk":
                    link = self.autolinker.link_perk(to_link)
                elif link_type == "skill":
                    link = self.autolinker.link_skill(to_link)
                elif link_type == "spell":
                    link = self.autolinker.link_spell(to_link)
                if isinstance(x, list):
                    if link:
                        result += f"[li][url:{link}]{x[0]}[/url] {x[1]}[/li]"
                    else:
                        result += f"{x[0]} {x[1]}"
                else:
                    if link:
                        result += f"[li][url:{link}]{x}[/url][/li]"
                    else:
                        result += f"[li]{x}[/li]"

        result += list_end
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
                elif to_link == "tag":
                    link = self.autolinker.link_tag(i)
                if link:
                    result += f"[url:{link}]{i}[/url]"
                else:
                    result += i
            else:
                result += i
        return result