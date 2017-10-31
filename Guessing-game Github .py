import discord
from discord.ext import commands
import random

client = discord.Client()
embed = discord.Embed
listDrinks = [":cocktail:", ":tropical_drink:", ":wine_glass:", ":champagne:", ":sake:", ":coffee:", ":tea:"]
list2 = ["http://i.imgur.com/X45kQpP.gif", "https://thechive.files.wordpress.com/2016/12/13620363_951189108313525_5003265735381633948_n.jpg?quality=85&strip=info&w=600", "https://media.giphy.com/media/8McNH1aXZnVyE/giphy.gif", "https://i.imgflip.com/vbaka.jpg", "https://i.imgflip.com/kk0ma.jpg", "https://i.imgflip.com/12qa8i.jpg", "https://fsmedia.imgix.net/cd/c4/6e/97/0d7e/409e/b4c2/e4344cfa0b9a/best-star-wars-memes-6jpg.jpeg", "https://s-media-cache-ak0.pinimg.com/736x/49/89/59/4989593bc2ed22ece08d57ca4e956271.jpg", "https://i.imgur.com/hA3mMqTl.jpg", "https://media.giphy.com/media/lFEska6BXZfpe/giphy.gif", "http://cdn3-www.craveonline.com/assets/uploads/gallery/the-25-best-star-wars-memes/24-star-wars-memes.png", "https://s-media-cache-ak0.pinimg.com/736x/39/37/4f/39374f12f15460818026667b6658b2e0.jpg", "https://img.memecdn.com/gold_c_1256479.jpg", "https://pics.me.me/excuse-me-sir-awa-do-you-have-time-to-talk-12060002.png", "http://files.sharenator.com/c3po_meme-s640x430-376480.png", "http://weknowmemes.com/wp-content/uploads/2012/05/the-odds-against-navigating-this-asteroid-field-are-too-damn-high.jpg", "https://img.memecdn.com/yoda-master_o_184950.jpg", "https://i.redditmedia.com/6FKyF5FYilut95blRCckOZPO5aJG5IOKOO05wtsHRII.jpg?w=257&s=a5c711fd795492aedf00e4e429963573", "http://i.imgur.com/Lj8Rp66.png", "http://i.imgur.com/ZeR9JHQ.png", "http://i.imgur.com/VL2u3qT.jpg", "https://i.redditmedia.com/MMV2WHpLdHbM33KKhvo-RnV7hLxH99cAUkJ2Ia1O3uQ.png?w=1024&s=4026d18b9018222edc3f49f3d26c270b", "https://i.redditmedia.com/suucCW4KUXMK6JxcZ2OUcxUi1-8Kp-KjNzjXss-b7ss.jpg?w=384&s=2b86188ec46e68a1379ed4e758c155d1", "https://i.redditmedia.com/3v1hRFo6PIrH776AM5zDAyPfh4dRqU6oeWC2-1pLIwE.jpg?w=645&s=7d140010f8d9c69950383101d257a840", "http://i.amz.mshcdn.com/oNeYyfYfH9PYHeAV3poC4YRitaA=/fit-in/850x850/http%3A%2F%2Fmashable.com%2Fwp-content%2Fgallery%2Fstar-wars-memes%2Fjabba-the-pug.jpg", "http://i.amz.mshcdn.com/Ql8aG4WRKL2hSX8-anuVt2qmblI=/fit-in/850x850/http%3A%2F%2Fmashable.com%2Fwp-content%2Fgallery%2Fstar-wars-memes%2Ftumblr_lzo9fgercp1qgcqzko1_500.jpg", "https://i.imgur.com/cOBERsml.jpg", "https://pbs.twimg.com/media/CXIA-SAUAAAteB7.jpg", "https://img.buzzfeed.com/buzzfeed-static/static/2016-01/6/12/enhanced/webdr07/original-18585-1452099616-13.jpg?downsize=715:*&output-format=auto&output-quality=auto", "http://i.imgur.com/IU8v65E.png", "https://i.redditmedia.com/LBD9VghDj9CT4EXiM_MESHhwG9FnB4UY2-N3THvO9C4.png?w=1024&s=f5472592d963d5aa848fa2bb5fbdd756", "http://i.imgur.com/tt7c5mn.jpg", "https://i.redditmedia.com/zEuEH6jkwVFXIP8ozcZNQ9E3NZ0CRkaW-KS1ZxJ7d5I.png?w=424&s=58f7c0f79ac9d877208af5a8108ab0b0", "https://i.redditmedia.com/AE5_Uu7grRgbZKmj1m_bHsyv_c3zG3QTgVYYNOJiBg0.jpg?w=452&s=331ab51f3aee90181fdf58e4a5d871ce", "https://i.redditmedia.com/95o96K981SPmLKPmcjXf084zgGaYZOa8rp-ATGIHaBk.jpg?w=456&s=db5821bcba33fb45dcb2b370f5b15a04", "https://i.redditmedia.com/KIcMFRriIA_E_MDo4bZn7xRQI8qsHfftTlFUMqoh50A.jpg?w=1024&s=214897277ca3c0539d65f64527391b9f", "http://i.imgur.com/BhuSAL7.png", "https://i.redditmedia.com/hzSPcuzo0ijgoAQlowlq7hXxNV6rry1soru8zGUNScE.jpg?w=341&s=aecf32896b3223d8b3cde3107739b3c7", "https://i.imgur.com/g3QTiVr.jpg", "https://i.redditmedia.com/WJ0WJF5K_Bqo3LFkzeegm4a1WCd4d312A84OS9buBmg.jpg?w=768&s=6575d87e4c1b9e2b46763c2546ae563e", "https://images.discordapp.net/attachments/324329324562087937/336096832566460417/image.jpg?width=398&height=597", "https://images.discordapp.net/attachments/324329324562087937/334790726237945856/8f8de70058a98088a925accd48f34155.jpg?width=358&height=598"]
listmemes = ["https://quizizz.zendesk.com/hc/article_attachments/115002501069/1024x1024.jpg", "https://media.giphy.com/media/zDrQxFFgiiGoU/giphy.gif", "https://img.memesuper.com/e41b2b28f45edba623f5e17d307fedef_views-36-meme-animated-gif_400-400.gif", "http://media3.giphy.com/media/fKO3LF3DYpxpm/giphy.gif", "https://media.giphy.com/media/itmhTtVXA1kl2/giphy.gif", "https://img.memesuper.com/149e6a0eb5e1b2983d403c8659c65ebb_internet-memes-untitledgif-gif-memes_480-311.gif", "http://i0.kym-cdn.com/photos/images/newsfeed/000/328/752/fdc.gif", "https://images.discordapp.net/.eJwFwdENhCAMANBdGIDSllDObQgSNFFLoPd1ud197-e-83KbO8zG2gD2c1Wdu1-ms_Tmu2q_Whnn8lVvKGalHnd7bAEHkiARKeYcCVkyMAZJgilkRCbmD0Fq4sfT3f8FdhUgjA.pRNoerAAr4z0yNIxYDfXfHXipWg?width=279&height=300", "https://images.discordapp.net/.eJwFwdENhSAMAMBdGIDSFi1xG4IETdQSqF8vb3fvfu4dl9vcYdbnBrCfs-jY_TQduVXfVNtVcz-nL3pDNsvluOtjEziQBIlIMaVIyJKAMcgqSCkREi-CDCyL709z_w901CBd.No7_6fkScGRgsIHvCiHSn3_HbDg?width=400&height=268"]
listfunfacts = ["If you somehow found a way to extract all of the gold from the bubbling core of our lovely little planet, you would be able to cover all of the land in a layer of gold up to your knees.", "McDonalds calls frequent buyers of their food *'heavy users.'*", "The average person spends 6 months of their lifetime waiting on a red light to turn green.", "The largest recorded snowflake was in Keogh, MT during year 1887, and was 15 inches wide.", "You burn more calories sleeping than you do watching television.", "There are more lifeforms living on your skin than there are people on the planet.", "Southern sea otters have flaps of skin under their forelegs that act as pockets. When diving, they use these pouches to store rocks and food.", "In 1386 a pig in France was executed by public hanging for the murder of a child.", "One in every five adults believe that aliens are hiding in our planet disguised as humans.", "If you believe that you’re truly one in a million, there are still approximately 7,184 more people out there just like you.", "A single cloud can weight more than 1 million pounds.", "A human will eat on average 70 assorted insects and 10 spiders while sleeping.", "James Buchanan, the 15th U.S. president continuously bought slaves with his own money in order to free them.", "There are more possible iterations of a game of chess than there are atoms in the known universe.", "The average person walks the equivalent of three times around the world in a lifetime.", "Men are 6 times more likely to be struck by lightning than women.", "Coca-Cola would be green if coloring wasn’t added to it.", "You cannot snore and dream at the same time.", "The world’s oldest piece of chewing gum is over 9,000 years old!", "A coyote can hear a mouse moving underneath a foot of snow.", "Bolts of lightning can shoot out of an erupting volcano.", "New York drifts about one inch farther away from London each year.", "A U.S. dollar bill can be folded approximately 4,000 times in the same place before it will tear.", "A sneeze travels about 100 miles per hour.", "Earth has traveled more than 5,000 miles in the past 5 minutes.", "It would take a sloth one month to travel one mile.", "10% of the World’s population is left handed.", "A broken clock is right two times every day.", "According to Amazon, the most highlighted books on Kindle are the Bible, the Steve Jobs biography, and The Hunger Games.", "Bob Marley’s last words to his son before he died were “Money can’t buy life.”", "A mole can dig a tunnel that is 300 feet long in only one night.", "A hippo’s wide open mouth is big enough to fit a 4-foot-tall child in.", "Chewing gum while you cut an onion will help keep you from crying.", "If you were to stretch a Slinky out until it’s flat, it would measure 87 feet long.", "Al Capone’s business card said he was a used furniture dealer.", "There are more collect calls on Father’s Day than on any other day of the year.", "Banging your head against a wall burns 150 calories an hour.", "95% of people text things they could never say in person.", "A crocodile can’t poke its tongue out.", " It is physically impossible for pigs to look up into the sky.", " Guinness Book of Records holds the record for being the book most often stolen from Public Libraries.", "Banging your head against a wall burns 150 calories an hour.", "In the UK, it is illegal to eat mince pies on Christmas Day.", "Pteronophobia is the fear of being tickled by feathers.", "When hippos are upset, their sweats turns red.", "A flock of crows is known as a murder.", "Facebook Addition Disorder is a mental disorder identified by Psychologists.", "The average woman uses her height in lipstick every 5 years.", "29th May is officially Put Pillow on Your Fridge Day.", "Cherophobia is the fear of fun.","Human saliva has a boiling point three times that of regular water.","If you lift a kangaroo's tail off the ground, it can't hop.","Bananas are curved because they grows toward the sun.","Billy goats urinate on their own heads to smell more attractive to females.","The person who invented the Frisbee was cremated and made into frisbees after he died!","During your lifetime, you will produce enough saliva to fill two swimming pools. 😂","If Pinokio says: My Nose Will Grow Now, it would cause a paradox.","Polar bears can eat as many as 86 penguins in a single sitting. (If they live in the same place).","King Henry VIII slept with a gigantic axe beside him.","Movie trailers were originally shown after the movie, which is why they were called trailers.","An eagle can kill a young deer and fly away with it.","Heart attacks are more likely to happen on a Monday.","If you consistently fart for 6 years & 9 months, enough gas is produced to create the energy of an atomic bomb. 🔥","In 2015, more people were killed from injuries caused by taking a selfie than by shark attacks.","There is a species of spider called the 'Hobo Spider'."]

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    foldedmsg = message.content.casefold()
    lowermsgcontent = message.content.lower()
    if message.author == client.user:
        return
    if lowermsgcontent == '!commands':
        embed=discord.Embed(title="Hello there! You asked for help? Here it is!", color=discord.Colour(0x9CD3E8), description="A list of my commands. Commands not included in this list are used for administration by the Salporin dev team. If you like the bot, or have any questions, you can join the official server: https://discord.gg/8pFJVWN")
        embed.add_field(name="Fun", value="`!guess` for Guessing Game, `!Meme` for a meme, and `!Starwarsmeme` for a Star Wars meme.")
        embed.add_field(name="SWGoH", value="`!reddit` for SWGoH reddit, `!f2p-guide` for an easy and effective f2p guide, `!f2p-fleet` for a guide that will help you increase your fleet arena rank, ALL zeta abilities; type the name of the zeta character you want to get info about it, for example, you want info about Zylo, so you type: '!zKylo' and it will show the full desc, requirements and usage of the ability. NOTE: The requirements and usage aren't fully completed for all abilities so it isn't running yet. It will be online SOON.")
        embed.add_field(name="Other", value="`!add` to add Salporin to your server. Do `!getavatar @user` to get the avatar of a person (or yourself), `!drinks` to get a random drink, `!myjediname` to generate your own Jedi name, `!request` to send a request to the developers, and `!complaint` to send a complaint or a bug report to the developers.")
        embed.add_field(name="Special Thanks", value="""
        **Special thanks to the entire Salporin team**:
        Spock, the original creator of Salporin.
        TheLegendaryStrategist, who helped with the overall coding.
        Jenojo, who helped writing the characters.
        Procapper, the beta tester.
        Uniswer, who helped Spock during the early stages of the bot.
        U+808F, who runs me.
        And of course our other members Dajhmaster, Chromecobra and CT-032 who helped to improve the bot on many ways.
        """)
        embed.set_footer(text="Salporin | Help | Contact MisterSpock#9940 if you have any questions about the bot.",icon_url="https://images.discordapp.net/attachments/302116840199684096/308138975111938048/SALPORIN_002.png?width=300&height=300")

        player = message.author
        embed.set_author(name=player.name , icon_url=player.avatar_url)

        await client.send_message(message.author, embed=embed)
        await client.send_message(message.channel, "<@{}> Check your DMs!".format(message.author.id))


    if lowermsgcontent == '!help':
        embed=discord.Embed(title="Hello there! You asked for help? Here it is!", color=discord.Colour(0x9CD3E8), description="A list of my commands. Commands not included in this list are used for administration. If you like the bot, or have any questions, you can join the official server: https://discord.gg/8pFJVWN")
        embed.add_field(name="Fun", value="`!guess` for Guessing Game, `!Meme` for a meme, and `!Starwarsmeme` for a Star Wars meme.")
        embed.add_field(name="SWGoH", value="`!reddit` for SWGoH reddit, `!f2p-guide` for an easy and effective f2p guide, `!f2p-fleet` for a guide that will help you increase your fleet arena rank, ALL zeta abilities; type the name of the zeta character you want to get info about it, for example, you want info about Zylo, so you type: '!zKylo' and it will show the full desc, requirements and usage of the ability. NOTE: The requirements and usage aren't fully completed for all abilities so it isn't running yet. It will be online SOON.")
        embed.add_field(name="Other", value="`!add` to add Salporin to your server. Do `!getavatar @user` to get the avatar of a person (or yourself), `!drinks` to get a random drink, `!request` to send a request to the developers, and `!complaint` to send a complaint or a bug report to the developers.")
        embed.add_field(name="Special Thanks", value="""
        **Special thanks to the entire Salporin team**:
        Spock, the original creator of Salporin.
        TheLegendaryStrategist, who helped with the overall coding.
        Jenojo, who helped writing the characters.
        Procapper, the beta tester.
        Uniswer, who helped Spock during the early stages of the bot.
        U+808F, who runs me.
        And of course our other members Dajhmaster, Chromecobra and CT-032 who helped to improve the bot on many ways.
        """)
        embed.set_footer(text="Salporin | Help | Contact MisterSpock#9940 if you have any questions about the bot.",icon_url="https://images.discordapp.net/attachments/302116840199684096/308138975111938048/SALPORIN_002.png?width=300&height=300")

        player = message.author
        embed.set_author(name=player.name , icon_url=player.avatar_url)

        await client.send_message(message.author, embed=embed)
        await client.send_message(message.channel, "<@{}> Check your DMs!".format(message.author.id))


    if lowermsgcontent.startswith("!getavatar"):
        if len(message.mentions) == 0:
            avatardude = message.author
            embed=discord.Embed(title='Get the avatar of a specific user', color=discord.Colour(0x9CD3E8), description="The avatar of {}:".format(avatardude.name))
            embed.set_image(url=avatardude.avatar_url)
            await client.send_message(message.channel, embed=embed)


        if len(message.mentions) > 0:
            avatardude = next(iter(message.mentions), None)
            embed=discord.Embed(title='Get the avatar of a specific user', color=discord.Colour(0x9CD3E8), description="The avatar of {}:".format(avatardude.name))
            embed.set_image(url=avatardude.avatar_url)
            await client.send_message(message.channel, embed=embed)

    if lowermsgcontent == '!f2p-guide':
        await client.send_message(message.channel, 'https://forums.galaxy-of-heroes.starwars.ea.com/discussion/86926/adaptive-f2p-guide this is a good guide Mischka found. Follow the guide, and u will farm zetas soon! Cheers!')
        return

    if lowermsgcontent == '!stats':
        embed=discord.Embed(title='Stats', color=discord.Colour(0x9CD3E8), description="Quick stats for the devs.")
        embed.set_footer(text="Salporin | Stats | Contact MisterSpock#9940 if you have any questions about the bot.",icon_url="https://images.discordapp.net/attachments/302116840199684096/308138975111938048/SALPORIN_002.png?width=300&height=300")
        servamount=len(client.servers)
        msgamount=len(client.messages)
        vclients=len(client.voice_clients)
        embed.add_field(name="Servers", value='Salporin is in {} servers! Take a :cookie:!'.format(servamount))
        embed.add_field(name="Messages", value='{} Messages sent to me!'.format(msgamount))

        await client.send_message(message.channel, embed=embed)
        return

    if lowermsgcontent == '!f2p-fleet':
        await client.send_message(message.channel, 'You can follow this guide, it is pretty handy! https://youtu.be/ZYSMqyyg4f4')
        return


    if lowermsgcontent == '!drinks':
        drink = random.choice(listDrinks)
        await client.send_message(message.channel, 'Here, take some {}! Enjoy!'.format(drink))
        return

    if lowermsgcontent == '!funfact':
        funfact = random.choice(listfunfacts)
        meme = random.choice(listmemes)
        embed=discord.Embed(color = discord.Colour(0x9CD3E8), description="{}".format(funfact))
        player = message.author
        embed.set_author(name='A random fun fact for ' + str(player.name), icon_url=player.avatar_url)

        await client.send_message(message.channel, embed=embed)


    if lowermsgcontent == '!meme':
        meme = random.choice(listmemes)
        embed=discord.Embed(color = 11107397, description="Here, take a meme.")
        embed.set_image(url="{}".format(meme))
        player = message.author
        embed.set_author(name=player.name , icon_url=player.avatar_url)

        await client.send_message(message.channel, embed=embed)


    if lowermsgcontent == '!starwarsmeme':
        swmeme = random.choice(list2)
        embed=discord.Embed(color = 11107397, description="Here, a random Star Wars meme for you.")
        embed.set_image(url="{}".format(swmeme))
        player = message.author
        embed.set_author(name=player.name , icon_url=player.avatar_url)

        await client.send_message(message.channel, embed=embed)



    if lowermsgcontent == '!reddit':
        await client.send_message(message.channel, 'https://www.reddit.com/r/SWGalaxyOfHeroes/')
        return


    if lowermsgcontent == '!myjediname':
        newjediknight=message.author
        await client.send_message(message.channel, "Hi there! I am Salporin, and I'm going to generate your Jedi name. Please tell me your first name now. (1 word please, otherwise this might get messed up.)")

        message = await client.wait_for_message(author=message.author)
        first_name = message.content
        await client.send_message(message.channel, "Hey that is nice! Let's go to part 2! Please tell me your last name now. (Again, 1 word please!)")
        message = await client.wait_for_message(author=message.author)
        last_name = message.content
        await client.send_message(message.channel, "Ok, got it! Now tell me the name of your favorite actor. (And again, 1 word please.)")
        message = await client.wait_for_message(author=message.author)
        actor_name = message.content
        await client.send_message(message.channel, "Allright, noted. For the last part, I need the city/town where you live in. If you don't want to share personal info that's allright~ just give up a fake thing. (Once again I need it in 1 word.)")
        message = await client.wait_for_message(author=message.author)
        city_name = message.content
        first_jedi_name = last_name[:3] + first_name[:2]
        last_jedi_name = actor_name[:2] + city_name[:3]
        await client.send_message(message.channel, "Ha, we're done! Your Jedi name is {} {}!".format(first_jedi_name, last_jedi_name))
        embed=discord.Embed(title="You have generated your own Jedi name!", color=discord.Colour(0x7C8F55), description="You have fought well, young padawan. I feel you are ready to join our ranks as Jedi Knight {} {}. ".format(first_jedi_name, last_jedi_name))
        embed.set_image(url="https://vignette.wikia.nocookie.net/starwars/images/4/46/KnightingCeremony-CW21.jpg/revision/latest?cb=20110430163616")
        await client.send_message(newjediknight, embed=embed)







    if lowermsgcontent == '!add':
        embed=discord.Embed(title="Add me to your server!", color=discord.Colour(0x9CD3E8), description="[Invite Salporin to your server with this link!](https://discordapp.com/oauth2/authorize?&client_id=294871401687678976&scope=bot&permissions=0)")
        await client.send_message(message.channel, embed=embed)
        return


    if lowermsgcontent == '!bots-help':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title="Bots help - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
