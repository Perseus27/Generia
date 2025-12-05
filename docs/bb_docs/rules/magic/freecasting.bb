[h1|WhatIsFreecasting]What is Freecasting?[/h1]
Most spellcasting traditions have access to rituals that enable [i]Freecasting[/i] (e.g., [i][url:/w/generia-perseus27/a/bard-spells-article#Improvisation]Improvisation[/url], [url:/w/generia-perseus27/a/wizard-spells-E28093-tier-i-article#ThermalManipulation]Thermal Manipulation[/url][/i]). This allows for the casting of improvised spells in combat, capable of producing an effect as defined in the ritual description.
[br]The exact effects and costs of improvised spells are subject to negotiation between player and GM, though they should follow certain [url:#Guidelines]guidelines[/url].

[h1|FreecastCheck]Freecast Check[/h1]
Freecasting any spell requires an [i]Arcana[/i] or [i]Rites[/i] check, whichever makes more sense for the spell in question. The [section:clr-dc]DC[/section] for this check depends on the estimated tier of the spell's effect:
[br][b]Tier I:[/b] [section:clr-dc]DC[/section] [section:clr-value]10[/section]
[br][b]Tier II:[/b] [section:clr-dc]DC[/section] [section:clr-value]20[/section]
[br][b]Tier III:[/b] [section:clr-dc]DC[/section] [section:clr-value]30[/section]
[br][b]...[/b]
[br]The freecast check is [url:core#Eased]eased[/url] by the caster's primary [url:#SpellcastingAttributes]spellcasting attribute[/url] as well as any appropriate proficiency values (e.g., [i]Arcane, Cacophony, Luna...[/i])
[h4]Failure[/h4]
If the check fails, the spell does not materialize. In most cases, the caster does not lose any [section:clr-mp]MP[/section] for a failed freecasting attempt.
[h4]Success[/h4]
If the check succeeds, the caster may execute the improvised spell. If the spell targets an unwilling creature, player and GM must determine the [url:#CastType]Cast Type[/url] and any involved [url:#SpellcastingAttributes]attributes[/url].
[br]After executing all required rolls, the caster must make a [url:/generia/rules/magic/chaotic-magic#ChaosCheck]Chaos Check[/url].

[h1|CastingTypes]Casting Types[/h1]
There are five primary Casting Types: [url:def#SA]Spell Attacks[/url], [url:def#PA]Projectile Attacks[/url], [url:def#SD]Spell Defense[/url], [url:def#DC]Determined Cast[/url], and [url:def#Surecast]Surecast[/url].
[br]With the exception of [i]Surecast[/i],  each type requires various [url:#Attributes]Attributes[/url]:
[h2][section:clr-sa]Spell Attack[/section][/h2]
[b]Attributes:[/b] [i]Spellcasting Attribute[/i], [i]Save Attribute[/i]
[br][b]Syntax:[/b] [section:clr-sa]SA[/section] [section:clr-attr]Spellcasting Attribute Modifier[/section] vs [section:clr-attr]Save Attribute Modifier[/section]
[br][b]Use cases:[/b] Beam spells, AoE attack spells...
[h2][section:clr-pa]Projectile Attack[/section][/h2]
[b]Attributes:[/b] [i]Spellcasting Attribute[/i], [i](Secondary Attribute)[/i]
[br][b]Syntax:[/b] [section:clr-pa]PA[/section] [section:clr-attr]Spellcasting Attribute Modifier[/section] (+ [section:clr-attr]Secondary Attribute Modifier[/section])
[br][b]Use cases:[/b] Any spell that behaves like a [url:def#RangedAttack]ranged attack[/url].
[h2][section:clr-sd]Spell Defense[/section][/h2]
[b]Attributes:[/b] [i]Spellcasting Attribute[/i], [i]Secondary Attribute[/i]
[br][b]Syntax:[/b] [section:clr-sd]SD[/section] [section:clr-attr]Spellcasting Attribute Modifier[/section] + [section:clr-attr]Secondary Attribute Modifier[/section]
[br][b]Use cases:[/b] Reactive spells to defend against basic attacks or projectile attacks.
[h2][section:clr-dc]Determined Cast[/section][/h2]
[b]Attributes:[/b] [i]Spellcasting Attribute[/i], [i]Save Attribute[/i]
[br][b]Syntax:[/b] [section:clr-dc]DC[/section] [section:clr-attr]Spellcasting Attribute Modifier[/section] vs [section:clr-attr]Save Attribute Modifier[/section]
[br][b]Use cases:[/b] [section:clr-control]Control[/section] spells, [section:clr-affliction]Affliction[/section] spells, persistent spells (-> [section:clr-conc]Concentration[/section])...
[h2][section:clr-surecast]Surecast[/section][/h2]
[b]Attributes:[/b] None
[br][b]Syntax:[/b] None
[br][b]Use cases:[/b] [section:clr-support]Support[/section] spells, terrain-changing spells...

[h1|Attributes]Attributes[/h1]
[h2|SpellcastingAttributes]Spellcasting Attributes[/h2]
The primary [i]attribute[/i] for any freecast is the main spellcasting attribute of the caster's tradition:
[br][b][section:clr-attr]INT[/section]:[/b] Alchemist, Wizard
[br][b][section:clr-attr]WIL[/section]:[/b] Acolyte, Bard, Druid, Shaman
[br][b][section:clr-attr]PER[/section]:[/b] Nox, Sorcerer
[h4]Secondary Attributes[/h4]
Some [section:clr-pa]Projectile Attacks[/section] and [section:clr-sd]Spell Defenses[/section] may require a secondary attribute to make them comparable to [url:def#RangedAttack]ranged attacks[/url] and [url:def#Block]basic defenses[/url].
[br]The caster may pick any attribute for this, as long as the choice is reasonably justifiable.
[br][i][b]GM Note:[/b] INT, WIL, PER, or DEX tend be good picks, depending on spell and character flavor.[/i]
[h2|SaveAttributes]Save Attributes[/h2]
If a spell targets an unwilling creature, the target is entitled to a [section:clr-save]Save[/section]. This [i]Save Attribute[/i] should be chosen according to the following criteria:
[br][b][section:clr-attr]CON[/section]:[/b] Physical, not dodgeable
[br][b][section:clr-attr]STR[/section]:[/b] Physical, can be countered with sheer bodily strength
[br][b][section:clr-attr]DEX[/section]:[/b] Physical, dodgeable
[br][b][section:clr-attr]INT[/section]:[/b] Mental, interference with rational thinking
[br][b][section:clr-attr]WIL[/section]:[/b] Mental, interference with emotions/psyche
[br][b][section:clr-attr]PER[/section]:[/b] Mental, interference with perception

[h1|Guidelines]Guidelines[/h1]
[h2]SA Spells[/h2]
[h4]Tier I[/h4]
Beam attacks, single target [section:clr-affliction]Affliction[/section]/[section:clr-control]Control[/section]
[br]~[section:clr-value]1d6[/section]–[section:clr-value]2d6[/section] Damage
[br][section:clr-mp]1–2 MP[/section]
[h4]Tier II[/h4]
Beam attacks, AoE attacks (~2m radius), multi target attacks, multi target [section:clr-affliction]Affliction[/section]/[section:clr-control]Control[/section]
[br]~[section:clr-value]2d6[/section]–[section:clr-value]4d6[/section] Damage
[br][section:clr-mp]2–4 MP[/section]
[h4]Tier III[/h4]
Beam attacks, AoE attacks (4m+ radius), multi target attacks, multi target [section:clr-affliction]Affliction[/section]/[section:clr-control]Control[/section]
[br]~[section:clr-value]2d8[/section]+ Damage
[br][section:clr-mp]3+ MP[/section]
[h2]PA Spells[/h2]
[h4]Tier I[/h4]
Single target projectiles
[br]~[section:clr-value]1d8[/section]–[section:clr-value]2d8[/section] Damage
[br][section:clr-mp]1–2 MP[/section]
[h4]Tier II[/h4]
Single & multi target projectiles
[br]~[section:clr-value]2d8[/section]–[section:clr-value]4d8[/section] Damage
[br][section:clr-mp]2–4 MP[/section]
[h4]Tier III[/h4]
Single & multi target projectiles
[br]~[section:clr-value]2d10[/section]+ Damage
[br][section:clr-mp]3+ MP[/section]
[h2]SD Spells[/h2]
[h4]Tier I[/h4]
Reactive self-shielding
[br]~[section:clr-value]1d4[/section]–[section:clr-value]2d4[/section] Shielding
[br][section:clr-mp]1–2 MP[/section]
[h4]Tier II[/h4]
Reactive self-shielding, reactive ally shielding, reactive self-displacement
[br]~[section:clr-value]1d8[/section]–[section:clr-value]2d8[/section] Shielding
[br][section:clr-mp]2–4 MP[/section]
[h4]Tier III[/h4]
Reactive self-shielding, reactive ally shielding, reactive area/multitarget shielding, reactive self-displacement
[br]~[section:clr-value]1d12[/section]+ Shielding
[br][section:clr-mp]4+ MP[/section]
[h2]DC Spells[/h2]
[h4]Tier I[/h4]
Single target [section:clr-control]control[/section]/[section:clr-affliction]affliction[/section]
[br][section:clr-conc]Concentration[/section]
[h4]Tier II[/h4]
Multi target sustained damage, multi target [section:clr-control]control[/section]/[section:clr-affliction]affliction[/section], area [section:clr-control]control[/section]/[section:clr-affliction]affliction[/section]
[br][section:clr-conc]Concentration[/section]
[h4]Tier III[/h4]
Multi target sustained damage, multi target [section:clr-control]control[/section]/[section:clr-affliction]affliction[/section], area [section:clr-control]control[/section]/[section:clr-affliction]affliction[/section]
[br][section:clr-conc]Concentration[/section]
[h2]Surecast Spells[/h2]
[h4]Tier I[/h4]
Single target [section:clr-support]support[/section]/[section:clr-heal]healing[/section], [section:clr-terrain]terrain[/section] change, [section:clr-movement]movement[/section]
[h4]Tier II[/h4]
Multi target [section:clr-support]support[/section]/[section:clr-heal]healing[/section], area [section:clr-support]support[/section]/[section:clr-heal]healing[/section], [section:clr-terrain]terrain[/section] change, [section:clr-movement]movement[/section]
[h4]Tier III[/h4]
Multi target [section:clr-support]support[/section]/[section:clr-heal]healing[/section], area [section:clr-support]support[/section]/[section:clr-heal]healing[/section], [section:clr-terrain]terrain[/section] change, [section:clr-movement]movement[/section]