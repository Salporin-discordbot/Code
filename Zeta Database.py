import asyncio
import discord
from discord.ext import commands


description = '''Salporin, the SWGoH bot for discord.'''
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
    embed=discord.Embed(title='Thanks for inviting me!', color=discord.Colour(0x9CD3E8), description="Hi! Thanks for adding me to your server. I'm Salporin. To see my commands, and explanations, type: `!commands`. If you have any questions, you can join the official server: https://discord.gg/8pFJVWN. Cheers! :beers:")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/302116840199684096/308138975111938048/SALPORIN_002.png?width=300&height=300")
    await bot.send_message(server, embed=embed)
    
  
    

@bot.event
async def on_message(message):
    if message.content.startswith('!zKylo') or message.content.startswith ('!zKylo-Ren'):
        embed=discord.Embed(title="Zeta Kylo Ren --- Outrage",color = FIRST_ORDER_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_kyloren_special01.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_kyloren.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 16<:omega:327437590657499137> and 40<:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Deal Physical damage to target enemy and, if Kylo has full Health, inflict Stun for 1 turn. This attack deals 75% more damage if Kylo is below full Health.
       """)
        embed.add_field(name="**AFTER ZETA**:",value="""
Deal Physical damage [+15% Damage] to target enemy and, if Kylo has full Health, inflict Stun for 1 turn. This attack deals 75% more damage if Kylo is below full Health. Recover Protection equal to the damage dealt. 
       """)
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9.5          
Arena: 8 - W/ Any teams       
Raids: 9 - HAAT P1 Solo (Nerfed, but still able to solo, if you have some good RNG.)  

Overall: 26.75/30 
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Awesome zeta! Works in every team!")
        
        await bot.send_message(message.channel, embed=embed)
          
    if message.content.startswith('!zFOTP'):
        embed=discord.Embed(title="Zeta First Order TIE Pilot --- Keen Eye",color = FIRST_ORDER_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_firstordertiepilot.png") 
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13<:omega:327437590657499137> and 30<:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
First Order TIE Pilot has +15% Critical Chance and +20% Critical Damage, and gains Advantage for 3 turns whenever an enemy falls below full Health. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
First Order TIE Pilot has +30% Critical Chance [+15%] and +30% Critical Damage [+10%], and gains Advantage for 3 turns whenever an enemy falls below full Health. First Order TIE Pilot has a 70% chance to gain Foresight for 2 turns whenever he loses Advantage.
        """)                    
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7.5          
Arena: 8 - W/ First Order (FO team needs to be fully zeta'd ndalorian Retali- 4 zetas)       
Raids: 7 - Usable in First order P2 team

Overall: 23.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Decent zeta. Good for Raids and in Arena!")
        
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith('!zGar-Saxon'):
        embed=discord.Embed(title="Zeta Gar Saxon --- Mandalorian Retaliation",color = EMPIRE_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_gar_saxon.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10<:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Empire allies gain 50% Counter Chance and 40% Defense. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Empire allies gain 50% Counter Chance and 40% Defense. Whenever an Empire ally uses a Basic attack, they recover 5% Health.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7.5          
Arena: 7 - W/ Empire teams      
Raids: 8 - P1 HAAT Sink 

Overall: 22.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Useful zeta for Empire to counter-attack and regenerating Health frequently.")
        
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
        embed=discord.Embed(title="Zeta Grand Master Yoda --- Battle Meditation",color = JEDI_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_yodagrandmaster_special02.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_yodagrandmaster.png")
        embed.add_field(name="Requirements", value="Level 84, 20<:zeta:327437604465278977>, 16<:omega:327437590657499137> and 40<:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Yoda gains Tenacity Up, then grants each ally every non-unique buff he has (excluding Stealth and Taunt) for 2 turns, with a 40% chance to also grant Yoda 35% Turn Meter.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Yoda gains Tenacity Up and Foresight for 2 turns, then grants each ally every non-unique buff he has (excluding Stealth and Taunt) for 2 turns, with a 40% chance to also grant Yoda 35% Turn Meter. [Cooldown -1] 
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8          
Arena: 8 - W/ zQGJ teams      
Raids: 6 - Not a big improvement for raids. 

Overall: 21/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Fun to zeta. Helps to dodge an attack and fun to use with zQGJ in Squad Arena.")
        
        await bot.send_message(message.channel, embed=embed)

           
    if message.content.startswith('!zYoda'):
        embed=discord.Embed(title="Zeta Grand Master Yoda --- Grand Master's Guidance",color = JEDI_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_removeharmful.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_yodagrandmaster.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10<:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Jedi allies gain 30% Tenacity, gain 30% Turn Meter whenever they Resist a debuff, they gain Tenacity Up for 1 turn at the end of that turn.  
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Jedi allies gain 30% Tenacity, gain 30% Turn Meter whenever they Resist a debuff, and whenever they suffer a debuff they gain Tenacity Up for 1 turn at the end of that turn.  
        """)                           
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7.5          
Arena: 4 - Jedi teams are only viable with zQGJ teams at the moment.      
Raids: 3 - There is just no strategy discovered yet. Maybe somewhere in the future...  

Overall: 15.5/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="It looks decent, and it will probably be that too, but just not good enough for arena.")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('!zJyn'):
        embed=discord.Embed(title="Zeta Jyn Erso --- Into the Fray",color = REBEL_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_jyn.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10<:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Rebel allies have +35% Potency. Enemies that suffer debuffs during Rebel allies' turns have a 50% chance to also become Exposed for 2 turns. This Expose can't be Resisted.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Rebel allies have +35% Potency and recover 5% Protection whenever they gain a buff. Enemies that suffer debuffs during Rebel allies' turns have a 50% chance to also become Exposed for 2 turns. This Expose can't be Resisted.
        """)                             
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7          
Arena: 9.5  - W/ Rogue One or CLS teams     
Raids: 6 - Jyn is very good at the Pit (Rancor) raid, but this zeta doesn't add much up to that. 

Overall: 22.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Good zeta. Zeta this if you want your allies to stay healthy!")
        
        
        await bot.send_message(message.channel, embed=embed)            
         
    if message.content.startswith('!zJyn'):
        embed=discord.Embed(title="Zeta Jyn Erso --- Fierce Determination",color = REBEL_COLOR")
        embed.set_thumbnail(url="http://i.imgur.com/27YCJB8.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_jyn.png")
        embed.add_field(name="Requirements", value="Level 84, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Jyn gains 10% Potency each time she scores a Critical Hit.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Jyn is immune to Stuns and gains 10% Potency each time she scores a Critical Hit.
        """)                      
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War:  8         
Arena: 6 - W/ Rogue One or CLS teams      
Raids: 4 - She does good enough in raids without this zeta. 

Overall: 18/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="It's good, but not required.")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zK-2SO'):
        embed=discord.Embed(title="Zeta K-2SO --- Reprogrammed Imperial Droid",color = REBEL_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_k2so.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
K-2SO has +97.6% Counter Chance. This chance is halved while K-2SO is debuffed. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
K-2SO has +97.6% Counter Chance. This chance is halved while K-2SO is debuffed. In adition, K-2SO gains 1% Max Protection whenever he takes damage.
        """)                             
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 5 - Reasonable         
Arena: 4 - He's good W/ Rogue One teams, but this zeta doesn't make a real difference.      
Raids: 2 - K2 can do a little damage, but hey this zeta is just worthless for raids.  

Overall: 11/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="Not too bad zeta. But K2 only gains 1% Max Protection so this zeta is highly discouraged!")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zLuminara-Unduli'):
        embed=discord.Embed(title="Zeta Luminara Unduli --- Elegant Steps",color = JEDI_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_dodge.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_luminara.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Jedi Allies gain 15% Evasion and recover Health equal to 6% of Luminara's Max Health at the start of each of their turns. Non-Jedi allies receive half of the Evasion bonus and Heal Effect.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Jedi Allies gain 15% Evasion and recover Health equal to 8% of Luminara's Max Health [+2% Heal] at the start of each of their turns. Non-Jedi allies receive half of the Evasion bonus and Heal Effect. Whenever any ally gains a buff they do not have, they gain a Heal Over Time effect for 2 turns.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7         
Arena: 7.25 - W/ Fulcrum Ahsoka Tano and GK      
Raids: 3 - Not much use discovered YET.  

Overall: 22.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Decent zeta. Look: https://www.youtube.com/watch?v=qp42_VYBpws")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zPao'):
        embed=discord.Embed(title="Zeta Pao --- For Pipada",color = REBEL_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_pao.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Whenever a Rebel ally uses a basic attack, reduces Pao's cooldowns by 1.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Whenever a Rebel ally uses a basic attack, reduces Pao's cooldowns by 1 and Pao gains 5% Turn Meter.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 5         
Arena: 2 - :face_palm:    
Raids: 3 - Pao is epic in hAAT P1. But this zeta isn't going to help much. 

Overall: 10/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="Not. Good.")
        
        await bot.send_message(message.channel, embed=embed)
        

    if message.content.startswith('!zQGJ'):
        embed=discord.Embed(title="Zeta Qui-Gon Jinn --- Agility Training",color = JEDI_COLOR, description="Jedi Allies have +30 Speed, gain Offense equal to 3 times their Speed, and gain Foresight for 2 turns at the start of each encounter and whenever any unit is defeated.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_quigon.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""

        """)
        embed.add_field(name="**AFTER ZETA**:", value="""

        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9           
Arena: 9.75 - W/ Jedi, and if possible double zeta R2D2.       
Raids: 6 - Can do some damage in P1 hAAT, but Sink teams and Counter teams are still more effective.  

Overall: 25.75/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Great zeta. If you have been using jedi for the whole time whole you played this game, and you want to keep using them, then this is a very good choice for you.")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zR2D2'):
        embed=discord.Embed(title="Zeta R2-D2 --- Combat Analysis",color = REPUBLIC_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_astromech_r2d2.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
While R2-D2 is active, all allies gain 10% Critical Chance and 10% Accuracy. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
While R2-D2 is active, all allies gain 10% Critical Chance and 10% Accuracy. While R2-D2 is active, whenever a Light Side ally scores a Critical Hit, dispel all debuffs on them.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9.75          
Arena: 10 - W/ LS teams, especially Jedi and Rebel teams.       
Raids: 9.5 - hAAT P4  

Overall: 29.25/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Highly recommended zeta. LS characters cleanse themselves whenever they score a Critical Hit, very helpful in arena.")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zR2D2'):
        embed=discord.Embed(title="Zeta R2-D2 --- Number Crunch",color = REPUBLIC_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_extraturn.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_astromech_r2d2.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
At the start of battle, R2-D2 gains 10% Max Protection for each Droid ally, 10% Offense for each Galactic Republic ally, 10% Max Health for each Rebel ally, and 10% Potency for each Resistance ally. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
At the start of battle, R2-D2 gains 10% Max Protection for each Droid ally, 10% Offense for each Galactic Republic ally, 10% Max Health for each Rebel ally, and 10% Potency for each Resistance ally. At the start of battle, and when R2-D2 revives, other Droid, Galactic Republic, Rebel, and Resistance allies gain 10% of R2-D2's Max Protection, Offense, Max Health, and Potency until R2-D2 is defeated. 
        """)                    
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9.75           
Arena: 10 - W/ LS teams, especially Jedi and Rebel teams.   
Raids: 9.5 - hAAT P4, he keeps the buffs up

Overall: 29.25/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Amazing zeta. Some characters will gain certain bonus depending on their factions.")
        
        
        await bot.send_message(message.channel, embed=embed)


        
    if message.content.startswith('!zRey'):
        embed=discord.Embed(title="Zeta Rey (Scavenger) --- Focused Strikes",color = RESISTANCE_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_reyjakku.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
As long as she has no debuffs, Rey has +25% Offense.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
As long as she has no debuffs, Rey has +25% Offense and inflicts Daze for 2 turns whenever she uses a Special ability. This effect can't be Resisted.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7 - not a big improvement, but still handy.          
Arena: 8 - W/ Resistance         
Raids: 9 - hAAT P4 W/ Resistance (Inflicts Daze on B2 droids so they can't gain 100% TM.)

Overall: 24/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Good zeta if you run Resistance in hAAT, with this zeta they're able to solo P4 hAAT all day.")
         
    
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zSavage'): 
        embed=discord.Embed(title="Zeta Savage Opress --- Brute",color = SITH_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_savageopress.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Whenever Savage takes damage, he gains Offense Up, Defense Up for 1 turns and a 50% chance to gain 30% Turn Meter. At the end of his turns, Savage Dispels all debuffs on a random other Sith ally and gains those debuffs for 1 turn.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Whenever Savage takes damage, he gains Offense Up, Defense Up, and Heal Over Time for 2 turns [Buff Duration +1] and gains 30% Turn Meter [+50% TM Gain Chance]. At the end of his turns, Savage Dispels all debuffs on a random other Sith ally and gains those debuffs for 1 turn. Dispel all debuffs from Savage whenever he is Critically Hit.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 9.25 - W/ zMaul and zNihilus teams      
Raids: 8 - AAT Raids (Able to Solo P3 HAAT)

Overall: 27.25/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Good zeta. The more he got damage, the more TM and buffs he will be gaining!")
        
                        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zStormtrooper'): 
        embed=discord.Embed(title="Zeta Stormtrooper --- Wall of Stormtroopers",color = EMPIRE_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperstorm.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Stormtrooper gains 40% Defense for each living Empire ally. While Stormtrooper is active, Imperial Trooper allies have +30% Defense.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Stormtrooper gains 40% Defense for each living Empire ally and 40% Offense for each defeated Empire ally. While Stormtrooper is active, Imperial Trooper allies have +30% Defense.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 6           
Arena: 7 - W/ Imperial Troopers or Empire teams        
Raids: 3 - None 

Overall: 16/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="'Not a bad' zeta. The more defeated Empire allies, the more offense Stormtroopers wll be gaining!")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zAsajj'): 
        embed=discord.Embed(title="Zeta Asajj Ventress --- Nightsister Swiftness",color = NIGHTSISTER_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ventress.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Nightsister allies have +30 Speed, +30% Offense, and have a 25% chance to remove 10% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Nightsister allies have +30 Speed, +30% Offense, gain 50% Turn Meter when they fall below 100% Health, and have a 50% chance to remove 20% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9          
Arena: 7 - W/ Nightsister team        
Raids: 8 - Rancor Raids (With full Nightsisters team) 

Overall: 24/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Decent zeta. Will be removing TM, and gaining a lot of Speed! ")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zAsajj'): 
        embed=discord.Embed(title="Zeta Asajj Ventress --- Rampage",color = NIGHTSISTER_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ventress.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
When any ally or enemy is defeated, Asajj has a 25% chance to gain 35% Turn Meter, and, gains 10% Offense, 150% Critical Chance. Asajj has +15 Speed for each enemy with no buffs.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
When any ally or enemy is defeated, Asajj gains 35% Turn Meter [+75% TM Gain Chance], and, gains 15% Offense [+5%], 15% Critical Chance [+5%], and 5% Max Health (stacking) until the end of the encounter. Asajj has +15 Speed for each enemy with no buffs.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9.25          
Arena: 7.75 - W/ High-Damage teams      
Raids: 6 - This zeta is not isn't gonna help anything... 

Overall: 23/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Good zeta. She will gain buffs, and TM whenever enemies are defeated and a lot of Speed. ")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('!zBarriss'): 
        embed=discord.Embed(title="Zeta Barriss Offee --- Swift Recovery",color = JEDI_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_removeharmful.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_barriss_light.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
At the end of each of her turns, Barriss Dispels all debuffs from the debuffed ally with the lowest Health and gains 10% Turn Meter for each effect removed. Whenever an ally is Criticalax Heally Hit, Barriss gains 10% Turn Meter. This effect is disabled while Barriss is defeated.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
At the end of each of her turns, Barriss Dispels all debuffs from the debuffed ally with the lowest Health and gains 10% Turn Meter for each effect removed. Whenever an ally is Critically Hit, that ally recovers 20% of their Max Health and Barriss gains 10% Turn Meter. This effect is disabled while Barriss is defeated.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 9 - W/ Jedi teams or any teams (Counter against teams that deal a lot of Critical Hits)       
Raids: 7 - AAT Raids

Overall: 24/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Good zeta. Your allies will be recovering Health frequently and Barris will dispel all debuffs from an ally w/ the lowest Health.")        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zBoba"): 
        embed=discord.Embed(title="Zeta Boba Fett --- Bounty Hunter's Resolve",color = BOUNTY_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_mandalorian.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_bobafett.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
At the start of battle, and whenever he defeats an enemy, Boba Fett gains Bounty Hunter's Resolve until he is defeated. ***Bounty Hunter's Resolve***: Boba Fett ignores Taunts during his turn. When defeated, revive at 100% Health. This buff cannot be dispelled.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
At the start of battle, and whenever he defeats an enemy, Boba Fett recovers 100% Protection and gains Bounty Hunter's Resolve until he is defeated. ***Bounty Hunter's Resolve***: Boba Fett ignores Taunts during his turn. When defeated, revive at 100% Health. This buff cannot be dispelled.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9.25           
Arena: 9 - W/ Any teams      
Raids: 6 - None 

Overall: 24.25/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Incredible zeta. This will might turn the tide of the battles and keep Boba stays alive longer.")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zBodhi"): 
        embed=discord.Embed(title="Zeta Bodhi Rook --- Double Duty",color = REBEL_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_bodhi.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
While Bodhi is active, Rebel allies with Offense Up also gain +50% Defense. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
While Bodhi is active, Rebel allies with Offense Up also gain +50% Defense. At the end of each of his turns, Bodhi grants Offense Up for 2 turns to a random ally who doesn't have it.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7          
Arena: 7 - W/ Rebel teams       
Raids: 5 - None 

Overall: 19/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="'Not to bad' zeta. This shouldn't be priority above others!)
        
        await bot.send_message(message.channel, embed=embed)

        
    if message.content.startswith("!zPhasma"): 
        embed=discord.Embed(title="Zeta Captain Phasma --- Fire at Will",color = FIRST_ORDER_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_leader_default.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_phasma.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Whenever an ally attacks, they have a 20% chance to call a random ally to Assist. This chance is doubled if the attacking ally is First Order. If that ally had Advantage, they regain it for 2 turns.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Whenever an ally attacks, they have a 20% chance to call a random ally to Assist. This chance is tripled if the attacking ally is First Order. If that ally had Advantage, they regain it for 2 turns. First Order allies gain Advantage for 2 turns at the start of each encounter, can't be Critically Hit while they have Advantage, and gain 20% Potency.
        """)                 
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9.5           
Arena: 8 - W/ First Order teams       
Raids: 8 - Rancor Raids 

Overall: 25.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Great zeta. You will be gaining a lot of bonus attacks from this!")
        
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zCassian"): 
        embed=discord.Embed(title="Zeta Cassian Andor --- Groundwork",color = REBEL_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_cassian.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
At the start of each encounter, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel Tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
At the start of each encounter all Rebel allies gain Protection Up (20%) for 3 turns, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel Tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9           
Arena: 8 - W/ Rebel teams        
Raids: 8.75 - Rancor Raids 

Overall: 25.75/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Decent zeta. Rebel allies will be gaining a lot of bonuses from this ability!")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zCody"): 
        embed=discord.Embed(title="Zeta CC-2224 Cody --- Ghost Company Commander",color=discord.Colour(0xED9E27)")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_cody.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Clone allies gain 25% Critical Chance, and other allies gain half that amount. Cody gains 50% Defense for each living Clone ally and other Clone allies gain half that amount. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Clone allies gain 30% Critical Chance [+5%], and other allies gain half that amount. Cody gains 60% Defense [+10% Defense] for each living Clone ally and other Clone allies gain half that amount. Clone allies recover 5% of their Max Protection whenever they use a Basic ability.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War:  6.5           
Arena: 6 - W/ Clone teams       
Raids: 9.5 - P4 hAAT Raids

Overall: 21.5/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Great zeta. This will help your Clone allies to stay healthy. Useful for P4 AAT Raids")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zChewbacca"): 
        embed=discord.Embed(title="Zeta Clone Wars Chewbacca --- Defiant Roar",color=discord.Colour(0x633820)")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_chewbacca_special02.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_chewbacca.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 16 <:omega:327437590657499137> and 40 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Chewbacca recovers 40% of his Max Health, gains Defense Up for 3 Turns, and has a 25% Chance to gain 25% Turn Meter.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Chewbacca dispels all debuffs from himself, recovers 50% of his Max Health [+10% Heal], gains Defense Up for 3 Turns, and has a 50% Chance to gain 25% Turn Meter [+25% TM Gain Chance].
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 6          
Arena: 5 - W/ Any teams      
Raids: 3 - Nope, this zeta isn't gonna help anything
Overall: 14/30
        """)
        embed.add_field(name="Priority", value="Extremely Low")
        embed.add_field(name="Editors Note", value="Worst investment. If I were you, I'd never zeta this guy my entire SWGoH life.")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zDooku"): 
        embed=discord.Embed(title="Zeta Count Dooku --- Flawless Riposte",color = SITH_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_dooku.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Count Dooku has 100% Counter Chance. In addition, whenever he attacks outside of his turn, he deals 15% more damage, has a 25% chance to gain 45% Turn Meter.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Count Dooku has 100% Counter Chance. In addition, whenever he attacks outside of his turn, he deals 30% more damage [+15% Damage], has a 25% chance to gain 45% Turn Meter, recovers 10% Protection, and gains Critical Hit Immunity for 1 turn.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9          
Arena: 9.75 - W/ Sith teams       
Raids: 6 - None 

Overall: 24.75/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Incredible zeta. Will be recovering a lot of Protection and gaining Turn Meter when counter-attacking!")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zFives"): 
        embed=discord.Embed(title="Zeta CT-5555 Fives --- Tactical Awareness",color=discord.Colour(0x62779D)")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_fives.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Fives has 85% Counter Chance and +50% Counter Damage. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Fives has 85% Counter Chance and +50% Counter Damage. Fives gains 15% Turn Meter whenever another Clone ally takes damage and 7.5% Turn Meter whenever a non-Clone ally takes damage.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 6          
Arena: 7 - W/ Any teams       
Raids: 8.5 - AAT Raids

Overall: 21.5/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="Decent zeta. He will be gaining Turn Meter when his allies got damaged.")
        
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zMaul"): 
        embed=discord.Embed(title="Zeta Darth Maul --- Dancing Shadows",color = SITH_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_dodge.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_maul.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
All Sith allies gain 20% Evasion, gain 20% Turn Meter at the start of each encounter and whenever they Evade or are Critically Hit. The Turn Meter from this ability ignores Taunting allies.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
All Sith allies gain 20% Evasion, gain 20% Turn Meter and Stealth for 1 turn at the start of each encounter and whenever they Evade or are Critically Hit, can't be Critically Hit while Stealthed, and gain Advantage for 2 turns whenever Stealth expires. The Stealth and Turn Meter from this ability ignores Taunting allies
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9          
Arena: 10 - W/ Sith teams        
Raids: 8 - AAT Raids  
Overall: 27/30
        """)
        embed.add_field(name="Priority", value="Very high")
        embed.add_field(name="Editors Note", value="Absolutely incredible zeta. Grant Sith allies Evasion, Stealth and TM frequently. This should be prioritize above others if you want to run a good Sith team!")
                     
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zNihilus"): 
        embed=discord.Embed(title="Zeta Darth Nihilus --- Lord of Hunger",color = SITH_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_sith.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_nihilus.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Sith allies gain 60% Offense and 100% Health Steal. Sith allies lose all Protection and gain that much Max Health. Sith allies are immune to Healing effects that aren't Health Steal and can't score Critical Hits.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Sith allies gain 60% Offense and 150% Health Steal [+50% Health Steal]. Sith allies lose all Protection and gain that much Max Health. Sith allies are immune to Healing effects that aren't Health Steal and can't score Critical Hits.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9          
Arena: 9.25 - W/ Sith teams        
Raids: 8.5 - Rancor Raids  

Overall: 26.75/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Amazing zeta! This will help your Sith allies stronger and healthy all the time!")
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zNihilus"): 
        embed=discord.Embed(title="Zeta Darth Nihilus --- Wound in the Force",color = SITH_COLOR")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_kill.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_nihilus.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
At the start of each of his turns, Nihilus inflicts Damage Over Time for 2 turns on a random enemy that doesn't have any debuffs. If all enemies are debuffed, inflict Damage Over Time on a random enemy. 
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
At the start of each of his turns, Nihilus inflicts Damage Over Time for 2 turns on a random enemy that doesn't have any debuffs. If all enemies are debuffed, inflict Damage Over Time on a random enemy. At the start of each enemy turn, Nihilus inflicts Health Down on them for 2 turns.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 9           
Arena: 9.25 - W/ Sith teams      
Raids: 8.5 - Rancor Raids

Overall: 26.75/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Wonderful zeta! This will help you taking down your enemies faster and easier, this is shut down if the enemies had Tenacity Up.")
        await bot.send_message(message.channel, embed=embed) 


    if message.content.startswith("!zSidious"): 
        embed=discord.Embed(title="Zeta Darth Sidious --- Sadistic Glee",color = SITH_COLOR") 
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_heal.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_sidious.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="**BEFORE ZETA**:", value="""
Darth Sidious recovers 20% of his Max Health and a 25% chance to gain 50% Turn Meter whenever any unit is defeated. In addition, he has +35% Evasion against Jedi attacks.
        """)
        embed.add_field(name="**AFTER ZETA**:", value="""
Darth Sidious recovers 20% of his Max Health and gains 50% Turn Meter [100% TM Gain Chance] whenever any unit is defeated. In addition, he has +35% Evasion against Jedi attacks, +50% Potency, and gains Max Health equal to his Potency percentage.
        """)                     
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8          
Arena: 7.5 - W/ Sith teams      
Raids: 6 - None  

Overall: 21.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Pretty decent zeta. This will help Sidious becomes tougher and stronger! This also shouldn't be prioritize above others.")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zVader"): 
        embed=discord.Embed(title="Zeta Darth Vader --- Inspiring Through Fear",color = EMPIRE_COLOR, description="Empire and Sith allies gain 30% Offense and have a 50% chance to remove 20% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted. While Darth Vader is alive, enemies immediately regain Damage Over Time for 2 turns whenever Damage Over Time expires on them.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_vader.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8.5           
Arena: 8 - W/ Sith teams       
Raids: 8 - Rancor Raids (Nerfed, but if you have TM Removal, you might do this)

Overall: 24.5/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Incredible zeta. Very useful for Arena and Raids. This can be priority above others!")
        
        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!zDeath-Trooper"): 
        embed=discord.Embed(title="Zeta Death Trooper --- Krennic's Guard",color = EMPIRE_COLOR, description="Whenever Death Trooper scores a Critical Hit, he and Director Krennic recover 20% Health. Death Trooper has a 50% chance to gain 100% Turn Meter whenever Director Krennic takes damage. Director Krennic can't be Critically Hit while Death Trooper is alive. While Death Trooper is active, Imperial Trooper allies have +10% Health Steal.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_heal_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperdeath.png")
         embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 9 - W/ Imperial Troopers or Empire teams      
Raids: 6 - None 

Overall: 23/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Amazing zeta. This have several synergies mostly between Krennic and Deathtrooper!")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zKrennic"): 
        embed=discord.Embed(title="Zeta Director Krennic --- Director of Advanced Weapons Research",color = EMPIRE_COLOR, description="Empire allies gain 25% Critical Chance and 25% Potency. Debuffed enemies who are Critically Hit during an Empire ally's turn suffer Ability Block for 1 turn. This effect can't be Resisted. Empire allies recover 10% Protection whenever they score a Critical Hit.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_empire.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_krennic.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7.75           
Arena: 9 - W/ Empire teams      
Raids: 6 - None 

Overall: 22.75/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Incredible zeta. This works very well with Empire or Thrawn teams!")
                        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zFinn"): 
        embed=discord.Embed(title="Zeta Finn --- Balanced Tactics",color = RESISTANCE_COLOR, description="Resistance allies gain 30% Offense and 60% Defense, and other allies gain half that amount. Whenever a Resistance ally loses Foresight, they gain Advantage for 2 turns and whenever an enemy takes damage from Expose, reduce the cooldowns of all Resistance allies by 1 and grant them 35% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_finnjakku.png")
         embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 10           
Arena: 8 - W/ Resistance teams        
Raids: 10 - AAT Raids 

Overall: 28/30
        """)
        embed.add_field(name="Priority", value="High (Only if for Resistance teams)")
        embed.add_field(name="Editors Note", value="Decent zeta. This can only shine when with Resistances!")
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zFAT"): 
        embed=discord.Embed(title="Zeta Ahsoka Tano (Fulcrum) --- Whirlwind",color=discord.Colour(0xB6BBC1), description="Consume all buffs on Ahsoka and deal Physical damage to target enemy. This attack scores an additional hit for each type of buff consumed. The target can't Evade and has -50% Armor against this attack.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_ahsoka_adult_special02.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ahsokaadult.png")
         embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 16 <:omega:327437590657499137> and 40 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 8 - W/ Rebel teams      
Raids: 8 - Both 

Overall: 24/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="'Not too bad' zeta. This will help FAT to use this ability more frequently and help take down her enemies easier")
        
        await bot.send_message(message.channel, embed=embed)

    
    if message.content.startswith("!zFOST"): 
        embed=discord.Embed(title="Zeta First Order Stormtrooper --- Return Fire",color = FIRST_ORDER_COLOR, description="First Order Stormtrooper has +65% Counter Chance. Whenever First Order Stormtrooper uses any Ability he has a 50% chance to call a random ally to Assist, dealing 50% damage unless they are First Order. Then, if it was a First Order ally, grant them Advantage for 2 turns.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_firstordertrooper.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 8 - W/ First Order teams       
Raids: 6.5 - AAT Raids 

Overall: 21.5/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="Decent zeta. This will make FOST tougher and stronger when mostly w/ First Order.")
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!zTarkin"): 
        embed=discord.Embed(title="Zeta Grand Moff Tarkin --- Callous Conviction",color = EMPIRE_COLOR, description="Grand Moff Tarkin gains 100% Defense equal to his Potency Percentage and 20% Potency per debuffed enemy.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_empire.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_tarkinadmiral.png")
         embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 7 - W/ Empire teams       
Raids: 5 - None 

Overall: 20/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="Decent zeta. This will help him improve his Potency for **Ultimate Firepower!")
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!zTarkin"): 
        embed=discord.Embed(title="Zeta Grand Moff Tarkin --- Tighten the Grip",color = EMPIRE_COLOR, description="Empire allies gain 30 Speed. Inflict Defense Down and Expose for 2 turns on enemies that fall below 100% Health during Empire allies' turn. This effect can't be Resisted.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_tarkinadmiral.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 7  - W/ Empire teams     
Raids: 5 - None 

Overall: /30
        """)
        embed.add_field(name="Priority", value="Very Low")
        embed.add_field(name="Editors Note", value="Extremely underpowered zeta. If you can't get the enemies down below 100% Health then this zeta is useless!")
        
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!zVeers"): 
        embed=discord.Embed(title="Zeta General Veers --- Agressive Tactician",color = EMPIRE_COLOR, description="Whenever an enemy is defeated while Veers is active, Imperial Trooper allies gain Offense Up for 2 turns, gain 50% Turn Meter, and recover 10% Protection. While Veers is active, Imperial Trooper allies have +15% Critical Chance.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_attack_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_veers.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
       embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7          
Arena: 8.5 - W/ Imperial Troopers       
Raids: 5 - None 

Overall: 20.5/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Good zeta. This can only shine when you paired Veers with Imperial Troopers!")

        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith("!zThrawn"): 
        embed=discord.Embed(title="Zeta Grand Admiral Thrawn --- Legendary Strategist",color = EMPIRE_COLOR, description="Empire allies have +15% Max Protection, +25% Offense, and gain 20% Turn Meter whenever they Resist a detrimental effect or suffer a debuff. Whenever an Empire ally gains or loses a status effect, they recover 2% Protection. Empire allies gain a new Special ability, Maneuver: Dispel all debuffs on this character and gain 50% Turn Meter (Cooldown 3).")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_empire.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_thrawn.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Usage", value="Great ability to zeta! Recover 2% Protection whenever Empire allies lose or gain a status effect. They have bonus Max Protection, Offense, gain 20% on both Resist or suffer a debuff. You should zeta this if you want to keep your Empire allies healthy under this lead.")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 10          
Arena: 10        
Raids: 8 

Overall: 28/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Incredible zeta. This will help your Empire allies to stay alive longer in the battlefleid!")
        
        
        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith("!zThrawn"): 
        embed=discord.Embed(title="Zeta Grand Admiral Thrawn --- Ebb and Flow",color = EMPIRE_COLOR, description="Thrawn has +100% Counter Chance, +100% Tenacity, and -50% Speed while any enemies are Fractured. Whenever another Empire ally uses a Special ability while Thrawn is active, that ally gains 15% Turn Meter and, if any enemies are Fractured, Thrawn and Fractured enemies lose 15% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_extraturn.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_thrawn.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 10           
Arena: 10        
Raids: 10  

Overall: 30/30
        """)
        embed.add_field(name="Priority", value="Very High")
        embed.add_field(name="Editors Note", value="Insane zeta. Thrawn will no longer need Retribution, this will help him control his Fractured enemies and help him resisting detrimental effects a lot frequently!")
        
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith('!zPaploo'):   
        embed=discord.Embed(title="Zeta Paploo --- Don't Hold Back",color = discord.Colour(0xCD853F), description=" Whenever Paploo gains a status effect, he recovers 5% Health and Protection. Whenever Paploo gains Stealth, dispel Stealth and gain Taunt for 2 Turns. Paploo has +25% Speed whenever he does not have Taunt active.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_def.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://media.discordapp.net/attachments/331116027335147530/341612670572560384/tex.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 6 - W/ Ewoks team      
Raids: 5 - None 

Overall: 18/30
        """)
        embed.add_field(name="Priority", value="Very Low")
        embed.add_field(name="Editors Note", value="Decent zeta. This will help Paploo recover his Health and Protection frequenly because he gain buff on his abilities.")
        
        await bot.send_message(message.channel, embed=embed) 
                        
    if message.content.startswith('!zCLS'):   
        embed=discord.Embed(title="Zeta Commander Luke Skywalker --- Rebel Maneuvers",color = REBEL_COLOR, description=" Rebel allies have +50% Counter Chance, +50% Defense, and +15% Offense. Whenever an enemy Resists a detrimental effect, Rebel allies gain 5% Turn Meter.
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_rebel.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_lukebespin.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20<:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 10           
Arena: 10 - W/ Any teams      
Raids: 10 - Both 

Overall: 30/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Amazing zeta. Your squad will be gaining a lot of TM using this ability!")
        
        await bot.send_message(message.channel, embed=embed)
                            
     if message.content.startswith('!zCLS'):   
        embed=discord.Embed(title="Zeta Commander Luke Skywalker --- Learn Control",color = REBEL_COLOR, description=" While Luke doesn't have **Call to Action**, he has +50% Counter Chance, +50% Critical Avoidance, +50% Defense, +100% Tenacity, and gains 10% Turn Meter whenever another Rebel ally takes damage.
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_counterattack.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_lukebespin.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 10           
Arena: 10 - W/ Any teams      
Raids: 10 - Both 

Overall: 30/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Amazing zeta. Your CLS will be gaining a lot of bonuses and it will help you survive longer!")
        
        await bot.send_message(message.channel, embed=embed)
    
    if message.content.startswith('!zCLS'):   
        embed=discord.Embed(title="Zeta Commander Luke Skywalker --- It Binds All Things",color = REBEL_COLOR, description=" Luke has +40% Potency. Whenever Luke Resists a detrimental effect he recovers 5% Health and 5% Protection. Whenever Luke inflicts a debuff he gains 10% Turn Meter and other allies gain half that amount.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_extraturn.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_lukebespin.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 10           
Arena: 10 - W/ Any teams      
Raids: 10 - Both 

Overall: 30/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Absolutely insane zeta. Luke has bonus Potency, and whether he resist or inflict a debuff, he will gain a certain positive thing.")
        
        await bot.send_message(message.channel, embed=embed)
    
    if message.content.startswith('!zChirpa'):   
        embed=discord.Embed(title="Zeta Chief Chirpa --- Simple Tactics",color = discord.Colour(0xCD853F), description=" Ewok allies gain 20% Turn Meter and deal 10% more damage whenever they perform a Basic attack. These effects are halved for other allies. Whenever an Ewok ally uses a Special ability, 60% chance to call another random Ewok ally to Assist.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ewok_chirpa.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 6 - W/ Ewok teams      
Raids: 8 - AAT Raids 

Overall: 21/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Decent zeta. This will help you rekt your enemies easier. This is what make Chirpatine (Chirpa + Palpatine) special for Phase 3 AAT Raids!")
    
        await bot.send_message(message.channel, embed=embed)                    
    
    if message.content.startswith('!zHan-Solo'):   
        embed=discord.Embed(title="Zeta Han Solo (Raid) --- Shoots First",color = REBEL_COLOR, description="Han has +35% Counter Chance and +20% Critical Chance. The first time each turn Han uses his Basic attack, he attacks again dealing 50% less damage. Han takes a bonus turn at the start of each encounter. During this turn Han ignores Taunts and he can only use his Basic ability, but it will Stun the target for 1 turn and can't be Resisted.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_speed.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_han.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 8 - W/ Rebel teams      
Raids: 6 - None 

Overall: 22/30
        """)
        embed.add_field(name="Priority", value="High")
        embed.add_field(name="Editors Note", value="Insane zeta. This will you taking down your enemies way faster than before! Counter-attacks will make Han even more deadly because he can double-attacks everytime!")
    
        await bot.send_message(message.channel, embed=embed)
                            
    if message.content.startswith('!zLuke'):   
        embed=discord.Embed(title="Zeta Luke Skywalker (Farmboy) --- A New Hope",color = REBEL_COLOR, description="All allies gain 50% Tenacity. Whenever an ally Resists a detrimental effect they gain Advantage for 2 turns.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_removeharmful.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_luke_ep4.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 7 - W/ Rebel teams      
Raids: 5 - None 

Overall: 19/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="'Not too bad' zeta. This will help your squad resisting heavy debuffs easier, and turns them into Advantage for 2 turns.")
    
        await bot.send_message(message.channel, embed=embed)  
                            
    if message.content.startswith('!zLuke'):   
        embed=discord.Embed(title="Zeta Luke Skywalker (Farmboy) --- Draw a Bead",color = REBEL_COLOR, description="Luke has 25% Critical Chance. At the start of each of his turns, Luke gains 10% Critical Damage (stacking) until the end of the encounter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_luke_ep4.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 10 <:omega:327437590657499137> and 20 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 7           
Arena: 7 - W/ Rebel teams      
Raids: 5 - None 

Overall: 19/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Incredible zeta. If you left Luke (Farmboy) unchecked, he can deal insane amount of critical damage by stacking it every turn!")
    
        await bot.send_message(message.channel, embed=embed)
                            
    if message.content.startswith('!zSTH'):   
        embed=discord.Embed(title="Zeta Stormtrooper Han --- Bluff",color = REBEL_COLOR, description="Han has a 25% chance to remove 30% Turn Meter from each enemy at the start of each of his turns. In addition, Han recovers 5% Protection and has a 25% chance to remove 15% Turn Meter from each enemy when he is damaged.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_stun_immute.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_trooperstorm_han.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8.5           
Arena: 8.75 - W/ Rebel teams      
Raids: 5 - None 

Overall: 22.25/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Pretty decent zeta. You can remove Turn Meters from all enemies at the start of his turns, recover Protection and remove Turn Meter from all enemies whenever he's damaged!")
    
        await bot.send_message(message.channel, embed=embed) 
                            
    if message.content.startswith('!zLeia'):   
        embed=discord.Embed(title="Zeta Princess Leia --- Against the Odds",color = REBEL_COLOR, description="Whenever Leia attacks, she has a 55% chance to grant all allies Critical Chance Up for 2 turns, and recovers 5% Health and 5% Protection.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_heal_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_leia_princess.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 8 - W/ Rebel teams      
Raids: 5 - None 

Overall: 21/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="Good zeta. She can grant CC Up 2 turns to all allies, recover 5% Health and Protection whenever she attacks! So the more she attacks, the more health & protection she is recovering!")
    
        await bot.send_message(message.channel, embed=embed)
                            
     if message.content.startswith('!zOld-Ben'):   
        embed=discord.Embed(title="Zeta Obi-Wan Kenobi (Old Ben) --- Devoted Protector",color = REBEL_COLOR, description=" Old Ben gains Taunt for 2 turns. When this Taunt expires, Old Ben gains Taunt for 1 turn. All allies gain Defense Up for 2 turns.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.ability_obiwankenobioldhermit_event01.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_obiwanep4.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 16 <:omega:327437590657499137> and 40 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 8.25 - W/ Rebel teams      
Raids: 5 - None 

Overall: 21.25/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Amazing zeta! He gains Taunt for 2 turns. When it expires or dispels, he gains it again for 1 turn. This's a counter to Thrawn's Fracture!")
    
        await bot.send_message(message.channel, embed=embed)                  
                            
     if message.content.startswith('!zOld-Ben'):   
        embed=discord.Embed(title="Zeta Obi-Wan Kenobi (Old Ben) --- If You Strike Me Down",color = REBEL_COLOR, description="Whenever another Jedi or Rebel ally takes damage, Old Ben gains 5% Turn Meter. The first time Old Ben is defeated, all allies gain Offense Up and Speed Up for 2 turns, recover 50% Health and 50% Protection, and gain 25% Turn Meter.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_removeharmful.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_obiwanep4.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 8 - W/ Rebel teams      
Raids: 5 - None 

Overall: 21/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="Incredible zeta. When he is defeated, he grant buffs, recover Health & Protection for all allies!")
    
        await bot.send_message(message.channel, embed=embed)             
                            
    if message.content.startswith('!zLogray'):   
        embed=discord.Embed(title="Zeta Logray --- Shaman's Insight",color = discord.Colour(0xCD853F), description="Whenever an Ewok ally scores a Critical Hit, Logray gains 5% Turn Meter. While Logray is active, whenever an Ewok ally scores a Critical Hit, that ally gains Health Up for 2 turns, and then all Ewok allies with Health Up recover 10% Health.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_crit_buff.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ewok_logray.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8           
Arena: 6.5 - W/ Rebel teams      
Raids: 5 - None 

Overall: 19.5/30
        """)
        embed.add_field(name="Priority", value="Low")
        embed.add_field(name="Editors Note", value="'Not too bad' zeta. Grant Ewok allies Health Up for 2 turns whenever they score a Critical Hit!")
    
        await bot.send_message(message.channel, embed=embed)
                        
     if message.content.startswith('!zWicket'):   
        embed=discord.Embed(title="Zeta Wicket --- Furtive Tactics",color = discord.Colour(0xCD853F), description="Wicket gains 10% Critical Damage for each living Ewok ally and each Stealthed ally. At the end of his turn, Wicket has a 50% chance to take another turn. This chance is reduced to 10% if this effect triggered in the previous turn. Whenever Wicket scores a Critical Hit, all Ewok allies recover 4% Health and 2% Protection.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_extraturn.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_ewok_wicket.png")
        embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
        embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: 8.5           
Arena: 6.5 - W/ Rebel teams      
Raids: 5 - None 

Overall: 20/30
        """)
        embed.add_field(name="Priority", value="Medium")
        embed.add_field(name="Editors Note", value="'Incredible zeta. Ewok allies recover Health & Protection whenever Wicket scores a Critical Hit!")
    
        await bot.send_message(message.channel, embed=embed)             
      
     if message.content.startswith('!zDaka'):   
         embed=discord.Embed(title="Zeta Old Daka --- Served Again",color = NIGHTSISTER_COLOR")
         embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.abilityui_passive_heal_buff.png")
         embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
         embed.set_image(url="https://swgoh.gg/static/img/assets/tex.charui_daka.png")
         embed.add_field(name="Requirements", value="Level 82, 20<:zeta:327437604465278977>, 13 <:omega:327437590657499137> and 30 <:mk3:327437579672879105>")
         embed.add_field(name="**BEFORE ZETA**", value="When another ally is defeated, Old Daka gains 50% Turn Meter and the cooldown of Chant of Resurrection is reduced by 1. When another ally is Revived while Old Daka is active, the Revived ally gains 20% Turn Meter and gains Offense Up and Defense Up for 2 turns.")
         embed.add_field(name="**AFTER ZETA**", value="When another ally is defeated, Old Daka gains 50% Turn Meter and the cooldown of Chant of Resurrection is reduced by 1. When another ally is Revived while Old Daka is active, the Revived ally gains 20% Turn Meter and gains Offense Up and Defense Up for 2 turns, and Old Daka gains +10% Max Health (stacking) until the end of the encounter.")
         embed.add_field(name="Character Ratings (**NOTE**: The maximum score is 10)", value="""
Galactic War: ?           
Arena: ? - W/ ?      
Raids: ? - ?

Overall: 20/30
        """)
         embed.add_field(name="Priority", value="?")
         embed.add_field(name="Editors Note", value="'?")
    
        await bot.send_message(message.channel, embed=embed)                              
                                                    
                            
#beginning of characters database

    if message.content.startswith("!Aayla-Secura"): 
        embed=discord.Embed(title="**Aayla Secura**",color=discord.Colour(0000ff), description="Versatile attacker with high survivability through Dodge, Hitpoints, and self healing.")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_aaylasecura.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/f/f9/Aayla.jpg/revision/latest?cb=20120815094201")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability.")
        embed.add_field(name="Stats", value="`Power: 16497` `Speed: 125` `Health: 21490` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Inspiring Strike - <:basicaayla:329902968042160133>", value="Deal Physical damage to target enemy with a 35% chance to call an ally to Assist. If the assisting ally is a Jedi, they deal 50% more damage.")
        embed.add_field(name="Special Ability - Survivor - <:specialaayla:329908683767021568>", value="Deal Physical damage to target enemy and recover Health equal to 65% of the damage dealt.")
        embed.add_field(name="Leader Ability - Jedi Valor - <:leaderaayla:329908683448254464>", value="Jedi allies gain 40% Tenacity and recover 10% of their Max Health when they ward off an effect.")
        embed.add_field(name="Unique Ability - Superior Riposte - <:uniqueaayla:329908683385339914>", value="Aayla has +10% Critical Chance, 65% Counter Chance and +50% Counter Damage. In addition, she Stuns her target for 1 turn whenever she critically hits.")
        embed.add_field(name="Character Ratings", value="""
Galactic War:
Arena:
Raids:

Overall:
----------------------------------------
Farmability: <emoji>
        """)
        embed.add_field(name="Usage", value="Awesome character. Able to deal a lot of damage, Stuns, self-healing, and counter-attacks.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")

        await bot.send_message(message.channel, embed=embed)

        
    if message.content.startswith("!Admiral-Ackbar"): 
        embed=discord.Embed(title="**Admiral Ackbar**",color=discord.Colour(0000ff), description="Rebel Support that can Dispel debuffs and grant allies extra turns. <:Ackbaricon:331668407072063488>")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ackbaradmiral.png")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_image(url="http://img11.deviantart.net/f5fa/i/2010/065/8/e/admiral_ackbar_by_quibly.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability.")
        embed.add_field(name="Stats", value="`Power: 16695` `Speed: 119` `Health: 17520` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Quick Shot - <:ackbarbasic:331746458996965377>", value="Deal Physical damage to target enemy with a 55% chance to gain 45% Turn Meter.")
        embed.add_field(name="Special Ability - It's a Trap! - <:ackbarspecial1:331746459194097674>", value="Dispel all negative status effects from all allies. Each ally recovers 9% of their Max Health for each effect dispelled this way. Admiral Ackbar has a 25% chance to gain 40% Turn Meter.")
        embed.add_field(name="Special Ability - Tactical Genius - <:ackbarspecial2:331746458934181891>", value="Ackbar grants each ally the Tactical Genius effect. The first ally to use a Special ability while they have this effect gains 100% Turn Meter and recovers 30% of their Max Health. Tactical Genius ends whenever any ally triggers this effect or at the end of Ackbar's next turn.")
        embed.add_field(name="Leader Ability - Rebel Coordination - <:ackbarleader:331746459177320450>", value="Rebel allies have +25 Speed and +10% Tenacity. In addition, whenever an ally uses an ability that isn't an attack, they call a Rebel ally to Assist.")
        embed.add_field(name="Character Ratings", value="""
Galactic War:
Arena:
Raids:

Overall:
----------------------------------------
Farmability: <emoji>
        """)                    
        embed.add_field(name="Usage", value="Fanscinating Rebel Leader. Awesome (Not really) for AAT P1 for cleansing debuffs, for Emperor's Demise event, and ")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")


        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith("!Ahsoka-Tano"): 
        embed=discord.Embed(title="**Ahsoka Tano**",color=discord.Colour0000ff), description="Versatile Attacker with healing and superior stats as long as she can avoid suffering Critical Hits")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ahsoka.png")
        embed.set_image(url="https://www.wired.com/images_blogs/underwire/2010/11/ahsoka_660.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability.")
        embed.add_field(name="Stats", value="`Power: 16695` `Speed: 105` `Health: 16536` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Energetic Slash - <:ahsokabasic:331758794440704001>", value="Deal Physical damage to target enemy and Ahsoka recovers Health equal to 20% of her Max Health, increased to 30% on a Critical Hit.")
        embed.add_field(name="Special Ability - Protective Maneuver - <:ahsokaspecial:331758794914922496>", value="Deal Physical damage to target enemy. If the target had 50% Health or more, all allies recover Health equal to 30% of Ahsoka's Max Health; otherwise, this attack deals 50% more damage.")
        embed.add_field(name="Leader Ability - Quick Steps - <:ahsokaleader:331758794587635714>", value="Jedi and Nightsister allies have +14% Evasion, and gain 20% Turn Meter whenever they Evade.")
        embed.add_field(name="Unique Ability - Daring Padawan - <:ahsokaunique:331758794646487052>", value="Ahsoka has +45% Health, +45 Speed, and +15% Critical Chance. When Critically Hit, she loses one effect. When she defeats an enemy, she regains all of them. If Jedi Knight Anakin is present, Ahsoka gains Critical Hit Immunity for 2 turns at the start of each encounter and whenever she uses a Special ability.")
        embed.add_field(name="Usage", value="She has some synergy with Jedi Knight Anakin, and she seems to do pretty well in the tank raid (Mainly P1 and P3), however, she isn't in any team that can solo P3. Her special ability is also very nice, it deals a lot of damage. She has some superior bonuses, but they expire as she gets critical hit :frowning:")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")


        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!Fulcrum-Ahsoka-Tano"): 
        embed=discord.Embed(title="**Ahsoka Tano (Fulcrum)**",color=discord.Colour(0000ff), description="Enduring Rebel Attacker who shrugs off debuffs and consumes buffs to deal extra damage.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ahsokaadult.png")
        embed.set_image(url="http://vignette4.wikia.nocookie.net/starwarsrebels/images/e/ee/Ahsoka_rebels_1.png/revision/latest?cb=20150303094719")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Whirlwind.")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 148` `Health: 18444` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Balanced Strike - <:FATbasic:332113007863922698>", value="Deal Physical damage to target enemy, gain Protection Up (40%) for 2 turns, and grant Protection Up (40%) to a random ally that doesn't have it for 2 turns.")
        embed.add_field(name="Special Ability - Meditate - <:FATspecial:332113008413245440>", value="Ahsoka gains Foresight, Retribution, and each non-unique buff (excluding Taunt) present on other allies for 2 turns, then gains 15% Turn Meter for each buff on her.")
        embed.add_field(name="Special Ability - Whirlwind - <:FATspecial1:332113008165650433>", value="Consume all buffs on Ahsoka and deal Physical damage to target enemy. This attack scores an additional hit for each type of buff consumed. The target can't Evade and has -50% Armor against this attack.")
        embed.add_field(name="Unique Ability - Perseverance - <:FATunique:332113007805202435>", value="Ahsoka is immune to Damage Over Time effects and gains 30% Critical Avoidance. At the end of each turn, Ahsoka dispels all debuffs on herself and loses 10% Health for each debuff dispelled, then recovers 5% Health for each buff on her. This Health Loss can't defeat Ahsoka.")
        embed.add_field(name="Usage", value="An extremely good character, if it's used in the right way. In arena, she can be an absolute beast on offense, but, she is so bad on defense. The AI doesn't wait for getting as many buffs as possible on her before using whirlwind.")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")


        await bot.send_message(message.channel, embed=embed)


    if message.content.startswith("!Asajj-Ventress"): 
        embed=discord.Embed(title="**Asajj Ventress**",color=discord.Colour(ff0000), description="Nightsister controller with self healing who generates attack power on enemy death.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ventress.png")
        embed.set_image(url="https://lumiere-a.akamaihd.net/v1/images/Asajj-Ventress_d5ca9413.jpeg?region=67%2C0%2C1067%2C600&width=768")
        embed.add_field(name="<:zeta:327437604465278977>", value="2 Zeta abilities: Nightsister Swiftness and Rampage.")
        embed.add_field(name="Stats", value="`Power: 22081` `Speed: 104` `Health: 16829` (<:gearicong111:330366020365713408>, without mods)")
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
        embed=discord.Embed(title="**B2 Super Battle Droid**",color=discord.Colour(ff0000), description="Droid Tank that relentlessly punishes enemies that evade attacks or damage allies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_b2.png")
        embed.set_image(url="https://vignette3.wikia.nocookie.net/starwars/images/c/c5/Battle_droids_on_Geonosis.jpg/revision/latest?cb=20091202200543")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability ")
        embed.add_field(name="Stats", value="`Power: 15526` `Speed: 111` `Health: 23, 991`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Heavy Arms - <:B2Basic:336748251820589056>", value="Deal Physical Damage to target enemy and inflict Evasion Down for 2 turns")
        embed.add_field(name="Special Ability - Mow Down - <:B2Speial:336744781525024780>", value="Deal Physical damage to all enemies and Dispel all positive status effects on them, with 65% chance to also inflict Buff Immunity for 2 turns (applied before damage)")
        embed.add_field(name="Unique Ability - Relentless Barrage - <:B2Unique:336744523008835586>", value="B2 has a 40% chance to gain 100% Turn Meter when another ally is Evaded or damaged by an attack")
        embed.add_field(name="Usage", value="B2 Super Battle Droid is very effective againist any kinds of cleansers due to his **Mow Down** ability dispel all buffs with a 70% chance to inflict Buff Immunity for 2 turns and it is a disadvantage for characters like GK, Chaze, etc. since they always depend on buffs as an advantage. But don't leave as a tank, we want him to stay alive as long as possible!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Barriss-Offee"): 
        embed=discord.Embed(title="**Barriss Offee**",color=discord.Colour(0000ff), description="Jedi Healer that can balance party and Dispel allied Jedi frequently")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_barriss_light.png")
        embed.set_image(url="https://vignette3.wikia.nocookie.net/starwars/images/3/37/Barrisprofile2.jpg/revision/latest?cb=20070728014608")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Swift Recovery")
        embed.add_field(name="Stats", value="`Power: 18903` `Speed: 116` `Health: 25,707`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Invigorating Strike - <:BarrissBasic:336776045061734400>", value="Deal  Physical damage to target enemy with a 45% chance for all allies to recover 6% of Barriss Offee's Max Health")
        embed.add_field(name="Special Ability - Force Healer - <:BarrissSpecial:336776062346199052>", value="All allies have their current Health percentages equalized. (Health equalizing effects ignore Health Immunity) Then, each ally recovers 15% of their Max Health and gains Defense Up for 2 turns")
        embed.add_field(name="Leader Ability - No One Left Behind - <:BarrissLead:336776087575199754>", value="Jedi allies gain 20% Max Health, and other allies gain half that amount. In addition, at the start of each of their turns, Jedi allies heal for 8% of Barriss Offee's Max Health, and other allies heal half that amount")
        embed.add_field(name="Unique Ability - Swift Recovery - <:BarrissUnique:336776104956133376>", value="At the end of each of her turns, Barriss Dispels all debuffs for the debuffed ally with the lowest health and gains 10% Turn Meter for each effect removed. Whenever an ally is Critically Hit, that ally recovers 20% of their Max Health and Barriss gains 10% Turn Meter. This effect is disabled while Barriss is defeated.")
        embed.add_field(name="Usage", value="Barris Offee is not useful in offensive side, but sometimes her special ability can heal a insane amount of health. She is also good w/ a Jedi team on Phase 1 of AAT due to her unique called **Swift Recovery** allowed her to dispel all debuffs on the ally with the lowest health, and Jedi have a buff in AAT raid too!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Bistan"): 
        embed=discord.Embed(title="**Bistan**",color=discord.Colour(0000ff), description="Wild Rebel Attacker who gains Frenzy, debuffs enemies, and removes Turn Meter")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_bistan.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/6/68/Bistan-SW_Card_Trader.png/revision/latest?cb=20161103055247")
        embed.add_field(name="<:zeta:327437604465278977>", value="No zeta ability ")
        embed.add_field(name="Stats", value="`Power: 16695` `Speed: 145` `Health: 18,023`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Blast 'Em - <:BistanBasic:336789090001223702>", value="Deal Physical damage to target enemy with a 70% chance to inflict Damage Over Time for 3 turns")
        embed.add_field(name="Special Ability - Frenzy - <:BistanSpecial:336789090953592833>", value="Bistan gains **Frenzy** for 4 turns and all other allies gain 20% Turn Meter **Frenzy**: Whenever an ally uses a Special Ability, this unit gains 100% Turn Meter")
        embed.add_field(name="Special Ability - Gunner Tactics - <:BistanSpecial1:336789090752135168>", value="Deal Physical damage to target enemy and remove Turn Meter equal to Bistan's Potency")
        embed.add_field(name="Unique Ability - Amped Up - <:BistanUnique:336789090320121857>", value="Bistan gains 10% for each Rebel ally and each debuffed enemy")
        embed.add_field(name="Usage", value="Bistan is good on multiple type of modes in the game like raids, ships, etc. His 2nd special know as **Gunner Tactics**, it deal Physical Damage to an enemy and remove Turn Meters equal to Bistan's Potency. And his Frenzy buff when gain him 100% Turn Meters whenever an ally used a special ability but it have a large cooldowns of 7. Make sure you pump Bistan's Potency as high as so he can remove TM from the Rancor as many as possible but you don't have to worry about Potency modsets if you are under a Jyn leadership or having Potency as primary on cross mod (At least have one Potency modset on him :wink:")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Bodhi-Rook"): 
        embed=discord.Embed(title="**Bodhi Rook**",color=discord.Colour(0000ff), description="Clever Rebel Support who spots enemy units for his allies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_bodhi.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/d/d0/Bodhi_Rook_Fathead.png/revision/latest?cb=20161108051512")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Double Duty")
        embed.add_field(name="Stats", value="`Power: 18705` `Speed: 132` `Health: 16,371`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Call Targets - <:bodhibasic:337233186713239553>", value="Deal Physical damage to target enemy and inflict Evasion Down for 2 turns.")
        embed.add_field(name="Special Ability - Spotter - <:bodhispecial:337233198226472960>", value="Inflict target enemy with Evasion Down for 2 turns, which can't be Evaded. Target other ally gains Offense Up and Potency Up for 2 turns and is called to Assist. If the target ally is a Rebel, Bodhi gains 30% Turn Meter.")
        embed.add_field(name="Special Ability - Intercept Communications - <:bodhispecial1:337233209219612674>", value="Remove 10% Turn Meter from all enemies (doubled on Empire enemies) which can't be Evaded. All allies gain 10% Turn Meter (doubled on Rebel allies).")
        embed.add_field(name="Unique Ability - Double Duty - <:bodhiunique:337233223073398806>", value="While Bodhi is active, Rebel allies with Offense Up also gain +50% Defense. At the end of each his turns, Bodhi grants Offense Up for 2 turns to a random ally who doesn't have it. ")
        embed.add_field(name="Usage", value="Bodhi Rook is very useful for mid-game players and a threat again Zaul meta, because he can inflict Evasion Down for 2 turns. Zaul teams is always about evasion and critically hit for Stealth so Bodhi's Evasion Down can help your team defeat Zaul easier!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 

    if message.content.startswith("!Boba-Fett"): 
        embed=discord.Embed(title="Boba Fett",color=discord.Colour(ff0000), description="Ruthless Bounty Hunter Attacker who ignores Taunts, Ability Blocks and self-revives")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_bobafett.png")
        embed.set_image(url="http://posterposse.com/wp-content/uploads/2014/12/wallpaper-1967961.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Bounty Hunter's Resolve")
        embed.add_field(name="Stats", value="`Power: 19885` `Speed: 147` `Health: 15,677`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - EE-3 Carbine - <:bobabasic:337232781694468096>", value="Deal Physical damage to target enemy with a 50% chance (doubled against Scoundrels) to attack again. Each attack has a 70% chance to inflict Damage Over Time for 2 turns ")
        embed.add_field(name="Special Ability - Death From Above - <:bobaspecial:337232782042464267>", value="Deal Physical damage to all enemies with an 80% chance to inflict Ability Block for 1 turn and a 50% chance to inflict Damage Over Time for 2 turns. Inflict Ability Block on the selected target for 2 turns.")
        embed.add_field(name="Special Ability - Execute - <:bobaspecial1:337232781702725632>", value="Deal Physical damage to target enemy and dispel all status effects on them. Deal 30% more damage for each effect dispelled. Enemies defeated by this ability can't be revived. Reduce all cooldowns by 1 on a finishing blow. This attack can't be Evaded.")
        embed.add_field(name="Leader Ability - Dead or Alive - <:Bobalead:337232781287489536>", value="All allies gain 50% Critical Damage and 10% Critical Chance. Bounty Hunter allies gain 15 Speed for each debuffed enemy, gain Max Health equal to 50% of the total Potency of all Bounty Hunter allies, and gain 15% Turn Meter whenever a Thermal Detonator explodes.")
        embed.add_field(name="Unique Ability - Bounty Hunter's Resolve - <:bobaunique:337232781425770496>", value="At the start of battle, and whenever he defeats an enemy, Boba Fett recovers 100% Protection and gains Bounty Hunter's Resolve until he is defeated. Bounty Hunter's Resolve: Boba Fett ignores Taunts during his turn. When defeated, revive at 100% Health. Can't be Dispelled or prevented.")
        embed.add_field(name="Usage", value="Boba Fett is a must get for beginner players. His basic can deal insane amount of damages and his special known as **Death From Above** can sometimes inflict Ability Block on all enemies. His 2nd Special **Execute** can also terminated an enemy easily on a Critical Hit and they have about 3+ Buffs and on finishing blow, reduce all his cooldowns by 1 and that enemy cannot be revived under any kinds! But getting him to Gear 11 is not that easy :wink:")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
    
         
    if message.content.startswith("!Cad-Bane"): 
        embed=discord.Embed(title="**Cad Bane**",color=discord.Colour(ff0000), description="High damage attacker with a powerful stun and bonuses against Jedi characters ")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_cadbane.png")
        embed.set_image(url="http://overmental.com/wp-content/uploads/2015/07/4433746-8523675652-cad-b-790x556.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability ")
        embed.add_field(name="Stats", value="`Power: 16695` `Speed: 113` `Health: 14,623` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Gun Slinger - <:cadbasic:337234002345721867>", value="Deal Physical damage to target enemy with a 55% chance to attack again. Cad Bane has a 50% chance to gain 15% Turn Meter with each attack.")
        embed.add_field(name="Special Ability - Stun Glove - <:cadspecial:337234010587660298>", value="Deal unavoidable Physical damage to target enemy and Stun for 1 turn. In addition, remove 40% Turn Meter, or 100% Turn Meter if the target is a Jedi.")
        embed.add_field(name="Leader Ability - Hunter's Reflexes - <:cadleader:337234063498936323>", value="Scoundrel allies gain 20% Evasion and gain 25% Turn Meter whenever they Evade.")
        embed.add_field(name="Unique Ability - Jedi Hunter - <:cadunique:337234036126646273>", value="Cad Bane has +35% Critical Chance and +20% Critical Damage when attacking Jedi enemies")
        embed.add_field(name="Usage", value="Cad Bane is very useful when fighting against Jedi teams due to his special **Stun Glove** and his unique **Jedi Hunter** can give bonuses to Cad Bane. His basic ability have to attack again and it can deals devastate amount of damages sometimes. He is also good for Credit Heist, Droid Smuggling event, and Critical Chance Mod Challenge. But Cad Bane's pretty useless for other kinds in the game.")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")
                        
        await bot.send_message(message.channel, embed=embed) 
        
        
        
    if message.content.startswith("!Cody"): 
        embed=discord.Embed(title="**CC-2224 Cody**",color=discord.Colour(0000ff), description="Clone Attacker that Stuns and call tons of Assists")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_cody.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/4/44/End_Days.jpg/revision/latest?cb=20111028234105")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Ghost Company Commander")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 115` `Health: 15,328` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Alpha Strike - <:Codybasic:337572976700555264>", value="Deal Physical damage to target enemy and gain 20% Turn Meter. Gain an additional 20% Turn Meter if that enemy has more than 50% Health, and an additional 20% Turn Meter if that enemy has less than 50% Turn Meter")
        embed.add_field(name="Special Ability - AT-TE Mass-Driver Cannon - <:codyspecial:337572976725721088>", value="Deal Special damage to target enemy and 35% less damage to all other enemies. If this attack scores at least 2 Critical Hits, Stun the primary target for 1 turn.")
        embed.add_field(name="Special Ability - The 212th Attack  - <:codyspecial1:337572976801218560>", value="Call all Clone allies and one random ally to assist. These Assists deal 40% less damage. Each time an Assist scores a Critical Hit, reduce the cooldowns of this ability by 1.")
        embed.add_field(name="Leader Ability - Ghost Company Commander - <:codylead:337572976327131136>", value="Clone allies gain 30% Critical Chance, and other allies gain half that amount. Cody gains 60% Defense for each living Clone ally and other Clone allies gain half that amount. Clone allies recover 5% of their Max Protection whenever they use a Basic ability.")
        embed.add_field(name="Usage", value="CC-2224 Cody can be useful for AAT raids and Arena if pair with Clone Troopers. His Alpha Strike and AT-TE Mass-Driver Cannon can sometimes deal insane amount of damage. The 212th Attack can be used very frequently if everytime his allies score critical hits. He is very useful when leading a Clone team in Phase 4 HAAT, but he kinda useless for other aspects in the game 😞")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        


    if message.content.startswith("!Cassian-Andor"): 
        embed=discord.Embed(title="**Cassian Andor**",color=discord.Colour(0000ff), description="Rebel Support who buffs allies at the start of battle and debuffs enemies during the battle.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_cassian.png")
        embed.set_image(url="http://screenrant3.imgix.net/wp-content/uploads/2017/01/Diego-Luna-as-Captain-Cassian-Andor-in-Rogue-One-A-Star-Wars-Story.jpg?auto=format&cs=tinysrgb&q=20&w=1000&h=500&fit=crop&dpr=1.5")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Groundwork")
        embed.add_field(name="Stats", value="`Power: 18903` `Speed: 134` `Health: 17,562`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Two Steps Ahead - <:cassbasic:337572974339031041>", value="Deal Physical damage to target enemy with a 85% chance to inflict Buff Immunity for 2 turns.")
        embed.add_field(name="Special Ability - Shock Grenade - <:Cassspecial:337572976713269249>", value="Inflict Ability Block, Defense Down, Healing Immunity, Offense Down and Speed Down (once each) on random enemies for 2 turns. If the primary target is Empire, Expose them for 2 turns. If K-2SO is present, he is called to Assist. Then, gain 20% Turn Meter for each debuffed enemy.")
        embed.add_field(name="Special Ability - Crippling Shot- <:cassspecial1:337572976511680513>", value="At the start of each encounter all Rebel allies gain Protection Up (20%) for 3 turns, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.")
        embed.add_field(name="Unique Ability - Groundwork - <:CassUnique:337572976637640704>", value="At the start of each encounter all Rebel allies gain Protection Up (20%) for 3 turns, all Rebel Attackers gain Defense Up for 3 turns, all Rebel Supports gain Potency Up for 3 turns, and all Rebel tanks gain Tenacity Up for 3 turns. If K-2SO is present, he gains all of these buffs.")
        embed.add_field(name="Usage", value="Cassian Andor is a useful players for multiple type of aspects in game. His Shock Grenade can spread debuffs very frequently because is only have a cooldowns 2 and you gain Cassian 100% TM if all enemies have at least a debuff on them. His Crippling Shot can apply every single debuffs on that enemy's allies to that enemy. He paired very well with K2-SO since he can assist Cassian on his special and he gain all bonuses on his unique!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")

        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Captain-Phasma"): 
        embed=discord.Embed(title="**Captain Phasma**",color=discord.Colour(ff0000), description="High-damage First Order support that can grant allies many extra attacks.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_phasma.png")
        embed.set_image(url="http://vignette2.wikia.nocookie.net/movie-villains/images/f/f3/Star-wars-captain-phasma-figurine-0.jpg/revision/latest?cb=20160811084922")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Fire At Will")
        embed.add_field(name="Stats", value="`Power: 18705` `Speed: 121` `Health: 21,118` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Onslaught - <:Phasmabasic:337572976675389440>", value="Deal Physical damage to target enemy and inflict Defense Down for 2 turns on a Critical Hit. If this attack is not a Critical Hit, Phasma has a 50% chance to gain Advantage for 2 turns instead.")
        embed.add_field(name="Special Ability - Victory March - <:phasmaspecial1:337572976763469824>", value="All allies gain 50% Turn Meter and Advantage for 2 turns.")
        embed.add_field(name="Special Ability - Fusillade - <:phasmaspecial1:337572976327131150>", value="Deal Physical damage to all enemies with a 90% chance to inflict Speed Down for 2 turns.")
        embed.add_field(name="Leader Ability - Fire At Will - <:Phasmalead:337572976478126081>", value="Whenever an ally attacks, they have a 20% chance to call a random ally to Assist. This chance is triple if the attacking ally is First Order. If that ally had Advantage, they regain it for 2 turns. First Order allies gain Advantage for 2 turns at the start of each encounter, can't be Critically Hit while they have Advantage, and gain 20% Potency.")
        embed.add_field(name="Usage", value="She is a must get once you unlocked Galactic War at level 40. Her **Victory March** can make a huge change to the battle situation. Her **Fusillade** can slow down high-speed characters. Her leader ability **Fire At Will** can grant tons of extra attacks to non-First Order allies and the chances are even higher if the attacking ally is First Order.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
   

    if message.content.startswith("!Chirrut-Imwe"): 
        embed=discord.Embed(title="**Chirrut Îmwe**",color=discord.Colour(0000ff), description="Balanced Rebel Attacker who dispels debuffs, heal allies, and grants Tenacity Up")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_chirrut.png")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6BRiE5HC1jZssxhT9EsAYKkaxduWatWnNfJ9DLr9_h79mkM9ulA")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability ")
        embed.add_field(name="Stats", value="`Power: 17071` `Speed: 153` `Health: 16,074 ` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Staff Strike - <:chirbasic:337598218403708929>", value="Deal Physical damage to target enemy with a 70% chance to gain Heal Over Time for 3 turns. If the target is debuffed, grant Heal Over Time to a random ally for 3 turns.")
        embed.add_field(name="Special Ability - As The Force Wills - <:chirspecial:337598229808152576>", value="All allies have their current Health percentages equalized. Dispel all debuffs from all allies and grant them a Heal Over Time effect for 4 turns for each effect dispelled. Allies that weren't debuffed gain Tenacity Up for 3 turns.")
        embed.add_field(name="Special Ability - Strength of Purpose- <:Chirspecial1:337598237953490944>", value="Deal Physical damage to target enemy, dealing 20% more damage for each buffed ally. If Baze Malbus is present, he is called to Assist. ")
        embed.add_field(name="Unique Ability - Indomitable Will - <:chirunique:337598261013643265>", value="Chirrut Îmwe gains +17% Counter Chance and Health Steal for each living enemy, double for Empire enemies. If Baze Malbus is present, he also gains these bonuses.")
        embed.add_field(name="Unique Ability - Resolute Endurance  - <:chirunique1:337598283541118976>", value="Whenever a Rebel ally is Critically Hit, they gain Heal Over Time for 2 turns. At the start of each turn, if Chirrut Imwe is alive, all allies with Heal Over Time recover 4% of their Max Health")        
        embed.add_field(name="Usage", value="Chirrut Îmwe is kinda for mid-game or advanced player since he isn't F2P until you're level 60. He works extremely well with his friend, Baze Malbus. We can call him the 'HoT Master' in the game since his abilities are always related to buffs and HoT. His **As The Force Wills** can change the tide of the battle, and his **Strength of Purpose** can one-shot kill an enemy, his unique is very helpful because he can grant Rebel allies HoT whenevet they are Critically Hit and it gives Baze and Chirrut (AKA Chaze) counter chance and Health Steal. He works well with any kind of line-ups but the best when paired with Rebels.")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Chief-Nebit"): 
        embed=discord.Embed(title="**Chief Nebit**",color=discord.Colour(0000ff), description="Cunning Jawa Tank with Stealth synergies who can reduce cooldowns")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_jawa_nebit.png")
        embed.set_image(url="https://vignette1.wikia.nocookie.net/starwars/images/0/04/NebitHS-ANH.png/revision/latest?cb=20130226042239")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability ")
        embed.add_field(name="Stats", value="`Power: 16299` `Speed: 115` `Health: 27,248`(<:gearicong111:330366020365713408>, without mods")
        embed.add_field(name="Basic Ability - Sheltering Shot - <:Nebitbasic:337573879637606410>", value="Deal Physical damage to target enemy with a 70% chance to Protection Up equal to 20% of Nebit's Max Health for 2 turns to a random ally who is not Stealthed. ")
        embed.add_field(name="Special Ability - Distracting Negotiations -<:Nebitspecial:337573879612571648>", value="Nebit taunts for 2 turns and gain Heal Over Time for 3 turns. Reduce the cooldowns of all Jawa and Droid allies by 1. ")
        embed.add_field(name="Special Ability - Desert Ambush - <:NebitSpecial1:337573880732450816>", value="Deal Physical damage to target enemy and a random ally to Assist dealing 20% less damage. If the Assisting ally is a Jawa or a Droid, call another random ally to Assist. All Jawa called to Assist gain Stealth for 3 turns.")
        embed.add_field(name="Leader Ability - Raiding Parties - <:Nebitlead:337573880673599488>", value="Jawa and Droid allies gain 30% Critical Chance and inflict Critical Chance Down for 3 turns on a Critical Hit. ")
        embed.add_field(name="Usage", value="Chief Nebit is very useful when represent as a tank under a Droid team, he is a very solid characters who can taunt for 2 turns on his Distracting Negotiations, plus his Heal Over Time will let him to stay in the battlefield longer. His Desert Ambush can be use back-to-back if at least 2-3 Jawa or Droid allies is alive. But he is not that great when paired with non-Jawa or non-Droid allies. He is F2P once you unlocked Squad Arena.")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")        
     
        await bot.send_message(message.channel, embed=embed) 

    if message.content.startswith("!Chopper"): 
        embed=discord.Embed(title="**C1-10P 'Chopper'**",color=discord.Colour(0000ff), description="Surly Phoenix Support who Taunts and Dispels, and can recover Phoenix cooldowns.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_chopper.png")
        embed.set_image(url="http://a.dilcdn.com/bl/wp-content/uploads/sites/6/img/news/chopper1.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 16707` `Speed: 152` `Health: 18,962` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Reckless Fling- <:chopbasic:339727868022226944>", value="Deal Physical damage to target enemy and grant a random Phoenix ally Offense Up, Defense Up, or Speed Up at random for 2 turns, with a 60% chance to reduce that ally's cooldowns by 1.")
        embed.add_field(name="Special Ability - Cantankerous Clanker - <:chopspecial:339727868256976896>", value="Chopper gains Taunt for 1 turn. While he has this Taunt buff, Chopper gains 30% Evasion.")
        embed.add_field(name="Special Ability - Metal Menace - <:chopspecial1:339727868055519252>", value="Dispel all buffs on target enemy, For each buff dispelled away, all enemies lose 10% Turn Meter, and Chopper gains 25% Protection. Droid targets are also Stunned for 1 turn.")
        embed.add_field(name="Unique Ability - Maintenance Protocols - <:chopunique:339727867631894540>", value="At the start of his turn, Chopper recovers 15% of his Max Health. In addition, whenever he is damaged, he gains Protection Up (15%) if he doesn't have Protection Up.")
        embed.add_field(name="Usage", value="Chopper (AKA C1-10P) have various style of teams to play with like Resistance, Phoenix, No Dispeller, etc. teams. His Cantankerous Clanker can give him a huge evasion for 1 turn. His Metal Menace can recover a insane amount of Protection to keep him alive as long as possible. He is a very good characters under a Resistance team since he can make enemies lose Turn Meter and keep Resistance applying Exposes to enemies. He is a very good (not the best) character for beginners. 😎")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")     
        
        await bot.send_message(message.channel, embed=embed) 
       
    if message.content.startswith("!Thrawn"): 
        embed=discord.Embed(title="**Grand Admiral Thrawn**",color=discord.Colour(ff0000), description="Calculating Empire Leader who can halt enemies in their tracks, and grant Empire allies a new Special ability")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_thrawn.png")
        embed.set_image(url="https://s-media-cache-ak0.pinimg.com/736x/49/b7/c4/49b7c45708d56ea5919d55f4fcd5119d--grand-admiral-thrawn-empire.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="2 Zeta abilities: Legendary Strategist & Ebb and Flow")
        embed.add_field(name="Stats", value="`Power: 22081` `Speed: 150` `Health: 25,981`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Manipulate - <:thrawnbasic:340116356554817537>", value="Characters: Deal Special damage to target enemy, grant them Speed Up for 1 turn, or if they already had Ability Block, inflict Stun for 1 turn instead. When this Speed Up expires, inflict Ability Block for 1 turn. These effects can't be resisted. Raid Boss: Deal Special damage to target enemy and inflict Defense Down for 2 turns, which can't be Resisted.")
        embed.add_field(name="Special Ability - Fracture - <:thrawnspecial:340116356697554949>", value="Deal Special damage to target enemy 4 times, dispel all buffs on them, remove 50% Turn Meter, and inflict Fracture until the start of Thrawn's next turn or Thrawn is defeated. This Fracture can't be Copied or Dispelled. Fracture on Characters: Speed set to 0, can't gain buffs, bonus Attacks, or bonus Turn Meter. Fracture on Raid Bosses: -50% Speed (Doesn't stack with Speed Down), can't gain buffs, and -30% Counter Chance.")
        embed.add_field(name="Special Ability - Grand Admiral's Command - <:thrawnspecial1:340116357158928386>", value="Swap Turn Meter with target other ally. Dispel all debuffs on Thrawn and that ally, and they recover 40% Protection.")
        embed.add_field(name="Leader Ability - Legendary Strategist- <:thrawnlead:340116357037293570>", value="Empire allies have +15% Max Protection, +25% Offense, and gain 20% Turn Meter whenever they Resist a detrimental effect pr suffer a debuff. Whenever an Empire ally gains or loses a status effect, they recover 2% Protection. Empire allies gain a new Special ability, Maneuver: Dispel all debuffs on that character, and gain 50% Turn Meter (Cooldowns 3.)") 
        embed.add_field(name="Unique Ability - Ebb and Flow - <:thrawnunique:340116356802543620>", value="Thrawn has 100% Counter Chance, +100% Tenacity, and -50% Speed whenever any enemies are Fractured. Whenever an Empire ally uses a Special ability while Thrawn is active, that ally gains 15% Turn Meter and, if any enemies are Fractured, Thrawn and Fractured enemies lose 15% Turn Meter.")
        embed.add_field(name="Usage", value="Thrawn is an absolute amazing character. His **Manipulate** can turn Speed Up into Ability Block (easy with Darth Nihilus), or inflict Stun if they already had Ability Block. His **Fracture** (AKA Shock 2.0) can disabled an enemy for a while until Thrawn's next turn. **Grand Admiral's Command** allows Thrawn and an ally to dispel all debuffs on them and recover 40% Protection (that's a lot!). **Legendary Strategist** gives Empire allies a new Special ability to self-cleanse, something they really need. **Ebb & Flow** allows him to control Fracture enemies and give him insane bonuses!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master (Also The Chosen One)**")
                        
        await bot.send_message(message.channel, embed=embed) 
                        
    
    if message.content.startswith("!CS-P1"): 
        embed=discord.Embed(title="**Clone Sergeant - Phase I**",color=discord.Colour(0000ff), description="Clone Attacker with AoE damage and Turn Meter reduction")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclonegreen.png")
        embed.set_image(url="http://www.mwctoys.com/images1/review_sstroop_large.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 16120` `Speed: 107` `Health: 16,983` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Z-6 Rotary Blaster- <:csp1basic:340169202302320640>", value="Deal Physical damage to target enemy and gain 50% Turn Meter on a critical hit.")
        embed.add_field(name="Special Ability - Suppressive Fire - <:csp1special:340169202239275008>", value="Deal Physical damage to all enemies and remove 50% of their Turn Meter.")
        embed.add_field(name="Unique Ability - Concentrated Fire - <:csp1unique:340864936513372160>", value="Clone Sergeant - Phase I gains 4.5 Critical Chance Up for each living Clone ally. In addition, he has +10% Critical Damage and Offense Up for 2 turns whenever he critically hits.")
        embed.add_field(name="Usage", value="He is very good when under a Clone team team since he gains a bonus for each living Clone ally. His **Suppressive Fire** can deal a huge amount of damage. But he is not that good overall nowadays. He is your 1st character when you first started the game.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!Chewbacca"): 
        embed=discord.Embed(title="**Clone Wars - Chewbacca**",color=discord.Colour(0000ff), description="Durable Tank with both Taunt and self-Healing")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_chewbacca.png")
        embed.set_image(url="https://2.bp.blogspot.com/-ZIL336AWVFM/VZZwSksccgI/AAAAAAAAfGU/0MvC6isBM_M/s320/peter%2Bmayhew%2Bchewbacca%2Bepisode%2B3.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Defiant Roar")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 106` `Health: 25,368` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Bowcaster - <:chewiebasic:341175507225935874>", value="Deal Physical damage to target enemy with a 55% chance to remive 50% Turn Meter")
        embed.add_field(name="Special Ability - Wookiee Rage - <:chewiespecial:341175507670269952>", value="Chewbacca Taunts and gains 30% Health Up for 2 turns.")
        embed.add_field(name="Special Ability - Defiant Roar- <:chewiespecial1:341175507188187137>", value="Chewbacca dispels all debuffs from himself, recovers 50% of his Max Health, gains Defense Up for 3 turns, and has a 50% Chance to gain 25% Turn Meter.")
        embed.add_field(name="Leader Ability - Wookiee Resolve - <:chewielead:341175507745898496>", value="All allies have +50 Defense, and a 50% chance to gain Defense Up for 3 turns whenever they are damaged")
        embed.add_field(name="Usage", value="Chewbacca is a very good beginner character, he is your 3rd character in the game when you first started the game. But he is like the worst zeta character in the game. His **Defiant Roar** dispels all debuffs from himself and recovers half of his Max Health, it's a very useful ability. But he is very useless when comparing to advanced players. *DO NOT* zeta him unless you really need him!")
        embed.add_field(name="Ahnald Ranking", value="**Youngling**")
        
        await bot.send_message(message.channel, embed=embed) 
        
        
    if message.content.startswith("!CLS"): 
        embed=discord.Embed(title="**Commander Luke Skywalker**",color=discord.Colour(0000ff), description="Abilities (the complete command was too long, so we had to split it :joy:")
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
        
        embed=discord.Embed(title="**Commander Luke Skywalker**",color=discord.Colour(0000ff), description="Additional information.")
        embed.set_thumbnail(url='https://swgoh.gg/static/img/assets/tex.charui_lukebespin.png')
        embed.set_image(url="https://cnet4.cbsistatic.com/hub/i/r/2014/04/25/3ab1aceb-4bb6-42ca-95d5-5630fe3c5050/resize/570xauto/0efdbe9f91f476abc5626e3f85da3ef9/luke-bespin.jpg")
        embed.add_field(name="Stats", value="`Power: 24864` `Speed: 152` `Health: 18,010` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="<:zeta:327437604465278977>", value="3 Zeta abilities: Rebel Maneuvers, Learn Control & It Binds All Things.")
        embed.add_field(name="Usage", value="Commander Luke Skywalker is a absolute beast, definitely way better than our good old Farmboy Luke. He is a balanced character, great on both Offense and Defense. His basic **Destined Strike** can apply Defense Down, Speed Down and Stun. His special **Use the Force** can remove 100% Turn Meter and inflict Buff Immunity for 2 turns, perfect on a pre-taunter like Baze or Shoretrooper. **Call to Action** dispels all debuffs from Luke, and lets him gain 100% TM. His leader ability can give Rebel allies 50% Counter Chance. He is only available in the Hero's Journey (Legendary Event)")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**") 
        
        await bot.send_message(message.channel, embed=embed) 


       
        
    if message.content.startswith("!CUP"): 
        embed=discord.Embed(title="**Coruscant Underworld Police**",color=discord.Colour(0000ff), description="Support that shuts down enemies with Stuns and Offense Down")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_coruscantpolice.png")
        embed.set_image(url="https://vignette2.wikia.nocookie.net/starwars/images/1/1c/CSF_underworld.png/revision/latest?cb=20130224221934 ")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 15922` `Speed: 112` `Health: 15,432` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Non-Lethal Takedown - <:cupbasic:342948948086095873>", value="Deal Physical damage to target enemy with a 50% chance to Stun for one turn.")
        embed.add_field(name="Special Ability - Non-Lethal Crowd Control - <:cupspecial:342948948606189568>", value="Deal Physical damage to all enemies with a 70% chance to inflict Offense Down for 2 turns")
        embed.add_field(name="Unique Ability - Non-Lethal Specialist - <:cupunique:342948947884638219>", value="Coruscant Underworld Police gains 30% Potency. In addition, he gains 20% Turn Meter whenever he inflicts a negative status effect.")
        embed.add_field(name="Usage", value="CUP is like the worst character in the game. His **Non-Lethal Takedown** can Stun enemies. **Non-Lethal Specialist** grants him 30% Potency and gains 20% Turn Meter whenever he inflicts a debuff. His abilities is very simple.  He haven't got any kind of rework overall. Don't farm him in Squad Arena unless you think he is good, and I know you don't think like that.")
        embed.add_field(name="Ahnald Ranking", value="**Youngling**")        
        
        await bot.send_message(message.channel, embed=embed) 
       
        
    if message.content.startswith("!Count-Dooku"): 
        embed=discord.Embed(title="**Count Dooku**",color=discord.Colour(ff0000), description="High-damage attacker with stun, bonus attacks, and incredible counter-attacking")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_dooku.png")
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Count_Dooku.png/220px-Count_Dooku.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Flawless Riposte")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 167` `Health: 16,473` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Hindering Press - <:dookubasic:343004456633368576>", value="Deal Physical damage to target enemy with a 50% chance to attack again. These attacks have a 25% chance to Stun for 1 turn and a 25% chance to inflict Ability Block for 1 turn. Debuff chances doubled against Jedi")
        embed.add_field(name="Special Ability - Force Lightning - <:dookuspecial:343004456348286976>", value="Deal Special damage to target enemy with a 50% chance to Shock and Stun them for 1 turn, and a 50% chance to Stun a random enemy. Debuff chances doubled against Jedi.")
        embed.add_field(name="Special Ability - Master Tactician - <:dookulead:343004546613641217>", value="All allies gain 15% Evasion and gain Offense Up for 2 turns whenever they evade.")
        embed.add_field(name="Unique Ability - Flawless Riposte - <:dookunique:343004456348024832>", value="Count Dooku has 100% Counter Chance. In addition, whenever he attacks outside of his turn, he deals 30% more damage, has a 25% chance to gain 45% Turn Meter, recovers 10% Protection, and gains Critical Hit Immunity for 1 turn.")
        embed.add_field(name="Usage", value="Count Dooku is a very deadly character. His **Hindering Press** can Stun and Ability Block an enemy, which is super annoying on a counter attack. **Force Lightning** can also Stun an enemy, plus with a chance to Shock that enemy. His unique ability known as **Flawless Riposte** gives him 100% Counter Chance, in addition, he deals more damage, chance to gain 45% Turn Meter, and recovers 10% Protection when counter-attacking. When he fights with a Nihilus lead, he is unstoppable since Nihilus gives 150% Health Steal (w/ Zeta) so whenever Dooku counter-attacks someone, he heals a lot, which makes him sort of invincible, so you need Kylo, or someone else that stuns or inflicts healing immunity.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
        await bot.send_message(message.channel, embed=embed) 
                       
    if message.content.startswith("!Savage-Opress"):
        embed=discord.Embed(title="Savage Opress",color=discord.Colour(ff0000), description="Durable Attacker that crushes low-health units and becomes stronger when attacked")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_savageopress.png")
        embed.set_image(url="https://vignette4.wikia.nocookie.net/starwars/images/1/1b/Cybernetic_savageopress.jpeg/revision/latest?cb=20150324112612")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Brute")
        embed.add_field(name="Stats", value="`Power: 18903` `Speed: 123` `Health: 23,533` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Staggering Blow - <:savagebasic:343478306198388738>", value="Deal Physical damage to target enemy with a 50% chance (doubled on a Critical Hit) to inflict Offense Down for 2 turns.")
        embed.add_field(name="Special Ability - Overpower - <:savagespecial:343478306412167178>", value="Deal Physical damage to target enemy and gain Critical Chance Up and Critical Damage Up for 3 turns on a finishing blow. If the target has 50% Health or below, this attack deals massive damage and can't be Evaded.")
        embed.add_field(name="Leader Ability - Pain is Weakness - <:savageleadunique:343478306819014656>", value="Sith allies gain 75% Defense and 30% Tenacity. Other allies gain half those amounts.")
        embed.add_field(name="Unique Ability - Brute - <:savageleadunique:343478306819014656>", value="Whenever Savage takes damage, he gains Offense Up, Defense Up, and Heal Over Time for 2 turns and gains 30% Turn Meter. At the end of his turns, Savage Dispels all debuffs on a random other Sith ally and gains those debuffs for 1 turn. Dispel all debuffs from Savage whenever he is Critically Hit.")       
        embed.add_field(name="Usage", value="Savage Opress is a very good balanced character, he is good on both offense and defensive. His **Stagerring Blow** can deal a decent amount of damage, mostly because of the Offense Up buff, that he practically always has. **Overpower** can insta-kill an enemy if they are below 50% Health. His unique Brute can give some Defense Up, Offense Up, Heal over Time (stacking), and gains Turn Meter whenever he took damages. He is a great Sith and Beginner character overall!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed) 
        
    if message.content.startswith("!Sith-Trooper"):
        embed=discord.Embed(title="Sith Trooper",color=discord.Colour(ff0000), description="Sith Tank who Taunts and ignores enemy Protection")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_sithtrooper.png")
        embed.set_image(url="http://media.moddb.com/images/downloads/1/64/63278/Soldat_Imprial.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16120` `Speed: 95` `Health: 25,985` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Disruptor Blast - <:sithTbasic:343744322354806786>", value="Deal Physical damage to target enemy with a 70% chance to inflict Defense Down for 3 turns. If the target was already debuffed, ignore their Protection.")
        embed.add_field(name="Special Ability - Crimson Barrage - <:sithTspecial:343744322203680770>", value="Deal Physical damage to all enemies with a 70% chance to inflict Offense Down for 2 turns. Then gain Protection Up equal to 5% for each debuffed enemy for 2 turns. This attack ignores Protection.")
        embed.add_field(name="Unique Ability - Vaiken's Legacy - <:sithTunique:343744392713994242>", value="Sith Trooper has +100% Defense. Whenever a Sith ally uses a Special ability or falls below 50% Health, Sith Trooper gains Defense Up for 2 turns. If he already had Defense Up, he gains Taunt for 2 turns. If he already had Taunt, he gains Retribution for 2 turns. Sith Trooper gains Defense Up for 2 turns at the start of each encounter.")
        embed.add_field(name="Usage", value="Sith Trooper is a very good Sith tank. His damage outputs is kinda weak. His **Disruptor Blast** can inflict Defense Down for 3 turns, **Crimson Barrage** can inflict Offense Down, ignores Protection, and grant him Protection Up (5%) for each debuffed enemy for 2 turns. His **Vaiken's Legacy** can grant Defense Up -> Taunt -> Retribution whenever a Sith ally uses a Special ability. You want him to stay alive as long as possible.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")

        await bot.send_message(message.channel, embed=embed) 

        
    if message.content.startswith("!Sith-Assassin"):
        embed=discord.Embed(title="Sith Assassin",color=discord.Colour(ff0000), description="Elusive Sith Attacker with Stealth synergy")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_sithassassin.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 15922` `Speed: 151` `Health: 17,895` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Exploit Weakness - <:sithAbasic:343744206378106881>", value="Deal Physical damage to target enemy, inflict Evasion Down for 2 turns, and gain Offense Up for 2 turns. If the target was already debuffed, gain Stealth for 2 turns. If Sith Assassin already had Stealth, ignore the target's Protection.")
        embed.add_field(name="Special Ability - Dark Shroud - <:sithAspecial:343744207078293514>", value="Dispel all debuffs from Sith Assassin and gain Stealth and Foresight for 2 turns. If she already had Stealth, gain Speed Up and Tenacity Up for 2 turns. Sith allies gain 12% Turn Meter for each buff on her.")
        embed.add_field(name="Special Ability - Electrocute - <:sithAspecial1:343744206835286027>", value="Deal Physical damage to target enemy and inflict Stun for 1 turn. If Sith Assassin already had Stealth, Dispel all buffs from Sith Assassin, deal 5% more damage for each effect dispelled and each living Sith ally, and ignore the target's Protection.")   
        embed.add_field(name="Usage", value="Sith Assassin is an advanced Sith attacker. Her **Exploit Weakness** can deal a decent amount of damage and inflict Evasion Down for 2 turns. **Dark Shroud** gives her Stealth and Foresight, plus Speed Up and Tenacity Up for 2 turns (If she already had Stealth), and gives TM to Sith allies, so it's a very useful ability. Her 2nd Special, **Electrocute** deals huge amount of damage, if she has a lot of buffs and living Sith allies. She is a little bit of hard to farm overall.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")

        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith("!Echo"): 
        embed=discord.Embed(title="**CT-21-0408 'Echo'**",color=discord.Colour(0000ff), description="Clone Support that automatically Assists allies and can Dispel all enemies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_echo.png")
        embed.set_image(url="http://media.moddb.com/images/mods/1/13/12901/EchoARCarmor-TC.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16497` `Speed: 129` `Health: 16,850`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Supporting Fire - <:EchoBasic:344013068491030529>", value="Deal Physical damage to target enemy and grant 20% Turn Meter to random another ally with less than 50% Turn Meter.")
        embed.add_field(name="Special Ability - EMP Grenade - <:EchoSpecial:344013099449319435>", value="Deal Special damage to all enemies and Dispel all positive status effects on them.")
        embed.add_field(name="Unique Ability - By the Book - <:EchoUnique:344013124413685761> ", value="Clone allies recover 7% of their Max Health whenever they use a Basic ability. This effect can't trigger more than two times before their next turn, and is disabled if Echo is defeated.")
        embed.add_field(name="Unique Ability - Follow-Up - <:EchoUnique1:344013144445812739>", value="Whenever another ally uses a Basic ability during their turn, Echo has a 30% chance to Assist, dealing 40% less damage. This Assist chance is doubled if the attacking ally is a Clone.")
        embed.add_field(name="Usage", value="Echo is very good mid-game character. His **EMP Grenade** can deal mass damage to all enemies. He has 2 Unique abilities known as **By the Book** allowed his Clone allies to recover 7% of their Max Health but can only be triggered twice before their next turn. **Follow-Up** will allow Echo to Assist his ally and the chance is doubled if a Clone ally is attacking. He is pretty good when paired with Clones in Raids, but Squad Arena, meh. He is farmable in the Guild Store and the Fleet Store.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")   
        
        await bot.send_message(message.channel, embed=embed)
        

    if message.content.startswith("!Fives"): 
        embed=discord.Embed(title="**CT-5555 'Fives'**",color=discord.Colour(0000ff), description="Tank character with high Defense, enemy speed reduction and joint attack ability")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_fives.png")
        embed.set_image(url="https://s-media-cache-ak0.pinimg.com/736x/bd/77/06/bd770684904c737613405932d038e3a6.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Tactical Awareness")
        embed.add_field(name="Stats", value="`Power: 18705` `Speed: 115` `Health: 26,741`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Dual DC-17 Blasters - <:5sBasic:344012837888458752>", value="Deal Physical damage to target enemy and inflict Speed Down for 2 turns. Attack again if enemy is inflicted with Speed Down.")
        embed.add_field(name="Special Ability - Combined Fire - <:5sSpecial:344012855005151232>", value="Deal Physical damage to target enemy and call a random ally to Assist. If the Assisting ally is a Clone, both attackers deal 75% more damage.")
        embed.add_field(name="Leader Ability - Veteran Clone Trooper - <:5sLead:344012868426924034>", value="Clone allies gain 65 Defense, and other allies gain half that amount.")
        embed.add_field(name="Unique Ability - Tactical Awareness - <:5sUnique:344012880045277194>", value="Fives has 85% Counter Chance and +50% Counter Damage. Fives gains 15% Turn Meter whenever another Clone ally takes damage and 7.5% Turn Meter whenever a non-Clone ally takes damage.")
        embed.add_field(name="Usage", value="Fives is a great beginning character overall. He can counter attack a lot but it becomes useless when he gets inflicted with Daze :weary:. As usual, a tank - always good at Defense, never good at Offense - his damage is very low but can reap enemies' health slowly but surely. He works well with a Clone team!")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
        
        await bot.send_message(message.channel, embed=embed)
                        
    if message.content.startswith("!Chief-Chirpa"): 
        embed=discord.Embed(title="**Chief Chirpa (Reworked)**",color=discord.Colour(0000ff), description="Ewok Leader that greatly improves ally Basic abilities")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ewok_chirpa.png")
        embed.set_image(url="https://vignette3.wikia.nocookie.net/starwars/images/a/a1/Chief_Chirpa.jpg/revision/latest?cb=20091202194819")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Simple Tactics")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 116` `Health: 18,941`  (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Bounding Strike - <:ChirBasic:345902905666043904>", value="Deal Physical damage to target enemy. In addition, Chirpa gains 35% Turn Meter if that enemy had more than 50% Turn Meter.")
        embed.add_field(name="Special Ability - Ancestral Secrets - <:ChirSpecial:345902929196089355>", value="All allies recover 20% of their Max Health and gain Heal Over Time (20%) for 3 turns. Ewok allies also gain Retribution for 2 turns and Heal Over Time for 1 additional turn.")
        embed.add_field(name="Special Ability - Tribal Unity - <:ChirSpecial1:345903076160569345>", value="Grant all allies Speed Up for 2 turns, then call all Ewok allies and one other random ally to Assist.")
        embed.add_field(name="Unique Ability - Simple Tactics - <:ChirLead:345903090739970049>", value= "Ewok allies gain 20% Turn Meter and deal 10% more damage whenever they perform a Basic attack. These effects are halved for other allies. Whenever an Ewok ally uses a Special ability, 60% chance to call another random Ewok ally to Assist.")
        embed.add_field(name="Usage", value="Chirpa is a great character, but he is only F2P farmable at Cantina 5-B. His basic can gain Chirpa 35% TM. **Ancestral Secrets** heal all allies and gain them Heal over Time for 3 turns, plus Ewok allies gain HoT for an additional turn, and Retribution for 2 turns. **Tribal Unity** can all Ewok allies and a random allies to Assist. He is the most important when you're running a Ewok team!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")
        
        await bot.send_message(message.channel, embed=embed)
 
    if message.content.startswith("!Rex"): 
        embed=discord.Embed(title="**CT-7567 'Rex'**",color=discord.Colour(0000ff), description="Clone leader with a variety of abilities to support and protect Clone allies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_trooperclone_rex.png")
        embed.set_image(url="https://i0.wp.com/MynockManor.com/wp-content/uploads/2015/10/Rex-and-Ahsoka-Reunited.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 16497` `Speed: 140` `Health: 13,570` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Impeding Shot - <:RexBasic:344013203820249088>", value="Deal Physical damage to target enemy and remove 25% Turn Meter")
        embed.add_field(name="Special Ability - Squad Discipline - <:RexSpecial:344013223126761472>", value="Dispel all negative status effects on all allies and grant them Tenacity Up for 3 turns. Clone allies gain 60% Turn Meter, plus an additional 10% Turn Meter for each effect dispelled this way, and other allies gain half that amount.")
        embed.add_field(name="Special Ability - Subdue - <:RexSpecial1:344013241913049088>", value="Deal Physical damage to target enemy, plus bonus damage equal to 25% of the target's Maximum Health.")
        embed.add_field(name="Leader Ability - Brother In Arms - <:RexLead:344013258371366932>, value="Clone allies gain 20% Max Health, and other allies gain half that amount. In addition, whenever an ally suffers a Critical Hit, all Clone allies gain 15% Turn Meter, and other allies gain half that amount.")
        embed.add_field(name="Usage", value="Rex is a amazing character for advanced players. **Impeding Shot** remove 25% TM from an enemy, it always an useful ability in Raids. His **Squad Discipline** dispels all debuffs, grant them Tenacity Up, and a good amount of TM. His 2nd Special **Subdue** deals insane amount of damage to an enemy. He is a popular meta nowadays overall.")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
                         
    if message.content.startswith("!Darth-Maul"): 
        embed=discord.Embed(title="Darth Maul",color=discord.Colour(ff0000), description="Deadly Attacker that gains power and extra turns as enemies are defeated")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_maul.png")
        embed.set_image(url="https://vignette4.wikia.nocookie.net/starwars/images/5/50/Darth_Maul_profile.png")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Dancing Shadows")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 100` `Health: 14,319` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Raging Storm - <:MaulBasic:343784947468992523>", value="Deal Physical damage to target enemy. On a finishing blow, gain 100% Turn Meter and Offense Up for 2 turns. This attack deals double damage to Jedi.")
        embed.add_field(name="Special Ability - Whirling Blades - <:MaulSpecial:343784968096448514>", value="Deal Physical damage to all enemies and inflict Daze for 2 turns. This attack deals double damage to Jedi.")
        embed.add_field(name="Leader Ability - Dancing Shadows - <:MaulLeadUnique:343784985221922827>" value="All Sith allies gain 20% Evasion, gain 20% Turn Meter and Stealth for 1 turn at the start of each encounter and whenever they Evade or are Critically Hit, can't be Critically Hit while Stealthed, and gain Advantage for 2 turns whenever Stealth expires. The Stealth and Turn Meter from this ability ignores Taunting allies.")
        embed.add_field(name="Unique Ability - Power of Hatred - <:MaulLeadUnique:343784985221922827>" value="Darth Maul gains 20% Max Health, gains Max Health equal to 10% of the damage he deals, and Potency equal to 0.3% of his Max Health. Whenever an enemy is defeated, Darth Maul gains bonuses for the rest of the encounter. First Enemy: 25% Critical Chance Second Enemy: 25% Evasion Third Enemy: 25% Max Health recovery on hitting with an attack.")
        embed.add_field(name="Usage", value="Maul is a fabulous character, Zaul (`!zMaul`) is even more deadly. His basic deals insane amount of damage, and deals double damage on Jedi enemies. **Whirling Blades** inflicts Daze on all enemies for 2 turns (Incredibly good for Counter-Attackers), and still deals double damage on Jedi. His leader ability gains Sith allies Stealth, 20% Turn Meter whenever they are critically hits or Evaded an attack, after Stealth expires, they gain Advantage for 2 turns. His unique give bonuses as enemies are defeated. He is a absolute famous meta nowadays.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
        await bot.send_message(message.channel, embed=embed)
                        
    
    if message.content.startswith("!Nihilus"): 
        embed=discord.Embed(title="**Darth Nihilus**",color=discord.Colour(ff0000), description="Sith Support that can instantly defeat enemies by draining cooldowns")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_nihilus.png")
        embed.set_image(url="https://static.comicvine.com/uploads/scale_small/4/48954/1246062-darth_nihilus_by_neecoala.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="2 Zeta abilities: Lord of Hunger and Wound in the Force")
        embed.add_field(name="Stats", value="`Power: 21685` `Speed: 120` `Health: 24,093` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Ceaseless Craving - <:NihiBasic:343787365858410507>", value="Deal Special damage to target enemy and Dispel all buffs on them. If any buffs were dispelled, reduce the cooldown of Drain Force by 1")
        embed.add_field(name="Special Ability - Drain Force - <:NihiSpecial:343787382874701835>", value="Deal Special damage to all enemies with a 50% chance (doubled against debuffed enemies) to increase their cooldowns by 1. For each cooldown increased, reduce the cooldown of Annihilate by 1.")
        embed.add_field(name="Special Ability - Annihilate - <:NihiSpecial1:343787392202702850>", value="Instantly defeat target enemy. Nihilus gains Max Health equal to the target's Max Health. The defeated target can't be Revived. This ability can't be Evaded and starts on cooldown.")
        embed.add_field(name="Leader Ability - Lord of Hunger - <:NihiLead:343787415254728704>", value="Sith allies gain 60% Offense and 150% Health Steal. Sith allies lose all Protection and gain that much Max Health. Sith allies are immune to Healing effects that aren't Health Steal and can't score Critical Hits.")
        embed.add_field(name="Unique Ability - Wound in the Force - <:NihiUnique:343787433378316300>", value="At the start of each of his turns, Nihilus inflicts Damage Over Time for 2 turns on a random enemy that doesn't have any debuffs. If all enemies are debuffed, inflict Damage Over Time on a random enemy. At the start of each enemy turn, Nihilus inflicts Health Down on them for 2 turns."
        embed.add_field(name="Usage", value="Nihilus is completely amazing in Arena and Raids, he is viable at 3* <:gearicong8:330366019979706380>. His basic can deal good damage and dispel all buffs on that enemy (Good for Thrawn's basic). **Drain Force** can increase enemy's cooldowns by 1 (100% chance if they were debuffed!), and decrease Annihilate's cooldowns by 1 per Cooldowns Increase applied. The one and only ability, **Annihilate** - Instantly defeat an enemy no matter what. His lead give Sith allies tons of Health Steal, and turns all Protection into Max Health. **Wound in the Force** apply DoT and Health Down, BUT disabled if they have Tenacity Up!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")
                        
        await bot.send_message(message.channel, embed=embed)
                        
    if message.content.startswith("!Darth-Sidious"):
        embed=discord.Embed(title="Darth Sidious",color=discord.Colour(ff0000), description="Brutal Attacker effective against Healers and Jedi while boosting allied Criticals as a Leader")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=https://swgoh.gg/static/img/assets/tex.charui_sidious.png)
        embed.set_image(url=https://lumiere-a.akamaihd.net/v1/images/open-uri20150608-27674-9qc5ag_07797936.jpeg?region=0%2C0%2C1200%2C675)
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Sadistic Glee")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 161` `Health: 15,013` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Death Stroke - <:SidiousBasic:344013281507147776>", value="Deal Physical damage to target enemy and inflict Healing Immunity for 3 turns with a 50% chance (doubled if the target is debuffed) to ignore Defense.")
        embed.add_field(name="Special Ability - Demoralizing Blows - <:SidiousSpecial:344013319021133825>", value="Deal Physical damage to all enemies and inflict Damage Over Time and Expose for 2 turns. This attack inflicts two additional Damage Over Time effects on a Critical Hit.")
        embed.add_field(name="Leader Ability - Unlimited Power - <:SidiousLead:344013352386691073>", value="All allies gain 15% Critical Chance and 30% Critical Damage. Sith allies gain 2% Offense until the end of battle when they score a Critical Hit.")
        embed.add_field(name="Unique Ability - Sadistic Glee - <:SidiousUnique:344013374042013698>", value="Darth Sidious recovers 20% of his Max Health and gains 50% Turn Meter whenever any unit is defeated. In addition, he has +35% Evasion against Jedi attacks, +50% Potency, and gains Max Health equal to his Potency percentage.")
        embed.add_field(name="Usage", value="This guy seem mysterious but his kits is not underpowered! His basic can ignore enemies's defense and prevent enemy from being heals (AKA: Healing Immunity). His special is drops in several DoT in a row! His leader ability improves allies' Critical Chance (CC) and Critical Damage (CD). His unique is amazing when zeta'd, recover Health, gain Turn Meter whenever any enemy are defeated, gain Potency and Max Health equal to his Potency")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
        await bot.send_message(message.channel, embed=embed)
                        
    if message.content.startswith("!Darth-Vader"):
        embed=discord.Embed(title="Darth Vader",color=discord.Colour(ff0000), description="Fearsome Attacker that applies AoE Damage Over Time, and crushes debuffed targets for extra turns")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=https://swgoh.gg/static/img/assets/tex.charui_vader.png)
        embed.set_image(url=http://screenrant.com/wp-content/uploads/darth-vader-10-most-dangerous-star-wars-villains.jpeg)
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Inspiring Through Fear")
        embed.add_field(name="Stats", value="`Power: 18903` `Speed: 121` `Health: 26,610` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Terrifying Swing - <:VaderBasic:343795687579975693>", value="Deal Physical damage to target enemy with an 80% chance to inflict Ability Block for 1 turn. Jedi targets cannot Evade or Resist the effects of this attack.")
        embed.add_field(name="Special Ability - Force Crush - <:VaderSpecial:343795712531628033>", value="Deal Physical damage to all enemies and inflict Speed Down and 3 Damage Over Time effects for 2 rounds.")
        embed.add_field(name="Special Ability - Culling Blade - <:VaderSpecial1:343795728759390219>", value="Deal Physical damage to target enemy and dispels all debuffs on them. This attack deals 50% more damage for each effect dispelled and grants 100% Turn Meter on a finishing blow. This attack can't be Evaded.")
        embed.add_field(name="Leader Ability - Inspiring Through Fear - <:VaderLead:343795772539797504>", value="Empire and Sith allies gain 30% Offense and have a 50% chance to remove 20% Turn Meter when they damage an enemy. This Turn Meter removal can't be Resisted. While Darth Vader is alive, enemies immediately regain Damage Over Time for 2 turns whenever Damage Over Time expires on them.")
        embed.add_field(name="Usage", value="This JKA 2.0 is pretty damn awesome. His basic apply Ability Block (Great for Thrawn as usual). **Force Crush** can apply tons of Damage over Time (DoT) and Speed Down. His **Culling Blade** is amazing, crush all debuffs, turns all into bonus damages, great for Rancor Raids to demolish the Rancor for all the DoT stacked,a nd other debuffs. His leader is what make him good for Raids, Turn Meter Removal/Reduction (TMR), BUT only works with Sith or Empire. Getting this him isn't that easy, only viable in achievement rewards, Fleet Store, and Shard Shop, BUT he don't appear that often!")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
    if message.content.startswith("!Dathcha"):
        embed=discord.Embed(title="Dathcha",color=discord.Colour(ff0000), description="Versatile Support able to Ability Block and Stealth, effective against Droids or with Jawas")
        embed.set_footer(text="Salporin | SWGoH",   icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=https://swgoh.gg/static/img/assets/tex.charui_jawa_dathcha.png)
        embed.set_image(url=https://vignette1.wikia.nocookie.net/starwars/images/8/88/Datcha.jpg/revision/latest?cb=20061102084342)
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16695` `Speed: 137` `Health: 15,584` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Hit and Run - <:DatchaBasic:344012908038193152>", value="Deal Physical damage to target enemy with a 60% chance to gain Stealth for 2 turns.")
        embed.add_field(name="Special Ability - Scout Instincts - <:DatchaSpecial:344012924127543297>", value="Deal Special damage to all enemies with a 50% chance to inflict Ability Block for 1 turn and a 50% chance to Stun Droids for 1 turn")
        embed.add_field(name="Leader Ability - Decommission - <:DatchaLead:344012935133134848>", value="Whenever an ally damages a Droid, they have an 80% chance to  inflict Defense Down for 3 turns and a 25% chance to remove 25% Turn Meter.")
        embed.add_field(name="Unique Ability - Droid Hunter - <:DathchaUnique:344012945807769600>", value="Dathcha gains 4.5% Critical Chance for each living Jawa ally. In addition, he has +15% Critical Damage.")
        embed.add_field(name="Usage", value="This Jawa is pretty decent. His basic can deal decent amount of damage. **Scout Instincts** can inflict Ability Block and stun Droids! His leader can inflict Defense Down with a chance to remove TM whenever they damage a Droid, and **Droid Hunter** grant him Critical Chance and 15% Critical Damage. Overall, he's not that great when come to his kits and stats!")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")
        
        await bot.send_message(message.channel, embed=embed)                
    
    if message.content.startswith("!Death-Trooper"):
        embed=discord.Embed(title="Death Trooper",color=discord.Colour(ff0000), description="Terrifying Empire Attacker who inflicts debilitating debuffs and prevents revives")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=https://swgoh.gg/static/img/assets/tex.charui_trooperdeath.png)
        embed.set_image(url="https://www.sideshowtoy.com/wp-content/uploads/2016/11/star-wars-rogue-one-death-trooper-sixth-scale-hot-toys-feature-902905.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Krennic's Guard")
        embed.add_field(name="Stats", value="`Power: 19101` `Speed: 124` `Health: 25,382` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Track Down - <:DeathTrooperBasic:344012997716475904>", value="Deal Physical damage to target enemy with a 70% chance to inflict Daze for 3 turns. If the target was already Dazed, Stun them for 1 turn. If the target is a Rebel, attack again.")
        embed.add_field(name="Special Ability - Death Trooper Grenade - <:DeathTrooperSpecial:344013013549973524>", value="Deal Physical damage to all enemies and Dispel all buffs on them with a 70% chance to inflict Healing Immunity for 2 turns. Enemies who were not buffed have their cooldowns increased by 1.")
        embed.add_field(name="Special Ability - Terminate - <:DeathTrooperSpecial1:344013032424341505>", value="Deal Physical damage to target enemy. If the target is suffering any debuffs, this attack is a guaranteed Critical Hit. If there are any defeated enemies, also inflict Deathmark for 2 turns. Targets defeated by Terminate can't be revived.")
        embed.add_field(name="Unique Ability - Krennic's Guard - <:DeathTrooperUnique:344013051420344320>", value="Whenever Death Trooper scores a Critical Hit, he and Director Krennic recover 20% Health. Death Trooper has a 50% chance to gain 100% Turn Meter whenever Director Krennic takes damage. Director Krennic can't be Critically Hit while Death Trooper is alive. While Death Trooper is active, Imperial Trooper allies have +10% Health Steal.")
        embed.add_field(name="Usage", value="Deathtrooper is incredibly amazing. His basic can inflict Daze, a very powerful debuffs nowadays. **Death Trooper Grenade** is damn good, dispel all buffs and inflict Healing Immunity or increase enemies's cooldowns by 1 if they didn't have any buffs. This ability is damn powerful, **Terminate** infict **Deathmark** (Character taunts, lose 50% of their Max Health when hit), BUT it can be dispel :disappointed:, and gurantee a Critical Hit if they were debuffed! This guy works extremely well with mostly Empire and/or Imperial Trooper teams. Overall, his kits is very amazing!")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")  
                        
        await bot.send_message(message.channel, embed=embed)                
    
    if message.content.startswith("!Dengar"):
        embed=discord.Embed(title="Dengar",color=discord.Colour(ff0000), description="Adaptable Scoundrel attacker that Stuns and inflicts Tenacity Down.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=https://swgoh.gg/static/img/assets/tex.charui_dengar.png)
        embed.set_image(url=https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiLz-CwxerVAhWKbrwKHa7vCwgQjRwIBw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DHmPIJvkoOI0&psig=AFQjCNHW0-Max1dOsC9Wf35YTCvCUPQhSg&ust=1503480996977991)
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16497` `Speed: 109` `Health: 23,994` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Target Spotted - <:DengarBasic:344014959107375106>", value="Deal Physical damage to target enemy. If the target is suffering from any debuffs, there is a 60% chance to call an Ally to assist. If the assisting ally is a Scoundrel, the attack is guaranteed to be a Critical Hit.")
        embed.add_field(name="Special Ability - Blast and Smash - <:DengarSpecial:344014970649837568>", value="Deal Physical damage to target enemy with a 50% chance to inflict Speed Down for 3 turns. If the target had 50% Turn Meter or more, they are also Stunned for 1 turn.")
        embed.add_field(name="Special Ability - Mini-Mine Mayhem - <:DengarSpecial1:344014983748780033>", value="Deal Physical damage to all enemies, then inflict negative status effects on all enemies that suffer a Critical Hit. Effects inflicted depend on number of Critical Hits scored. 1 Critical Hit: Tenacity Down for 3 turns 2 Critical Hits: Damage Over Time for 3 turns 3 Critical Hits: 50% Turn Meter Reduction")
        embed.add_field(name="Unique Ability - Grizzled Veteran - <:DengarUnique:344014997850161152>", value="Whenever Dengar receives a Critical Hit, he gains Stealth for 2 turns. Whenever an enemy evades Dengar’s attack, he gains +60% Turn Meter. Whenever Dengar suffers a negative status effect, he gains Tenacity Up for 2 turns.")                
        embed.add_field(name="Usage", value="Dengar is a pretty decent Bounty Hunter and Scoundrel. His basic can call an ally to Assist, gurantee a Critical Hit if the Assisting ally is Scoundrel. His 1st special can inflict Speed Down and Stun enemies. **Mini-Mine Mayhem** can inflict debuffs depends on how many Critical Hits scored! His unique give 60% TM if they evade his attack, gains Stealth if he was Critically Hit, and he gains Tenacity Up whenever he suffer a debuff! Overall, he can awesome for Credit Heist, he's not really made for Arena, he's too underpowered")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")  
                        
        await bot.send_message(message.channel, embed=embed) 
                        
    if message.content.startswith("!Krennic"):
        embed=discord.Embed(title="Director Krennic",color=discord.Colour(ff0000), description="Intimidating Empire Support who inflicts devastating debuffs and slows enemies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=https://swgoh.gg/static/img/assets/tex.charui_krennic.png)
        embed.set_image(url=https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjQ3PzYx-rVAhWDUrwKHejbD_gQjRwIBw&url=http%3A%2F%2Fwww.inafarawaygalaxy.com%2F2016%2F05%2Fdirector-krennic-quotes-rogueone-starwars-benmendelsohn.html&psig=AFQjCNHx5J-9xfrESQkZ2OHRFguU_UtVvw&ust=1503481622657672)
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Director of Advanced Weapons Research")
        embed.add_field(name="Stats", value="`Power: 19279` `Speed: 129` `Health: 16,826` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Test Their Defenses - <:KrennicBasic:344014831202074624>", value="Deal Special damage to target enemy and inflict Tenacity Down for 3 turns.")
        embed.add_field(name="Special Ability - Death Trooper Assault - <:KrennicSpecial:344014841612206081>", value="Deal Special damage to all enemies with a 70% chance to inflict Stagger for 2 turns. If any enemies are debuffed, revive Death Trooper with 20% Health for each debuffed enemy. If Death Trooper is present, he is called to Assist.")
        embed.add_field(name="Special Ability - Experimental Weaponry - <:KrennicSpecial1:344014853855379458>", value="Deal Special damage to target enemy and inflict a debuff (Attacker: Stun, Healer/Support: Ability Block, Tank: Buff Immunity) for 2 turns. If the target is a Rebel, also inflict Speed Down for 2 turns.")
        embed.add_field(name="Leader Ability - Director of Advanced Weapons Research - <:KrennicLead:344014867738394629>", value="Empire allies gain 25% Critical Chance and 25% Potency. Debuffed enemies who are Critically Hit during an Empire ally's turn suffer Ability Block for 1 turn. This effect can't be Resisted. Empire allies recover 10% Protection whenever they score a Critical Hit.")
        embed.add_field(name="Unique Ability - Immeasurable Power - <:KrennicUnique:344014881151778816>", value="Director Krennic gains 10% Critical Damage for each debuffed enemy and 10% Critical Damage for each Rebel enemy. If Death Trooper is present he also gains these bonuses.")
        embed.add_field(name="Usage", value="Krennic is damn amazing, and even more when with Deathtrooper. His basic can deal mass damage and inflict Tenacity Down (Great for Rancor Raids for other allies to inflict tons of debuffs). **Death Trooper Assault** can inflict Stagger (Lose 100% TM when hit), revive Deathtrooper w/ 20% Health per enemies w/ debuffs. **Experimental Weaponry** can inflict a certain debuff due to their roles (Attacker, Healer/Support, Tank). His leader abiliy is damn good for Thrawn, inflict Ability Block to debuffed enemies when they're Critically Hit during Empire turns, gain bonus Potency and CC, and recover Protection whenever Empire allies socre a Critical Hit. Overall, he is a very amazing character.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
        await bot.send_message(message.channel, embed=embed)                
                        
    if message.content.startswith("!Eeth-Koth"):
        embed=discord.Embed(title="Eeth Koth",color=discord.Colour(0000ff), description="Stunning Jedi Support extremely effective against Droids")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=?)
        embed.set_image(url=?)
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16695` `Speed: 144` `Health: 16,971` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Breaching Strike - <:EKBasic:344014894309441538>", value="Deal Physical damage to target enemy with a 50% chance to inflict Defense Down for 3 turns. If the target is a Droid, this attack has a 100% chance.")
        embed.add_field(name="Special Ability - Force Push - <:EKSpecial:344014906565066752>", value="Deal Special damage to target enemy with a 75% chance to Stun for 1 turn and a 100% chance to inflict Ability Block for 3 turns if the target is a Droid.")
        embed.add_field(name="Leader Ability - Stalwart Jedi Defender - <:EKLead:344014918858833920>", value="Jedi allies gain 60 Defense.")
        embed.add_field(name="Unique Ability - Anti-Droid Specialist - <:EKUnique:344014935652696064>", value="Eeth Koth has +35% Critical Chance and +20% Critical Damage when attacking Droids.")
        embed.add_field(name="Usage", value="Eeth Koth is only effective when fighting w/ Droids. His basic can apply Defense Down. **Force Push** can Stun and inflict Ability Block for 3 turns (that's insane), BUT only if the target was Droid. His unique give him Critical Chance and Critical Damage when he's attacking a Droid. Overall, his kits mostly made for to counter Droids!") 
        embed.add_field(name="Ahnald Ranking", value="**Youngling**")  
                        
        await bot.send_message(message.channel, embed=embed) 
    
    if message.content.startswith("!Palpatine"): 
        embed=discord.Embed(title="**Emperor Palpatine**",color=discord.Colour(ff0000), description="Overwhelming Sith Support who inflicts Shock and can Stun targets for multiple turns.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="ihttps://swgoh.gg/static/img/assets/tex.charui_palpatineemperor.png")
        embed.set_image(url="http://screenrant.com/wp-content/uploads/2016/11/Emperor-Palpatine-meme-from-Star-Wars.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 16675` `Speed: 122` `Health: 15,263`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Lightning Strike - <:PalpBasic:344015032008572948>", value="Deal Special damage to target enemy and Shock them for 3 turns. Then, Palpatine gains 15% Turn Meter for each Shocked enemy. ")
        embed.add_field(name="Special Ability - Power of the Dark Side - <:PalpSpecial:344015046411681792>", value="Deal Special damage to all enemies with a 70% chance to Stun them for 1 turn. Shocked enemies are Stunned for 2 turns and have their Shock dispelled.")
        embed.add_field(name="Special Ability - Let the Hate Flow - <:PalpSpecial1:344015067064434698>", value="All allies gain Offense Up for 2 turns and all units lose 5% of their Max Health. Palpatine recovers health equal to 150%  the total amount lost. For each Shocked enemy gain 50% Turn Meter and refresh the duration of Shock to 2 turns.")
        embed.add_field(name="Leader Ability -  Emperor of the Galactic Empire - <:PalpLead:344015113562619905>", value="Empire and Sith allies gain +32% Potency and Max Health. Jedi and Rebel enemies have -32% Potency and Evasion. Whenever an Empire ally inflicts a debuff during their turn, they gain 20% Turn Meter. Whenever a Sith ally inflicts a debuff during their turn, they recover 20% of their Max Health.")
        embed.add_field(name="Unique Ability - Crackling Doom - <:PalpUnique:344015149817921536>", value="At the end of his turns, Palpatine deals Special damage to all Shocked enemies and then deals Special damage to all Jedi and Rebels enemies. This damage can't defeat enemies.")
        embed.add_field(name="Usage", value="Emperor Palpatine is a __rare__ character, available in the Emperor's Demise (Rare Event), but he is amazing! His **Lightning Strike** can Shock enemies (Shock: Immune to heal, can't gain Buffs, or bonus Turn Meter). **Power of the Dark Side** can Stun the whole enemy team sometimes. His 2nd is a fabulous self-healing ability. Overall, his kits is absolutely amazing! **Cracking Doom** deal Special damage to Shock, Jedi, and Rebel enemies at the end of his turns, BUT it can't defeat enemy.")
        embed.add_field(name="Ahnald Ranking", value="**Grand Master**")    
        
        await bot.send_message(message.channel, embed=embed) 
    
    if message.content.startswith("!Ewok-Elder"):
        embed=discord.Embed(title="Ewok Elder (Reworks)",color=discord.Colour(0000ff), description="Ewok Healer that specializes in Revives")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ewok_chief.png")
        embed.set_image(url=?)
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16120` `Speed: 122` `Health: 19,633` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Guiding Strike - <:EEBasic:345903137069989899>", value="Deal Physical damage to target enemy with a 60% chance to gain 50% Turn Meter, grant other Ewok allies half that amount, and grant other allies 10% Turn Meter.")
        embed.add_field(name="Special Ability - Tribal Healer - <:EESpecial:345903151422898176>", value="Dispel all debuffs on all allies. All allies recover Health equal to 30% of Ewok Elder's Max Health with a 35% chance to revive defeated allies at 15% Health.")
        embed.add_field(name="Special Ability - Power of the Forest - <:EESpecial1:345903165499244545>", value="Revive a random defeated ally at 40% Health with a 55% chance for Ewok Elder to gain 45% Turn Meter. If the revived ally is an Ewok, they are called to Assist. Whenever an Ewok ally is defeated, reduce the cooldown of this ability by 1.")
        embed.add_field(name="Usage", value="Ewok Elder is a good character on reviving other allies. His basic can grant a lot of TM to himself and Ewok allies. **Tribal Healer** is a very good ability, dispel all debuffs on all allies, all allies recover Health, and with a chance to revive defeated allies. His 2nd special can revive an ally at 40% Health, call to Assist if the revived ally is an Ewok. Overall, he is a decent character for beginner and mid-game players!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")    
        
        await bot.send_message(message.channel, embed=embed) 
                        
    if message.content.startswith("!Ewok-Scout"):
        embed=discord.Embed(title="Ewok Scout (Reworked)",color=discord.Colour(0000ff), description="Powerful single-target Attacker that becomes evasive with Ewok allies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ewok_scout.png")
        embed.set_image(url=?)
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 15922` `Speed: 140` `Health: 14,029` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Ewok Ambush - <:ScoutBasic:345903183052144640>", value="Deal Physical damage to target enemy with a 55% chance to remove 50% Turn Meter.")
        embed.add_field(name="Special Ability - Rushing Attack - <:ScoutSpecial:345903199741542401>", value="Deal Physical damage to target enemy with an additional 50% chance of a Critical Hit and call a random ally to Assist.")
        embed.add_field(name="Unique Ability - Tribal Tactics - <:ScoutUnique:345903215797207040>", value="Ewok Scout gains 5% Evasion for each living Ewok ally and gains 30% Turn Meter whenever he Evades an attack or lands a Critical Hit.")
        embed.add_field(name="Usage", value="Ewok Scout will be unlocked once you complete Stage 1 Light Side Normal. His basic has a chance to remove 1/2 of the TM from that enemy, and deal huge damage. **Rushing Strike** can deal a insane amount of damage on a Critical Hit. His unique grant him Evasion for each living Ewok ally, and gains TM whenever he Evades an attack or lands a Critical Hit. He's a decent character overall!")
        embed.add_field(name="Ahnald Ranking", value="**Padawan**")                  
                          
        await bot.send_message(message.channel, embed=embed) 
                        
    if message.content.startswith("!Ezra-Bridger"): 
        embed=discord.Embed(title="**Ezra Bridger**",color=discord.Colour(0000ff), description="Versatile Phoenix Attacker that can perform a variety of effect based on the Roles of allies.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_ezra_s3.png")
        embed.set_image(url="http://pm1.narvii.com/6242/871e94adff28e5837b424bea2748794f5ee7e40c_hq.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 16299` `Speed: 143` `Health: 19,421` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Rushing Strike - <:EzraBasic:344014778944978955>", value="Deal Physical damage to target enemy with a 40% chance to attack again.")
        embed.add_field(name="Special Ability - Flourish - <:EzraSpecial:344014793927032852>", value="Deal Physical damage to target enemy and Dispel all buffs on them. If the enemy had no buffs, this attack cooldown is reduced by 1 and Ezra gains 50% Turn Meter instead.")
        embed.add_field(name="Special Ability - Watch and Learn - <:EzraSpecial1:344014805205778432>", value="Target ally attacks and then Ezra assists them, dealing 20% more damage. Both attackers gain a bonus effect based on the chosen ally's role: - Attacker: +100% Crit on this attack - Tank: Protection Up (40%) for 2 turns - Support: +40% Turn Meter Gain.")
        embed.add_field(name="Unique Ability - Push Through - <:EzraUnique:344014817885159425>", value="Ezra gains 10% Offense at the end of his turns. The effect can stack up to 40%. This bonus is reset if Ezra is defeated.")
        embed.add_field(name="Usage", value="Ezra is a fabulous character for all players at any levels, he is farmable at Cantina Battle 2-B or Fleet Store. His **Rushing Strike** has a chance to attack again, and doubled if Ezra isn't debuffed. **Flourish** can deal a insane amount of damage, and dispel all buffs from that enemy. **Watch and Learn** give both of them a bonus effect based on the Assist role. Ezra is great for Palpatine, Thrawn and Yoda event.")
        embed.add_field(name="Ahnald Ranking", value="**Master**")
                        
        await bot.send_message(message.channel, embed=embed) 
                          
    if message.content.startswith("!Finn"):
        embed=discord.Embed(title="Finn",color=discord.Colour(0000ff), description="Resistance tank that keeps the pressure up with a balance between offense and defense")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_finnjakku.png")
        embed.set_image(url="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiaua7k_OzVAhUBxLwKHe_uA0AQjRwIBw&url=http%3A%2F%2Fwww.starwars.com%2Fnews%2F12-things-we-learned-about-rey-finn-and-poe-from-before-the-awakening&psig=AFQjCNFBOVGR_cucafUFoZEgU3ZmK4Dsnw&ust=1503564589764456")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Balanced Tactics")
        embed.add_field(name="Stats", value="`Power: 18903` `Speed: 119` `Health: 26,036` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Crack Shot - <:FinnBasic:345948308172308483>", value="Deal Physical damage to target enemy. This attack deals 100% more damage to enemies that haven't already been struck by it.")
        embed.add_field(name="Special Ability - Hold the Line - <:FinnSpecial:345948326560006144>", value="Finn gains Advantage and Defense Up for 2 turns and Dispels all debuffs from all allies. Finn and Poe Dameron gain Heal Over Time (20%) for 2 turns.")
        embed.add_field(name="Special Ability - Take Down - <:FinnSpecial1:345948351080169483>", value="Deal Physical damage to target enemy and Expose them for 2 turns with an 80% chance to Stun them for 1 turn.")
        embed.add_field(name="Leader Ability - Balanced Tactics - <:FinnLead:345948366951284757>", value="Resistance allies gain 30% Offense and 60% Defense, and other allies gain half that amount. Whenever a Resistance ally loses Foresight, they gain Advantage for 2 turns and whenever an enemy takes damage from Expose, reduce the cooldowns of all Resistance allies by 1 and grant them 35% Turn Meter.")                      
        embed.add_field(name="Usage", value="Finn is a amazing character for advanced players. His basic can deal insane damage if that enemy hasn't been struc by it. His 1st special dispel all debuffs from all allies, gains Defense Up and Advantage, Finn and Poe gain HoT for 2 turns. **Take Down** can Stun and Expose enemies. His leader ability is MANDATORY if you want to run a Resistance team in Phase 2 or 4 of AAT Raids, whenever an enemy takes damage from Expose, all Resistance allies gain 35% TM and reduce their cooldowns by 1, that's insane - if they keep hitting Expose, they can use their special abilities over and over again.")                   
        embed.add_field(name="Ahnald Ranking", value="**Knight**")                  
                          
        await bot.send_message(message.channel, embed=embed)
                        
    if message.content.startswith("!FOO"):
        embed=discord.Embed(title="First Order Officer",color=discord.Colour(ff0000), description="First Order support that grants Advantage and can manipulate both ally and enemy Turn Meters")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url=?)
        embed.set_image(url="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwixzo_JgobWAhVDTbwKHX5IDjsQjRwIBw&url=http%3A%2F%2Fstarwars.wikia.com%2Fwiki%2FFirst_Order_officer&psig=AFQjCNEOpaPlGk1dMnieV2QYIEwcaYmscQ&ust=1504425113485234")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta Ability")
        embed.add_field(name="Stats", value="`Power: 16948` `Speed: 145` `Health: 15,283` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Capitalize - <:FOOBasic:345948391261339648>", value="Deal Physical damage to target enemy. This attack has +20% Critical Damage. If any ally has Advantage, this attack is a guaranteed Critical Hit.")
        embed.add_field(name="Special Ability - Marching Orders - <:FOOSpecial:345948418507538432>", value="Target other ally gains 100% Turn Meter and Advantage for 2 turns. If that ally is First Order, they also gain Offense Up for 3 turns. Dispel all debuffs from First Order Officer and target ally and grant them both Tenacity Up for 2 turns.")
        embed.add_field(name="Special Ability - Pinning Shot - <:FOOSpecial1:345948460270485515>", value="Physical damage to target enemy and remove 50% Turn Meter. If any Turn Meter is removed this way, each ally gains 15% Turn Meter. All First Order allies have their Cooldowns reduced by 1.")
        embed.add_field(name="Usage", value="Great character for beginners. Can maniplute both allies & enemies' TM!")    
        embed.add_field(name="Ahnald Ranking", value="**Knight**") 
                        
        await bot.send_message(message.channel, embed=embed)  
                        
    if message.content.startswith("!FOST"):
        embed=discord.Embed(title="First Order Stormtrooper",color=discord.Colour(ff0000), description="First Order tank that uses Advantage to disrupt enemies")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://www.sideshowtoy.com/wp-content/uploads/2015/09/star-wars-first-order-squad-leader-stormtrooper-sixth-scale-hot-toys-feature-902539.jpg")
        embed.set_image(url="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj9jM-og4bWAhXKnZQKHV-cC_wQjRwIBw&url=http%3A%2F%2Fstarwars.wikia.com%2Fwiki%2FStormtrooper_(First_Order)&psig=AFQjCNFtFUZ79JM_OOaTk64ftp_oGufLMQ&ust=1504425351018998")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Return Fire")
        embed.add_field(name="Stats", value="`Power: 19144` `Speed: 116` `Health: 26,400` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Hindering Shot - <:FOSTBasic:345948544928055296>", value="Deal Physical damage to target enemy with a 50% chance to inflict Speed Down for 1 turn. This chance is increased to 100% on a Critical Hit. If First Order Stormtrooper has Advantage, Dispel all buffs from the target.")
        embed.add_field(name="Special Ability - The Order Relentless - <:FOSTSpecial:345948580801937408>", value="All allies gain 25% Turn Meter and Defense Up for 4 turns. First Order Stormtrooper Dispels all debuffs from himself and then gains Advantage and Taunt for 2 turns.")
        embed.add_field(name="Unique Ability - Return Fire - <:FOSTUnique:345948604839755777>", value="First Order Stormtrooper has +65% Counter Chance. Whenever First Order Stormtrooper uses any Ability he has a 50% chance to call a random ally to Assist, dealing 50% damage unless they are First Order. Then, if it was a First Order ally, grant them Advantage for 2 turns.")                  
        embed.add_field(name="Usage", value="Awesome FO Tank. Can take a lot of hits and counter-attacks!")
        embed.add_field(name="Ahnald Ranking", value="**Knight**") 
                        
        await bot.send_message(message.channel, embed=embed)   
                        
    if message.content.startswith("!FOTP"):
        embed=discord.Embed(title="First Order Tie Pilot",color=discord.Colour(ff0000), description="First Order attacker that can deal extreme damage in a single turn with Advantage")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://www.sideshowtoy.com/wp-content/uploads/2015/09/star-wars-first-order-tie-pilot-sixth-scale-hot-toys-feature-902555.jpg")
        embed.set_image(url="https://www.sideshowtoy.com/wp-content/uploads/2015/09/star-wars-first-order-tie-pilot-sixth-scale-hot-toys-feature-902555.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta Ability: Keen Eye")
        embed.add_field(name="Stats", value="`Power: 19144` `Speed: 128` `Health: 15,043` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Double Tap - <:FOTPBasic:345948484865622019>", value="Deal Physical damage to target enemy with a 50% chance to attack again. This chance is doubled if First Order TIE Pilot has Advantage. If the second attack scores a Critical Hit, gain Advantage for 2 turns.")
        embed.add_field(name="Special Ability - Gun Down - <:FOTPSpecial:345948514242789396>", value="Deal Physical damage to target enemy and inflict Offense Down for 2 turns on a Critical Hit. If First Order TIE Pilot has Advantage, also inflict Buff Immunity and Health Down for 2 turns.")
        embed.add_field(name="Unique Ability - Keen Eye - <:FOTPUnique:345948533888909312>", value="First Order TIE Pilot has +30% Critical Chance and +30% Critical Damage, and gains Advantage for 3 turns whenever an enemy falls below full Health. First Order TIE Pilot has a 70% chance to gain Foresight for 2 turns whenever he loses Advantage 
        embed.add_field(name="Usage", value="Incredible First Order character. Can multi-attack when using Basic and deal insane damage!")
        embed.add_field(name="Ahnald Ranking", value="**Master**") 
                        
        await bot.send_message(message.channel, embed=embed)    
                        
                        
    if message.content.startswith("!Gamorrean-Guard"): 
        embed=discord.Embed(title="**Gamorrean Guard**",color=discord.Colour(ff0000), description="Aggressive Tank that Taunts and Counters with multiple Damage Over Time effects.")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_gamorreanguard.png")
        embed.set_image(url="https://vignette2.wikia.nocookie.net/starwars/images/2/23/Gamorrean_Guard_with_Axe.jpg/revision/latest?cb=20060813142536")
        embed.add_field(name="<:zeta:327437604465278977>", value="No Zeta ability")
        embed.add_field(name="Stats", value="`Power: 16948` `Speed: 118` `Health: 23,826`(<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - Hack and Slash - <:PigBasic:344458181868781568>", value="Deal Physical damage to target enemy and inflict two Damage Over Time effects for 3 turns.")
        embed.add_field(name="Special Ability - Muscle In - <:PigSpecial:344458210012299274>", value="Gamorrean Guard Taunts and gains Retribution for 2 turns. The Gamorrean Guard gains Protection equal to 20% of his Max Health while Taunting.")
        embed.add_field(name="Special Ability - Punch Through - <:PigSpecial1:344458229641773056>", value="Deal Physical damage to target enemy and Expose them for 2 turns.")
        embed.add_field(name="Usage", value="Quite useless character, but decent tank. Gamorrean Guard can apply tons of DoT, Taunt, and Expose enemies.")                 
        embed.add_field(name="Ahnald Ranking", value="**Youngling**") 
        
        await bot.send_message(message.channel, embed=embed)                 
                        
    if message.content.startswith("!Gar-Saxon"): 
        embed=discord.Embed(title="**Gar Saxon**", color=discord.Colour(ff0000), description="Leader who grants Empire allies Counter Chance and Assists them when they Counter Attack")
        embed.set_footer(text="Salporin | SWGoH", icon_url="https://lh3.googleusercontent.com/cWRI4jOO0fq5KP2HOh6V2BoCFhEwI2XghBMrKiamVgFi3YrxdD7lt0_dyIPhBwmpWQ=w300-rw")
        embed.set_thumbnail(url="https://swgoh.gg/static/img/assets/tex.charui_gar_saxon.png")
        embed.set_image(url="http://assets.nydailynews.com/polopoly_fs/1.2976083.1487426569!/img/httpImage/image.jpg_gen/derivatives/article_750/rebels19f-4-web.jpg")
        embed.add_field(name="<:zeta:327437604465278977>", value="1 Zeta ability: Mandalorian Retaliation (!zGar-Saxon)")
        embed.add_field(name="Stats", value="`Power: 8758` `Speed: 127` `Health: 21,955` (<:gearicong111:330366020365713408>, without mods)")
        embed.add_field(name="Basic Ability - On The Hunt -<:SaxonBasic:344458253624934422>", value="Deal Physical damage to target enemy with a 70% chance to inflict Speed Down for 2 turns. If the target already had Speed Down, reduce Gar Saxon's cooldowns by 1.")
        embed.add_field(name="Special Ability - Calculated Ambush - <:SaxonSpecial:344458276777361428>", value="Deal Physical damage to all enemies, dealing double damage to enemies with less than 50% Turn Meter. Enemies that had at least 50% Turn Meter lose 30% Turn Meter.")
        embed.add_field(name="Leader Ability - Mandalorian Retaliation - <:SaxonLead:344458294737502209>", value="Empire allies gain 50% Counter Chance and 40% Defense. Whenever an Empire ally uses a Basic attack, they recover 5% Health.")
        embed.add_field(name="Unique Ability - Viceroy's Vengeance - <:SaxonUnique:344458331634663425>", value="Whenever another ally attacks during an enemy turn, Gar Saxon has a 100% chance to Assist.")
        embed.add_field(name="Usage", value="Awesome Empire character. His zeta works great with CLS or Ima-Gun-Di counter teams.")
        embed.add_field(name="Ahnald Ranking", value="**Knight**")  
        #HERE YOU GO, SPOCK! HOPE YOU ENJOY
        #I'M SORRY IF I SCREWED UP SOMEWHERE
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                          
                          
                          
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('I am made by MisterSpock#9940, NeverGiveUp {Grand Admiral}#0288 and Uniswer#6572, and U+808F hosts me. Thanks to run me!')
    print('------')                               
bot.run('insert token!')