To find information about non-zeta and/or zeta characters:
    ☆  Type "![charname]" for non-zeta characters
    ☆  Type "!z[charname]" for zeta characters
E.g "!Admiral-Ackbar" and it will give you full info about Admiral Ackbar.
       "!zThrawn" and it will give you Thrawn's Zeta Abilities.
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return


    if lowermsgcontent == '!recruiting-help':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title="Recruiting help - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
Please post like this:
[Time zone: GMT/EST/PDT]
[Daily Reset: xx:xx]
[Guild reset: xx:xx]
[Preferred Raid Time: xx:xx]
[Location: Country - City/Town]
[SWGOH Name: Your IGN]
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return

    if lowermsgcontent == '!mods-help':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title="Mods help - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
To find the mods info for specific characters,
    ☆  Type: ";mods [charname]"
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return


    if lowermsgcontent == '!game-rules':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title="In-Game Rules - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
3. **BE ACTIVE**, We are very happy to have you with us here. So be active, as a part of a community. If you having trouble about guild tickets, contact your guild officers/leader!.
5. **CREATE YOUR SWGOH.GG ACCOUNT**, if you are a SWGoH players and don't have "swgoh.gg" account, go to https://swgoh.gg/accounts/login. If you already have one, go to -> <#331115555694182403> and post your link there.
6. **PLAY OFTEN**, we are very active throughout the day, so we highly recommended for your contribution that you should do 600 Tickets everyday. If you don't know how to do that, ask your guild officers:)
7. **THREE-STRIKES SYSTEM**, in case there are a lot of violations or negativity in this server, so we created the "Three-Strikes System", so each time you make a mistake in-game or here, you will receive a punishments in the following below:

     ☆  1st Strike: 0-Damage in the next raid (You will still receive a reward)
     ☆  2nd Strike: Temporary boot for the guild until that raid end. You will be re-invite after the raid ended.
     ☆  3rd Strike: Removal from guild
