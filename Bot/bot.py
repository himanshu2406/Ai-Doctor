from keras.models import load_model
import cv2
import numpy as np
from discord.ext import commands
import requests
import time
import os
import random
import hashlib
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import json
import pickle
import re
import textwrap
import asyncio
import uuid 
import imgkit
pred = ''
probabilities = 0

def pred_scan(img):
	global pred
	global probabilities
	model = load_model('C:/Users/Administrator/Desktop/AI Doc/pneumonia_pred_new.h5')
	#The Location for h5 file

	imageee = 'C:/Users/Administrator/Desktop/AI Doc/pic1.jpeg'
	#location for pic file , it;s rewritten on every request
	img = cv2.imread(imageee)
	img = cv2.resize(img,(64,64))
	img = np.reshape(img,[1,64,64,3])

	#classes = model.predict_classes(img)
	classes = model.predict(img)
	probabilities = model.predict(img)
	#print(classes)


	#cvimg = cv2.imread(imageee)
	#cv2.imshow('img',cvimg)
	if classes == [[1]]:
	  pred = 'POSITIVE'
	else:
		pred = 'NEGATIVE'
		probabilities = 1 - probabilities


'''
	print("------------PREDICTION--------------")
	print()
	print("PNEUMONIA TEST RESULT : ",pred)
	print('The probability of the test being {} is {}% '.format(pred,int(probabilities*100)))
	print("------------------------------------")
'''


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.command(pass_context=True,help = "Restarts the bot, requires admin permission")
@commands.has_role('admin')
async def restart(ctx):
	await ctx.send('Restarting...')
	print('Restarting...')
	try:
		await client.logout()
	finally:
		os.system("py -3 bot.py")

@client.command(pass_context=True, help = "Shuts Down The bot, Requires admin permission")
@commands.has_role('admin')
async def shutdown(ctx):
	await ctx.send('Bot is Shut Down')
	print('Shut Down Command Received')
	await client.logout()
	return

@client.command(pass_context=True)
@commands.has_role('admin')
async def botservers(ctx):
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers")
    for guild in client.guilds:
        await ctx.send(guild.name + ' : ' + str(guild.id))
    return

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')


@client.command(pass_context=True, help = "!d url_to_the_scan")
#@commands.has_role('botuser')
async def d(ctx, args):
	global pred
	global probabilities
	await ctx.send('Please wait a few seconds...')
	try:
		with open('pic1.jpeg', 'wb') as handle:
			response = requests.get(args, stream=True)

			if not response.ok:
				print(response)
				return

			for block in response.iter_content(1024):
				if not block:
					break

				handle.write(block)
	except:
		pass
	try:
		pred_scan(args)
		#await ctx.send(pred)
		#await ctx.send("------------PREDICTION--------------")
		#await ctx.send("PNEUMONIA TEST RESULT : " + pred)
		#await ctx.send('The probability of the test being ' + pred+' is ' +str(int(probabilities*100)) + '%')
		#await ctx.send("------------------------------------")
		if pred == 'POSITIVE':
			rang = 0xed3726
		else:
			rang = 0x44e32b
		embedVar = discord.Embed(title= pred, description="PNEUMONIA TEST RESULT : " + pred, color=rang)
		embedVar.add_field(name="Confidence - ", value=str(int(probabilities*100)), inline=False)
		embedVar.add_field(name="Imp-", value='The bot can be inaccurate, even when the confidence is 100% , we would always recommend consulting a doctor !', inline=False)
		await ctx.send(embed=embedVar)


	except:
		pass
	return


@client.event
async def on_message(message):
	# do previous on_message stuff here
	await client.process_commands(message) # add at bottom to allow commands to work

client.run(TOKEN)
