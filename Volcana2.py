import discord
import asyncio
from discord.ext.commands import bot
from urllib.parse import urlencode

import random
import hashlib
import base64
from discord.game import Game as botgame

import requests
import socket

z_bot = discord.Client()
z_bot_id = 312428416127467522


@z_bot.event
async def on_ready():
    print("Client Has Logged In\n")    
    print("Volcana has arrived\n")
    print('Client ID = ', z_bot_id)
    
    await z_bot.change_presence(game=discord.Game(name='v!help | v!version |'))

@z_bot.event
async def on_message(message):
##Random Replies

    if message.content.startswith('v!hello'):
            await z_bot.send_message(message.channel, 'Hello Sexy, I am ``l33T`` ')  

    if message.content.startswith('v!owner'):
            await z_bot.send_message(message.channel, '``Jazz Owns Volcana`` ')

    if message.content.startswith('v!servers'):
            server_count = len(z_bot.servers)
            await z_bot.send_message(message.channel, server_count)

    if message.content.startswith('v!version'):
            await z_bot.send_message(message.channel, '``The current Volcana Version is v.1.0.1``') 


    if message.content.startswith('fuck'):
            await z_bot.send_message(message.channel, 'You mean ``duck``, to *duck* from school shooters... ')  


    if message.content.startswith('v!arrow'):
            await z_bot.send_message(message.channel, '```        \n'        
 ' /=/                 \n'
 '/ /_____ _____ _____ \n'
 '\ \_____|_____|_____|\n'
 ' \=\                 ```')
                   
 
##Help commands

    if message.content.startswith('v!help'):
            await z_bot.send_message(message.channel, " ```"
                "***Welcome to Volcana v. 1.0.1***\n COMMANDS...\n "
                                     "<--Getting Replies-->\n"
                                     " v!hello >> Get a reply.\n"
                                     " v!ping >> Test connection.\n"
                                     " v!owner >> Display the owner of the bot.\n"
                                     " v!root --site >> Where Volcana comes from.\n"
                                     " v!servers >> Volcanas server count.\n"
                                     " v!version >> Displays the current version of the bot.\n"
                                     " v!say >> Have volcana say stuff you type.\n"
                                     "<--Art Work-->\n"
                                     " v!arrow >> Volcana draws an arrow.\n"
                                     "<--Random Gens-->\n"
                                     " v!md5 --random >> Randomly Generates MD5 hash.\n"
                                     " v!memes >> Randomly Generate memes.\n"
                                     " v!malware >> Generates Malware.\n"
                                     "<--Invite-->\n"
                                     " v!invite >> Invite me to your server.\n"
                                     "<--Learn To Code-->\n"
                                     " v!coding --python >> Learn to Code in Python.\n"
                                     " v!coding --c++ >> Learn To Code in C++.\n"
                                     " v!coding --php >> Learn To Code in PHP.\n"
                                     " v!coding --C >> Learn To Code in C.\n"
                                     " v!coding --java >> Learn to Code in Java\n"
                                     "<--Search Tools-->\n"
                                     " v!urban (word) >> Type a word to be defined from Urban Dictionary\n"
                                     "<--Password Gens-->\n"
                                     " v!pass --weak >> Generates weak password list.\n"
                                     " v!pass --strong >> Generates strong password list.\n"
                                     " v!pass --rockyou.txt >> Generates rockyou.txt password List.\n"
                                     "<--Penetration Testing Tools-->\n"
                                     " v!harvest --email --passwords >> Gets the Password for each email harvested.\n"
                                     " v!ddos --check >> Replies whats going on in the DOSing communtiy.\n"
                                     "<--Encryption-->\n"
                                     " v!md5enc (string) >> Type a word or string to encrypt.\n"
                                     " v!base64enc (string) >> Type a word or string to encode.\n"
                                     "<--Owner Only Commands-->\n"
                                     " v!nuke >> Deletes All messages in a channel. \n"
                                     " v!purge (x) >> Deletes Specified Value of messages in a channel. \n"
                                     "<--Devs-->\n"
                                     " Developed by Jazz#3217```")
                                     
                                     
                                      