11. **RAID TICKETS**, We want to do raids as soon as possible, so if you do 600 everyday, that mean 4200 tickets per week. So if you don't reach 4200 each week, you will receive a strike due to your tickets:
     ☆  Anyone between 3600 to 4199 will receive 1 strike
     ☆  Anyone below 3600 will receive 2 strikes
     ☆  Anyone below 3000 will receive 3 strikes
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return


    if lowermsgcontent == '!discord-rules':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title="Discord Rules - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
1. VIOLATIONS, We don't like negativity here so everyone will have arguments sometimes but we will not accept violations that go to far... Contact one of our Officers to have a fair arguments
2. BE KIND, We appreciate everyone of you who joined here. We also like to request that you need to be nice and thankful for what you received! :smiley:
4. INVITE YOUR FRIENDS HERE, if you have friend(s) that is/are needing a guild... Use this link: https://discord.gg/FezMJ7H and invite them here
joined cantina
8. IF YOU'RE GOING AWAY, in case you know that you're going for a vacation and you can't access the game for a few days, post your duration of days/weeks that you're going away, and the reason in the -> <#331115094014558209> channel.
9. GET INVOLVED,

  ☆  Share us your fortune -> <#331116400334602241>
  ☆  Help us improve this server -> <#331121104456515586>
  ☆  Be a part of this community -> <#331114285432307723>
