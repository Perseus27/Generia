[h1|General]General[/h1]
[h3|Round]Round[/h3]
A combat round comprises one [url:#Turn]turn[/url] for every combatant. Each combatant can take only one turn per round. Turn order within a combat round is determined by [url:values#Initiative]Initiative[/url].
[br]The round ends once every combatant has finished their turn; a new round begins if at least two opposing sides remain able to fight.
[br][i]A combat round represents about 6 seconds of “real time.”[/i]

[h3|Turn]Turn[/h3]
Each combatant has one [url:#AttackAction]Attack Action[/url], one [url:#UtilityAction]Utility Action[/url], and one [url:#MovementAction]Movement Action[/url] per turn.
[br]A creature has one turn per [url:#Round]combat round[/url]. A turn ends once the creature has taken or forfeited all of its actions.

[h3|Phase]Phase[/h3]
A [i]Phase[/i] is a period of roughly [section:clr-value]15 minutes[/section]. This unit matters only outside of combat.

[h1|Combat]Combat[/h1]
[h3|Actions]Actions[/h3]
[h4|AttackAction]Attack Action[/h4]
An Attack Action can take [i]one[/i] of the following forms:
[ul]
[li]A [url:#BasicAttack]basic attack[/url] with an equipped weapon[/li]
[li]An offensive skill[/li]
[li]An offensive spell[/li]
[li]A [url:#Grappling]grapple[/url][/li]
[li]Item usage[/li]
[/ul]

[h4|UtilityAction]Utility Action[/h4]
A Utility Action can take [i]one[/i] of the following forms:
[ul]
[li]A defensive or utility skill[/li]
[li]A defensive or utility spell[/li]
[li]Weapon swap[/li]
[li]Item usage[/li]
[/ul]

[h4|MovementAction]Movement Action[/h4]
A Movement Action can take [i]one[/i] of the following forms:
[ul]
[li]Movement (up to the acting creature’s maximum [url:values#MS]Movement Speed[/url])[/li]
[li]A movement skill[/li]
[li]A spell with the tag [section:clr-movement]MOVEMENT[/section][/li]
[/ul]

[h3|Reaction]Reaction[/h3]
Each combatant has [b]one[/b] possible [b][section:clr-reaction]reaction[/section][/b] during [i]every[/i] combatant’s [url:#Turn]turn[/url]. A reaction can take [i]one[/i] of the following forms:
[ul]
[li]A reactive skill[/li]
[li]A reactive spell[/li]
[/ul]

[h3|FreeAction]Free Action / Reaction[/h3]
Some abilities can be used as [i]Free Actions[/i] or [i]Free Reactions[/i]. A creature has an unlimited amount of Free Actions during its own turn, and an unlimited amount of Free Reactions at any point in or out of combat.

[h3|HiddenAction]Hidden Action[/h3]
Some skills and spells can be used as a [i]hidden action[/i]; the action specifies a governing [section:clr-attr]attribute[/section]. Other creatures may attempt a [section:clr-attr]PER[/section] check against the action attribute’s [section:clr-dc]DC[/section] to identify the action.

[h2|BasicAttack]Basic Attack[/h2]
[h3|MeleeAttack]Melee Attack[/h3]
A melee attack is a simple attack with a combatant’s melee weapon against a target in reach.
[br][b]Procedure:[/b]
[ol]
[li]Attacker rolls [b][section:clr-roll]1d20[/section][/b] + [url:values#AttackValue]Attack Value[/url][/li]
[li]Defender may [url:#Dodge]dodge[/url], [url:#Parry]parry[/url], or [url:#Block]block[/url] the rolled value[/li]
[/ol]
If the defender fails to dodge or parry, they take damage equal to the attacker’s rolled [url:#WeaponDamage]weapon damage[/url].

[h3|RangedAttack]Ranged Attack[/h3]
[b]See [url:/generia/rules/combat/ranged-combat]Ranged Combat[/url] for details.[/b]
[br]A ranged attack, like a [url:#MeleeAttack]melee attack[/url], is a simple attack with a ranged weapon against a target within range.
[br][b]Procedure:[/b]
[ol]
[li]Attacker rolls [b][section:clr-roll]1d20[/section][/b] + [url:values#AttackValue]Attack Value[/url] (see [url:/generia/rules/combat/ranged-combat]Ranged Combat[/url] for Advantage, etc.)[/li]
[li]Defender may [url:#Dodge]dodge[/url] the rolled value (see [url:/generia/rules/combat/ranged-combat]Ranged Combat[/url] for Advantage, etc.)[/li]
[/ol]
If the defender fails to dodge, they take damage equal to the attacker’s rolled [url:#WeaponDamage]weapon damage[/url].

[h3|Block]Block[/h3]
The defender attempts to intercept an incoming attack with a weapon or shield.
[br]Roll the block check ([url:values#BlockValue][b]Block Value[/b][/url] + [b][section:clr-roll]1d12[/section][/b]) and compare it to the attacker’s roll.
[ul]
[li][b]Block roll ≥ attack roll:[/b]
[br]Block succeeds. Incoming damage is reduced by [url:values#BlockStrength]Block Strength[/url].[/li]
[li][b]Block roll < attack roll:[/b]
[br]Block fails. Defender takes full damage.[/li]
[/ul]

[h3|Parry]Parry[/h3]
The defender attempts to deflect an incoming attack with their own weapon.
[br]First, roll the parry check ([url:values#ParryValue][b]Parry Value[/b][/url] + [b][section:clr-roll]1d12[/section][/b]) and compare it to the attacker’s roll.
[ul]
[li][b]Parry roll ≥ attack roll[/b] and [b][section:clr-roll]d12[/section] ≥ 10[/b]:
[br]Perfect parry; defender takes no damage.[/li]
[li][b]Parry roll ≥ attack roll[/b] and [b][section:clr-roll]d12[/section] < 10[/b]:
[br]Parry succeeds; defender chooses the hit zone.
[br]Defender may roll another [b][section:clr-roll]d12[/section][/b]. If it meets or exceeds the previous result, they take no damage.[/li]
[li][b]Parry roll < attack roll:[/b]
[br]Parry fails; defender takes full damage.[/li]
[/ul]
After parrying, the defender has four options:
[ol]
[li]Do nothing[/li]
[li]Move [section:clr-value]2[/section] meters*[/li]
[li]Reduce the opponent’s next defense roll by [[section:clr-value]weapon proficiency value[/section]][/li]
[li]Use [url:skills1#Counter][i]Counter[/i][/url], if learned[/li]
[/ol]
*The attacker’s [url:perksC#Opportunist][i]Opportunist[/i][/url] perk is not triggered, but nearby enemies’ may be.

[h3|Dodge]Dodge[/h3]
Characters can [i]dodge[/i] weapon attacks and projectiles. To succeed, match the attack roll with [b][section:clr-attr]DEX-MOD[/section] + [section:clr-attr]PER-MOD[/section] + [section:clr-roll]1d12[/section][/b]. On success, all damage is avoided; on failure, the character takes full damage.

[h3|WeaponDamage]Weapon Damage (Melee)[/h3]
Melee weapon damage consists of:
[ul]
[li]The weapon’s base damage value[/li]
[li][b][section:clr-attr]STR-MOD[/section][/b] multiplied by the weapon’s damage rating ([b]DR[/b]) (e.g., for a rapier [b][section:clr-attr]STR-MOD[/section] * 0.5[/b])[/li]
[li]Any bonuses from skills, rituals, or spells[/li]
[/ul]
For ranged weapon damage, please refer to [url:/generia/rules/combat/ranged-combat]Ranged Combat[/url].

[h3|Hit]Hit[/h3]
An attack is a [i]hit[/i] if it overcomes the target’s [url:values#AV]Armor Value (AV)[/url] or [url:values#MD]Magic Defense (MD)[/url].

[h3|HitZone]Hit Zone[/h3]
The [i]hit zone[/i] of a successful [url:#MeleeAttack]melee attack[/url] or projectile attack is determined by a [section:clr-roll]1d10[/section] roll:
[ul]
[li]1–5: Torso[/li]
[li]6–7: Arms[/li]
[li]8–9: Legs[/li]
[li]10: Head[/li]
[/ul]

[h3|Backstab]Backstab[/h3]
Attacks from outside the target’s field of view count as [i]backstabs[/i].
[br]Each attack counted as a backstab has [url:core#Advantage]Advantage 1[/url] on the attack roll.

[h3|MountedCombat]Mounted Combat[/h3]
Rider and mount always act simultaneously on the rider’s Initiative.
[h4]Attacks[/h4]
All [url:#BasicAttack]basic[/url] and [url:#RangedAttack]ranged[/url] attacks made from the back of a mount have [url:core#Disadvantage]Disadvantage 1[/url] if the mount moved this turn.
[h4]Defense[/h4]
Mounted [url:#Dodge]dodge[/url] checks have [url:core#Disadvantage]Disadvantage 1[/url] but are [url:core#Eased]eased[/url] by the value of the [url:/w/generia-perseus27/a/fertigkeiten-E28093-zivil-article]civil skill[/url] [i]Riding[/i]. Use the mount’s [section:clr-attr]DEX[/section].
[br]The rider can [url:#Block]block[/url] and [url:#Parry]parry[/url] basic attacks normally, even if the attack targets the mount.
[h4]Movement[/h4]
The mount gains one free movement or sprint action per rider turn. To perform an additional [url:#Actions]action[/url] (attack or utility), the rider must spend one of their own actions.

[h1|Magic]Magic[/h1]
[h3|EtherealEffects]Ethereal Effects[/h3]
If not otherwise specified in the spell description, most spells and [url:/generia/rules/magic/freecasting]freecasts[/url] produce [i]ethereal[/i] effects. This means that any objects or elements conjured dissolve into pure mana after [section:clr-value]one Phase[/section] has passed, or earlier at the caster's discretion. If the summoned object has been consumed or otherwise absorbed by a non-ethereal creature or object, it takes [section:clr-value]1d6 absolute damage per spell tier[/section] once the Phase ends.
[br]For example, the water produced by a wizard's [url:/w/generia-perseus27/a/wizard-spells-E28093-kinetics-article#WaterJet]Water Jet[/url] cannot be used to permanently fill a pond. However, if the wizard instead uses [url:/w/generia-perseus27/a/wizard-spells-E28093-kinetics-article#KineticManipulation]Kinetic Manipulation[/url] to draw pre-existing groundwater to the surface, it will not disappear.
[br][i]Stone spells are usually not ethereal.[/i]

[h3|Foci]Foci[/h3]
If not otherwise specified, all spellcasting traditions require specific [url:ench#Focus]enchanted[/url] items to channel magic. If a caster does not have access to their focus, they have [url:core#Disadvantage]Disadvantage 1[/url] on all magic-related rolls, and all targets have [url:core#Advantage]Advantage 1[/url] on all [section:clr-save]saves[/section] against their magic.

[h2|SpellTypes]Spell Types[/h2]
[h3|SA]Spell Attack ([section:clr-sa]SA[/section])[/h3]
A [i]spell attack[/i] sets the target value for a successful [url:core#Save]save[/url] against a spell’s effects. Its attack value is [section:clr-roll]1d20[/section] plus the attribute modifier listed in the syntax.
[h4]Syntax[/h4]
[section:clr-sa]SA[/section] [section:clr-attr]Attack Attribute Modifier[/section] vs [section:clr-attr]Save Attribute Modifier[/section]

[h3|PA]Projectile Attack ([section:clr-pa]PA[/section])[/h3]
Projectile attacks are similar to most [url:#RangedAttack]ranged attacks[/url]. They can be [url:def#Dodge]dodged[/url] like regular projectiles, [url:def#Block]blocked[/url] with a shield, and sometimes parried if the character has the necessary perks. Their attack value is [section:clr-roll]1d20[/section] plus the attribute modifier listed in the syntax.
[h4]Syntax[/h4]
[section:clr-pa]PA[/section] [section:clr-attr]Attribute Modifier[/section]

[h3|SD]Spell Defense ([section:clr-sd]SD[/section])[/h3]
A [i]Spell Defense[/i] roll is used by defensive spells that counter enemy melee attacks and projectiles (magical or mundane), e.g., [i]Arcane Barrier[/i].
[br]Like other defensive options ([url:#Block]Block[/url], [url:#Dodge]Dodge[/url], [url:#Parry]Parry[/url]), it uses [section:clr-roll]1d12[/section] plus the attribute modifier(s) in the syntax. If the result meets or exceeds the attack value, the defensive spell takes effect.
[h4]Syntax[/h4]
[section:clr-sd]SD[/section] [section:clr-attr]Attribute Modifier(s)[/section]

[h3|DC]Determined Cast ([section:clr-dc]DC[/section])[/h3]
[i]See [url:core#DC]Determined Check[/url].[/i]
In regards to spell usage, a [i]determined cast[/i] is a simplified [url:#SA]Spell Attack[/url] that uses a flat [section:clr-value]10[/section] instead of a [section:clr-roll]1d20[/section] roll.
[h4]Syntax[/h4]
[section:clr-dc]DC[/section] [section:clr-attr]Attack Attribute Modifier[/section] vs [section:clr-attr]Save Attribute Modifier[/section]
[h4]DC+[/h4]
The [section:clr-dc]DC+[/section] is a special type of Determined Cast, where a [section:clr-roll]1d20[/section] is rolled to determine the result, but any die result below [section:clr-value]10[/section] is ignored and considered a fixed [section:clr-value]10[/section].

[h3|Surecast]Surecast[/h3]
A [i]Surecast[/i] spell does not require an initial check from either caster or target, but may require a roll determining the effect, e.g. [i]Shield[/i]. Most [section:clr-support]support[/section] spells are Surecast spells.
[h4]Syntax[/h4]
[section:clr-surecast]SURECAST[/section]

[h2|SpellKeywords]Spell Keywords[/h2]
[h3|Affliction]Affliction[/h3]
Spells with the keyword [b][section:clr-affliction]AFFLICTION[/section][/b] usually cause negative status effects.

[h3|Concentration]Concentration[/h3]
Spells with the keyword [b][section:clr-conc]CONCENTRATION[/section][/b] maintain their effects as long as the caster can concentrate on the spell.
[br]A creature can concentrate on only one spell at a time unless modified by perks.
[br]A creature may freely choose on its turn or at any time as a [b][section:clr-reaction]reaction[/section][/b] to end [section:clr-conc]Concentration[/section].
[br]When the caster is [url:#Hit]hit[/url], they must succeed on a [b][section:clr-attr]CON[/section][/b] or [b][section:clr-attr]WIL[/section][/b] save (“concentration save”) equal to half the incoming damage or [section:clr-value]10[/section], whichever is higher. On a failure, concentration ends.

[h3|Control]Control[/h3]
Spells with the keyword [b][section:clr-control]CONTROL[/section][/b] usually cause some form of crowd control through status effects, zoning or displacement.

[h3|Field]Field[/h3]
Spells with the keyword [b][section:clr-field]FIELD[/section][/b] trigger their effect when a creature enters a square within the radius or begins its turn there.
[br]The effect is triggered again for every subsequent square entered.

[h3|Heal]Heal[/h3]
Spells with the keyword [b][section:clr-heal]HEAL[/section][/b] usually provide magical healing.

[h3|Meta]Meta[/h3]
Spells with the keyword [b][section:clr-meta]META[/section][/b] usually interact with other spells instead of directly with creatures or the environment.

[h3|Movement]Movement[/h3]
Spells with the keyword [b][section:clr-movement]MOVEMENT[/section][/b] usually cause the caster to change position in some way.

[h3|Ritual]Ritual[/h3]
Spells with the keyword [b][section:clr-ritual]RITUAL[/section][/b] can be cast only outside of combat and usually require several minutes to hours (or even days) of preparation. In return, their effects are comparatively strong or last a long time.

[h3|Support]Support[/h3]
Spells with the keyword [b][section:clr-support]SUPPORT[/section][/b] usually cause positive status effects.

[h3|Terrain]Terrain[/h3]
Spells with the keyword [b][section:clr-terrain]TERRAIN[/section][/b] usually shape the battlefield in a physical manner.

[h3|Zone]Zone[/h3]
Spells with the keyword [b][section:clr-zone]ZONE[/section][/b] trigger their effect when a creature enters the radius or begins its turn there.

[h3|Upcast]Upcast[/h3]
If a spell has the [b][section:clr-upcast]UPCAST X[/section][/b] keyword, the caster can amplify the spell for increased [section:clr-mp]MP[/section] cost. MP costs increase roughly following the Fibonacci sequence; the effect increases linearly.
[br][b]Example:[/b]
[br][i]Arcane Barrier[/i] has the keyword [b][section:clr-upcast]UPCAST 5[/section][/b]. Upcasting produces the following result:
[table][tr][th]Cast Level[/th][th]Cost (MP)[/th][th]Effect[/th][/tr]
[tr][td]1[/td]
[td][b][section:clr-mp]1[/section][/b][/td]
[td][b][section:clr-roll]1d6[/section][/b][/td]
[/tr]
[tr][td]2[/td]
[td][b][section:clr-mp]2[/section][/b][/td]
[td][b][section:clr-roll]2d6[/section][/b][/td]
[/tr]
[tr][td]3[/td]
[td][b][section:clr-mp]3[/section][/b][/td]
[td][b][section:clr-roll]3d6[/section][/b][/td]
[/tr]
[tr][td]4[/td]
[td][b][section:clr-mp]5[/section][/b][/td]
[td][b][section:clr-roll]4d6[/section][/b][/td]
[/tr]
[tr][td]5[/td]
[td][b][section:clr-mp]8[/section][/b][/td]
[td][b][section:clr-roll]5d6[/section][/b][/td]
[/tr][/table]

[h1|Misc]Movement and Miscellaneous[/h1]
[h3|Sneaking]Sneaking[/h3]
To move unseen, a creature makes an [b][section:clr-attr]DEX[/section] check[/b] against the opponent’s [b][section:clr-attr]PER[/section]-[section:clr-dc]DC[/section][/b] [i]([section:clr-attr]PER-MOD[/section] + 10)[/i].
[br]Apply:
[ul]
[li][b]Total cover:[/b] +2 Advantage[/li]
[li][b]Full cover:[/b] +1 Advantage[/li]
[li][b]Half cover:[/b] +0 Advantage[/li]
[li][b]No cover:[/b] −1 Advantage[/li]
[li][b]Open field:[/b] −2 Advantage[/li]
[/ul]
Use the least-covered square the creature crosses within the opponent’s line of sight for the check.
[br]Additionally, consider the lighting conditions. Dim light grants an additional [section:clr-value]+1 Advantage[/section], while total darkness grants [section:clr-value]+2[/section].

[h3|Jumping]Jumping[/h3]
A creature can attempt to jump to any spot using any action. First determine the [i]jump score[/i] ([b][section:clr-attr]STR-MOD[/section][/b] + [b][section:clr-attr]DEX-MOD[/section][/b] + [section:clr-roll]1d20[/section]).
[br]If the jump score exceeds [b](jump height * 4) + (jump distance * 2)[/b], the jump succeeds. If it is lower than [b]((jump height * 4) + (jump distance * 2)) * 2[/b], the creature becomes [url:status#OffBalance]off-balance[/url].
[h4]Example[/h4]
A creature wants to jump 2 meters high and 6 meters far, so the DC is b + (6*2) = 20[/b].
[br]To land without losing balance, meet twice that value: [b]40[/b].

[h3|FallDamage]Fall Damage[/h3]
Falling creatures take [section:clr-roll-noex]1d4[/section] [url:dmgtype#Absolute]absolute[/url] damage for every meter of fall distance. The total damage is increased by [section:clr-value]1[/section] for each point of [i]Total Weight[/i] above the [i]Carry Limit[/i].
[h4|FallCheck]Fall Check[/h4]
When a creature begins to fall, it may attempt a fall check ([section:clr-attr]DEX-MOD[/section] + [section:clr-value][i]Athletics[/i][/section]) against the highest of these values, if they are applicable:
[ul]
[li]the [section:clr-dc]DC[/section] of whatever caused the fall[/li]
[li][section:clr-value]half[/section] of the incoming damage of the attack that caused the fall[/li]
[li][section:clr-value]10[/section] (default)[/li]
[/ul]
On success, the creature manages to stabilize itself during the fall and reduces the falling distance considered for the damage calculation by [section:clr-attr]DEX-MOD[/section].
[br][b]Example:[/b]
[br]Creature X has an [section:clr-attr]DEX-MOD[/section] of [section:clr-value]3[/section] and falls [section:clr-value]5 meters[/section]. If it fails the fall check, it takes [section:clr-roll-noex]5d4[/section] absolute damage. If it succeeds, it only takes [section:clr-roll-noex]2d4[/section] absolute damage.

[h3|Grappling]Grappling[/h3]
A creature with suitable limbs may, as an Attack Action, attempt to grab another creature and immobilize it.
[br]First the grappler must succeed on an unarmed [url:#MeleeAttack]melee attack[/url]. This attack deals no damage.
[br]If the target fails to parry or dodge, it becomes [url:status#Grappled]grappled[/url].