##Memes Generator
    if message.content.startswith('v!memes'):   
        memelist = ["https://s-media-cache-ak0.pinimg.com/736x/d8/a7/a9/d8a7a9b8023513bf04c5e68059e415ca.jpg",
                    "http://theawesomedaily.com/wp-content/uploads/2017/01/most-offensive-memes-6-1.jpg",
                    "https://68.media.tumblr.com/f449d8738724cd74dafc1a63671e1984/tumblr_o6j2dt3WUx1s3o4dso1_400.gif",
                    "https://i.imgflip.com/18mwyi.jpg",
                    "http://i2.wp.com/www.fussedblogger.com/wp-content/uploads/2014/01/Best-Internet-memes-20.jpg?resize=357%2C357",
                    "https://i.imgflip.com/143lz6.jpg",
                    "https://cdn.discordapp.com/attachments/281891534276788224/315558049173471232/IgOIKz1.gif",
                    "https://i.ytimg.com/vi/Yj7ja6BANLM/maxresdefault.jpg",
                    "http://i1.kym-cdn.com/photos/images/facebook/000/862/065/0e9.jpg",
                    "http://i1.kym-cdn.com/entries/icons/medium/000/003/619/Untitled-1.jpg",
                    "http://i3.kym-cdn.com/entries/icons/medium/000/004/006/y-u-no-guy.jpg",
                    "https://tenor.co/tsvD.gif"]

        newlist = random.choice(memelist)
        await z_bot.send_message(message.channel, newlist)
 
##ENCRYPTION  
    if message.content.startswith('v!md5enc'):
            aa1 = message.content.replace('v!md5enc ', '')
            fa1 = hashlib.md5(aa1.encode())
            digestedhash = fa1.hexdigest()

            await z_bot.send_message(message.channel, digestedhash)

    if message.content.startswith('v!base64enc'):
        await z_bot.send_message(message.channel, base64.b64encode(message.content.partition(' ')[2].encode('utf-8')))

   
    if  message.content.startswith('v!md5 --random'):   
         hashlist = [" f81d87d97f50e9032c6e5c5cb4f98e79 ",
                    " 26138c0d6b01add332c4f4e9bbd359f6 ",
                    " 1590a77ab9ab84ad8fea2e3965a659ef ",
                    " 9ac9a6735010b9ea2648eeb0b6b31f3a ",
                    " 1d6c192517ba6b8eedbe23148a36911e ",
                    " 917de6b05d74a18e6241a8d00dce6a3a "]

         hashlist = random.choice(hashlist)
         await z_bot.send_message(message.channel, hashlist)

    if message.content.startswith('v!ping'):
                await z_bot.send_message(message.channel, '**Pong!** ')


    if message.content.startswith('v!invite'):
                await z_bot.send_message(message.channel, '*Use this link to invite me to your server...*\n'
                                    'https://discordapp.com/oauth2/authorize?client_id=312428416127467522&scope=bot&permissions=1073216767')

    
    if message.content.startswith('v!coding --python'):
                await z_bot.send_message(message.channel, 'https://youtu.be/D48iCw3WWpI ')

    
    if message.content.startswith('v!coding --c++'):
                await z_bot.send_message(message.channel, 'https://youtu.be/_r5i5ZtUpUM ')

    
    if message.content.startswith('v!coding --php'):
                await z_bot.send_message(message.channel, 'https://www.youtube.com/watch?v=7TF00hJI78Y ')

    if message.content.startswith('v!coding --C'):
                await z_bot.send_message(message.channel, 'https://youtu.be/-CpG3oATGIs ')

    if message.content.startswith('v!coding --java'):
                await z_bot.send_message(message.channel, 'https://youtu.be/WPvGqX-TXP0 ')

 
    if message.content.startswith('v!pass --weak'):
                await z_bot.send_message(message.channel, '```Weak passwords...\n'
                                     '123456    porsche firebird    prince  rosebud'
'2  password    guitar  butter  beach   jaguar'
'3  12345678    chelsea united  amateur great'
'4  1234    black   turtle  7777777 cool'
'5  pussy   diamond steelers    muffin  cooper'
'6  12345   nascar  tiffany redsox  1313'
'7  dragon  jackson zxcvbn  star    scorpio'
'8  qwerty  cameron tomcat  testing mountain'
'9  696969  654321  golf    shannon madison'
'10 mustang computer    bond007 murphy  987654'
'11 letmein amanda  bear    frank   brazil'
'12 baseball    wizard  tiger   hannah  lauren'
'13 master  xxxxxxxx    doctor  dave    japan'
'14 michael money   gateway eagle1  naked'
'15 football    phoenix gators  11111   squirt'
'16 shadow  mickey  angel   mother  stars'
'17 monkey  bailey  junior  nathan  apple' 
'18 abc123  knight  thx1138 raiders alexis'
'19 pass    iceman  porno   steve   aaaa'
'20 fuckme  tigers  badboy  forever bonnie``` ')


    if message.content.startswith('v!pass --strong'):
            await z_bot.send_message(message.channel, '```Ad*&##@frs!DljY-\n'
'SJSH^%SD$DU\n'
'G563#gdG!@%$\n'
'_Oil8&6hj##g\n'
'339U^&YJSnxx\n'
'!!nu&67899654-\n'
'VjsdjklHJK1341.\n'
'()GtsjGKgjs$$^79\n```')
 

    if message.content.startswith('v!haxzor'):
            await z_bot.send_message(message.channel, '*Urban Dictionary Term for haxzor...*\n'
                'http://www.urbandictionary.com/define.php?term=haxzor')
            

