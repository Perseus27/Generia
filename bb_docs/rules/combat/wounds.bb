[h1|Basics]Basics[/h1]
When a creature suffers damage that exceeds its [url:values#WT]Wound Treshold[/url] ([b]WT[/b]), it receives one wound per exceedance. When the total number of sustained wounds reaches the creature’s [url:values#Wounds]Wound Limit[/url] ([b]WL[/b]), it becomes [url:#Unconsciousness]unconscious[/url].
[br]Examples (for [b]WT 10[/b]):
[ul]
[li]The creature takes 8 damage. It gains no wound.[/li]
[li]The creature takes 14 damage. It gains one wound.[/li]
[li]The creature takes 21 damage. It gains two wounds.[/li]
[li]The creature takes 10 damage. It gains no wound.[/li]
[/ul]
If, after receiving a wound, the creature’s total wounds exceed half of its WL, it must make a [b][section:clr-attr]CON[/section][/b] [section:clr-save]Save[/section] against [section:clr-value][total sustained wounds] * 2[/section]. On a failure, the creature becomes [url:#Unconsciousness]unconscious[/url].
[br]If a creature suffers more than one wound from a single attack, it must make a [url:#WoundCheck]Wound Check[/url] for each wound after the first.
[br][i]For creatures with the [url:/w/generia-perseus27/a/creature-tags-article]Colossus[/url] tag, the Save difficulty is only [section:clr-value][total sustained wounds] * 1[/section].[/i]

[h1|WoundCheck]Wound Check[/h1]
A Wound Check determines a wound’s severity. Roll a simple [section:clr-roll]1d20[/section]. On [section:clr-value]10 or higher[/section], the wound counts as [i][url:#LightWounds]light[/url][/i]. On [section:clr-value]9 or lower[/section], it counts as [i][url:#SevereWounds]severe[/url][/i]. Wound Checks automatically fail if that specific attack has already inflicted two wounds.

[h1|Execution]Execution[/h1]
If a creature has already reached its WL, every additional wound converts one light wound into a severe wound.

[h1|Healing]Healing[/h1]
[h2|LightWounds]Light Wounds[/h2]
To heal a light wound, [i][section:clr-heilung]healing points[/section][/i] from spells or items (e.g., healing potions) must exceed the [url:values#WT]Wound Treshold[/url] ([b]WT[/b]). Each exceedance of WT heals one wound.
[h2|SevereWounds]Severe Wounds[/h2]
Severe wounds can only be healed outside combat via specialized rituals or equipment, typically requiring a Medicine check. The status effect [i][url:status#Regeneration]Regeneration[/url][/i] has no effect on severe wounds.
[h2|MedicineChecks]Medicine Checks[/h2]
A Medicine check is usually* [b]Difficulty 20[/b]. This value is [url:core#Eased]eased[/url] by the wounded creature’s [section:clr-attr]CON-MOD[/section] and by the healer’s Medicine skill value. On success, one wound—light** or severe—is healed.
[br][i]*For exceptionally complicated wounds, the GM may [url:core#Hindered]hinder[/url] the check at their discretion.[/i]
[br][i]**When healing a light wound, the healer gains [url:core#Advantage]Advantage 1[/url] if they possess the Medicine skill.[/i]

[h1|Unconsciousness]Unconsciousness[/h1]
[i]See also: [url:status#Unconscious]Unconscious[/url][/i]
[br]An unconscious creature cannot take actions or reactions and counts as [url:status#Prone]Prone[/url]. [url:def#AttackAction]Attack Actions[/url] against an unconscious creature automatically hit. All [section:clr-save]Saves[/section] (except [section:clr-attr]CON[/section] Saves) automatically fail.
[br]If the total number of wounds on an unconscious creature is below its WL, it may, at the start of its turn and when taking damage or receiving healing, attempt a [section:clr-attr]CON[/section] Save against [section:clr-value]10[/section], [url:core#Hindered]hindered[/url] by [section:clr-value][total sustained wounds * 2][/section]. On a success, the creature is no longer unconscious.
[br][i]For creatures with the [url:/w/generia-perseus27/a/creature-tags-article]Colossus[/url] tag, the Save is only hindered by [section:clr-value][total sustained wounds * 1][/section].[/i]*