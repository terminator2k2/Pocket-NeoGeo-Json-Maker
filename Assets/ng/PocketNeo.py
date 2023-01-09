######################################################################################################################
# Python - Script By Terminator2k2 & Timothee Groleau - Creates json files for Analogue Pocket NeoGeo Rom Set.       #
# Big Thank You to Timothee Groleau (timotheeg) who re-wrote the script.                                             #
# Big Thank You to Mazamars312 for porting/Fixes to the Superb Neogeo Core For The Analogue Pocket.                  #
# Big Thank You To all involved in creating this core for The MiSTer Project.                                        #
######################################################################################################################

import os
import sys
import json
import fileinput
import re
import copy


try:
    with open('romset.json', 'r') as romsetFile:
        supportedGames = json.load(romsetFile)
    print("Loaded {} supported game definitions from romset".format(len(supportedGames)))
except:
    print("Romset definition is not found")
    exit(1)


dirName = "Mazamars312.NeoGeo"
try:
    os.makedirs(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


root='./common'
installedGames = { item: True for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) }
print("Found {} installed games".format(len(installedGames)))


with open('./template.json') as template_file:
    template = json.load(template_file)


gamesToProcess = [ game for game in supportedGames if game["code"] in installedGames ]


memoryMap = {
    "PVC-Cart": "0xf0000024",
    "PCM":      "0xf0000028",
    "SMA-Cart": "0xf000002C",
    "CMC-Chip": "0xf0000030",
    "OFFSET":   "0xf000003C",
    "CTOLINK":  "0xf0000040",
}

print("")

for game in gamesToProcess:
    print("Processing {} ({})".format(game["code"], game["name"]))

    gameFilePath = './{}/{}.json'.format(dirName, game["name"])

    content = copy.deepcopy(template)
    content["instance"]["data_path"] = game["code"]

    if ("memory_writes" in game):
        for memId, data in game["memory_writes"].items():
            content["instance"]["memory_writes"].append({
                "address": memoryMap[memId],
                "data": data
            })

    if ("has_prom1" in game and game["has_prom1"] == True):
        content["instance"]["data_slots"].append({
            "id": 8, # hardcoded 8 is not cool, but matches template
            "filename": "prom1",
        })

    # write to game file
    with open(gameFilePath, 'w') as gameJsonFile:
        gameJsonFile.write(json.dumps(content, indent=2))


os.remove('./template.json')
os.remove('./romset.json')
os.remove('./PocketNeo.py')

print("")
print("Analogue Pocket Neogeo {} game json files created successfully in folder {} ".format(len(gamesToProcess), dirName))      
print("Script Created by Terminator2k2 & timotheeg - Enjoy")  