#purge commands(deletes mesages)                             
    if message.content.startswith('v!pass --rockyou.txt'):
            await z_bot.send_message(message.channel, '**Link to the worldlist...**\nhttps://github.com/danielmiessler/SecLists/blob/master/Passwords/rockyou-50.txt ') 
               

    if message.content.startswith('v!nuke'):
            await z_bot.send_message(message.channel, '*Waiting to check...* ')
            if  message.author.id == '281889942840541185':
                purge_fromchannel = z_bot.get_channel(message.channel.id)
                await z_bot.purge_from(purge_fromchannel, limit=1000, check=None)
            
            elif message.author.id != '281889942840541185':
                await z_bot.send_message(message.channel, '**Sorry, only Jazz can use this Godly Power.** ')
 
    if message.content.startswith('v!purge'):
            try:
                purgeint = int(message.content.replace('v!purge ', ''))
                await z_bot.send_message(message.channel, '*Waiting to check...*')

            except ValueError:
                await z_bot.send_message(message.channel, '**Purge Value is Invalid**')
                return
            if message.author.id == '281889942840541185':
                purge_fromchannel = z_bot.get_channel(message.channel.id)
                await z_bot.purge_from(purge_fromchannel, limit=int(purgeint), check=None)

            elif message.author.id != '281889942840541185':
                await z_bot.send_message(message.channel, '**Jazz only has this Holy Power. **')

    if message.content.startswith('v!urban '):
               themsg2 = message.content.replace('v!urban ', '')
               totallink = 'http://www.urbandictionary.com/define.php?term=' + themsg2
               await z_bot.send_message(message.channel, totallink)


    if message.content.startswith('v!resolve'):
        website_user = message.content.replace('v!resolve ', '')
        
    
