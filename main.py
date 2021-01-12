# bot.py
import os
import random
from pathlib import Path

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} has connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    axolotl_facts = [
        "Ever wondered about the origin of the word 'axolotl'? 'Atl' means 'water', and 'xolotl' means 'dog', "
        "after the Xlotl, the canine Aztec deity. ",
        "Did you know that wild axolotl are rarely white? They are normally greenish brown, or black.",
        "Those silly branches on an axolotl's head are actually the salamander's gills!",
        "Wild axolotls can only be found in the lakes and canals of Xochimilco, Mexco.",
        "Axolotls eat small fish, worms, and anything it can find that will fit in their mouth.",
        "Axolotls are actually critically endangered, due to to loss of habitat, pollution and the introduction "
        "of invasive species like tilapia and carp.",
        "In an attempt to save the critically endangered species, researchers have been known to build little "
        "shelters out of rocks and reeds for the axolotls to live and hide in!",
        "There were about 6000 wild axolotls documented in a 1998 survey, but today you'd be lucky to find any at all!",
        "The natives of Xochimilco, Mexico, used to eat axolotl and often served them as tamales, alongside cornmeal.",
        "There is a restaurant in Osaka, Japan that serves whole, deep-fried axolotl. Crunchy!",
        "Xolotl, a dog-headed Aztec god after whom the species is named, would lead the souls of the dead to "
        "the Underworld.",
        "Xolotl, a dog-headed Aztec god after whom the species is named, is said to have transformed into an axolotl "
        "to hide from those who were trying to kill him.",
        "Axolotls exhibit Neoteny, which means they get bigger as they age but they never 'mature' (for example, like "
        "tadpoles growing legs and becoming frogs).",
        "Although axolotls keep their gills and stay in water their whole lives, they can (in rare cases) transform "
        "and lose their gills to become land animals, transforming into something similar to their close relative, "
        "the tiger salamander.",
        "Scientists have discovered that a shot of iodine can induce metamorphosis in axolotls, which causes them to "
        "transform, lose their gills and give them the ability to live outside of water (don't try this at home!).",
        "While it's not unsual for amphibians to be able to regenerate, axolotls have been known to regenerate more "
        "than just limbs - they can rebuild their jaws, spine, and even brain!",
        "Scientists have successfully transplanted organs from one axolotl to another, thanks to their ability to "
        "regenerate parts of their bodies.",
        "Axolotls are the best."
    ]

    if "axolotl" and "pic" in message.content:
        path = Path("D:\Vivialyn\Projects\Axobotl\static")
        axolotl_pics = [str(pic) for pic in path.iterdir()]
        random_pic = random.choice(axolotl_pics)
        await message.channel.send(file=discord.File(random_pic))

    elif "axolotl" and "fact" in message.content:
        response = random.choice(axolotl_facts)
        await message.channel.send(response)

    elif "thank" and "bot" in message.content:
        await message.channel.send("*happy axolotl noises*")

    elif "tamara" in message.content:
        await message.channel.send("Did you know that Tamara is my favourite person?")

client.run(TOKEN)
