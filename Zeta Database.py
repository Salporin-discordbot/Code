import asyncio
import discord
from discord.ext import commands


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)
embed=discord.Embed
FIRST_ORDER_COLOR = 5447450
EMPIRE_COLOR = 328965
JEDI_COLOR = 4624416
REBEL_COLOR = 14312485
REPUBLIC_COLOR = 16777215
RESISTANCE_COLOR = 16729344
SITH_COLOR = 9045767
NIGHTSISTER_COLOR = 11484517
BOUNTY_COLOR = 14198054


@bot.event
async def on_server_join(server):
    embed=discord.Embed(title='Thanks for inviting me!', color=discord.Colour(0x9CD3E8), description="Hi! Thanks for adding me to your server. I'm Salporin. To see my commands, and explanations, type: `!commands`. If you have any questions, you can join the official server: https://discord.gg/8pFJVWN. Cheers!")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/302116840199684096/308138975111938048/SALPORIN_002.png?width=300&height=300")
    await bot.send_message(server, embed=embed)
    
@bot.event
async def on_member_join(member):
    joinserver=member.server
    text001="**{}**, welcome to ".format(member)
    text002=text001 + "**{}**. Have a great time here!".format(joinserver)
    embed=discord.Embed(title='Member joined', color=discord.Colour(0x9CD3E8), description=text002)
    embed.set_thumbnail(url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/103/waving-hand-sign_1f44b.png")
    await bot.send_message(joinserver, embed=embed)    
    

@bot.event
async def on_message(message):
    if message.content.startswith('!zKylo') or message.content.startswith ('!zKylo-Ren'):
        embed=discord.Embed(title="Zeta Kylo Ren --- Outrage",color = FIRST_ORDER_COLOR, description=" Deal Physical damage to target enemy, and, if Kylo has full Health, inflict Stun for 1 turn. This attack deals 75% more damage if Kylo is below full Health. Recover Protection equal to the damage dealt.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_kyloren_special01.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_kyloren.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 16<:omega:327437590657499137> and 40<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Awesome in Arena and GW. Also, able to solo P1 of hAAT.")
        
        await bot.send_message(message.channel, embed=embed)
          
    if message.content.startswith('!zFOTP'):
        embed=discord.Embed(title="Zeta First Order TIE Pilot --- Keen Eye",color = FIRST_ORDER_COLOR, description=" First Order TIE Pilot has +30% Critical Chance and +30% Critical Damage, and gains Advantage for 3 turns whenever an enemy falls below full Health. First Order TIE Pilot has a 70% chance to gain Foresight for 2 turns whenever he loses Advantage.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_firstordertiepilot.png") 
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13<:omega:327437590657499137> and 30<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Huge survivability in arena, big damage boost in raids, and great survivability in raids. In arena, FOTP dies first alot, so a Zeta would really boost your damage and survivability. He will be much harder to kill first.")
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith('!zGar-Saxon'):
        embed=discord.Embed(title="Zeta Gar Saxon --- Mandalorian Retaliation",color = EMPIRE_COLOR, description=" Whenever an Empire ally uses a basic attack, they recover 5% Health.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_gar_saxon.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10<:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Gar Saxon zeta allows to gain 5% hp on basic. Since Empire allies have 50% chance to counter, it can be a lot of hp that they gain back. BUT Zaul can apply daze and possibly shut your team down.")
        
        await bot.send_message(message.channel, embed=embed)
     
      
    if message.content.startswith('!Zeta'):
        embed=discord.Embed(title="Ability Material Zeta",color = 2440557, description=" Rare Ability Material, can be collected with the [Fleet Ability Materials Challenge](https://youtu.be/QaWo7Bl569g), or bought in Fleet Shipments.")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.skill_zeta.png")
        embed.add_field(name="Quantity", value="You need 20 Zeta Materials for 1 Zeta Upgrade.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        
        await bot.send_message(message.channel, embed=embed)

        
    if message.content.startswith('!Omega'):
        embed=discord.Embed(title="Ability Material Omega",color = 15386951, description="  A rare material used to upgrade character abilities beyond Level 70. This can only be obtained at Level 80 every day by completing all Daily Activities.")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.skill_pentagon_gold.png")
        embed.add_field(name="Quantity", value="You need 5 (or 3) Omega Materials for 1 Omega Upgrade, but you also need them for Zeta Upgrades.")         
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zYoda'):
        embed=discord.Embed(title="Zeta Grand Master Yoda --- Battle Meditation",color = JEDI_COLOR, description=" Yoda gains Tenacity Up and Foresight for 2 turns, then grants each other ally every positive status effect he has for 2 turns, with a 40% chance to also grant Yoda 35% Turn Meter. (Unique status effects can't be copied.)")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_yodagrandmaster_special02.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_yodagrandmaster.png")
        embed.add_field(name="Requirements", value="Level 84, 20<:zeta:327437604465278977>, 16<:omega:327437590657499137> and 40<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Provides greater survivability in arena and is a solid, though not required, investment for a zQGJ Jedi team. Not required for raid content.")
        
        await bot.send_message(message.channel, embed=embed)

           
    if message.content.startswith('!zYoda'):
        embed=discord.Embed(title="Zeta Grand Master Yoda --- Grand Master's Guidance",color = JEDI_COLOR, description=" Jedi allies gain 30% Tenacity, gain 30% Turn Meter whenever they resist a debuff, and whenever they suffer a debuff they gain Tenacity Up for 1 turn at the end of that turn.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_removeharmful.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_yodagrandmaster.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10<:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Great for preventing debuffs from growing out of control and turning them into turn meter gain. Tenacity Up after a debuff helps prevent more debuffs from being applied. This then works with the other part of his ability that gives TM for each debuff resisted. Tenacity Up effectively turns every new potential debuff into 30% TM.")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('!zJyn'):
        embed=discord.Embed(title="Zeta Jyn Erso --- Into the Fray",color = REBEL_COLOR, description=" Rebel allies have +35% Potency and recover 5% Protection whenever they gain a buff. Enemies that suffer debuffs during Rebel allies' turns have a 50% chance to also become Exposed for 2 turns. This Expose can't be resisted.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_jyn.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10<:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Jyn is meant to use in a Rogue One team. This zeta is mostly used in Arena, in combination with Zeta Cassian (`!Groundwork`). If you have the entire Rogue One team maxed out, then this Zeta might be a good choice for you!")
        
        await bot.send_message(message.channel, embed=embed)            
         
    if message.content.startswith('!zJyn'):
        embed=discord.Embed(title="Zeta Jyn Erso --- Fierce Determination",color = REBEL_COLOR, description=" Jyn is immune to Stun and gains 10% Potency each time she scores a Critical Hit.")
        embed.set_thumbnail(url="http://i.imgur.com/27YCJB8.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_jyn.png")
        embed.add_field(name="Requirements", value="Level 84, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="This upgrade only adds that Jyn will be immune to Stun. That's not a real big upgrade, but if you want her to be even more solid in raids, or just improve her arena stats, then do it!")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zK-2SO'):
        embed=discord.Embed(title="Zeta K-2SO --- Reprogrammed Imperial Droid",color = REBEL_COLOR, description="K-2SO has +97.6% Counter Chance. This chance is halved while K-2SO is debuffed. In adition, K-2SO gains 1% Max Protection whenever he takes damage.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_k2so.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="When K2 has his zeta ability, he gains 1% Max Protection whenever he takes damage, that means -> if he took damage 10 times, he gains 10% Max Protection. And he still has 97.6% Counter chance from his previous upgrades, but sadly it will be halved if he has a debuff! :frowning:. This zeta will not affect your team a lot, so zeta'ing K2 is highly discouraged.")        
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zLuminara-Unduli'):
        embed=discord.Embed(title="Zeta Luminara Unduli --- Elegant Steps",color = JEDI_COLOR, description="Jedi Allies gain 15% Evasion and recover Health equal to 8% of Luminara's Max Health at the start of each of their turns. Non-Jedi allies receive half of the Evasion bonus and Heal Effect. Whenever any ally gains a buff they do not have, they gain a Heal Over Time effect for 2 turns.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_dodge.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_luminara.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zPao'):
        embed=discord.Embed(title="Zeta Pao --- For Pipada",color = REBEL_COLOR, description="Whenever a Rebel ally uses a basic attack, reduces Pao's cooldowns by 1 and Pao gains 5% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_pao.png")
        
        await bot.send_message(message.channel, embed=embed)
        

    if message.content.startswith('!zQGJ'):
        embed=discord.Embed(title="Zeta Qui-Gon Jinn --- Agility Training",color = JEDI_COLOR, description="Jedi Allies have +30 Speed, gain Offense equal to 3 times their Speed, and gain Foresight for 2 turns at the start of each encounter and whenever any unit is defeated.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_quigon.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zR2D2'):
        embed=discord.Embed(title="Zeta R2-D2 --- Combat Analysis",color = REPUBLIC_COLOR, description="While R2-D2 is active, all allies gain 10% Critical Chance and 10% Accuracy. While R2-D2 is active, whenever a Light Side ally scores a Critical Hit, dispel all debuffs on them.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_astromech_r2d2.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zR2D2'):
        embed=discord.Embed(title="Zeta R2-D2 --- Number Crunch",color = REPUBLIC_COLOR, description="At the start of battle, R2-D2 gains 10% Max Protection for each Droid ally, 10% Offense for each Galactic Republic ally, 10% Max Health for each Rebel ally, and 10% Potency for each Resistance ally. At the start of battle, and when R2-D2 revives, other Droid, Galactic Republic, Rebel, and Resistance allies gain 10% of R2-D2's Max Protection, Offense, Max Health, and Potency until R2-D2 is defeated.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_extraturn.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_astromech_r2d2.png")
        
        await bot.send_message(message.channel, embed=embed)


        
    if message.content.startswith('!zRey'):
        embed=discord.Embed(title="Zeta Rey --- Focused Strikes",color = RESISTANCE_COLOR, description="As long as she has no debuffs, Rey has +25% Offense and inflicts Daze for 2 turns whenever she uses a Special ability. This effect can't be Resisted.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_reyjakku.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zSavage'): 
        embed=discord.Embed(title="Zeta Savage Opress --- Brute",color = SITH_COLOR, description="Whenever Savage takes damage, he gains Offense Up, Defense Up, and Heal Over Time for 2 turns and gains 30% Turn Meter. At the end of his turns, Savage Dispels all debuffs on a random other Sith ally and gains those debuffs for 1 turn. Dispel all debuffs from Savage whenever he is Critically Hit.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_savageopress.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zStormtrooper'): 
        embed=discord.Embed(title="Zeta Stormtrooper --- Wall of Stormtroopers",color = EMPIRE_COLOR, description="Stormtrooper gains 40% Defense for each living Empire ally and 40% Offense for each defeated Empire ally. While Stormtrooper is active, Imperial Trooper allies have +30% Defense.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperstorm.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zAsajj'): 
        embed=discord.Embed(title="Zeta Asajj Ventress --- Nightsister Swiftness",color = NIGHTSISTER_COLOR, description="Nightsister allies gain 28 Speed, gain 50% Turn Meter when they fall below 100% Health, and have a 50% chance to remove 20% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ventress.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zAsajj'): 
        embed=discord.Embed(title="Zeta Asajj Ventress --- Rampage",color = NIGHTSISTER_COLOR, description="Whenever any ally or enemy is defeated, Asajj Ventress gains Offense Up and Critical Chance Up for two actions and gains 50% Turn Meter. Asajj Ventress gains 15 Speed for each enemy with no buffs.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ventress.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zBarriss'): 
        embed=discord.Embed(title="Zeta Barriss Offee --- Swift Recovery",color = JEDI_COLOR, description="At the end of each of her turns, Barriss Dispels all debuffs from the debuffed ally with the lowest Health and gains 10% Turn Meter for each effect removed. Whenever an ally is Critically Hit, that ally recovers 20% of their Max Health and Barriss gains 10% Turn Meter. This effect is disabled while Barriss is defeated.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_removeharmful.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_barriss_light.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zBoba"): 
        embed=discord.Embed(title="Zeta Boba Fett --- Bounty-Hunter's-Resolve",color = BOUNTY_COLOR, description="At the start of battle, and whenever he defeats an enemy, Boba Fett recovers 100% Protection and gains Bounty Hunter's Resolve until he is defeated. ***Bounty Hunter's Resolve***: Boba Fett ignores Taunts during his turn. When defeated, revive at 100% Health. This buff cannot be dispelled.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_mandalorian.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_bobafett.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zBodhi"): 
        embed=discord.Embed(title="Zeta Bodhi Rook --- Double Duty",color = REBEL_COLOR, description="While Bodhi is active, Rebel allies with Offense Up also gain +50% Defense. At the end of each of his turns, Bodhi grants Offense Up for 2 turns to a random ally who doesn't have it.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_bodhi.png")
        
        await bot.send_message(message.channel, embed=embed)

        
    if message.content.startswith("!zPhasma"): 
        embed=discord.Embed(title="Zeta Captain Phasma --- Fire at Will",color = FIRST_ORDER_COLOR, description="Whenever an ally attacks, they have a 20% chance to call a random ally to Assist. This chance is tripled if the attacking ally is First Order. If that ally had Advantage, they regain it for 2 turns. First Order allies gain Advantage for 2 turns at the start of each encounter, can't be Critically Hit while they have Advantage, and gain 20% Potency.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_leader_default.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_phasma.png")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zCassian"): 
        embed=discord.Embed(title="Zeta Cassian Andor --- Groundwork",color = REBEL_COLOR, description="At the start of each encounter all Rebel allies gain Protection Up (20%) for 3 turns, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel Tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_cassian.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zCody"): 
        embed=discord.Embed(title="Zeta CC-2224 Cody --- Ghost-Company-Commander",color=discord.Colour(0xED9E27), description="Clone allies gain 30% Critical Chance, and other allies gain half that amount. Cody gains 60% Defense for each living Clone ally and other Clone allies gain half that amount. Clone allies recover 5% of their Max Protection whenever they use a Basic ability.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_cody.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zChewbacca"): 
        embed=discord.Embed(title="Zeta Clone Wars Chewbacca --- Defiant Roar",color=discord.Colour(0x633820), description="Chewbacca dispels all debuffs from himself, recovers 50% of his Max Health, gains Defense Up for 3 Turns, and has a 50% Chance to gain 25% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_chewbacca_special02.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_chewbacca.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zDooku"): 
        embed=discord.Embed(title="Zeta Count Dooku --- Flawless Riposte",color = SITH_COLOR, description="Count Dooku has 100% Counter Chance. In addition, whenever he attacks outside of his turn, he deals 30% more damage, has a 25% chance to gain 45% Turn Meter, recovers 10% Protection, and gains Critical Hit Immunity for 1 turn.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_dooku.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zFives"): 
        embed=discord.Embed(title="Zeta CT-5555 Fives --- Tactical Awareness",color=discord.Colour(0x62779D), description="Fives has 85% Counter Chance and +50% Counter Damage. Fives gains 15% Turn Meter whenever another Clone ally takes damage and 7.5% Turn Meter whenever a non-Clone ally takes damage.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_fives.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zMaul"): 
        embed=discord.Embed(title="Zeta Darth Maul --- Dancing Shadows",color = SITH_COLOR, description="All Sith allies gain 20% Evasion, gain 20% Turn Meter and Stealth for 1 turn at the start of each encounter and whenever they Evade or are Critically Hit, can't be Critically Hit while Stealthed, and gain Advantage for 2 turns whenever Stealth expires. The Stealth and Turn Meter from this ability ignores Taunting allies.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_dodge.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_maul.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zNihilus"): 
        embed=discord.Embed(title="Zeta Darth Nihilus --- Lord of Hunger",color = SITH_COLOR, description="Sith allies gain 60% Offense and 150% Health Steal. Sith allies lose all Protection and gain that much Max Health. Sith allies are immune to Healing effects that aren't Health Steal and can't score Critical Hits.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_sith.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_nihilus.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zNihilus"): 
        embed=discord.Embed(title="Zeta Darth Nihilus --- Wound in the Force",color = SITH_COLOR, description="At the start of each of his turns, Nihilus inflicts Damage Over Time for 2 turns on a random enemy that doesn't have any debuffs. If all enemies are debuffed, inflict Damage Over Time on a random enemy. At the start of each enemy turn, Nihilus inflicts Health Down on them for 2 turns.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_kill.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_nihilus.png")
        
        await bot.send_message(message.channel, embed=embed) 


    if message.content.startswith("!zSidious"): 
        embed=discord.Embed(title="Zeta Darth Sidious --- Sadistic Glee",color = SITH_COLOR, description="Darth Sidious recovers 20% of his Max Health and gains 50% Turn Meter whenever any unit is defeated. In addition, he has +35% Evasion against Jedi attacks, +50% Potency, and gains Max Health equal to his Potency percentage.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_heal.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_sidious.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zVader"): 
        embed=discord.Embed(title="Zeta Darth Vader --- Inspiring Through Fear",color = EMPIRE_COLOR, description="Empire and Sith allies gain 30% Offense and have a 50% chance to remove 20% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted. While Darth Vader is alive, enemies immediately regain Damage Over Time for 2 turns whenever Damage Over Time expires on them.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_vader.png")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zDeath-Trooper"): 
        embed=discord.Embed(title="Zeta Death Trooper --- Krennic's Guard",color = EMPIRE_COLOR, description="Whenever Death Trooper scores a Critical Hit, he and Director Krennic recover 20% Health. Death Trooper has a 50% chance to gain 100% Turn Meter whenever Director Krennic takes damage. Director Krennic can't be Critically Hit while Death Trooper is alive. While Death Trooper is active, Imperial Trooper allies have +10% Health Steal.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_heal_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperdeath.png")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zKrennic"): 
        embed=discord.Embed(title="Zeta Director Krennic --- Director of Advanced Weapons Research",color = EMPIRE_COLOR, description="Empire allies gain 25% Critical Chance and 25% Potency. Debuffed enemies who are Critically Hit during an Empire ally's turn suffer Ability Block for 1 turn. This effect can't be Resisted. Empire allies recover 10% Protection whenever they score a Critical Hit.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_empire.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_krennic.png")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zFinn"): 
        embed=discord.Embed(title="Zeta Finn --- Balanced Tactics",color = RESISTANCE_COLOR, description="Resistance allies gain 30% Offense and 60% Defense, and other allies gain half that amount. Whenever a Resistance ally loses Foresight, they gain Advantage for 2 turns and whenever an enemy takes damage from Expose, reduce the cooldowns of all Resistance allies by 1 and grant them 35% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_finnjakku.png")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zFAT"): 
        embed=discord.Embed(title="Zeta Ahsoka Tano (Fulcrum) --- Whirlwind",color=discord.Colour(0xB6BBC1), description="Consume all buffs on Ahsoka and deal Physical damage to target enemy. This attack scores an additional hit for each type of buff consumed. The target can't Evade and has -50% Armor against this attack.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_ahsoka_adult_special02.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ahsokaadult.png")
        
        await bot.send_message(message.channel, embed=embed)

    
    if message.content.startswith("!zFOST"): 
        embed=discord.Embed(title="Zeta First Order Stormtrooper --- Return Fire",color = FIRST_ORDER_COLOR, description="First Order Stormtrooper has +65% Counter Chance. Whenever First Order Stormtrooper uses any Ability he has a 50% chance to call a random ally to Assist, dealing 50% damage unless they are First Order. Then, if it was a First Order ally, grant them Advantage for 2 turns.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_firstordertrooper.png")
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!zTarkin"): 
        embed=discord.Embed(title="Zeta Grand Moff Tarkin --- Callous Conviction",color = EMPIRE_COLOR, description="Grand Moff Tarkin gains 100% Defense equal to his Potency Percentage and 20% Potency per debuffed enemy.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_empire.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_tarkinadmiral.png")
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!zTarkin"): 
        embed=discord.Embed(title="Zeta Grand Moff Tarkin --- Tighten the Grip",color = EMPIRE_COLOR, description="Empire allies gain 30 Speed. Inflict Defense Down and Expose for 2 turns on enemies that fall below 100% Health during Empire allies' turn. This effect can't be Resisted.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_tarkinadmiral.png")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zVeers"): 
        embed=discord.Embed(title="Zeta General Veers --- Agressive Tactician",color = EMPIRE_COLOR, description="Whenever an enemy is defeated while Veers is active, Imperial Trooper allies gain Offense Up for 2 turns, gain 50% Turn Meter, and recover 10% Protection. While Veers is active, Imperial Trooper allies have +15% Critical Chance.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_veers.png")
        
        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith("!zThrawn"): 
        embed=discord.Embed(title="Zeta Grand Admiral Thrawn --- Legendary Strategist",color=discord.Colour(0x8EBEF4), description="Empire allies have +15% Max Protection, +25% Offense, and gain 20% Turn Meter whenever they Resist a detrimental effect or suffer a debuff. Whenever an Empire ally gains or loses a status effect, they recover 2% Protection. Empire allies gain a new Special ability, Maneuver: Dispel all debuffs on this character and gain 50% Turn Meter (Cooldown 3).")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_empire.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_thrawn.png")
        
        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith("!zThrawn"): 
        embed=discord.Embed(title="Zeta Grand Admiral Thrawn --- Ebb and Flow",color=discord.Colour(0x8EBEF4), description="Thrawn has +100% Counter Chance, +100% Tenacity, and -50% Speed while any enemies are Fractured. Whenever another Empire ally uses a Special ability while Thrawn is active, that ally gains 15% Turn Meter and, if any enemies are Fractured, Thrawn and Fractured enemies lose 15% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_extraturn.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_thrawn.png")
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith('!zPaploo'):   
        embed=discord.Embed(title="Zeta Paploo --- Don't Hold Back",color = discord.Colour(0xCD853F), description=" Whenever Paploo gains a status effect, he recovers 5% Health and Protection. Whenever Paploo gains Stealth, dispel Stealth and gain Taunt for 2 Turns. Paploo has +25% Speed whenever he does not have Taunt active.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://media.discordapp.net/attachments/331116027335147530/341612670572560384/tex.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13<:omega:327437590657499137> and 30<:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Ewok Tank, who will gain health with Buffs and Taunts to protect his Furry Friends")
        
        await bot.send_message(message.channel, embed=embed)        
    
#beginning of characters database

    if message.content.startswith("!Aayla-Secura"): 
        embed=discord.Embed(title="**Aayla Secura**",color=discord.Colour(0x5693B8), description="Versatile attacker with high survivability through Dodge, Hitpoints, and self healing.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_aaylasecura.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/f/f9/Aayla.jpg/revision/latest?cb=20120815094201")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability.")
        embed.add_field(name="Stats", value="`Power: 8851` `Speed: 125` `Health: 21490` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Inspiring Strike - <:basicaayla:329902968042160133>", value="Deal Physical damage to target enemy with a 35% chance to call an ally to Assist. If the assisting ally is a Jedi, they deal 50% more damage.")
        embed.add_field(name="Special Ability - Survivor - <:specialaayla:329908683767021568>", value="Deal Physical damage to target enemy and recover Health equal to 65% of the damage dealt.")
        embed.add_field(name="Leader Ability - Jedi Valor - <:leaderaayla:329908683448254464>", value="Jedi allies gain 40% Tenacity and recover 10% of their Max Health when they ward off an effect.")
        embed.add_field(name="Unique Ability - Superior Riposte - <:uniqueaayla:329908683385339914>", value="Aayla has +10% Critical Chance, 65% Counter Chance and +50% Counter Damage. In addition, she Stuns her target for 1 turn whenever she critically hits.")
        embed.add_field(name="Usage", value="She is amazing in a team led by Ima-Gun, her self heal is pretty epic and she stuns like a b*tch.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")

        await bot.send_message(message.channel, embed=embed)

        
    if message.content.startswith("!Admiral-Ackbar"): 
        embed=discord.Embed(title="**Admiral Ackbar**",color=discord.Colour(0xB98D6D), description="Rebel Support that can Dispel debuffs and grant allies extra turns. <:Ackbaricon:331668407072063488>")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ackbaradmiral.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="http://img11.deviantart.net/f5fa/i/2010/065/8/e/admiral_ackbar_by_quibly.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability.")
        embed.add_field(name="Stats", value="`Power: 9050` `Speed: 119` `Health: 17520` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Quick Shot - <:ackbarbasic:331746458996965377>", value="Deal Physical damage to target enemy with a 55% chance to gain 45% Turn Meter.")
        embed.add_field(name="Special Ability - It's a Trap! - <:ackbarspecial1:331746459194097674>", value="Dispel all negative status effects from all allies. Each ally recovers 9% of their Max Health for each effect dispelled this way. Admiral Ackbar has a 25% chance to gain 40% Turn Meter.")
        embed.add_field(name="Special Ability - Tactical Genius - <:ackbarspecial2:331746458934181891>", value="Ackbar grants each ally the Tactical Genius effect. The first ally to use a Special ability while they have this effect gains 100% Turn Meter and recovers 30% of their Max Health. Tactical Genius ends whenever any ally triggers this effect or at the end of Ackbar's next turn.")
        embed.add_field(name="Leader Ability - Rebel Coordination - <:ackbarleader:331746459177320450>", value="Rebel allies have +25 Speed and +10% Tenacity. In addition, whenever an ally uses an ability that isn't an attack, they call a Rebel ally to Assist.")
        embed.add_field(name="Usage", value="He is good as rebel leader, however i would recommend wedge lead instead of him in Arena and in Galactic War. His **It's a trap!** ability is also nice for P1 Tank raid, becouse it heals pretty much when there are lots of debuffs. Also, the **Tactical Genius** effect can be super effective (See that pokemon reference) if it is used on the right way. (like Lando double down hitting twice) I also really needed him to complete The Emperor's Desmise (The event to unlock Palpatine). He is pretty handy in PVE too.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")


        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith("!Ahsoka-Tano"): 
        embed=discord.Embed(title="**Ahsoka Tano**",color=discord.Colour(0xB98D6D), description="Versatile Attacker with healing and superior stats as long as she can avoid suffering Critical Hits")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ahsoka.png")
        embed.set_image(url="https://www.wired.com/images_blogs/underwire/2010/11/ahsoka_660.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability.")
        embed.add_field(name="Stats", value="`Power: 8311` `Speed: 105` `Health: 16536` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Energetic Slash - <:ahsokabasic:331758794440704001>", value="Deal Physical damage to target enemy and Ahsoka recovers Health equal to 20% of her Max Health, increased to 30% on a Critical Hit.")
        embed.add_field(name="Special Ability - Protective Maneuver - <:ahsokaspecial:331758794914922496>", value="Deal Physical damage to target enemy. If the target had 50% Health or more, all allies recover Health equal to 30% of Ahsoka's Max Health; otherwise, this attack deals 50% more damage.")
        embed.add_field(name="Leader Ability - Quick Steps - <:ahsokaleader:331758794587635714>", value="Jedi and Nightsister allies have +14% Evasion, and gain 20% Turn Meter whenever they Evade.")
        embed.add_field(name="Unique Ability - Daring Padawan - <:ahsokaunique:331758794646487052>", value="Ahsoka has +45% Health, +45 Speed, and +15% Critical Chance. When Critically Hit, she loses one effect. When she defeats an enemy, she regains all of them. If Jedi Knight Anakin is present, Ahsoka gains Critical Hit Immunity for 2 turns at the start of each encounter and whenever she uses a Special ability.")
        embed.add_field(name="Usage", value="She has some synergy with Jedi Knight Anakin, and she seems to do pretty well in the tank raid (Mainly P1 and P3), however, she isn't in any team that can solo P3. Her special ability is also very nice, it deals a lot of damage. She has some superior bonuses, but they expire as she gets critical hit :frowning:")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")


        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!Fulcrum-Ahsoka-Tano"): 
        embed=discord.Embed(title="**Fulcrum Ahsoka Tano**",color=discord.Colour(0xB98D6D), description="Enduring Rebel Attacker who shrugs off debuffs and consumes buffs to deal extra damage.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ahsokaadult.png")
        embed.set_image(url="http://vignette4.wikia.nocookie.net/starwarsrebels/images/e/ee/Ahsoka_rebels_1.png/revision/latest?cb=20150303094719")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Whirlwind.")
        embed.add_field(name="Stats", value="`Power: 8945` `Speed: 148` `Health: 18444` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Balanced Strike - <:FATbasic:332113007863922698>", value="Deal Physical damage to target enemy, gain Protection Up (40%) for 2 turns, and grant Protection Up (40%) to a random ally that doesn't have it for 2 turns.")
        embed.add_field(name="Special Ability - Meditate - <:FATspecial:332113008413245440>", value="Ahsoka gains Foresight, Retribution, and each non-unique buff (excluding Taunt) present on other allies for 2 turns, then gains 15% Turn Meter for each buff on her.")
        embed.add_field(name="Special Ability - Whirlwind - <:FATspecial1:332113008165650433>", value="Consume all buffs on Ahsoka and deal Physical damage to target enemy. This attack scores an additional hit for each type of buff consumed. The target can't Evade and has -50% Armor against this attack.")
        embed.add_field(name="Unique Ability - Perseverance - <:FATunique:332113007805202435>", value="Ahsoka is immune to Damage Over Time effects and gains 30% Critical Avoidance. At the end of each turn, Ahsoka dispels all debuffs on herself and loses 10% Health for each debuff dispelled, then recovers 5% Health for each buff on her. This Health Loss can't defeat Ahsoka.")
        embed.add_field(name="Usage", value="An extremely good character, if it's used in the right way. In arena, she can be an absolute beast on offense, but, she is so bad on defense. The AI doesn't wait for getting as many buffs as possible on her before using whirlwind.")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")


        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!Asajj-Ventress"): 
        embed=discord.Embed(title="**Asajj Ventress**",color=11484517, description="Nightsister controller with self healing who generates attack power on enemy death.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ventress.png")
        embed.set_image(url="https://lumiere-a.akamaihd.net/v1/images/Asajj-Ventress_d5ca9413.jpeg?region=67%2C0%2C1067%2C600&width=768")
        embed.add_field(name="<:zeta:327437604465278977>", value="2 Zeta abilities: Nightsister Swiftness and Rampage.")
        embed.add_field(name="Stats", value="`Power: 8740` `Speed: 104` `Health: 16829` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Cruel Strike - <:asajjbasic:332486020094492683>", value="Deal Physical damage to target enemy with a 35% chance to Stun for 1 turn.")
        embed.add_field(name="Special Ability - Strike Fear - <:asajjspecial:332486020438294528>", value="Dispel all positive status effects from all enemies and Asajj recovers 40% of her Max Health. For each effect dispelled this way, Asajj recovers an additional 9% Max Health and has a 50% chance to remove 10% Turn Meter.")
        embed.add_field(name="Special Ability - Endless Wrath - <:asajjspecial1:332486020345888770>", value="Deal Special damage to all enemies and refresh all cooldowns on a finishing blow.")
        embed.add_field(name="Leader Ability - Nightsister Swiftness - <:asajjlead:332486020320985099>", value="Nightsister allies gain 28 Speed, gain 50% Turn Meter when they fall below 100% Health, and have a 50% chance to remove 20% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted.")
        embed.add_field(name="Unique Ability - Rampage - <:asajjunique:332486020727832577>", value="Whenever any ally or enemy is defeated, Asajj Ventress gains Offense Up and Critical Chance Up for two actions and gains 50% Turn Meter. Asajj Ventress gains 15 Speed for each enemy with no buffs.")
        embed.add_field(name="Usage", value="Asajj Ventress is kind of underrated nowadays. Zaul, Rex, Zader, etc. are overwhelming her. But she can be deadly if you use her the right way, her  **Cruel Strike** can stun enemies if you're lucky. Her Self-Heal Special known as **Strike Fear** can dispel all buffs from all enemies and she can recover health on that + her base. Her **Endless Wrath** can refresh all cooldowns if she killed at least one enemy using **Endless Wrath**")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        #PLEASE I GOTTA FINISH THIS BEFORE STARTING OFF WITH ANOTHER
        # OMFG THANK YOU EZRA


        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!B2"): 
        embed=discord.Embed(title="**B2 Super Battle Droid**",color=discord.Colour(0x6D6F6E), description="Droid Tank that relentlessly punishes enemies that evade attacks or damage allies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_b2.png")
        embed.set_image(url="https://vignette3.wikia.nocookie.net/starwars/images/c/c5/Battle_droids_on_Geonosis.jpg/revision/latest?cb=20091202200543")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability ")
        embed.add_field(name="Stats", value="`Power: 8536` `Speed: 111` `Health: 23, 991`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Heavy Arms - <:B2Basic:336748251820589056>", value="Deal Physical Damage to target enemy and inflict Evasion Down for 2 turns")
        embed.add_field(name="Special Ability - Mow Down - <:B2Speial:336744781525024780>", value="Deal Physical damage to all enemies and Dispel all positive status effects on them, with 65% chance to also inflict Buff Immunity for 2 turns (applied before damage)")
        embed.add_field(name="Unique Ability - Relentless Barrage - <:B2Unique:336744523008835586>", value="B2 has a 40% chance to gain 100% Turn Meter when another ally is Evaded or damaged by an attack")
        embed.add_field(name="Usage", value="B2 Super Battle Droid is very effective againist any kinds of cleansers due to his **Mow Down** ability dispel all buffs with a 70% chance to inflict Buff Immunity for 2 turns and it is a disadvantage for characters like GK, Chaze, etc. since they always depend on buffs as an advantage. But don't leave as a tank, we want him to stay alive as long as possible!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Barriss-Offee"): 
        embed=discord.Embed(title="**Barriss Offee**",color=discord.Colour(0x1F1A20), description="Jedi Healer that can balance party and Dispel allied Jedi frequently")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_barriss_light.png")
        embed.set_image(url="https://vignette3.wikia.nocookie.net/starwars/images/3/37/Barrisprofile2.jpg/revision/latest?cb=20070728014608")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Swift Recovery")
        embed.add_field(name="Stats", value="`Power: 9012` `Speed: 116` `Health: 25,707`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Invigorating Strike - <:BarrissBasic:336776045061734400>", value="Deal  Physical damage to target enemy with a 45% chance for all allies to recover 6% of Barriss Offee's Max Health")
        embed.add_field(name="Special Ability - Force Healer - <:BarrissSpecial:336776062346199052>", value="All allies have their current Health percentages equalized. (Health equalizing effects ignore Health Immunity) Then, each ally recovers 15% of their Max Health and gains Defense Up for 2 turns")
        embed.add_field(name="Leader Ability - No One Left Behind - <:BarrissLead:336776087575199754>", value="Jedi allies gain 20% Max Health, and other allies gain half that amount. In addition, at the start of each of their turns, Jedi allies heal for 8% of Barriss Offee's Max Health, and other allies heal half that amount")
        embed.add_field(name="Unique Ability - Swift Recovery - <:BarrissUnique:336776104956133376>", value="At the end of each of her turns, Barriss Dispels all debuffs for the debuffed ally with the lowest health and gains 10% Turn Meter for each effect removed. Whenever an ally is Critically Hit, that ally recovers 20% of their Max Health and Barriss gains 10% Turn Meter. This effect is disabled while Barriss is defeated.")
        embed.add_field(name="Usage", value="Barris Offee is not useful in offensive side, but sometimes her special ability can heal a insane amount of health. She is also good w/ a Jedi team on Phase 1 of AAT due to her unique called **Swift Recovery** allowed her to dispel all debuffs on the ally with the lowest health, and Jedi have a buff in AAT raid too!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Bistan"): 
        embed=discord.Embed(title="**Bistan**",color=discord.Colour(0x675440), description="Wild Rebel Attacker who gains Frenzy, debuffs enemies, and removes Turn Meter")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_bistan.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/6/68/Bistan-SW_Card_Trader.png/revision/latest?cb=20161103055247")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability ")
        embed.add_field(name="Stats", value="`Power: 8864` `Speed: 145` `Health: 18,023`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Blast 'Em - <:BistanBasic:336789090001223702>", value="Deal Physical damage to target enemy with a 70% chance to inflict Damage Over Time for 3 turns")
        embed.add_field(name="Special Ability - Frenzy - <:BistanSpecial:336789090953592833>", value="Bistan gains **Frenzy** for 4 turns and all other allies gain 20% Turn Meter **Frenzy**: Whenever an ally uses a Special Ability, this unit gains 100% Turn Meter")
        embed.add_field(name="Special Ability - Gunner Tactics - <:BistanSpecial1:336789090752135168>", value="Deal Physical damage to target enemy and remove Turn Meter equal to Bistan's Potency")
        embed.add_field(name="Unique Ability - Amped Up - <:BistanUnique:336789090320121857>", value="Bistan gains 10% for each Rebel ally and each debuffed enemy")
        embed.add_field(name="Usage", value="Bistan is good on multiple type of modes in the game like raids, ships, etc. His 2nd special know as **Gunner Tactics**, it deal Physical Damage to an enemy and remove Turn Meters equal to Bistan's Potency. And his Frenzy buff when gain him 100% Turn Meters whenever an ally used a special ability but it have a large cooldowns of 7. Make sure you pump Bistan's Potency as high as so he can remove TM from the Rancor as many as possible but you don't have to worry about Potency modsets if you are under a Jyn leadership or having Potency as primary on cross mod (At least have one Potency modset on him :wink:")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Bodhi-Rook"): 
        embed=discord.Embed(title="**Bodhi Rook**",color=discord.Colour(0x675440), description="Clever Rebel Support who spots enemy units for his allies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_bodhi.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/d/d0/Bodhi_Rook_Fathead.png/revision/latest?cb=20161108051512")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Double Duty")
        embed.add_field(name="Stats", value="`Power: 8519` `Speed: 132` `Health: 16,371`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Call Targets - <:bodhibasic:337233186713239553>", value="Deal Physical damage to target enemy and inflict Evasion Down for 2 turns.")
        embed.add_field(name="Special Ability - Spotter - <:bodhispecial:337233198226472960>", value="Inflict target enemy with Evasion Down for 2 turns, which can't be Evaded. Target other ally gains Offense Up and Potency Up for 2 turns and is called to Assist. If the target ally is a Rebel, Bodhi gains 30% Turn Meter.")
        embed.add_field(name="Special Ability - Intercept Communications - <:bodhispecial1:337233209219612674>", value="Remove 10% Turn Meter from all enemies (doubled on Empire enemies) which can't be Evaded. All allies gain 10% Turn Meter (doubled on Empire allies).")
        embed.add_field(name="Unique Ability - Double Duty - <:bodhiunique:337233223073398806>", value="While Bodhi is active, Rebel allies with Offense Up also gain +50% Defense. At the end of each his turns, Bodhi grants Offense Up for 2 turns to a random ally who doesn't have it. ")
        embed.add_field(name="Usage", value="Bodhi Rook is very useful for mid-game players and a threat again Zaul meta, because he can inflict Evasion Down for 2 turns. Zaul teams is always about evasion and critically hit for Stealth so Bodhi's Evasion Down can help your team defeat Zaul easier!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 

    if message.content.startswith("!Boba-Fett"): 
        embed=discord.Embed(title="Boba Fett",color=discord.Colour(0x636B5E), description="Ruthless Bounty Hunter Attacker who ignores Taunts, Ability Blocks and self-revives")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_bobafett.png")
        embed.set_image(url="http://posterposse.com/wp-content/uploads/2014/12/wallpaper-1967961.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Bounty Hunter's Resolve")
        embed.add_field(name="Stats", value="Power: 8457 Speed: 147 Health: 15,677  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - EE-3 Carbine - <:bobabasic:337232781694468096>", value="Deal Physical damage to target enemy with a 50% chance (doubled against Scoundrels) to attack again. Each attack has a 70% chance to inflict Damage Over Time for 2 turns ")
        embed.add_field(name="Special Ability - Death From Above - <:bobaspecial:337232782042464267>", value="Deal Physical damage to all enemies with an 80% chance to inflict Ability Block for 1 turn and a 50% chance to inflict Damage Over Time for 2 turns. Inflict Ability Block on the selected target for 2 turns.")
        embed.add_field(name="Special Ability - Execute - <:bobaspecial1:337232781702725632>", value="Deal Physical damage to target enemy and dispel all status effects on them. Deal 30% more damage for each effect dispelled. Enemies defeated by this ability can't be revived. Reduce all cooldowns by 1 on a finishing blow. This attack can't be Evaded.")
        embed.add_field(name="Leader Ability - Dead or Alive - <:Bobalead:337232781287489536>", value="All allies gain 50% Critical Damage and 10% Critical Chance. Bounty Hunter allies gain 15 Speed for each debuffed enemy, gain Max Health equal to 50% of the total Potency of all Bounty Hunter allies, and gain 15% Turn Meter whenever a Thermal Detonator explodes.")
        embed.add_field(name="Unique Ability - Bounty Hunter's Resolve - <:bobaunique:337232781425770496>", value="At the start of battle, and whenever he defeats an enemy, Boba Fett recovers 100% Protection and gains Bounty Hunter's Resolve until he is defeated. Bounty Hunter's Resolve: Boba Fett ignores Taunts during his turn. When defeated, revive at 100% Health. Can't be Dispelled or prevented.")
        embed.add_field(name="Usage", value="Boba Fett is a must get for beginner players. His basic can deal insane amount of damages and his special known as **Death From Above** can sometimes inflict Ability Block on all enemies. His 2nd Special **Execute** can also terminated an enemy easily on a Critical Hit and they have about 3+ Buffs and on finishing blow, reduce all his cooldowns by 1 and that enemy cannot be revived under any kinds! But getting him to Gear 11 is not that easy :wink:")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
    
         
    if message.content.startswith("!Cad-Bane"): 
        embed=discord.Embed(title="**Cad Bane**",color=discord.Colour(0x352E3B), description="High damage attacker with a powerful stun and bonuses against Jedi characters ")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_cadbane.png")
        embed.set_image(url="http://overmental.com/wp-content/uploads/2015/07/4433746-8523675652-cad-b-790x556.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability ")
        embed.add_field(name="Stats", value="`Power: 8679` `Speed: 113` `Health: 14,623` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Gun Slinger - <:cadbasic:337234002345721867>", value="Deal Physical damage to target enemy with a 55% chance to attack again. Cad Bane has a 50% chance to gain 15% Turn Meter with each attack.")
        embed.add_field(name="Special Ability - Stun Glove - <:cadspecial:337234010587660298>", value="Deal unavoidable Physical damage to target enemy and Stun for 1 turn. In addition, remove 40% Turn Meter, or 100% Turn Meter if the target is a Jedi.")
        embed.add_field(name="Leader Ability - Hunter's Reflexes - <:cadleader:337234063498936323>", value="Scoundrel allies gain 20% Evasion and gain 25% Turn Meter whenever they Evade.")
        embed.add_field(name="Unique Ability - Jedi Hunter - <:cadunique:337234036126646273>", value="Cad Bane has +35% Critical Chance and +20% Critical Damage when attacking Jedi enemies")
        embed.add_field(name="Usage", value="Cad Bane is very useful when fighting against Jedi teams due to his special **Stun Glove** and his unique **Jedi Hunter** can give bonuses to Cad Bane. His basic ability have to attack again and it can deals devastate amount of damages sometimes. He is also good for Credit Heist, Droid Smuggling event, and Critical Chance Mod Challenge. But Cad Bane's pretty useless for other kinds in the game.")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")
                        
        await bot.send_message(message.channel, embed=embed) 
        
        
        
    if message.content.startswith("!Cody"): 
        embed=discord.Embed(title="**CC-2224 Cody**",color=discord.Colour(0xE0A233), description="Clone Attacker that Stuns and call tons of Assists")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_cody.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/4/44/End_Days.jpg/revision/latest?cb=20111028234105")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Ghost Company Commander")
        embed.add_field(name="Stats", value="`Power: 8630` `Speed: 115` `Health: 15,328` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Alpha Strike - <:Codybasic:337572976700555264>", value="Deal Physical damage to target enemy and gain 20% Turn Meter. Gain an additional 20% Turn Meter if that enemy has more than 50% Health, and an additional 20% Turn Meter if that enemy has less than 50% Turn Meter")
        embed.add_field(name="Special Ability - AT-TE Mass-Driver Cannon - <:codyspecial:337572976725721088>", value="Deal Special damage to target enemy and 35% less damage to all other enemies. If this attack scores at least 2 Critical Hits, Stun the primary target for 1 turn.")
        embed.add_field(name="Special Ability - The 212th Attack  - <:codyspecial1:337572976801218560>", value="Call all Clone allies and one random ally to assist. These Assists deal 40% less damage. Each time an Assist scores a Critical Hit, reduce the cooldowns of this ability by 1.")
        embed.add_field(name="Leader Ability - Ghost Company Commander - <:codylead:337572976327131136>", value="Clone allies gain 30% Critical Chance, and other allies gain half that amount. Cody gains 60% Defense for each living Clone ally and other Clone allies gain half that amount. Clone allies recover 5% of their Max Protection whenever they use a Basic ability.")
        embed.add_field(name="Usage", value="CC-2224 Cody can be useful for AAT raids and Arena if pair with Clone Troopers. His Alpha Strike and AT-TE Mass-Driver Cannon can sometimes deal insane amount of damage. The 212th Attack can be used very frequently if everytime his allies score critical hits. He is very useful when leading a Clone team in Phase 4 HAAT, but he kinda useless for other aspects in the game 😞")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        


    if message.content.startswith("!Cassian-Andor"): 
        embed=discord.Embed(title="**Cassian Andor**",color=discord.Colour(0x304551), description="Rebel Support who buffs allies at the start of battle and debuffs enemies during the battle.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_cassian.png")
        embed.set_image(url="http://screenrant3.imgix.net/wp-content/uploads/2017/01/Diego-Luna-as-Captain-Cassian-Andor-in-Rogue-One-A-Star-Wars-Story.jpg?auto=format&cs=tinysrgb&q=20&w=1000&h=500&fit=crop&dpr=1.5")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Groundwork")
        embed.add_field(name="Stats", value="`Power: 8698` `Speed: 134` `Health: 17,562`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Two Steps Ahead - <:cassbasic:337572974339031041>", value="Deal Physical damage to target enemy with a 85% chance to inflict Buff Immunity for 2 turns.")
        embed.add_field(name="Special Ability - Shock Grenade - <:Cassspecial:337572976713269249>", value="Inflict Ability Block, Defense Down, Healing Immunity, Offense Down and Speed Down (once each) on random enemies for 2 turns. If the primary target is Empire, Expose them for 2 turns. If K-2SO is present, he is called to Assist. Then, gain 20% Turn Meter for each debuffed enemy.")
        embed.add_field(name="Special Ability - Crippling Shot- <:cassspecial1:337572976511680513>", value="At the start of each encounter all Rebel allies gain Protection Up (20%) for 3 turns, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.")
        embed.add_field(name="Unique Ability - Groundwork - <:CassUnique:337572976637640704>", value="At the start of each encounter all Rebel allies gain Protection Up (20%) for 3 turns, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.")
        embed.add_field(name="Usage", value="Cassian Andor is a useful players for multiple type of aspects in game. His Shock Grenade can spread debuffs very frequently because is only have a cooldowns 2 and you gain Cassian 100% TM if all enemies have at least a debuff on them. His Crippling Shot can apply every single debuffs on that enemy's allies to that enemy. He paired very well with K2-SO since he can assist Cassian on his special and he gain all bonuses on his unique!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")

        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Captain-Phasma"): 
        embed=discord.Embed(title="**Captain Phasma**",color=discord.Colour(0xE3E9E8), description="High-damage First Order support that can grant allies many extra attacks.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_phasma.png")
        embed.set_image(url="http://vignette2.wikia.nocookie.net/movie-villains/images/f/f3/Star-wars-captain-phasma-figurine-0.jpg/revision/latest?cb=20160811084922")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Fire At Will")
        embed.add_field(name="Stats", value="`Power: 8431` `Speed: 121` `Health: 21,118` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Onslaught - <:Phasmabasic:337572976675389440>", value="Deal Physical damage to target enemy and inflict Defense Down for 2 turns on a Critical Hit. If this attack is not a Critical Hit, Phasma has a 50% chance to gain Advantage for 2 turns instead.")
        embed.add_field(name="Special Ability - Victory March - <:phasmaspecial1:337572976763469824>", value="All allies gain 50% Turn Meter and Advantage for 2 turns.")
        embed.add_field(name="Special Ability - Fusillade - <:phasmaspecial1:337572976327131150>", value="Deal Physical damage to all enemies with a 90% chance to inflict Speed Down for 2 turns.")
        embed.add_field(name="Leader Ability - Fire At Will - <:Phasmalead:337572976478126081>", value="Whenever an ally attacks, they have a 20% chance to call a random ally to Assist. This chance is triple if the attacking ally is First Order. If that ally had Advantage, they regain it for 2 turns. First Order allies gain Advantage for 2 turns at the start of each encounter, can't be Critically Hit while they have Advantage, and gain 20% Potency.")
        embed.add_field(name="Usage", value="She is a must get once you unlocked Galactic War at level 40. Her **Victory March** can make a huge change to the battle situation. Her **Fusillade** can slow down high-speed characters. Her leader ability **Fire At Will** can grant tons of extra attacks to non-First Order allies and the chances are even higher if the attacking ally is First Order.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
   

    if message.content.startswith("!Chirrut-Imwe"): 
        embed=discord.Embed(title="**Chirrut Îmwe**",color=discord.Colour(0x4C0B07), description="Balanced Rebel Attacker who dispels debuffs, heal allies, and grants Tenacity Up")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_chirrut.png")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6BRiE5HC1jZssxhT9EsAYKkaxduWatWnNfJ9DLr9_h79mkM9ulA")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability ")
        embed.add_field(name="Stats", value="`Power: 8559` `Speed: 153` `Health: 16,074 ` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Staff Strike - <:chirbasic:337598218403708929>", value="Deal Physical damage to target enemy with a 70% chance to gain Heal Over Time for 3 turns. If the target is debuffed, grant Heal Over Time to a random ally for 3 turns.")
        embed.add_field(name="Special Ability - As The Force Wills - <:chirspecial:337598229808152576>", value="All allies have their current Health percentages equalized. Dispel all debuffs from all allies and grant them a Heal Over Time effect for 4 turns for each effect dispelled. Allies that weren't debuffed gain Tenacity Up for 3 turns.")
        embed.add_field(name="Special Ability - Strength of Purpose- <:Chirspecial1:337598237953490944>", value="Deal Physical damage to target enemy, dealing 20% more damage for each buffed ally. If Baze Malbus is present, he is called to Assist. ")
        embed.add_field(name="Unique Ability - Indomitable Will - <:chirunique:337598261013643265>", value="Chirrut Îmwe gains +17% Counter Chance and Health Steal for each living enemy, double for Empire enemies. If Baze Malbus is present, he also gains these bonuses.")
        embed.add_field(name="Unique Ability - Resolute Endurance  - <:chirunique1:337598283541118976>", value="Whenever a Rebel ally is Critically Hit, they gain Heal Over Time for 2 turns. At the start of each turn, if Chirrut Imwe is alive, all allies with Heal Over Time recover 4% of their Max Health")        
        embed.add_field(name="Usage", value="Chirrut Îmwe is kinda for mid-game or advanced player since he isn't F2P until you're level 60. He works extremely well with his friend, Baze Malbus. We can call him the 'HoT Master' in the game since his abilities are always related to buffs and HoT. His **As The Force Wills** can change the tide of the battle, and his **Strength of Purpose** can one-shot kill an enemy, his unique is very helpful because he can grant Rebel allies HoT whenevet they are Critically Hit and it gives Baze and Chirrut (AKA Chaze) counter chance and Health Steal. He works well with any kind of line-ups but the best when paired with Rebels.")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Chief-Nebit"): 
        embed=discord.Embed(title="**Chief Nebit**",color=discord.Colour(0x5B3A3D), description="Cunning Jawa Tank with Stealth synergies who can reduce cooldowns")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_jawa_nebit.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/0/04/NebitHS-ANH.png/revision/latest?cb=20130226042239")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability ")
        embed.add_field(name="Stats", value="`Power: 8963` `Speed: 115` `Health: 27,248`(<:gearicong111:330366020365713408>, without mods")
        embed.add_field(name="Basic Ability - Sheltering Shot - <:Nebitbasic:337573879637606410>", value="Deal Physical damage to target enemy with a 70% chance to Protection Up equal to 20% of Nebit's Max Health for 2 turns to a random ally who is not Stealthed. ")
        embed.add_field(name="Special Ability - Distracting Negotiations -<:Nebitspecial:337573879612571648>", value="Nebit taunts for 2 turns and gain Heal Over Time for 3 turns. Reduce the cooldowns of all Jawa and Droid allies by 1. ")
        embed.add_field(name="Special Ability - Desert Ambush - <:NebitSpecial1:337573880732450816>", value="Deal Physical damage to target enemy and a random ally to Assist dealing 20% less damage. If the Assisting ally is a Jawa or a Droid, call another random ally to Assist. All Jawa called to Assist gain Stealth for 3 turns.")
        embed.add_field(name="Leader Ability - Raiding Parties - <:Nebitlead:337573880673599488>", value="Jawa and Droid allies gain 30% Critical Chance and inflict Critical Chance Down for 3 turns on a Critical Hit. ")
        embed.add_field(name="Usage", value="Chief Nebit is very useful when represent as a tank under a Droid team, he is a very solid characters who can taunt for 2 turns on his Distracting Negotiations, plus his Heal Over Time will let him to stay in the battlefield longer. His Desert Ambush can be use back-to-back if at least 2-3 Jawa or Droid allies is alive. But he is not that great when paired with non-Jawa or non-Droid allies. He is F2P once you unlocked Squad Arena.")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")        
     
        await bot.send_message(message.channel, embed=embed) 

    if message.content.startswith("!Chopper"): 
        embed=discord.Embed(title="**C1-10P 'Chopper'**",color=discord.Colour(0xD17A43), description="Surly Phoenix Support who Taunts and Dispels, and can recover Phoenix cooldowns.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_chopper.png")
        embed.set_image(url="http://a.dilcdn.com/bl/wp-content/uploads/sites/6/img/news/chopper1.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 8848` `Speed: 152` `Health: 18,962` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Reckless Fling- <:chopbasic:339727868022226944>", value="Deal Physical damage to target enemy and grant a random Phoenix ally Offense Up, Defense Up, or Speed Up at random for 2 turns, with a 60% chance to reduce that ally's cooldowns by 1.")
        embed.add_field(name="Special Ability - Cantankerous Clanker - <:chopspecial:339727868256976896>", value="Chopper gains Taunt for 1 turn. While he has this Taunt buff, Chopper gains 30% Evasion.")
        embed.add_field(name="Special Ability - Metal Menace - <:chopspecial1:339727868055519252>", value="Dispel all buffs on target enemy, For each buff dispelled away, all enemies lose 10% Turn Meter, and Chopper gains 25% Protection. Droid targets are also Stunned for 1 turn.")
        embed.add_field(name="Unique Ability - Maintenance Protocols - <:chopunique:339727867631894540>", value="At the start of his turn, Chopper recovers 15% of his Max Health. In addition, whenever he is damaged, he gains Protection Up (15%) if he doesn't have Protection Up.")
        embed.add_field(name="Usage", value="Chopper (AKA C1-10P) have various style of teams to play with like Resistance, Phoenix, No Dispeller, etc. teams. His Cantankerous Clanker can give him a huge evasion for 1 turn. His Metal Menace can recover a insane amount of Protection to keep him alive as long as possible. He is a very good characters under a Resistance team since he can make enemies lose Turn Meter and keep Resistance applying Exposes to enemies. He is a very good (not the best) character for beginners. 😎")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")     
        
        await bot.send_message(message.channel, embed=embed) 
       
    if message.content.startswith("!Thrawn"): 
        embed=discord.Embed(title="**Grand Admiral Thrawn**",color=discord.Colour(0x8EBEF4), description="Calculating Empire Leader who can halt enemies in their tracks, and grant Empire allies a new Special ability")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_thrawn.png")
        embed.set_image(url="https://s-media-cache-ak0.pinimg.com/736x/49/b7/c4/49b7c45708d56ea5919d55f4fcd5119d--grand-admiral-thrawn-empire.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="2 Zeta abilities: Legendary Strategist & Ebb and Flow")
        embed.add_field(name="Stats", value="`Power: 9990` `Speed: 150` `Health: 25,981`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Manipulate - <:thrawnbasic:340116356554817537>", value="Characters: Deal Special damage to target enemy, grant them Speed Up for 1 turn, or if they already had Ability Block, inflict Stun for 1 turn instead. When this Speed Up expires, inflict Ability Block for 1 turn. These effects can't be resisted. Raid Boss: Deal Special damage to target enemy and inflict Defense Down for 2 turns, which can't be Resisted.")
        embed.add_field(name="Special Ability - Fracture - <:thrawnspecial:340116356697554949>", value="Deal Special damage to target enemy 4 times, dispel all buffs on them, remove 50% Turn Meter, and inflict Fracture until the start of Thrawn's next turn or Thrawn is defeated. This Fracture can't be Copied or Dispelled. Fracture on Characters: Speed set to 0, can't gain buffs, bonus Attacks, or bonus Turn Meter. Fracture on Raid Bosses: -50% Speed (Doesn't stack with Speed Down), can't gain buffs, and -30% Counter Chance.")
        embed.add_field(name="Special Ability - Grand Admiral's Command - <:thrawnspecial1:340116357158928386>", value="Swap Turn Meter with target other ally. Dispel all debuffs on Thrawn and that ally, and they recover 40% Protection.")
        embed.add_field(name="Leader Ability - Legendary Strategist- <:thrawnlead:340116357037293570>", value="Empire allies have +15% Max Protection, +25% Offense, and gain 20% Turn Meter whenever they Resist a detrimental effect pr suffer a debuff. Whenever an Empire ally gains or loses a status effect, they recover 2% Protection. Empire allies gain a new Special ability, Maneuver: Dispel all debuffs on that character, and gain 50% Turn Meter (Cooldowns 3.)") 
        embed.add_field(name="Unique Ability - Ebb and Flow - <:thrawnunique:340116356802543620>", value="Thrawn has 100% Counter Chance, +100% Tenacity, and -50% Speed whenever any enemies are Fractured. Whenever an Empire ally uses a Special ability while Thrawn is active, that ally gains 15% Turn Meter and, if any enemies are Fractured, Thrawn and Fractured enemies lose 15% Turn Meter.")
        embed.add_field(name="Usage", value="Thrawn is an absolute amazing character. His **Manipulate** can turn Speed Up into Ability Block (easy with Darth Nihilus), or inflict Stun if they already had Ability Block. His **Fracture** (AKA Shock 2.0) can disabled an enemy for a while until Thrawn's next turn. **Grand Admiral's Command** allows Thrawn and an ally to dispel all debuffs on them and recover 40% Protection (that's a lot!). **Legendary Strategist** gives Empire allies a new Special ability to self-cleanse, something they really need. **Ebb & Flow** allows him to control Fracture enemies and give him insane bonuses!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master (Also The Chosen One)**")
                        
        await bot.send_message(message.channel, embed=embed) 
                        
    
    if message.content.startswith("!CS-P1"): 
        embed=discord.Embed(title="**Clone Sergeant - Phase I**",color=discord.Colour(0x61813D), description="Clone Attacker with AoE damage and Turn Meter reduction")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclonegreen.png")
        embed.set_image(url="http://www.mwctoys.com/images1/review_sstroop_large.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 8415` `Speed: 107` `Health: 16,983` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Z-6 Rotary Blaster- <:csp1basic:340169202302320640>", value="Deal Physical damage to target enemy and gain 50% Turn Meter on a critical hit.")
        embed.add_field(name="Special Ability - Suppressive Fire - <:csp1special:340169202239275008>", value="Deal Physical damage to all enemies and remove 50% of their Turn Meter.")
        embed.add_field(name="Unique Ability - Concentrated Fire - <:csp1unique:340864936513372160>", value="Clone Sergeant - Phase I gains 4.5 Critical Chance Up for each living Clone ally. In addition, he has +10% Critical Damage and Offense Up for 2 turns whenever he critically hits.")
        embed.add_field(name="Usage", value="He is very good when under a Clone team team since he gains a bonus for each living Clone ally. His **Suppressive Fire** can deal a huge amount of damage. But he is not that good overall nowadays. He is your 1st character when you first started the game.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Chewbacca"): 
        embed=discord.Embed(title="**Clone Wars - Chewbacca**",color=discord.Colour(0x48331B), description="Durable Tank with both Taunt and self-Healing")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_chewbacca.png")
        embed.set_image(url="https://2.bp.blogspot.com/-ZIL336AWVFM/VZZwSksccgI/AAAAAAAAfGU/0MvC6isBM_M/s320/peter%2Bmayhew%2Bchewbacca%2Bepisode%2B3.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Defiant Roar")
        embed.add_field(name="Stats", value="`Power: 9246` `Speed: 106` `Health: 25,368` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Bowcaster - <:chewiebasic:341175507225935874>", value="Deal Physical damage to target enemy with a 55% chance to remive 50% Turn Meter")
        embed.add_field(name="Special Ability - Wookiee Rage - <:chewiespecial:341175507670269952>", value="Chewbacca Taunts and gains 30% Health Up for 2 turns.")
        embed.add_field(name="Special Ability - Defiant Roar- <:chewiespecial1:341175507188187137>", value="Chewbacca dispels all debuffs from himself, recovers 50% of his Max Health, gains Defense Up for 3 turns, and has a 50% Chance to gain 25% Turn Meter.")
        embed.add_field(name="Leader Ability - Wookiee Resolve - <:chewielead:341175507745898496>", value="All allies have +50 Defense, and a 50% chance to gain Defense Up for 3 turns whenever they are damaged")
        embed.add_field(name="Usage", value="Chewbacca is a very good beginner character, he is your 3rd character in the game when you first started the game. But he is like the worst zeta character in the game. His **Defiant Roar** dispels all debuffs from himself and recovers half of his Max Health, it's a very useful ability. But he is very useless when comparing to advanced players. *DO NOT* zeta him unless you really need him!")
        embed.add_field(name="Ahnald Ranking", value="**Youngling**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!CLS"): 
        embed=discord.Embed(title="**Commander Luke Skywalker**",color=discord.Colour(0x5E70C4), description="Abilities (the complete command was too long, so we had to split it :joy:")
        embed.set_thumbnail(url='https://swgoh.gg/static/img/assets/tex.charui_lukebespin.png')
        embed.set_image(url="https://cnet4.cbsistatic.com/hub/i/r/2014/04/25/3ab1aceb-4bb6-42ca-95d5-5630fe3c5050/resize/570xauto/0efdbe9f91f476abc5626e3f85da3ef9/luke-bespin.jpg")       
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.add_field(name="Basic Ability - Destined Strike - <:CLSbasic:345574020500160513>", value="Deal Physical damage to target enemy and inflict Speed Down and Defense Down for 2 turns. If the target already had Speed Down, remove 30% Turn Meter. If the target already had Defense Down, inflict Stun for 1 turn.")
        embed.add_field(name="Special Ability - Use the Force - <:CLSspecial:345509763423010816>", value="Deal Physical damage to target enemy, Dispel all buffs on them, remove 100% Turn Meter, and inflict Buff Immunity and Tenacity Down for 2 turns. Reduce the cooldown of this ability by 1 if the target didn't have full Health.")
        embed.add_field(name="Special Ability - Call to Action - <:CLSSpecial1:345574030763622400>", value="Dispel all debuffs on Luke. Luke gains 100% Turn Meter and recovers 40% Health and 40% Protection. If Luke doesn't have the Call to Action unique buff, he gains it until the next time this ability is used. Call to Action: Luke ignores Taunts during his turn and has +50% Accuracy, +50% Critical Chance, and +50% Critical Damage. Can't be Dispelled or prevented.")
        embed.add_field(name="Leader Ability - Rebel Maneuvers - <:CLSLead:345155613493428224>", value="Rebel allies have +50% Counter Chance, +50% Defense, and +15% Offense. Whenever an enemy Resists a detrimental effect, Rebel allies gain 5% Turn Meter.")   
        embed.add_field(name="Unique Ability - Learn Control - <:CLSUnique:345155639754096640>", value="While Luke doesn't have Call to Action, he has +50% Counter Chance, +50% Critical Avoidance, +50% Defense, +100% Tenacity, and gains 10% Turn Meter whenever another Rebel ally takes damage.")
        embed.add_field(name="Unique Ability - It Binds All Things - <:CLSUnique1:345155658548510720>", value="Luke has +40% Potency. Whenever Luke Resists a detrimental effect he recovers 5% Health and 5% Protection. Whenever Luke inflicts a debuff he gains 10% Turn Meter and other allies gain half that amount.")
        
        await bot.send_message(message.channel, embed=embed) 
        
        embed=discord.Embed(title="**Commander Luke Skywalker**",color=discord.Colour(0x5E70C4), description="Additional information.")
        embed.set_thumbnail(url='https://swgoh.gg/static/img/assets/tex.charui_lukebespin.png')
        embed.set_image(url="https://cnet4.cbsistatic.com/hub/i/r/2014/04/25/3ab1aceb-4bb6-42ca-95d5-5630fe3c5050/resize/570xauto/0efdbe9f91f476abc5626e3f85da3ef9/luke-bespin.jpg")
        embed.add_field(name="Stats", value="`Power: 9654` `Speed: 152` `Health: 18,010` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="<:zeta:327437604465278977>", value="3 Zeta abilities: Rebel Maneuvers, Learn Control & It Binds All Things.")
        embed.add_field(name="Usage", value="Commander Luke Skywalker is a absolute beast, definitely way better than our good old Farmboy Luke. He is a balanced character, great on both Offense and Defense. His basic **Destined Strike** can apply Defense Down, Speed Down and Stun. His special **Use the Force** can remove 100% Turn Meter and inflict Buff Immunity for 2 turns, perfect on a pre-taunter like Baze or Shoretrooper. **Call to Action** dispels all debuffs from Luke, and lets him gain 100% TM. His leader ability can give Rebel allies 50% Counter Chance. He is only available in the Hero's Journey (Legendary Event)")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**") 
        
        await bot.send_message(message.channel, embed=embed) 


       
        
    if message.content.startswith("!CUP"): 
        embed=discord.Embed(title="**Coruscant Underworld Police**",color=discord.Colour(0x7B6E39), description="Support that shuts down enemies with Stuns and Offense Down")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_coruscantpolice.png")
        embed.set_image(url="https://vignette2.wikia.nocookie.net/starwars/images/1/1c/CSF_underworld.png/revision/latest?cb=20130224221934 ")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 8438` `Speed: 112` `Health: 15,432` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Non-Lethal Takedown - <:cupbasic:342948948086095873>", value="Deal Physical damage to target enemy with a 50% chance to Stun for one turn.")
        embed.add_field(name="Special Ability - Non-Lethal Crowd Control - <:cupspecial:342948948606189568>", value="Deal Physical damage to all enemies with a 70% chance to inflict Offense Down for 2 turns")
        embed.add_field(name="Unique Ability - Non-Lethal Specialist - <:cupunique:342948947884638219>", value="Coruscant Underworld Police gains 30% Potency. In addition, he gains 20% Turn Meter whenever he inflicts a negative status effect.")
        embed.add_field(name="Usage", value="CUP is like the worst character in the game. His **Non-Lethal Takedown** can Stun enemies. **Non-Lethal Specialist** grants him 30% Potency and gains 20% Turn Meter whenever he inflicts a debuff. His abilities is very simple.  He haven't got any kind of rework overall. Don't farm him in Squad Arena unless you think he is good, and I know you don't thik that.")
        embed.add_field(name="Ahnald Ranking", value="**Youngling**")        
        
        await bot.send_message(message.channel, embed=embed) 
       
        
    if message.content.startswith("!Count-Dooku"): 
        embed=discord.Embed(title="**Count Dooku**",color=discord.Colour(0x98062B), description="High-damage attacker with stun, bonus attacks, and incredible counter-attacking")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_dooku.png")
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Count_Dooku.png/220px-Count_Dooku.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Flawless Riposte")
        embed.add_field(name="Stats", value="`Power: 8547` `Speed: 167` `Health: 16,473` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Hindering Press - <:dookubasic:343004456633368576>", value="Deal Physical damage to target enemy with a 50% chance to attack again. These attacks have a 25% chance to Stun for 1 turn and a 25% chance to inflict Ability Block for 1 turn. Debuff chances doubled against Jedi")
        embed.add_field(name="Special Ability - Force Lightning - <:dookuspecial:343004456348286976>", value="Deal Special damage to target enemy with a 50% chance to Shock and Stun them for 1 turn, and a 50% chance to Stun a random enemy. Debuff chances doubled against Jedi.")
        embed.add_field(name="Special Ability - Master Tactician - <:dookulead:343004546613641217>", value="All allies gain 15% Evasion and gain Offense Up for 2 turns whenever they evade.")
        embed.add_field(name="Unique Ability - Flawless Riposte - <:dookunique:343004456348024832>", value="Count Dooku has 100% Counter Chance. In addition, whenever he attacks outside of his turn, he deals 30% more damage, has a 25% chance to gain 45% Turn Meter, recovers 10% Protection, and gains Critical Hit Immunity for 1 turn.")
        embed.add_field(name="Usage", value="Count Dooku is a very deadly character. His **Hindering Press** can Stun and Ability Block an enemy, which is super annoying on a counter attack. **Force Lightning** can also Stun an enemy, plus with a chance to Shock that enemy. His unique ability known as **Flawless Riposte** gives him 100% Counter Chance, in addition, he deals more damage, chance to gain 45% Turn Meter, and recovers 10% Protection when counter-attacking. When he fights with a Nihilus lead, he is unstoppable since Nihilus gives 150% Health Steal (w/ Zeta) so whenever Dooku counter-attacks someone, he heals a lot, which makes him sort of invincible, so you need Kylo, or someone else that stuns or inflicts healing immunity.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
        await bot.send_message(message.channel, embed=embed) 
                       
    if message.content.startswith("!Savage-Opress"):
        embed=discord.Embed(title="Savage Opress",color=discord.Colour(0xE1C65D), description="Durable Attacker that crushes low-health units and becomes stronger when attacked")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_savageopress.png")
        embed.set_image(url="https://vignette4.wikia.nocookie.net/starwars/images/1/1b/Cybernetic_savageopress.jpeg/revision/latest?cb=20150324112612")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Brute")
        embed.add_field(name="Stats", value="`Power: 8906` `Speed: 123` `Health: 23,533` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Staggering Blow - <:savagebasic:343478306198388738>", value="Deal Physical damage to target enemy with a 50% chance (doubled on a Critical Hit) to inflict Offense Down for 2 turns.")
        embed.add_field(name="Special Ability - Overpower - <:savagespecial:343478306412167178>", value="Deal Physical damage to target enemy and gain Critical Chance Up and Critical Damage Up for 3 turns on a finishing blow. If the target has 50% Health or below, this attack deals massive damage and can't be Evaded.")
        embed.add_field(name="Leader Ability - Pain is Weakness - <:savageleadunique:343478306819014656>", value="Sith allies gain 75% Defense and 30% Tenacity. Other allies gain half those amounts.")
        embed.add_field(name="Unique Ability - Brute - <:savageleadunique:343478306819014656>", value="Whenever Savage takes damage, he gains Offense Up, Defense Up, and Heal Over Time for 2 turns and gains 30% Turn Meter. At the end of his turns, Savage Dispels all debuffs on a random other Sith ally and gains those debuffs for 1 turn. Dispel all debuffs from Savage whenever he is Critically Hit.")       
        embed.add_field(name="Usage", value="Savage Opress is a very good balanced character, he is good on both offense and defensive. His **Stagerring Blow** can deal a decent amount of damage, mostly because of the Offense Up buff, that he practically always has. **Overpower** can insta-kill an enemy if they are below 50% Health. His unique Brute can give some Defense Up, Offense Up, Heal over Time (stacking), and gains Turn Meter whenever he took damages. He is a great Sith and Beginner character overall!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
    if message.content.startswith("!Sith-Trooper"):
        embed=discord.Embed(title="Sith Trooper",color=discord.Colour(0x822621), description="Sith Tank who Taunts and ignores enemy Protection")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_sithtrooper.png")
        embed.set_image(url="http://media.moddb.com/images/downloads/1/64/63278/Soldat_Imprial.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 9249` `Speed: 95` `Health: 25,985` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Disruptor Blast - <:sithTbasic:343744322354806786>", value="Deal Physical damage to target enemy with a 70% chance to inflict Defense Down for 3 turns. If the target was already debuffed, ignore their Protection.")
        embed.add_field(name="Special Ability - Crimson Barrage - <:sithTspecial:343744322203680770>", value="Deal Physical damage to all enemies with a 70% chance to inflict Offense Down for 2 turns. Then gain Protection Up equal to 5% for each debuffed enemy for 2 turns. This attack ignores Protection.")
        embed.add_field(name="Unique Ability - Vaiken's Legacy - <:sithTunique:343744392713994242>", value="Sith Trooper has +100% Defense. Whenever a Sith ally uses a Special ability or falls below 50% Health, Sith Trooper gains Defense Up for 2 turns. If he already had Defense Up, he gains Taunt for 2 turns. If he already had Taunt, he gains Retribution for 2 turns. Sith Trooper gains Defense Up for 2 turns at the start of each encounter.")
        embed.add_field(name="Usage", value="Sith Trooper is a very good Sith tank. His damage outputs is kinda weak. His **Disruptor Blast** can inflict Defense Down for 3 turns, **Crimson Barrage** can inflict Offense Down, ignores Protection, and grant him Protection Up (5%) for each debuffed enemy for 2 turns. His **Vaiken's Legacy** can grant Defense Up -> Taunt -> Retribution whenever a Sith ally uses a Special ability. You want him to stay alive as long as possible.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")

        await bot.send_message(message.channel, embed=embed) 

        
    if message.content.startswith("!Sith-Assassin"):
        embed=discord.Embed(title="Sith Assassin",color=discord.Colour(0x822621), description="Elusive Sith Attacker with Stealth synergy")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_sithassassin.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 8583` `Speed: 151` `Health: 17,895` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Exploit Weakness - <:sithAbasic:343744206378106881>", value="Deal Physical damage to target enemy, inflict Evasion Down for 2 turns, and gain Offense Up for 2 turns. If the target was already debuffed, gain Stealth for 2 turns. If Sith Assassin already had Stealth, ignore the target's Protection.")
        embed.add_field(name="Special Ability - Dark Shroud - <:sithAspecial:343744207078293514>", value="Dispel all debuffs from Sith Assassin and gain Stealth and Foresight for 2 turns. If she already had Stealth, gain Speed Up and Tenacity Up for 2 turns. Sith allies gain 12% Turn Meter for each buff on her.")
        embed.add_field(name="Special Ability - Electrocute - <:sithAspecial1:343744206835286027>", value="Deal Physical damage to target enemy and inflict Stun for 1 turn. If Sith Assassin already had Stealth, Dispel all buffs from Sith Assassin, deal 5% more damage for each effect dispelled and each living Sith ally, and ignore the target's Protection.")   
        embed.add_field(name="Usage", value="Sith Assassin is an advanced Sith attacker. Her **Exploit Weakness** can deal a decent amount of damage and inflict Evasion Down for 2 turns. **Dark Shroud** gives her Stealth and Foresight, plus Speed Up and Tenacity Up for 2 turns (If she already had Stealth), and gives TM to Sith allies, so it's a very useful ability. Her 2nd Special, **Electrocute** deals huge amount of damage, if she has a lot of buffs and living Sith allies. She is a little bit of hard to farm overall.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")

        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!Echo"): 
        embed=discord.Embed(title="**CT-21-0408 'Echo'**",color=discord.Colour(0x62779D), description="Clone Support that automatically Assists allies and can Dispel all enemies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_echo.png")
        embed.set_image(url="http://media.moddb.com/images/mods/1/13/12901/EchoARCarmor-TC.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 8543` `Speed: 129` `Health: 16,850`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Supporting Fire - <:EchoBasic:344013068491030529>", value="Deal Physical damage to target enemy and grant 20% Turn Meter to random another ally with less than 50% Turn Meter.")
        embed.add_field(name="Special Ability - EMP Grenade - <:EchoSpecial:344013099449319435>", value="Deal Special damage to all enemies and Dispel all positive status effects on them.")
        embed.add_field(name="Unique Ability - By the Book - <:EchoUnique:344013124413685761> ", value="Clone allies recover 7% of their Max Health whenever they use a Basic ability. This effect can't trigger more than two times before their next turn, and is disabled if Echo is defeated.")
        embed.add_field(name="Unique Ability - Follow-Up - <:EchoUnique1:344013144445812739>", value="Whenever another ally uses a Basic ability during their turn, Echo has a 30% chance to Assist, dealing 40% less damage. This Assist chance is doubled if the attacking ally is a Clone.")
        embed.add_field(name="Usage", value="Echo is very good mid-game character. His **EMP Grenade** can deal mass damage to all enemies. He has 2 Unique abilities known as **By the Book** allowed his Clone allies to recover 7% of their Max Health but can only be triggered twice before their next turn. **Follow-Up** will allow Echo to Assist his ally and the chance is doubled if a Clone ally is attacking. He is pretty good when paired with Clones in Raids, but Squad Arena, meh. He is farmable in the Guild Store and the Fleet Store.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")   
        
        await bot.send_message(message.channel, embed=embed)
        

    if message.content.startswith("!Fives"): 
        embed=discord.Embed(title="**CT-5555 'Fives'**",color=discord.Colour(0x62779D), description="Tank character with high Defense, enemy speed reduction and joint attack ability")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_fives.png")
        embed.set_image(url="https://s-media-cache-ak0.pinimg.com/736x/bd/77/06/bd770684904c737613405932d038e3a6.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Tactical Awareness")
        embed.add_field(name="Stats", value="`Power: 9231` `Speed: 115` `Health: 26,741`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Dual DC-17 Blasters - <:5sBasic:344012837888458752>", value="Deal Physical damage to target enemy and inflict Speed Down for 2 turns. Attack again if enemy is inflicted with Speed Down.")
        embed.add_field(name="Special Ability - Combined Fire - <:5sSpecial:344012855005151232>", value="Deal Physical damage to target enemy and call a random ally to Assist. If the Assisting ally is a Clone, both attackers deal 75% more damage.")
        embed.add_field(name="Leader Ability - Veteran Clone Trooper - <:5sLead:344012868426924034>", value="Clone allies gain 65 Defense, and other allies gain half that amount.")
        embed.add_field(name="Unique Ability - Tactical Awareness - <:5sUnique:344012880045277194>", value="Fives has 85% Counter Chance and +50% Counter Damage. Fives gains 15% Turn Meter whenever another Clone ally takes damage and 7.5% Turn Meter whenever a non-Clone ally takes damage.")
        embed.add_field(name="Usage", value="Fives is a great beginning character overall. He can counter attack a lot but it becomes useless when he gets inflicted with Daze :weary:. As usual, a tank - always good at Defense, never good at Offense - his damage is very low but can reap enemies' health slowly but surely. He works well with a Clone team!")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
        
        await bot.send_message(message.channel, embed=embed)
        
        
        
        
        
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('I am made by MisterSpock#9940, NeverGiveUp {Grand Admiral}#0288 and Uniswer#6572, and U+808F hosts me. Thanks to run me!')
    print('------')                               
bot.run('token')