#Malware generator
    if  message.content.startswith('v!malware'):
        malwlist = [" https://github.com/fatihsirin/Cryptolocker-1.0.0 ",
                        " https://github.com/ytisf/theZoo ",
                        " https://github.com/MinhasKamal/TrojanCockroach ",
                        " https://github.com/fdiskyou/malware ",
                        " https://github.com/Visgean/Zeus ",
                        " https://en.wikipedia.org/wiki/Internet_Explorer "]

        malwlist = random.choice(malwlist)
        await z_bot.send_message(message.channel, malwlist)


    if message.content.startswith('v!ddos --check'):
                await z_bot.send_message(message.channel, '**Here is whats going on in the packet sending communtiy...**\n'
                                     'http://map.norsecorp.com/#/')

    if message.content.startswith('v!root --site'):
                await z_bot.send_message(message.channel, '**Where i came from...**\n'
                                     'http://www.rootsecurity.tk/')

    if message.content.startswith('v!harvest --email --passwords'):
                await z_bot.send_message(message.channel, '```<--Volcanas Harvest Data Emails/Passwords-->```')
                await z_bot.send_message(message.channel, '```dberthold@msn.com:marsh64sq\n'
'tiamatus1@yahoo.com:wilorfy1\n'
'seahawksrul@yahoo.com:hddwight2\n'
'ctrviking@gmail.com:123456789az\n'
'tristaniveson@gmail.com:brenton1\n'
'c_gleffe@yahoo.com:christian1\n'
'jsoservice@yahoo.com:stormtrooper\n'
'samditslear@gmail.com:12378910\n'
'mertdostol@hotmail.com:kabus22\n'
'goldman1645@hotmail.com:Tr02038630\n'
'bekkam666@gmail.com:1dora2\n'
'luke.knight10@yahoo.com:jacob29\n'
'klwentland@verizon.net:ncc1701\n'
'office.scheinost@gmail.com:TinkaSchila13\n'
'loveisminecraft03@gmail.com:fiw632wIq\n'
'P1r0d0x@gmail.com:frombirzaiinlithuaniaupes12\n'
'lindsaywdennis@gmail.com:pineapple2005\n'
'korthman@gmail.com:3cb85dae\n'
'jon@jon-whitehouse.com:jacypoo2\n'
'laceyncarey@live.com:catheran235\n'
'kali.zaborski@gmail.com:iguana28\n'
'jp@catch-coeur.com.au:Jimmy24\n'
'lemusjuanjose@gmail.com:Chenenito12\n'
'lena.pacheco78@rocketmail.com:Colorado15\n'
'koolbro04@yahoo.com:awesome11\n'
'kpastrana72@gmail.com:Budder101\n'
'lilushik73@yahoo.com:barselona\n'
'ivivey@gmail.com:livvy21333\n'
'iddorocks0326@hotmail.com:Stormchaser01\n'
'rjk1993@yahoo.co.uk:andrew123\n'
'marbooysen1@mweb.co.za:gold10\n'
'Krista.Breckweg@gmail.com:Anton999\n'
'louisesofie94@hotmail.com:gllomop9\n'
'liam-mc@hotmail.co.uk:wicked1020\n'
'massoverride@gmail.com:1426tim\n'
'marygrace0428@yahoo.com:ariannacee0428\n'
'mastermind_nl@msn.com:zoeyvetcool2006\n'
'nevbmo@gmail.com:Hedgehog10\n'
'Migdrivers@Jimclonts.com:Fortress52\n'
'nicke@toplinepaint.com.au:1234567890asdfghjkl\n'
'noedentremont@hotmail.com:noemeckel\n'
'msrtina.spatz@gmail.com:Ramybaer2004\n'
'noanvp@gmail.com:j3rr3yfad3\n'
'mmadison059@gmail.com:catmulan6\n'
'montanovictoriano@gmail.com:coco1994\n'
'olliecwilliams@gmail.com:grey16\n'
'mystical_angel335@hotmail.com:mizone12\n'
'mpoh98@gmail.com:JesusFreak98\n'
'mike04016@gmail.com:adidas\n'
'pamelakuziak@gmail.com:5butterlover\n'
'patrick@gobbens.nl:4881xz\n'
'pilardumont@yahoo.es:nenito10\n'
'pautumnsun@aol.com:aidan10\n'
'legosam36@gmail.com:Vernie24\n'
'r@corfield.f9.co.uk:ramses49\n'
'qazyone@gmail.com:qwertyone\n'
'olijv@hotmail.co.uk:vicko001\n'
'pjboud@comcast.net:emerson95\n'
'niroshpd@yahoo.com:int12345\n'
'npminso623@aol.com:Dagger623\n'
'sweetjexist@gmail.com:pepper269```')




z_bot.run("token")