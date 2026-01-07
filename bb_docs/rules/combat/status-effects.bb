[h1|Definitions]Definitions[/h1]
[h2]Stacking Effects[/h2]
[h4]Damage Tiers[/h4]
Status effects that deal damage against [url:values#TN]Toughness (TN)[/url] or heal over time (e.g., [url:#Bleeding]Bleeding[/url], [url:#Burning]Burning[/url], [url:#Poisoned]Poisoned[/url], [url:#Regeneration]Regeneration[/url]) can stack with repeated application. The maximum tier is [section:clr-value][b]5[/b][/section].
[br][b]Example:[/b] A creature has [url:#Bleeding]Bleeding 1[/url]. If it receives Bleeding 1 (or 2) again, the effect increases to Bleeding 2 (or 3).
[br]At the start of each round, the creature may make a [section:clr-attr]CON[/section] [section:clr-save]Save[/section] against [b][ [section:clr-value]10 + tier[/section] ][/b]. On a success, reduce the tier by [section:clr-zahl]1[/section].

[h2]Determined Check (Origin Value)[/h2]
The status effect’s [section:clr-dc]Determined Check (DC)[/section] equals:
[ul]
[li]for magical origin: [b]10 + [section:clr-attr]spell attack attribute MOD[/section][/b][/li]
[li]for physical origin (e.g., [i][url:#Stunned]stunned[/url][/i] by a blunt weapon): [b]10 + [section:clr-attr]STR-MOD[/section][/b][/li]
[li]or another value, if specified in the effect description.[/li]
[/ul]
[h4]Removal[/h4]
When an effect is actively dispelled/removed (e.g., by a spell), use the above [b][section:clr-dc]DC[/section][/b] as the check difficulty.

[h2|Classification]Classification[/h2]
Each status effect belongs to one or more classifications. There are various spells, perks, items and other effects that interact with certain classifications, but not necessarily others.
[h4|Mental]Mental[/h4]
If a status effect is saved against with a mental attribute ([section:clr-attr]INT[/section], [section:clr-attr]WIL[/section], [section:clr-attr]PER[/section]), it counts as [i]mental[/i].
[h4|Physical]Physical[/h4]
If a status effect is saved against with a physical attribute ([section:clr-attr]CON[/section], [section:clr-attr]STR[/section], [section:clr-attr]DEX[/section]), it counts as [i]physical[/i].
[h4|Magical]Magical[/h4]
If the source of a status effect is magical in nature (e.g., a spell, ritual, enchanted item...), it counts as [i]magical[/i].
[h4|Mundane]Mundane[/h4]
If the source of a status effect is non-magical in nature (e.g., [url:#Stunned]Stunned[/url] through Blunt damage, [url:#Sick]Sick[/url] through the common flu), it counts as [i]mundane[/i].


[hr]
[h1|DoTHoT]DoT / HoT[/h1]

[container:statusblock]
[h4|Bleeding]Bleeding[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Takes physical damage against [url:values#TN]TN[/url] at the start of the turn.
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[br][i](Removed by healing magic or healing potions.)[/i]
[/container]

[container:statusblock]
[h4|Burning]Burning[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Takes fire damage against [url:values#TN]TN[/url] at the start of the turn.
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[/container]

[container:statusblock]
[h4|Decay]Decay[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Takes Void damage at the start of the turn against [url:values#TN]Toughness (TN)[/url].
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[/container]

[container:statusblock]
[h4|Lightburn]Lightburn[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Takes light damage at the start of the turn against [url:values#TN]Toughness (TN)[/url].
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[/container]

[container:statusblock]
[h4|Poisoned]Poisoned[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Takes poison damage against [url:values#TN]TN[/url] at the start of the turn.
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[/container]

[container:statusblock]
[h4|Regeneration]Regeneration[/h4]
[section:clr-support]SUPPORT[/section]
[br]Gains healing points at the start of the turn; these accumulate across rounds.
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[br][i]The effect loses one tier (and any excess points) as soon as a wound is successfully healed (or inflicted).[/i]
[br][i]Ineffective on [url:/w/generia-perseus27/a/wounds-article#SchwereWunden]severe wounds[/url].[/i]
[br][i]The effect ends if the creature has no light wounds or the tier drops below 1.[/i]
[/container]

[container:statusblock]
[h4|Spellburn]Spellburn[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Takes arcane damage at the start of the turn against [url:values#TN]Toughness (TN)[/url].
[br][b]Tier 1:[/b] [b][section:clr-roll-noex]1d4[/section][/b]
[br][b]Tier 2:[/b] [b][section:clr-roll-noex]1d6[/section][/b]
[br][b]Tier 3:[/b] [b][section:clr-roll-noex]1d8[/section][/b]
[br][b]Tier 4:[/b] [b][section:clr-roll-noex]1d10[/section][/b]
[br][b]Tier 5:[/b] [b][section:clr-roll-noex]1d12[/section][/b]
[/container]

[h1|AfflictionAndControl]Affliction and Control[/h1]
[container:statusblock]
[h4|Blinded]Blinded X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on [url:def#RangedAttack]ranged attacks[/url] and [section:clr-pa]projectile attacks[/section], and on defense rolls against ranged and spell projectiles.
[br][i]At the end of each of the creature’s turns, reduce [section:clr-zahl]X[/section] by [section:clr-zahl]1[/section].[/i]
[/container]

[container:statusblock]
[h4|Brittle]Brittle X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]The affected [url:def#HitZone]hit zone[/url] loses [url:values#AV]Armor Value (AV)[/url] equal to [section:clr-value]X[/section].
[br]If a shield is affected, it loses [url:values#BlockStrength]Block Strength[/url] equal to [section:clr-value]X[/section].
[br][i]Permanent.[/i]
[/container]

[container:statusblock]
[h4|Charmed]Charmed[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br]Cannot attack the caster’s faction.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]WIL[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn or when taking damage.
[/container]

[container:statusblock]
[h4|Chilled]Chilled[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br]Counts as [url:#Slowed]Slowed[/url] and [url:#Drowsy]Drowsy[/url].
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]CON[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the end of the turn.
[/container]

[container:statusblock]
[h4|Confused]Confused[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on attack rolls. Cannot communicate with allies.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]INT[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the end of the turn or when taking damage.
[/container]

[container:statusblock]
[h4|Disarmed]Disarmed[/h4]
[section:clr-control]CONTROL[/section]
[br]An equipped weapon is unavailable until the creature spends any [url:def#Actions]action[/url] to pick it up/equip it again.
[/container]

[container:statusblock]
[h4|Drowsy]Drowsy[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on [section:clr-attr]DEX[/section] and [section:clr-attr]PER[/section] checks as well as [url:/w/generia-perseus27/a/keywords-article#Concentration]concentration[/url] saves.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]PER[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the end of the turn.
[br]Can be removed by a [url:def#AttackAction]melee Attack Action[/url] from an ally.
[/container]

[container:statusblock]
[h4|Frail]Frail[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br][section:clr-attr]CON[/section] checks have [url:core#Disadvantage]Disadvantage 1[/url] (except the [section:clr-save]Save[/section] against this effect).
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]CON[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn or whenever a wound is healed. The save has [url:core#Advantage]Advantage 1[/url] if the creature is not wounded.
[/container]

[container:statusblock]
[h4|Frozen]Frozen[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br]Cannot take actions or reactions.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]STR[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn or upon exposure to heat.
[/container]

[container:statusblock]
[h4|Frightened]Frightened[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on attack rolls. Movement toward an enemy counts as [url:#Slowed]Slowed[/url].
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]WIL[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the end of the turn or when taking damage.
[/container]

[container:statusblock]
[h4|Grappled]Grappled[/h4]
[section:clr-control]CONTROL[/section]
[br]May not perform Movement Actions. [url:core#Disadvantage]Disadvantage 2[/url] on Dodge, Parry, and Block rolls.
[br]The grappler must spend an Attack or Utility Action each turn to maintain the grapple and has [url:core#Advantage]Advantage 1[/url] on unarmed or short-weapon attacks against the grappled creature.
[br]The grappled creature may, as any action, initiate a [b][section:clr-attr]STR[/section][/b] [url:core#OpposedCheck]Opposed Check[/url] against the grappler.
[br]On success, the effect ends and the creature is free.
[br]On failure, it remains grappled.
[/container]

[container:statusblock]
[h4|Hyperpathia]Hyperpathia[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]When the creature suffers a wound, it must succeed on a [b][section:clr-attr]CON[/section][/b] or [b][section:clr-attr]WIL[/section][/b] save against the effect’s [section:clr-dc]DC[/section]. On a failure, the status changes to [url:#Stunned]Stunned[/url].
[/container]

[container:statusblock]
[h4|Knockback]Knockback X[/h4]
[section:clr-control]CONTROL[/section]
[br]The affected creature is knocked [section:clr-value]X meters[/section] away from the effect source, unless another direction is specified. If the effect source is a larger creature, [section:clr-value]X[/section] is doubled for each tier of difference. If the effect source is a smaller creature, [section:clr-value]X[/section] is halved instead.
[br]If the affected creature collides with another creature or environment, certain other status effects (or any combinations thereof) may be triggered, depending on the severity of the collision:
[br][b]Harmless:[/b] No effect
[br][b]Bump:[/b] [url:#OffBalance]Off-Balance[/url]
[br][b]Impact:[/b] [url:#Prone]Prone[/url]
[br][b]Crash:[/b] [url:#Stunned]Stunned[/url] + [url:#OffBalance]Off-Balance[/url]/[url:#Prone]Prone[/url]
[br]A creature may attempt a [section:clr-attr]CON[/section], [section:clr-attr]STR[/section], or [section:clr-attr]DEX[/section] [section:clr-save]save[/section] against the knockback's [section:clr-dc]DC[/section] to reduce the effect by one stage.
[br][i]The collision severity is determined by the players' and GM's common sense.[/i]
[/container]

[container:statusblock]
[h4|OffBalance]Off-Balance[/h4]
[section:clr-control]CONTROL[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on Dodge, Parry, and Block rolls as well as [section:clr-attr]DEX[/section] checks.
[br]The creature may spend any [url:def#Actions]action[/url] to end the effect. If it receives the effect a second time, it becomes [url:#Prone]Prone[/url].
[br]It also becomes [url:#Prone]Prone[/url] if it is still off-balance at the end of its next turn.
[br][i]An ally may spend 2 meters of movement to stabilize the creature and end the effect.[/i]
[/container]

[container:statusblock]
[h4|Panicked]Panicked[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on attack rolls. Must use [url:def#Actions]all available actions[/url] to move as far as possible away from the effect’s originator.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]WIL[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn or when taking damage.
[/container]

[container:statusblock]
[h4|Prone]Prone[/h4]
[section:clr-control]CONTROL[/section]
[br]May not perform Movement Actions. [url:core#Disadvantage]Disadvantage 2[/url] on Dodge, Parry, and Block rolls.
[br]At the start of its turn, the creature may spend any [url:def#Actions]action[/url] to end the effect.
[br][i]An ally may spend 4 meters of movement to help the creature up and end the effect.[/i]
[/container]

[container:statusblock]
[h4|Restrained]Restrained[/h4]
[section:clr-control]CONTROL[/section]
[br]May not perform Movement Actions. [url:core#Disadvantage]Disadvantage 2[/url] on Dodge, Parry, and Block rolls.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]STR[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn.
[/container]

[container:statusblock]
[h4|Shocked]Shocked X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Dodge, Parry, and attack rolls are [url:core#Hindered]hindered[/url] by [section:clr-value]X[/section] until the end of the creature's next turn.
[/container]

[container:statusblock]
[h4|Sick]Sick[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Counts as [url:status#Weakened]Weakened[/url] and [url:status#Slowed]Slowed[/url].
[br][i]Can be removed by a successful Medicine check or cleansing spells.[/i]
[/container]

[container:statusblock]
[h4|Silenced]Silenced[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Cannot communicate audibly and cannot speak [url:/w/generia-perseus27/a/magical-definitions-article#Formeln]spell incantations[/url].
[/container]

[container:statusblock]
[h4|Slowed]Slowed X[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br]Movement Speed is halved.
[br][i](Meaning: each meter of movement costs [section:clr-zahl]2[/section] MS.)[/i]
[br][i]At the end of each of the creature’s turns, reduce [section:clr-zahl]X[/section] by [section:clr-zahl]1[/section].[/i]
[/container]

[container:statusblock]
[h4|Stunned]Stunned[/h4]
[section:clr-affliction]AFFLICTION[/section], [section:clr-control]CONTROL[/section]
[br][url:core#Disadvantage]Disadvantage 1[/url] on all rolls (except the [section:clr-save]Save[/section] against this effect). Also counts as [url:#Slowed]Slowed[/url].
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]WIL[/section] or [section:clr-attr]CON[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn or when taking damage.
[/container]

[container:statusblock]
[h4|Vulnerable]Vulnerable X Y[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]Incoming damage type [i][b]X[/b][/i] is increased by [section:clr-zahl]50%[/section] for [i][b]Y[/b][/i] rounds.
[br][i][b]Example vulnerabilities:[/b] Fire, Ice, Magical, Sharp, Blunt, Physical[/i]
[/container]

[container:statusblock]
[h4|Weakened]Weakened[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br][section:clr-attr]STR[/section] checks have [url:core#Disadvantage]Disadvantage 1[/url].
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]CON[/section][/b] vs [b][section:clr-dc]DC[/section][/b] at the start of the turn.
[/container]

[hr]

[h1|Support]Support[/h1]
[container:statusblock]
[h4|Hidden]Hidden X[/h4]
[section:clr-support]SUPPORT[/section]
[br]Gains [url:core#Advantage]Advantage X[/url] on [url:def#Sneaking]Sneaking[/url] checks.
[/container]

[container:statusblock]
[h4|Immune]Immune X Y[/h4]
[section:clr-support]SUPPORT[/section]
[br]Incoming damage type [i][b]X[/b][/i] is negated for [i][b]Y[/b][/i] rounds.
[br][i][b]Example immunities:[/b] Fire, Ice, Magical, Sharp, Blunt, Physical[/i]
[br]if a status effect (e.g., [url:#Poisoned]Poisoned[/url], [url:#Frightened]Frightened[/url]) is specified instead of a damage type, the creature cannot be affected with this status effect.
[/container]

[container:statusblock]
[h4|Levitating]Levitating[/h4]
[section:clr-support]SUPPORT[/section]
[br]Levitates a certain height above the ground. Levitating MS is effect-dependent.
[br][b]Tier 1:[/b] [b]2 meters[/b]
[br][b]Tier 2:[/b] [b]4 meters[/b]
[br][b]Tier 3:[/b] [b]6 meters[/b]
[/container]

[container:statusblock]
[h4|Resistant]Resistant X Y[/h4]
[section:clr-support]SUPPORT[/section]
[br]Incoming damage type [i][b]X[/b][/i] is halved for [i][b]Y[/b][/i] rounds.
[br][i][b]Example resistances:[/b] Fire, Ice, Magical, Sharp, Blunt, Physical[/i]
[/container]

[hr]

[h1|Curses]Curses[/h1]
[h2]Info[/h2]
Curses are rare and particularly insidious status effects that cannot be regularly saved against. The must instead be removed through cleansing spells, rituals, or items.
[h2]Curse Severity[/h2]
Curses have different level of severity. These are specified in the curse description.
[h2]Curse DC[/h2]
The [section:clr-dc]DC[/section] of a curse depends on its severity. The default DC of [section:clr-value]10[/section] is increased by [section:clr-value]10[/section] for each severity level.
[br][b]Severity 1:[/b] [section:clr-value]20[/section]
[br][b]Severity 2:[/b] [section:clr-value]30[/section]
[br][b]Severity 3:[/b] [section:clr-value]40[/section]
[br][b]etc.[/b]

[container:statusblock]
[h4|AttributeCurse]Attribute Curse[/h4]
All rolls involving the specified attribute are [url:core#Hindered]hindered[/url] by [[section:clr-value]Severity[/section]].
[/container]

[container:statusblock]
[h4|StatusCurse]Status Curse[/h4]
Permanently applies a specified [url:status]status effect[/url]. This status effect remains active until the curse is broken.
[/container]

[container:statusblock]
[h4|ValueCurse]Value Curse[/h4]
Directly reduces the specified [url:values]value[/url] by [[section:clr-value]Severity[/section]].
[/container]

[container:statusblock]
[h4|Corruption]Corruption[/h4]
Under the corrupting influence of the Void. Common symptoms include:
Loss of empathy and inhibitions, violent urges, insensitivity to pain, and an appetite for very fresh meat.
[br][b]Severity 1:[/b]
[ul]
[li]Healing points received are halved.[/li]
[li]Permanent [url:#Vulnerable]Vulnerability[/url] [i]Light[/i].[/li]
[li][url:values#WL]WL[/url] is increased by [section:clr-value]1[/section].[/li]
[/ul]
[b]Severity 2:[/b]
[ul]
[li]Healing points received are negated.[/li]
[li][url:core#Advantage]Advantage 1[/url] on [section:clr-attr]CON[/section] checks.[/li]
[li][url:core#Disadvantage]Disadvantage 1[/url] on [section:clr-attr]WIL[/section] checks.[/li]
[li]Permanent [url:#Resistant]Resistance[/url] [i]Void[/i].[/li]
[li]Permanent [url:#Vulnerable]Vulnerability[/url] [i]Fire[/i].[/li]
[li][url:values#WL]WL[/url] is increased by [section:clr-value]1[/section].[/li]
[/ul]
[b]Severity 3:[/b]
[ul]
[li]Permanent [url:#Immune]Immunity[/url] [i][url:#Unconscious]Unconsciousness[/url][/i].[/li]
[li]Consuming unsouled food no longer regenerates [section:clr-en]EN[/section].[/li]
[li][url:values#WL]WL[/url] is increased by [section:clr-value]1[/section].[/li]
[/ul]
The effects are cumulative.
[/container]

[hr]

[h1|Misc]Miscellaneous[/h1]
[container:statusblock]
[h4|Confined]Confined[/h4]
The creature cannot use its full range of movement. Primarily affects [url:eqtags#Long]long[/url] and [url:eqtags#Short]short[/url] weapons.
[br]A creature counts as [i]confined[/i] if:
[br][b]a)[/b] it is positioned directly adjacent to terrain in two or more directions, or
[br][b]b)[/b] it is directly surrounded by three or more creatures of the same (or bigger) size, or
[br][b]c)[/b] common sense dictates that it should be.
[/container]

[container:statusblock]
[h4|Isolated]Isolated[/h4]
A creature is isolated if its nearest ally is more than 4 meters away.
[br]Creatures with the tag [i]Colossus[/i] are immune.
[/container]

[container:statusblock]
[h4|Unconscious]Unconscious[/h4]
[i]See also: [url:wounds#Unconsciousness]Wounds[/url][/i]
[br]Cannot take actions or reactions and counts as [url:#Prone]Prone[/url]. [url:def#AttackAction]Attack Actions[/url] against an unconscious creature automatically hit. All [section:clr-save]Saves[/section] (except [section:clr-attr]CON[/section] saves) automatically fail.
[br][b][section:clr-save]Save[/section]:[/b] [b][section:clr-attr]CON[/section][/b] vs [section:clr-zahl]10[/section] [url:core#Hindered]hindered[/url] by [section:clr-zahl][total wounds * 2][/section] at the start of the turn and when taking damage or receiving healing.
[br][i]This save is only possible if the [url:values#Wounds]Wound Limit (WL)[/url] has not been reached.[/i]
[/container]

[hr]

[h1|BonusesAndPenalties]Bonuses & Penalties[/h1]
[h2]Info[/h2]
If not specified otherwise or upheld by [section:clr-conc]Concentration[/section], bonuses and penalties end after [section:clr-value]one application[/section], or after [section:clr-value]one Phase[/section] if they are not applied.
[br]Bonuses and penalties can be [i]cleansed[/i] by specific spells or items. Their [section:clr-dc]DC[/section] equals [section:clr-value]10 + X[/section].

[container:statusblock]
[h4|AttackBonus]Attack Bonus X[/h4]
[section:clr-support]SUPPORT[/section]
[br]The next basic attack roll is [/b] [url:core#Eased]eased[/url] by [b][section:clr-value]X[/section][/b].
[br][i]If not upheld with Concentration:[/i]
[/container]

[container:statusblock]
[h4|AttackPenalty]Attack Penalty X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]The next basic attack roll is [url:core#Hindered]hindered[/url] by [b][section:clr-value]X[/section][/b].
[/container]

[container:statusblock]
[h4|DamageBonus]Damage Bonus X[/h4]
[section:clr-support]SUPPORT[/section]
[br]The damage roll of the next basic attack is increased by [b][section:clr-value]X[/section][/b].
[br][i]Ends after the next basic attack, regardless of its success.[/i]
[/container]
[container:statusblock]
[h4|DamagePenalty]Damage Penalty X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]The damage roll of the next basic attack is decreased by [b][section:clr-value]X[/section][/b].
[br][i]Ends after the next basic attack, regardless of its success.[/i]
[/container]

[container:statusblock]
[h4|DefenseBonus]Defense Bonus X[/h4]
[section:clr-support]SUPPORT[/section]
[br]The next block, dodge, or parry roll is [url:core#Eased]eased[/url] by [b][section:clr-value]X[/section][/b].
[/container]
[container:statusblock]
[h4|DefensePenalty]Defense Penalty X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]The next block, dodge, or parry roll is [url:core#Hindered]hindered[/url] by [b][section:clr-value]X[/section][/b].
[/container]

[container:statusblock]
[h4|HealingBonus]Healing Bonus X[/h4]
[section:clr-support]SUPPORT[/section]
[br]One instance of incoming [section:clr-healing]Healing[/section] is increased by [b][section:clr-value]X[/section][/b].
[br][i]HoT effects like [url:#Regeneration]Regeneration[/url] are not affected.[/i]
[/container]
[container:statusblock]
[h4|HealingPenalty]Healing Penalty X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]One instance of incoming [section:clr-healing]Healing[/section] is decreased by [b][section:clr-value]X[/section][/b].
[br][i]HoT effects like [url:#Regeneration]Regeneration[/url] are not affected.[/i]
[/container]

[container:statusblock]
[h4|MovementBonus]Movement Bonus X[/h4]
[section:clr-support]SUPPORT[/section]
[br]MS is increased by [b][section:clr-value]X[/section][/b] for the next Movement Action.
[/container]
[container:statusblock]
[h4|MovementPenalty]Movement Penalty X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]MS is decreased by [b][section:clr-value]X[/section][/b] for the next Movement Action.

[/container]
[container:statusblock]
[h4|SaveBonus]Save Bonus X[/h4]
[section:clr-support]SUPPORT[/section]
[br]The next save is [url:core#Eased]eased[/url] by [b][section:clr-value]X[/section][/b].
[br][i]Only applies to non-status effect saves.[/i]
[/container]
[container:statusblock]
[h4|SavePenalty]Save Penalty X[/h4]
[section:clr-affliction]AFFLICTION[/section]
[br]The next save is [url:core#Hindered]hindered[/url] by [b][section:clr-value]X[/section][/b].
[br][i]Only applies to non-status effect saves.[/i]
[/container]