10. BE ACTIVE, As a part of a community, we recommended you to do all of these!

  ☆  Check the server twice per day!
  ☆ Contribute 600 Raid Tickets everyday! (Minimum of 300)
11. RAID TICKETS, We want to do raids as soon as possible, so if you do 600 everyday, that mean 4200 tickets per week. So if you don't reach 4200 each week, you will receive a strike due to your tickets:
     ☆  Anyone between 3600 to 4199 will receive 1 strike
     ☆  Anyone below 3600 will receive 2 strikes
     ☆  Anyone below 3000 will receive 3 strikes
NOTE: See rule 7 for strikes informations
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return


    if lowermsgcontent == '!abb':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title=">>>Common Abbreviations<<< - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
RPS = Rock, Paper, Scissors
BTW = By The Way
BRB = Be Right Back
GTG = Got to Go
NVM = Never Mind
TTYL = Talk To You Later
RN = Right Now
>>>Discord Abbreviations<<<
vc = voice chat

>>>Game Abbreviations<<
~GW = Galactic War
~TM = Turn Meter
~SCT = Special Challenge Team(s)
~RNG = Random Number Generator. aka Luck. (Also called RNGesus)
~Debuff =/= Dispell (Debuff is a negative buff, dispell is removing buffs/debuffs)
~CA = Call Assist (Ability some characters have)
~DT = Double Tap (sometimes used for Multiattack in general)
~Mats = Materials for gear upgrades.
~CG = Capital Games
~Whale = Player who spends a lot of money on the game.
~Dolphin = Player spends some money on the game.
~Plankton = Player spends Zero money on the game.
~RND = Random
~DPS = Damage per second
~Toon = Characters
~Molasses = Extremely slow characters (i.e. Boba Fett)
~Glass Cannon = Extreme damage, very fragile character.
~Cupcake = Non-threatening character. (i.e. Chewie or Barris)
~Nerf = Reduce CharName power/abilities.
~ F2P = Free to play
~ P2P = Pay to play
~ P2W = Pay to win
~AoE/AE = Area of Effect
~DD = Damage Dealer
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return


    if lowermsgcontent == '!guild-application':
        if message.server.id =='331114285432307723':
            embed=discord.Embed(title="Guild Application - ΣΔ Legends HQ", color=discord.Colour(0x696969), description="""
Please post the following information into <#337593205501591552>

Game Name | Player Level | # of 7/6/5 Stars | # of Gear 11 | # of Gear 10 | Ally Code | TimeZone or Country
Example: SanHolo|80|15/7/20|2|12|123-456-789 | EST

Or, just post your https://swgoh.gg/ link and TimeZone.
""")
            embed.set_footer(text="Salporin | Custom Command | ΣΔ Legends HQ",icon_url="https://images-ext-1.discordapp.net/external/wlm0NEVOnO_kjRA2ma9dN4Wmr4eU5Lxltu1A2PrjXeA/https/discordapp.com/api/guilds/331114285432307723/icons/3edbcee918d765c17a0011cab694d5f4.jpg?width=100&height=100")
            await client.send_message(message.channel, embed=embed)
            return



    if message.content.startswith('!request'):
        sugserver = message.server.name
        sugchannel = message.channel
        sugauthor = message.author
        content = message.content
        embed=discord.Embed(title="📬 Hello devs! There is mail for you! Request by " + str(sugauthor), color=discord.Colour(0x9CD3E8), description=content.strip("!request"))
        embed.set_thumbnail(url=sugauthor.avatar_url)
        embed.add_field(name="Info", value="Suggestion was sent from the server **{}**".format(sugserver))

        await client.send_message(client.get_channel(id="337274001850236928"), embed=embed)
        await client.send_message(sugchannel, "Request sent.")
        return


    if message.content.startswith('!complaint'):
        sugserver = message.server.name
        sugchannel = message.channel
        sugauthor = message.author
        content = message.content
        embed=discord.Embed(title="📬 Hello devs! There is mail for you! Complaint by " + str(sugauthor), color=discord.Colour(0x9CD3E8), description=content.strip("!complaint"))
        embed.set_thumbnail(url=sugauthor.avatar_url)
        embed.add_field(name="Server", value="Complaint was sent from the server **{}**".format(sugserver))

        await client.send_message(client.get_channel(id="302116375210622977"), embed=embed)
        await client.send_message(sugchannel, "Complaint sent.")
        return



    if lowermsgcontent == '!guess':
        player=message.author
        embed=discord.Embed(title="🎲 Guessing Game", color=discord.Colour(0x2ecc71), description="Guess a number between 1 to 10!")
        embed.set_author(name=player.name , icon_url=player.avatar_url)
        await client.send_message(message.channel, embed=embed)

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=20.0, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            embed=discord.Embed(title="🎲 Guessing Game", color=discord.Colour(0x2ecc71), description='Sorry, you took too long. The right answer was {}. Be faster next time! :wink:'.format(answer))
            embed.set_author(name=player.name , icon_url=player.avatar_url)
            await client.send_message(message.channel, embed=embed)
            return
        if int(guess.content) == answer:
            embed=discord.Embed(title="🎲 Guessing Game", color=discord.Colour(0x2ecc71), description='You are right! Take a :cookie:')
            embed.set_author(name=player.name , icon_url=player.avatar_url)
            await client.send_message(message.channel, embed=embed)
            await client.send_message(player, 'Here is your :cookie:, enjoy!')
        else:
            embed=discord.Embed(title="🎲 Guessing Game", color=discord.Colour(0x2ecc71), description="Sorry. The right answer is actually {}. Good luck :wink:".format(answer))
            embed.set_author(name=player.name , icon_url=player.avatar_url)
            await client.send_message(message.channel, embed=embed)
            await client.send_message(player, '<:newjoy:334992563993968642>')



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='!add to invite me to your server, !commands for help'))


client.run('TOKEN')
