[h1]What are Creature Tags?[/h1]
Creature tags are passive features that are usually inherent to a species (or, more rarely, individuals). With very few exceptions (e.g., [i][url:#Colossus]Colossus[/url][/i]), they are attained at birth and cannot be gained or removed without drastic changes to the creature's fundamental nature.

[h1]Tags[/h1]
[container:orgblock]
[h4|Colossus]Colossus[/h4]
[url:values#WT]Wound Treshold[/url] ([b]WT[/b]) is halved, but [url:values#WL]Wound Limit[/url] ([b]WL[/b]) is doubled.
[br]This tag is gained automatically upon reaching a [section:clr-attr]CON[/section] value of [section:clr-value]20[/section].
[br][i]Effects are doubled (i.e., WT is quartered and WL is quadrupled) upon reaching [section:clr-value]40[/section] [section:clr-attr]CON[/section].[/i]
[br][i]The effects of [url:NaturesArmor]Nature's Armor[/url] and [url:#NaturesWill]Nature's Will[/url] are halved as well to avoid unkillable beasts.[/i]
[/container]

[container:orgblock]
[h4|Fast]Fast X[/h4]
[url:values#MS]Movement Speed[/url] ([b]MS[/b]) is increased by [section:clr-value]X[/section].
[h4|Slow]Slow X[/h4]
[url:values#MS]Movement Speed[/url] ([b]MS[/b]) is reduced by [section:clr-value]X[/section].
[h4|Sluggish]Sluggish[/h4]
Universal Action [url:actions#Sprint]Sprint[/url] is unavailable.
[/container]

[container:orgblock]
[h4|Flying]Flying X[/h4]
The creature is inherently capable of flight, with an unmodified [url:values#MS]movement speed[/url] of [section:clr-value]X[/section].
[h4|Levitating]Levitating X[/h4]
The creature naturally levitates [section:clr-value]X[/section] meters above the ground. Regular [url:values#MS]movement speed[/url] applies.
[/container]

[container:orgblock]
[h4|Immunity]Immunity X[/h4]
Permanent [url:status#Immune]Immune X[/url].
[h4|Resistance]Resistance[/h4]
Permanent [url:status#Resistant]Resistant X[/url].
[h4|Vulnerability]Vulnerability X[/h4]
Permanent [url:status#Vulnerable]Vulnerable X[/url].
[/container]

[container:orgblock]
[h4|Mindless]Mindless[/h4]
The creature is immune to [url:status]mental status effects[/url] and [url:wounds#Unconsciousness]Unconsciousness[/url].
[br]Prerequisite: [section:clr-attr]WIL 0[/section].
[h4|Construct]Construct[/h4]
[url:values#WL]Wound Limit[/url] ([b]WL[/b]) is set to [section:clr-attr]CON-MOD[/section] or [section:clr-value]3[/section], whichever is higher. [url:../creature-sizes]Creature Size[/url] rules are applied afterward.
[br]Prerequisite tag: [url:#Mindless]Mindless[/url].
[br][i]This tag is meant for artificial beings with no will of their own.[/i]
[/container]

[container:orgblock]
[h4|Miniboss]Miniboss[/h4]
Slaying this creature awards twice the experience points.
[/container]

[container:orgblock]
[h4|Mount]Mount X[/h4]
This creature can be used as a mount if [i][url:/generia/character/proficiencies/proficiencies-civilian/]Riding[/url][/i] proficiency is [section:clr-value]X[/section] or higher.
[/container]

[container:orgblock]
[h4|NaturalDefenses]Natural Defenses[/h4]
Gains both [i]Nature's Armor[/i] and [i]Nature's Will[/i].
[h4|NaturesArmor]Nature's Armor[/h4]
This creature is protected by some form of natural armor (thick fur, scales, exoskeleton...)
[br][url:values#AV]Armor Value[/url] is increased by the following values:
[ul]
[li]Head: [section:clr-attr]CON-MOD[/section]-2[/li]
[li]Torso: [section:clr-attr]CON-MOD[/section][/li]
[li]Arms: [section:clr-attr]CON-MOD[/section]-1[/li]
[li]Legs: [section:clr-attr]CON-MOD[/section]-1[/li]
[/ul]
[h4|NaturesWill]Nature's Will[/h4]
This creature is protected by the magical energies that suffuse all of nature.
[br][url:values#MD]Magical Defense[/url] is increased by [section:clr-attr]WIL-MOD[/section].
[/container]

[container:orgblock]
[h4|Reflexes]Reflexes X[/h4]
[url:def#Block]Block[/url], [url:def#Dodge]Dodge[/url], and [url:def#Parry]Parry[/url] rolls are [url:core#Eased]eased[/url] (or, in case of negative [section:clr-value]X[/section], [url:core#Hindered]hindered[/url]) by [section:clr-value]X[/section].
[/container]

[container:orgblock]
[h4|Sapient]Sapient[/h4]
Sapient creatures are significantly more dangerous than beasts and beast-like monsters. Due to the increased risk of engaging them in combat, they award as much experience as a character of the same level when slain.
[br][i]Sapient creatures often have access to skills, spells, and perks usually reserved for characters.[/i]
[/container]

[container:orgblock]
[h4|Tough]Tough X[/h4]
[url:values#TN]Toughness[/url] ([b]TN[/b]) is increased by [section:clr-value]X[/section].
[/container]

[container:orgblock]
[h4|Trained]Trained X[/h4]
Total SP are increased by [section:clr-value]X[/section].
[br][i]This tag reflects high-quality training, e.g. military, clerical or similar.[/i]
[h4]Untrained X[/h4]
Total SP are decreased by [section:clr-value]X[/section].
[br][i]This tag reflects a lack of training, education or experience, e.g. common bandits or particularly lazy adventurers.[/i]
[/container]