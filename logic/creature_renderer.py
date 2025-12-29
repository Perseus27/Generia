from bb_renderer import BB_Renderer

class Creature_Renderer:
    
    ATTRIBUTE_ORDER = ["CON", "STR", "DEX", "INT", "WIL", "PER"]
    VALUE_ORDER = ["EN", "MP", "MPR", "WL", "WT", "TN", "MS"]
    ARMOR_ORDER = ["head", "torso", "arms", "legs", "md", "enc"]
    DEFAULT_HITZONES = ["Head", "Torso", "Arms", "Legs"]

    BB_HELPER = BB_Renderer()
    
    def __init__(self, yaml_input, autolinker):
        self.yaml_input = yaml_input;
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
[container:creature-info-container]
[br]
[br][b]Tags:[/b]
[br]{tag_list}
[/container]
        """
        return self.BB_HELPER.process(info_bb)
    
    def format_notes(self):
        return self.BB_HELPER.process(self.yaml_input.get("notes"))
    

    def format_actions(self):
        all_items = self.yaml_input.get("actions", {})
        actions = self.build_actions_from_category(all_items.get("active", {}))
        passives = self.build_actions_from_category(all_items.get("passive", {}))
        return {"active":self.BB_HELPER.process(actions), "passive":self.BB_HELPER.process(passives)}
    
    def format_loot(self):
        return self.BB_HELPER.process(self.build_list_from_array(self.yaml_input.get("loot")))


    def format_to_html(self):
        actions = self.format_actions()
        result = f"""
<div class="creature-block">
    <div class="creature-toprow">
        <h3 id="{self.yaml_input.get("id")}">{self.yaml_input.get("name")}</h3>
    </div>
    <div class="creature-content-head">
        <div class="creature-general">
            <h6>General</h6>
            <div class="creature-value-table">
                <span class="creature-table-title">Attributes</span>
                {self.format_attributes()}
            </div>
            <div class="creature-value-table">
                <span class="creature-table-title">Values</span>
                {self.format_values()}
            </div>
            <div class="creature-value-table">
                <span class="creature-table-title">Armor</span>
                {self.format_armor()}
            </div>
        </div>
        <div class="creature-general">
            <h6>Info</h6>
            <div class="creature-info">
                {self.format_info()}
            </div>
            <div class="creature-notes">
                {self.format_notes()}
            </div>
        </div>
    </div>
    <div class="creature-content-body">
        <div class="creature-content-tile">
            <h6>Actions</h6>
            {actions.get("active")}
        </div>
        <div class="creature-content-tile">
            <h6>Passives</h6>
            {actions.get("passive")}
        </div>
        <div class="creature-content-loot">
            <h6>Loot</h6>
            {self.format_loot()}
        </div>
    </div>
</div>
        """
        #result = self.format_attributes()
        self.html_output = result


    def build_list_from_array(self, input_array):
        list_start = "[ul]"
        list_end = "[/ul]"
        result = list_start
        if len(input_array):
            for x in input_array:
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
    
    def build_actions_from_category(self, input_category):
        result = ""
        if len(input_category):
            for x in input_category:
                result += "[container:creature-action-container]"
                for subitem in x:
                    #result+=subitem
                    if subitem == "name":
                        result += "[section:creature-action-name]"+x.get(subitem)+"[/section]"
                    elif subitem == "type":
                        result += "[br][section:creature-action-type]"+x.get(subitem)+"[/section]"
                    elif subitem == "damage":
                        result += f"[container:creature-action-subitem][section:clr-roll]{x.get(subitem)}[/section][/container]"
                    elif subitem == "hit":
                        result += f"[container:creature-action-subitem][section:clr-hit]{x.get(subitem)}[/section][/container]"
                    elif subitem == "skills":
                        result += f"[container:creature-action-subitem]{self.format_list_comma(x.get(subitem), 'skill')}[/container]"
                    elif subitem == "perks":
                        result += f"[container:creature-action-subitem]{self.format_list_comma(x.get(subitem), 'perk')}[/container]"
                    elif subitem == "effect":
                        y = x.get(subitem)
                        if isinstance(y, list):
                            for z in y:
                                result += f"[container:creature-action-subitem]{z}[/container]"
                        else:
                            result += f"[container:creature-action-subitem]{y}[/container]"
                    else:
                        result += "[container:creature-action-subitem]"+x.get(subitem)+"[/container]"
                result += "[/container]"
        return result

    def format_list_comma(self, input_list, to_link=False):
        result = ""
        first = True
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
                if to_link == "class":
                    link = self.autolinker.link_class(i)
                elif to_link == "tag":
                    link = self.autolinker.link_tag(i)
                elif to_link == "skill":
                    link = self.autolinker.link_skill(i)
                elif to_link == "perk":
                    link = self.autolinker.link_perk(i)
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