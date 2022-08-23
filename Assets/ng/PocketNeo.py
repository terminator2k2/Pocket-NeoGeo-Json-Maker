######################################################################################################################
# Python - Script By Terminator2k2 - Creates json files for Analogue Pocket NeoGeo Rom Set. This requires an up to   #
# date template.json in the same folder as this file. output files go to a folder named   "Mazamars312.NeoGeo"       #
# Big Thank You to Mazamars312 for porting/Fixes to the Superb Neogeo Core For The Analogue Pocket.                  #
# Big Thank You To all involved in creating this core for The MiSTer Project.                                        #
######################################################################################################################

import os
import sys
import fileinput
import re

#reads game files in common folder and creates list
Gamelist =  open('Gamelist.txt','w')
root='./common'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
for dir in dirlist:
        print(dir, file = Gamelist)
Gamelist.close()  


#os.makedirs("Mazamars312.NeoGeo") 
dirName = "Mazamars312.NeoGeo"
try:
    os.makedirs("Mazamars312.NeoGeo")    
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', '2020bb'):
        # open both files
        message = '2020bb success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/2020 Super Baseball.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/2020 Super Baseball.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "2020bb" in each line
                 line = line.replace("GameFolder/", "2020bb")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("2020bb not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', '2020bbh'):
        # open both files
        message = '2020bbh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/2020 Super Baseball (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/2020 Super Baseball (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "2020bbh" in each line
                 line = line.replace("GameFolder/", "2020bbh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("2020bbh not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', '2020bba'):
        # open both files
        message = '2020bba success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/2020 Super Baseball (set 2).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/2020 Super Baseball (set 2).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "2020bba" in each line
                 line = line.replace("GameFolder/", "2020bba")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("2020bba not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', '3countb'):
        # open both files
        message = '3countb success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/3 Count Bout.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/3 Count Bout.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "3countb" in each line
                 line = line.replace("GameFolder/", "3countb")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("3countb not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'alpham2'):
        # open both files
        message = 'alpham2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Alpha Mission II.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Alpha Mission II.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "alpham2" in each line
                 line = line.replace("GameFolder/", "alpham2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("alpham2 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'alpham2p'):
        # open both files
        message = 'alpham2p success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Alpha Mission II Proto.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Alpha Mission II Proto.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "alpham2p" in each line
                 line = line.replace("GameFolder/", "alpham2p")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("alpham2p not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'androdun'):
        # open both files
        message = 'androdun success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Andro Dunos.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Andro Dunos.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "androdun" in each line
                 line = line.replace("GameFolder/", "androdun")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("androdun not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'aodk'):
        # open both files
        message = 'aodk success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Aggressor\'s of Dark Kombat.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Aggressor\'s of Dark Kombat.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "aodk" in each line
                 line = line.replace("GameFolder/", "aodk")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("aodk not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'aof'):
        # open both files
        message = 'aof success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Art of Fighting.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Art of Fighting.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "aof" in each line
                 line = line.replace("GameFolder/", "aof")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("aof not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'aof2'):
        # open both files
        message = 'aof2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Art of Fighting 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Art of Fighting 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "aof2" in each line
                 line = line.replace("GameFolder/", "aof2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("aof2 not found")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'aof2a'):
        # open both files
        message = 'aof2a success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Art of Fighting 2 (NGH-056).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Art of Fighting 2 (NGH-056).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "aof2a" in each line
                 line = line.replace("GameFolder/", "aof2a")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("aof2a not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'aof3'):
        # open both files
        message = 'aof3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Art of Fighting 3.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Art of Fighting 3.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "aof3" in each line
                 line = line.replace("GameFolder/", "aof3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("aof3 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'b2b'):
        # open both files
        message = 'b2b success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Bang Bang Buster\'s.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Bang Bang Buster\'s.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "b2b" in each line
                 line = line.replace("GameFolder/", "b2b")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("b2b not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'bakatono'):
        # open both files
        message = 'bakatono success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Bakatonosama Mahjong Manyuuki.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Bakatonosama Mahjong Manyuuki.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "bakatono" in each line
                 line = line.replace("GameFolder/", "bakatono")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("bakatono not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'bangbead'):
        # open both files
        message = 'bangbead success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Bang Bead.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Bang Bead.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "bangbead" in each line
                 line = line.replace("GameFolder/", "bangbead")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("bangbead not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'bjourney'):
        # open both files
        message = 'bjourney success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Blue\'s Journey.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Blue\'s Journey.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "bjourney" in each line
                 line = line.replace("GameFolder/", "bjourney")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("bjourney not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'blazstar'):
        # open both files
        message = 'blazstar success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Blazing Star.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Blazing Star.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "blazstar" in each line
                 line = line.replace("GameFolder/", "blazstar")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("blazstar not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'breakers'):
        # open both files
        message = 'breakers success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Breakers.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Breakers.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "breakers" in each line
                 line = line.replace("GameFolder/", "breakers")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("breakers not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'breakrev'):
        # open both files
        message = 'breakrev success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Breakers Revenge.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Breakers Revenge.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "breakrev" in each line
                 line = line.replace("GameFolder/", "breakrev")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("breakrev not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'bstars'):
        # open both files
        message = 'bstars success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Baseball Stars Professional.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Baseball Stars Professional.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "bstars" in each line
                 line = line.replace("GameFolder/", "bstars")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("bstars not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'bstarsh'):
        # open both files
        message = 'bstarsh success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Baseball Stars Professional (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Baseball Stars Professional (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "bstarsh" in each line
                 line = line.replace("GameFolder/", "bstarsh")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("bstarsh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'bstars2'):
        # open both files
        message = 'bstars2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Baseball Stars 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Baseball Stars 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "bstars2" in each line
                 line = line.replace("GameFolder/", "bstars2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("bstars2 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'burningf'):
        # open both files
        message = 'burningf success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Burning Fight.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Burning Fight.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "burningf" in each line
                 line = line.replace("GameFolder/", "burningf")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("burningf not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'brningfh'):
        # open both files
        message = 'brningfh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Burning Fight (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Burning Fight (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "brningfh" in each line
                 line = line.replace("GameFolder/", "brningfh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("brningfh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'brnngfpa'):
        # open both files
        message = 'brnngfpa success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Burning Fight (prototype).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Burning Fight (prototype).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "brnngfpa" in each line
                 line = line.replace("GameFolder/", "brnngfpa")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("brnngfpa not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'brningfp'):
        # open both files
        message = 'brningfp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Burning Fight (proto older).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Burning Fight (proto older).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "brningfp" in each line
                 line = line.replace("GameFolder/", "brningfp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("brningfp not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'columnsn'):
        # open both files
        message = 'columnsn success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Columns.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Columns.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "columnsn" in each line
                 line = line.replace("GameFolder/", "columnsn")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("columnsn not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'crswd2bl'):
        # open both files
        message = 'crswd2bl success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Crossed Swords 2 (CD conv).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Crossed Swords 2 (CD conv).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "crswd2bl" in each line
                 line = line.replace("GameFolder/", "crswd2bl")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("crswd2bl not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'crsword'):
        # open both files
        message = 'crsword success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Crossed Swords.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Crossed Swords.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "crsword" in each line
                 line = line.replace("GameFolder/", "crsword")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("crsword not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ctomaday'):
        # open both files
        message = 'ctomaday success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Captain Tomaday.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Captain Tomaday.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ctomaday" in each line
                 line = line.replace("GameFolder/", "ctomaday")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ctomaday not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'cyberlip'):
        # open both files
        message = 'cyberlip success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Cyber-Lip.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Cyber-Lip.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "cyberlip" in each line
                 line = line.replace("GameFolder/", "cyberlip")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("cyberlip not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'diggerma'):
        # open both files
        message = 'diggerma success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Digger Man.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Digger Man.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "diggerma" in each line
                 line = line.replace("GameFolder/", "diggerma")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("diggerma not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'doubledr'):
        # open both files
        message = 'doubledr success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Double Dragon.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Double Dragon.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "doubledr" in each line
                 line = line.replace("GameFolder/", "doubledr")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("doubledr not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'dragonsh'):
        # open both files
        message = 'dragonsh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Dragons Heaven.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Dragons Heaven.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "dragonsh" in each line
                 line = line.replace("GameFolder/", "dragonsh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("dragonsh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'eightman'):
        # open both files
        message = 'eightman success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Eight Man.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Eight Man.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "eightman" in each line
                 line = line.replace("GameFolder/", "eightman")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("eightman not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fatfursp'):
        # open both files
        message = 'fatfursp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fatal Fury Special.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fatal Fury Special.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fatfursp" in each line
                 line = line.replace("GameFolder/", "fatfursp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fatfursp not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ftfurspa'):
        # open both files
        message = 'ftfurspa success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fatal Fury Special (NGM-058).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fatal Fury Special (NGM-058).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ftfurspa" in each line
                 line = line.replace("GameFolder/", "ftfurspa")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ftfurspa not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fatfury1'):
        # open both files
        message = 'fatfury1 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fatal Fury.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fatal Fury.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fatfury1" in each line
                 line = line.replace("GameFolder/", "fatfury1")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fatfury1 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fatfury2'):
        # open both files
        message = 'fatfury2 success'
        print (message)
        with open('template3.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fatal Fury 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fatal Fury 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fatfury2" in each line
                 line = line.replace("GameFolder/", "fatfury2")
                 line = line.replace("0xCTOLINK", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fatfury2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fatfury3'):
        # open both files
        message = 'fatfury3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fatal Fury 3.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fatal Fury 3.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fatfury3" in each line
                 line = line.replace("GameFolder/", "fatfury3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fatfury3 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fbfrenzy'):
        # open both files
        message = 'fbfrenzy success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Football Frenzy.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Football Frenzy.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fbfrenzy" in each line
                 line = line.replace("GameFolder/", "fbfrenzy")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fbfrenzy not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fightfev'):
        # open both files
        message = 'fightfev success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fight Fever.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fight Fever.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fightfev" in each line
                 line = line.replace("GameFolder/", "fightfev")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fightfev not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fghtfeva'):
        # open both files
        message = 'fghtfeva success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fight Fever (set 2).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fight Fever (set 2).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fghtfeva" in each line
                 line = line.replace("GameFolder/", "fghtfeva")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fghtfeva not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'flipshot'):
        # open both files
        message = 'flipshot success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Battle Flip Shot.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Battle Flip Shot.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "flipshot" in each line
                 line = line.replace("GameFolder/", "flipshot")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("flipshot not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'frogfest'):
        # open both files
        message = 'frogfest success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Frog Feast.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Frog Feast.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "frogfest" in each line
                 line = line.replace("GameFolder/", "frogfest")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("frogfest not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'froman2b'):
        # open both files
        message = 'froman2b success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Idol Mahjong Final Romance 2 (CD conv).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Idol Mahjong Final Romance 2 (CD conv).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "froman2b" in each line
                 line = line.replace("GameFolder/", "froman2b")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("froman2b not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'fswords'):
        # open both files
        message = 'fswords success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Fighters Swords.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Fighters Swords.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "fswords" in each line
                 line = line.replace("GameFolder/", "fswords")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("fswords not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'galaxyfg'):
        # open both files
        message = 'galaxyfg success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Galaxy Fight Universal Warriors.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Galaxy Fight Universal Warriors.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "galaxyfg" in each line
                 line = line.replace("GameFolder/", "galaxyfg")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("galaxyfg not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ganryu'):
        # open both files
        message = 'ganryu success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ganryu.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ganryu.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ganryu" in each line
                 line = line.replace("GameFolder/", "ganryu")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ganryu not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'garoubl'):
        # open both files
        message = 'garoubl success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Garou - Mark of the Wolves (bootleg).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Garou - Mark of the Wolves (bootleg).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "garoubl" in each line
                 line = line.replace("GameFolder/", "garoubl")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("garoubl not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'garou'):
        # open both files
        message = 'garou success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Garou - Mark of the Wolves.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Garou - Mark of the Wolves.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "garou" in each line
                 line = line.replace("GameFolder/", "garou")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000002")
                 line = line.replace("0xCMC-Chip", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("garou not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'garouh'):
        # open both files
        message = 'garouh success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Garou - Mark of the Wolves (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Garou - Mark of the Wolves (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "garouh" in each line
                 line = line.replace("GameFolder/", "garouh")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000003")
                 line = line.replace("0xCMC-Chip", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("garouh not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'garoup'):
        # open both files
        message = 'garoup success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Garou - Mark of the Wolves (proto).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Garou - Mark of the Wolves (proto).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "garoup" in each line
                 line = line.replace("GameFolder/", "garoup")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("garoup not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ghostlop'):
        # open both files
        message = 'ghostlop success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ghostlop.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ghostlop.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ghostlop" in each line
                 line = line.replace("GameFolder/", "ghostlop")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ghostlop not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'goalx3'):
        # open both files
        message = 'goalx3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Goal! Goal! Goal!.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Goal! Goal! Goal!.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "goalx3" in each line
                 line = line.replace("GameFolder/", "goalx3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("goalx3 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'gowcaizr'):
        # open both files
        message = 'gowcaizr success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Voltage Fighter Gowcaizer.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Voltage Fighter Gowcaizer.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "gowcaizr" in each line
                 line = line.replace("GameFolder/", "gowcaizr")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("gowcaizr not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'gpilots'):
        # open both files
        message = 'gpilots success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ghost Pilots.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ghost Pilots.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "gpilots" in each line
                 line = line.replace("GameFolder/", "gpilots")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00280000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("gpilots not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'gpilotsh'):
        # open both files
        message = 'gpilotsh success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ghost Pilots (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ghost Pilots (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "gpilotsh" in each line
                 line = line.replace("GameFolder/", "gpilotsh")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00280000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("gpilotsh not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'gururin'):
        # open both files
        message = 'gururin success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Gururin.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Gururin.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "gururin" in each line
                 line = line.replace("GameFolder/", "gururin")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("gururin not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'hyprnoid'):
        # open both files
        message = 'hyprnoid success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Hypernoid.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Hypernoid.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "hyprnoid" in each line
                 line = line.replace("GameFolder/", "hyprnoid")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("hyprnoid not found")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ironclad'):
        # open both files
        message = 'ironclad success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ironclad.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ironclad.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ironclad" in each line
                 line = line.replace("GameFolder/", "ironclad")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ironclad not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'irnclado'):
        # open both files
        message = 'irnclado success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ironclad (bootleg).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ironclad (bootleg).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "irnclado" in each line
                 line = line.replace("GameFolder/", "irnclado")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("irnclado not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'irrmaze'):
        # open both files
        message = 'irrmaze success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Irritating Maze.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Irritating Maze.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "irrmaze" in each line
                 line = line.replace("GameFolder/", "irrmaze")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("irrmaze not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'janshin'):
        # open both files
        message = 'janshin success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Janshin Densetsu Quest of Jongmaster.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Janshin Densetsu Quest of Jongmaster.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "janshin" in each line
                 line = line.replace("GameFolder/", "janshin")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("janshin not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'joyjoy'):
        # open both files
        message = 'joyjoy success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Puzzled.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Puzzled.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "joyjoy" in each line
                 line = line.replace("GameFolder/", "joyjoy")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("joyjoy not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kabukikl'):
        # open both files
        message = 'kabukikl success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Far East of Eden Kabuki Klash.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Far East of Eden Kabuki Klash.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kabukikl" in each line
                 line = line.replace("GameFolder/", "kabukikl")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kabukikl not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'karnovr'):
        # open both files
        message = 'karnovr success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Karnov\'s Revenge.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Karnov\'s Revenge.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "karnovr" in each line
                 line = line.replace("GameFolder/", "karnovr")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("karnovr not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kizuna'):
        # open both files
        message = 'kizuna success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Kizuna Encounter Super Tag Battle.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Kizuna Encounter Super Tag Battle.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kizuna" in each line
                 line = line.replace("GameFolder/", "kizuna")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kizuna not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kf2k2mp2'):
        # open both files
        message = 'kf2k2mp2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2002 Magic Plus II, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2002 Magic Plus II, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kf2k2mp2" in each line
                 line = line.replace("GameFolder/", "kf2k2mp2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kf2k2mp2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kf2k2mp'):
        # open both files
        message = 'kf2k2mp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2002 Magic Plus, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2002 Magic Plus, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kf2k2mp" in each line
                 line = line.replace("GameFolder/", "kf2k2mp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kf2k2mp not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof2000'):
        # open both files
        message = 'kof2000 success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2000, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2000, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof2000" in each line
                 line = line.replace("GameFolder/", "kof2000")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000005")
                 line = line.replace("0xCMC-Chip", "0x00000002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof2000 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof2001h'):
        # open both files
        message = 'kof2001h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2001, The (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2001, The (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof2001h" in each line
                 line = line.replace("GameFolder/", "kof2001h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof2001h not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof2001'):
        # open both files
        message = 'kof2001 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2001, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2001, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof2001" in each line
                 line = line.replace("GameFolder/", "kof2001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof2001 not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof2002'):
        # open both files
        message = 'kof2002 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2002, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2002, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof2002" in each line
                 line = line.replace("GameFolder/", "kof2002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof2002 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof2003'):
        # open both files
        message = 'kof2003 success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 2003, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 2003, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof2003" in each line
                 line = line.replace("GameFolder/", "kof2003")
                 line = line.replace("0xPVC-Cart", "0x00000001")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof2003 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof2k4se'):
        # open both files
        message = 'kof2k4se success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters Special Edition 2004, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters Special Edition 2004, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof2k4se" in each line
                 line = line.replace("GameFolder/", "kof2k4se")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof2k4se not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kf10thep'):
        # open both files
        message = 'kf10thep success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters 10th Anniversary, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters 10th Anniversary, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kf10thep" in each line
                 line = line.replace("GameFolder/", "kf10thep")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kf10thep not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof94'):
        # open both files
        message = 'kof94 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'94, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'94, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof94" in each line
                 line = line.replace("GameFolder/", "kof94")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof94 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof95'):
        # open both files
        message = 'kof95 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'95, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'95, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof95" in each line
                 line = line.replace("GameFolder/", "kof95")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof95 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof95a'):
        # open both files
        message = 'kof95a success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'95, The (NGM-084).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'95, The (NGM-084).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof95a" in each line
                 line = line.replace("GameFolder/", "kof95a")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof95a not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof95h'):
        # open both files
        message = 'kof95h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'95, The (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'95, The (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof95h" in each line
                 line = line.replace("GameFolder/", "kof95h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof95h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof96'):
        # open both files
        message = 'kof96 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'96, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'96, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof96" in each line
                 line = line.replace("GameFolder/", "kof96")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof96 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof96h'):
        # open both files
        message = 'kof96h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'96, The (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'96, The (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof96h" in each line
                 line = line.replace("GameFolder/", "kof96h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof96h not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof97'):
        # open both files
        message = 'kof97 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'97, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'97, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof97" in each line
                 line = line.replace("GameFolder/", "kof97")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof97 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof97h'):
        # open both files
        message = 'kof97h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'97, The (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'97, The (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof97h" in each line
                 line = line.replace("GameFolder/", "kof97h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof97h not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof97k'):
        # open both files
        message = 'kof97k success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'97, The (Korean).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'97, The (Korean).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof97k" in each line
                 line = line.replace("GameFolder/", "kof97k")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof97k not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof97oro'):
        # open both files
        message = 'kof97oro success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'97, The Chongchu Jianghu Plus 2003.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'97, The Chongchu Jianghu Plus 2003.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof97oro" in each line
                 line = line.replace("GameFolder/", "kof97oro")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof97oro not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof97pls'):
        # open both files
        message = 'kof97pls success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'97 Plus, The (Bootleg).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'97 Plus, The (Bootleg).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof97pls" in each line
                 line = line.replace("GameFolder/", "kof97pls")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof97pls not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof98h'):
        # open both files
        message = 'kof98h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof98h" in each line
                 line = line.replace("GameFolder/", "kof98h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof98h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof98a'):
        # open both files
        message = 'kof98a success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest (NGM-2420).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest (NGM-2420).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof98a" in each line
                 line = line.replace("GameFolder/", "kof98a")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof98a not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof98'):
        # open both files
        message = 'kof98 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof98" in each line
                 line = line.replace("GameFolder/", "kof98")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof98 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof98k'):
        # open both files
        message = 'kof98k success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest (Korean).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'98, The - The Slugfest (Korean).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof98k" in each line
                 line = line.replace("GameFolder/", "kof98k")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof98k not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof99p'):
        # open both files
        message = 'kof99p success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'99, The Millennium Battle (proto).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'99, The Millennium Battle (proto).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof99p" in each line
                 line = line.replace("GameFolder/", "kof99p")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof99p not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof99'):
        # open both files
        message = 'kof99 success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'99, The Millennium Battle.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'99, The Millennium Battle.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof99" in each line
                 line = line.replace("GameFolder/", "kof99")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000001")
                 line = line.replace("0xCMC-Chip", "0x00000000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof99 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kof99e'):
        # open both files
        message = 'kof99e success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Fighters \'99, The Millennium Battle (earlier).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Fighters \'99, The Millennium Battle (earlier).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kof99e" in each line
                 line = line.replace("GameFolder/", "kof99e")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000001")
                 line = line.replace("0xCMC-Chip", "0x00000000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kof99e not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kog'):
        # open both files
        message = 'kog success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of Gladiators.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of Gladiators.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kog" in each line
                 line = line.replace("GameFolder/", "kog")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kog not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kotm'):
        # open both files
        message = 'kotm success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of the Monsters.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of the Monsters.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kotm" in each line
                 line = line.replace("GameFolder/", "kotm")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kotm not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kotmh'):
        # open both files
        message = 'kotmh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of the Monsters (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of the Monsters (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kotmh" in each line
                 line = line.replace("GameFolder/", "kotmh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kotmh not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kotm2'):
        # open both files
        message = 'kotm2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of the Monsters 2 The Next Thing.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of the Monsters 2 The Next Thing.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kotm2" in each line
                 line = line.replace("GameFolder/", "kotm2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kotm2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'kotm2p'):
        # open both files
        message = 'kotm2p success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/King of the Monsters 2 The Next Thing (proto).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/King of the Monsters 2 The Next Thing (proto).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "kotm2p" in each line
                 line = line.replace("GameFolder/", "kotm2p")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("kotm2p not found")

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lans2004'):
        # open both files
        message = 'lans2004 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Lansquenet 2004 (Shock Troopers 2nd Squad).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Lansquenet 2004 (Shock Troopers 2nd Squad).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lans2004" in each line
                 line = line.replace("GameFolder/", "lans2004")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lans2004 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lastblad'):
        # open both files
        message = 'lastblad success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Blade, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Blade, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lastblad" in each line
                 line = line.replace("GameFolder/", "lastblad")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lastblad not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lstbladh'):
        # open both files
        message = 'lstbladh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Blade, The (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Blade, The (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lstbladh" in each line
                 line = line.replace("GameFolder/", "lstbladh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lstbladh not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lastbld2'):
        # open both files
        message = 'lastbld2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Blade 2, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Blade 2, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lastbld2" in each line
                 line = line.replace("GameFolder/", "lastbld2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lastbld2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lasthope'):
        # open both files
        message = 'lasthope success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Hope.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Hope.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lasthope" in each line
                 line = line.replace("GameFolder/", "lasthope")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lasthope not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lastsold'):
        # open both files
        message = 'lastsold success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Soldier, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Soldier, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lastsold" in each line
                 line = line.replace("GameFolder/", "lastsold")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lastsold not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lbowling'):
        # open both files
        message = 'lbowling success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/League Bowling.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/League Bowling.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lbowling" in each line
                 line = line.replace("GameFolder/", "lbowling")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lbowling not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'legendos'):
        # open both files
        message = 'legendos success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Legend of Success Joe.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Legend of Success Joe.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "legendos" in each line
                 line = line.replace("GameFolder/", "legendos")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("legendos not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lresort'):
        # open both files
        message = 'lresort success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Resort.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Resort.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lresort" in each line
                 line = line.replace("GameFolder/", "lresort")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lresort not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'lresortp'):
        # open both files
        message = 'lresortp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Last Resort (prototype).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Last Resort (prototype).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "lresortp" in each line
                 line = line.replace("GameFolder/", "lresortp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("lresortp not found")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'magdrop2'):
        # open both files
        message = 'magdrop2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Magical Drop II.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Magical Drop II.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "magdrop2" in each line
                 line = line.replace("GameFolder/", "magdrop2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("magdrop2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'magdrop3'):
        # open both files
        message = 'magdrop3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Magical Drop III.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Magical Drop III.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "magdrop3" in each line
                 line = line.replace("GameFolder/", "magdrop3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("magdrop3 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'maglord'):
        # open both files
        message = 'maglord success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Magician Lord.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Magician Lord.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "maglord" in each line
                 line = line.replace("GameFolder/", "maglord")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("maglord not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'maglordh'):
        # open both files
        message = 'maglordh success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Magician Lord (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Magician Lord (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "maglordh" in each line
                 line = line.replace("GameFolder/", "maglordh")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("maglordh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'nblktiger'):
        # open both files
        message = 'nblktiger success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Black Tiger.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Black Tiger.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "nblktiger" in each line
                 line = line.replace("GameFolder/", "nblktiger")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("nblktiger not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mahretsu'):
        # open both files
        message = 'mahretsu success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Mahjong Kyo Retsuden.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Mahjong Kyo Retsuden.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mahretsu" in each line
                 line = line.replace("GameFolder/", "mahretsu")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mahretsu not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'marukodq'):
        # open both files
        message = 'marukodq success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Chibi Marukochan Deluxe Quiz.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Chibi Marukochan Deluxe Quiz.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "marukodq" in each line
                 line = line.replace("GameFolder/", "marukodq")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("marukodq not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'matrim'):
        # open both files
        message = 'matrim success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Power Instinct Matrimelee.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Power Instinct Matrimelee.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "matrim" in each line
                 line = line.replace("GameFolder/", "matrim")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("matrim not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'miexchng'):
        # open both files
        message = 'miexchng success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Money Puzzle Exchanger.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Money Puzzle Exchanger.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "miexchng" in each line
                 line = line.replace("GameFolder/", "miexchng")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("miexchng not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'minasan'):
        # open both files
        message = 'minasan success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Minasan no Okagesamadesu! Dai Sugoroku Taikai.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Minasan no Okagesamadesu! Dai Sugoroku Taikai.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "minasan" in each line
                 line = line.replace("GameFolder/", "minasan")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00280000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("minasan not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'MonitorTest'):
        # open both files
        message = 'MonitorTest success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Monitor Test ROM.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Monitor Test ROM.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "MonitorTest" in each line
                 line = line.replace("GameFolder/", "MonitorTest")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("MonitorTest not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'moshougi'):
        # open both files
        message = 'moshougi success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Shougi no Tatsujin - Master of Syougi.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Shougi no Tatsujin - Master of Syougi.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "moshougi" in each line
                 line = line.replace("GameFolder/", "moshougi")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("moshougi not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug'):
        # open both files
        message = 'mslug success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug" in each line
                 line = line.replace("GameFolder/", "mslug")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug2'):
        # open both files
        message = 'mslug2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug2" in each line
                 line = line.replace("GameFolder/", "mslug2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug2t'):
        # open both files
        message = 'mslug2t success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 2 Turbo.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 2 Turbo.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug2t" in each line
                 line = line.replace("GameFolder/", "mslug2t")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug2t not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug3'):
        # open both files
        message = 'mslug3 success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 3.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 3.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug3" in each line
                 line = line.replace("GameFolder/", "mslug3")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000004")
                 line = line.replace("0xCMC-Chip", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug3 not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug3h'):
        # open both files
        message = 'mslug3h success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 3 (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 3 (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug3h" in each line
                 line = line.replace("GameFolder/", "mslug3h")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug3h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug3c'):
        # open both files
        message = 'mslug3c success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 3 (Set 3).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 3 (Set 3).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug3c" in each line
                 line = line.replace("GameFolder/", "mslug3c")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug3c not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug4'):
        # open both files
        message = 'mslug4 success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 4.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 4.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug4" in each line
                 line = line.replace("GameFolder/", "mslug4")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug4 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug4h'):
        # open both files
        message = 'mslug4h success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 4 (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 4 (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug4h" in each line
                 line = line.replace("GameFolder/", "mslug4h")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug4h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ms4plus'):
        # open both files
        message = 'ms4plus success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 4 Plus.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 4 Plus.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ms4plus" in each line
                 line = line.replace("GameFolder/", "ms4plus")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ms4plus not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug5'):
        # open both files
        message = 'mslug5 success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 5.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 5.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug5" in each line
                 line = line.replace("GameFolder/", "mslug5")
                 line = line.replace("0xPVC-Cart", "0x00000001")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug5 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug5h'):
        # open both files
        message = 'mslug5h success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 5 (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 5 (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug5h" in each line
                 line = line.replace("GameFolder/", "mslug5h")
                 line = line.replace("0xPVC-Cart", "0x00000001")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug5h not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ms5plus'):
        # open both files
        message = 'ms5plus success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 5 Plus.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 5 Plus.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ms5plus" in each line
                 line = line.replace("GameFolder/", "ms5plus")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ms5plus not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslug6'):
        # open both files
        message = 'mslug6 success'
        print (message)
        with open('template5.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug 6.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug 6.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslug6" in each line
                 line = line.replace("GameFolder/", "mslug6")
                 line = line.replace("0xPVC-Cart", "0x00000000")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslug6 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mslugx'):
        # open both files
        message = 'mslugx success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Metal Slug X.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Metal Slug X.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mslugx" in each line
                 line = line.replace("GameFolder/", "mslugx")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mslugx not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'mutnat'):
        # open both files
        message = 'mutnat success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Mutation Nation.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Mutation Nation.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "mutnat" in each line
                 line = line.replace("GameFolder/", "mutnat")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("mutnat not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'nam1975'):
        # open both files
        message = 'nam1975 success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/NAM-1975.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/NAM-1975.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "nam1975" in each line
                 line = line.replace("GameFolder/", "nam1975")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("nam1975 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ncombat'):
        # open both files
        message = 'ncombat success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ninja Combat.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ninja Combat.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ncombat" in each line
                 line = line.replace("GameFolder/", "ncombat")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ncombat not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ncombath'):
        # open both files
        message = 'ncombath success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ninja Combat (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ninja Combat (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ncombath" in each line
                 line = line.replace("GameFolder/", "ncombath")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ncombath not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ncommand'):
        # open both files
        message = 'ncommand success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ninja Commando.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ninja Commando.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ncommand" in each line
                 line = line.replace("GameFolder/", "ncommand")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ncommand not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neobombe'):
        # open both files
        message = 'neobombe success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Bomberman.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Bomberman.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neobombe" in each line
                 line = line.replace("GameFolder/", "neobombe")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neobombe not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neocup98'):
        # open both files
        message = 'neocup98 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo-Geo Cup 98 The Road to the Victory.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo-Geo Cup 98 The Road to the Victory.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neocup98" in each line
                 line = line.replace("GameFolder/", "neocup98")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neocup98 not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neodrift'):
        # open both files
        message = 'neodrift success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Drift Out New Technology.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Drift Out New Technology.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neodrift" in each line
                 line = line.replace("GameFolder/", "neodrift")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neodrift not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neofight'):
        # open both files
        message = 'neofight success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Fight.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Fight.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neofight" in each line
                 line = line.replace("GameFolder/", "neofight")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neofight not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neomrdo'):
        # open both files
        message = 'neomrdo success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Mr Do.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Mr Do.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neomrdo" in each line
                 line = line.replace("GameFolder/", "neomrdo")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neomrdo not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neothund'):
        # open both files
        message = 'neothund success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Thunder.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Thunder.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neothund" in each line
                 line = line.replace("GameFolder/", "neothund")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neothund not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'neotris'):
        # open both files
        message = 'neotris success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/NeoTRIS.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/NeoTRIS.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "neotris" in each line
                 line = line.replace("GameFolder/", "neotris")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("neotris not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ninjamas'):
        # open both files
        message = 'ninjamas success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ninja Master\'s.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ninja Master\'s.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ninjamas" in each line
                 line = line.replace("GameFolder/", "ninjamas")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ninjamas not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'nitd'):
        # open both files
        message = 'nitd success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Nightmare in the Dark.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Nightmare in the Dark.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "nitd" in each line
                 line = line.replace("GameFolder/", "nitd")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("nitd not found")

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'nitdbl'):
        # open both files
        message = 'nitdbl success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Nightmare in the Dark (bootleg).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Nightmare in the Dark (bootleg).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "nitdbl" in each line
                 line = line.replace("GameFolder/", "nitdbl")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("nitdbl not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'overtop'):
        # open both files
        message = 'overtop success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/OverTop.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/OverTop.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "overtop" in each line
                 line = line.replace("GameFolder/", "overtop")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("overtop not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'panicbom'):
        # open both files
        message = 'panicbom success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Panic Bomber.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Panic Bomber.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "panicbom" in each line
                 line = line.replace("GameFolder/", "panicbom")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("panicbom not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pbobbl2n'):
        # open both files
        message = 'pbobbl2n success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Puzzle Bobble 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Puzzle Bobble 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pbobbl2n" in each line
                 line = line.replace("GameFolder/", "pbobbl2n")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pbobbl2n not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pbobblen'):
        # open both files
        message = 'pbobblen success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Puzzle Bobble.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Puzzle Bobble.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pbobblen" in each line
                 line = line.replace("GameFolder/", "pbobblen")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pbobblen not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pbbblenb'):
        # open both files
        message = 'pbbblenb success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Puzzle Bobble (bootleg).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Puzzle Bobble (bootleg).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pbbblenb" in each line
                 line = line.replace("GameFolder/", "pbbblenb")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pbbblenb not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pgoal'):
        # open both files
        message = 'pgoal success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Pleasure Goal.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Pleasure Goal.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pgoal" in each line
                 line = line.replace("GameFolder/", "pgoal")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pgoal not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pnyaa'):
        # open both files
        message = 'pnyaa success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Pochi and Nyaa.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Pochi and Nyaa.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pnyaa" in each line
                 line = line.replace("GameFolder/", "pnyaa")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pnyaa not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'popbounc'):
        # open both files
        message = 'popbounc success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Pop \'n Bounce.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Pop \'n Bounce.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "popbounc" in each line
                 line = line.replace("GameFolder/", "popbounc")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("popbounc not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'preisle2'):
        # open both files
        message = 'preisle2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Prehistoric Isle 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Prehistoric Isle 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "preisle2" in each line
                 line = line.replace("GameFolder/", "preisle2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("preisle2 not found")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pspikes2'):
        # open both files
        message = 'pspikes2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Power Spikes II.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Power Spikes II.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pspikes2" in each line
                 line = line.replace("GameFolder/", "pspikes2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pspikes2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'pulstar'):
        # open both files
        message = 'pulstar success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Pulstar.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Pulstar.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "pulstar" in each line
                 line = line.replace("GameFolder/", "pulstar")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("pulstar not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'puzzldpr'):
        # open both files
        message = 'puzzldpr success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Puzzle De Pon! R!.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Puzzle De Pon! R!.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "puzzldpr" in each line
                 line = line.replace("GameFolder/", "puzzldpr")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("puzzldpr not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'puzzledp'):
        # open both files
        message = 'puzzledp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Puzzle De Pon!.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Puzzle De Pon!.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "puzzledp" in each line
                 line = line.replace("GameFolder/", "puzzledp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("puzzledp not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'quizdai2'):
        # open both files
        message = 'quizdai2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Quiz Meitantei.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Quiz Meitantei.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "quizdai2" in each line
                 line = line.replace("GameFolder/", "quizdai2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("quizdai2 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'quizdais'):
        # open both files
        message = 'quizdais success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Quiz Daisousa Sen The Last Count Down.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Quiz Daisousa Sen The Last Count Down.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "quizdais" in each line
                 line = line.replace("GameFolder/", "quizdais")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("quizdais not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'quizdask'):
        # open both files
        message = 'quizdask success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Quiz Salibtamjeong The Last Count Down (Korean).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Quiz Salibtamjeong The Last Count Down (Korean).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "quizdask" in each line
                 line = line.replace("GameFolder/", "quizdask")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("quizdask not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'quizkof'):
        # open both files
        message = 'quizkof success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Quiz King of Fighters.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Quiz King of Fighters.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "quizkof" in each line
                 line = line.replace("GameFolder/", "quizkof")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("quizkof not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'quizkofk'):
        # open both files
        message = 'quizkofk success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Quiz King of Fighters (Korean).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Quiz King of Fighters (Korean).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "quizkofk" in each line
                 line = line.replace("GameFolder/", "quizkofk")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("quizkofk not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ragnagrd'):
        # open both files
        message = 'ragnagrd success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ragnagard.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ragnagard.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ragnagrd" in each line
                 line = line.replace("GameFolder/", "ragnagrd")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ragnagrd not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbff1'):
        # open both files
        message = 'rbff1 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbff1" in each line
                 line = line.replace("GameFolder/", "rbff1")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbff1 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbff1a'):
        # open both files
        message = 'rbff1a success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury (bug fix).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury (bug fix).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbff1a" in each line
                 line = line.replace("GameFolder/", "rbff1a")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbff1a not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbff2'):
        # open both files
        message = 'rbff2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury 2 The Newcomers.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury 2 The Newcomers.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbff2" in each line
                 line = line.replace("GameFolder/", "rbff2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbff2 not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbff2h'):
        # open both files
        message = 'rbff2h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury 2 The Newcomers (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury 2 The Newcomers (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbff2h" in each line
                 line = line.replace("GameFolder/", "rbff2h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbff2h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbff2k'):
        # open both files
        message = 'rbff2k success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury 2 The Newcomers (Korean).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury 2 The Newcomers (Korean).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbff2k" in each line
                 line = line.replace("GameFolder/", "rbff2k")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbff2k not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbffspec'):
        # open both files
        message = 'rbffspec success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury Special.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury Special.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbffspec" in each line
                 line = line.replace("GameFolder/", "rbffspec")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbffspec not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rbffspck'):
        # open both files
        message = 'rbffspck success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Real Bout Fatal Fury Special (Korean).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Real Bout Fatal Fury Special (Korean).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rbffspck" in each line
                 line = line.replace("GameFolder/", "rbffspck")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rbffspck not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ridhero'):
        # open both files
        message = 'ridhero success'
        print (message)
        with open('template4.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Riding Hero.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Riding Hero.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ridhero" in each line
                 line = line.replace("GameFolder/", "ridhero")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 line = line.replace("0xCTOLINK", "0x00000002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ridhero not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ridheroh'):
        # open both files
        message = 'ridheroh success'
        print (message)
        with open('template4.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Riding Hero (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Riding Hero (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ridheroh" in each line
                 line = line.replace("GameFolder/", "ridheroh")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 line = line.replace("0xCTOLINK", "0x00000002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ridheroh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'roboarmy'):
        # open both files
        message = 'roboarmy success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Robo Army.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Robo Army.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "roboarmy" in each line
                 line = line.replace("GameFolder/", "roboarmy")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("roboarmy not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'roboarma'):
        # open both files
        message = 'roboarma success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Robo Army (NGM-032).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Robo Army (NGM-032).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "roboarma" in each line
                 line = line.replace("GameFolder/", "roboarma")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("roboarma not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rotd'):
        # open both files
        message = 'rotd success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Rage of the Dragons.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Rage of the Dragons.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rotd" in each line
                 line = line.replace("GameFolder/", "rotd")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rotd not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'rotdh'):
        # open both files
        message = 'rotdh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Rage of the Dragons (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Rage of the Dragons (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "rotdh" in each line
                 line = line.replace("GameFolder/", "rotdh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("rotdh not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 's1945p'):
        # open both files
        message = 's1945p success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Strikers 1945 Plus.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Strikers 1945 Plus.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "s1945p" in each line
                 line = line.replace("GameFolder/", "s1945p")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("s1945p not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho'):
        # open both files
        message = 'samsho success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho" in each line
                 line = line.replace("GameFolder/", "samsho")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samshoh'):
        # open both files
        message = 'samshoh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samshoh" in each line
                 line = line.replace("GameFolder/", "samshoh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samshoh not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho2'):
        # open both files
        message = 'samsho2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown II.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown II.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho2" in each line
                 line = line.replace("GameFolder/", "samsho2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho2k'):
        # open both files
        message = 'samsho2k success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Saulabi Spirits (Korean release of Samurai Shodown II).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Saulabi Spirits (Korean release of Samurai Shodown II).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho2k" in each line
                 line = line.replace("GameFolder/", "samsho2k")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho2k not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'smsho2k2'):
        # open both files
        message = 'smsho2k2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Saulabi Spirits (Korean release of Samurai Shodown II, set 2).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Saulabi Spirits (Korean release of Samurai Shodown II, set 2).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "smsho2k2" in each line
                 line = line.replace("GameFolder/", "smsho2k2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("smsho2k2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho3'):
        # open both files
        message = 'samsho3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown III.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown III.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho3" in each line
                 line = line.replace("GameFolder/", "samsho3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho3 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho3h'):
        # open both files
        message = 'samsho3h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown III (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown III (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho3h" in each line
                 line = line.replace("GameFolder/", "samsho3h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho3h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho4'):
        # open both files
        message = 'samsho4 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown IV Amakusa\'s Revenge.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown IV Amakusa\'s Revenge.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho4" in each line
                 line = line.replace("GameFolder/", "samsho4")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho4 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho4k'):
        # open both files
        message = 'samsho4k success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Pae Wang Jeon Seol - Legend of a Warrior.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Pae Wang Jeon Seol - Legend of a Warrior.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho4k" in each line
                 line = line.replace("GameFolder/", "samsho4k")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho4k not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsh5sp'):
        # open both files
        message = 'samsh5sp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V Special.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V Special.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsh5sp" in each line
                 line = line.replace("GameFolder/", "samsh5sp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsh5sp not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'smsh5sph'):
        # open both files
        message = 'smsh5sph success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V Special (2nd release, less censored).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V Special (2nd release, less censored).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "smsh5sph" in each line
                 line = line.replace("GameFolder/", "smsh5sph")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("smsh5sph not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'smsh5spo'):
        # open both files
        message = 'smsh5spo success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V Special (1st release, censored).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V Special (1st release, censored).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "smsh5spo" in each line
                 line = line.replace("GameFolder/", "smsh5spo")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("smsh5spo not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho5'):
        # open both files
        message = 'samsho5 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho5" in each line
                 line = line.replace("GameFolder/", "samsho5")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho5 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho5b'):
        # open both files
        message = 'samsho5b success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V (bootleg).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V (bootleg).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho5b" in each line
                 line = line.replace("GameFolder/", "samsho5b")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho5b not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho5h'):
        # open both files
        message = 'samsho5h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho5h" in each line
                 line = line.replace("GameFolder/", "samsho5h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho5h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsho5x'):
        # open both files
        message = 'samsho5x success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V (XBOX version hack).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V (XBOX version hack).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsho5x" in each line
                 line = line.replace("GameFolder/", "samsho5x")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsho5x not found")

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsh5fe'):
        # open both files
        message = 'samsh5fe success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V Special Final Edition.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V Special Final Edition.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsh5fe" in each line
                 line = line.replace("GameFolder/", "samsh5fe")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsh5fe not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'samsh5pf'):
        # open both files
        message = 'samsh5pf success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Samurai Shodown V Perfect.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Samurai Shodown V Perfect.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "samsh5pf" in each line
                 line = line.replace("GameFolder/", "samsh5pf")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("samsh5pf not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'savagere'):
        # open both files
        message = 'savagere success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Savage Reign.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Savage Reign.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "savagere" in each line
                 line = line.replace("GameFolder/", "savagere")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("savagere not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sbp'):
        # open both files
        message = 'sbp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Super Bubble Pop.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Super Bubble Pop.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sbp" in each line
                 line = line.replace("GameFolder/", "sbp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sbp not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sdodgeb'):
        # open both files
        message = 'sdodgeb success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Super Dodge Ball.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Super Dodge Ball.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sdodgeb" in each line
                 line = line.replace("GameFolder/", "sdodgeb")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sdodgeb not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sengoku'):
        # open both files
        message = 'sengoku success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Sengoku.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Sengoku.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sengoku" in each line
                 line = line.replace("GameFolder/", "sengoku")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sengoku not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sengokuh'):
        # open both files
        message = 'sengokuh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Sengoku (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Sengoku (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sengokuh" in each line
                 line = line.replace("GameFolder/", "sengokuh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sengokuh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sengoku2'):
        # open both files
        message = 'sengoku2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Sengoku 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Sengoku 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sengoku2" in each line
                 line = line.replace("GameFolder/", "sengoku2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sengoku2 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sengoku3'):
        # open both files
        message = 'sengoku3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Sengoku 3.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Sengoku 3.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sengoku3" in each line
                 line = line.replace("GameFolder/", "sengoku3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sengoku3 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'shocktr2'):
        # open both files
        message = 'shocktr2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Shock Troopers 2nd Squad.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Shock Troopers 2nd Squad.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "shocktr2" in each line
                 line = line.replace("GameFolder/", "shocktr2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("shocktr2 not found")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'shocktro'):
        # open both files
        message = 'shocktro success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Shock Troopers.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Shock Troopers.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "shocktro" in each line
                 line = line.replace("GameFolder/", "shocktro")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("shocktro not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'shcktroa'):
        # open both files
        message = 'shcktroa success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Shock Troopers (set 2).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Shock Troopers (set 2).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "shcktroa" in each line
                 line = line.replace("GameFolder/", "shcktroa")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("shcktroa not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'socbrawl'):
        # open both files
        message = 'socbrawl success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Soccer Brawl.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Soccer Brawl.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "socbrawl" in each line
                 line = line.replace("GameFolder/", "socbrawl")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("socbrawl not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'scbrawlh'):
        # open both files
        message = 'scbrawlh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Soccer Brawl (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Soccer Brawl (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "scbrawlh" in each line
                 line = line.replace("GameFolder/", "scbrawlh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("scbrawlh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sonicwi2'):
        # open both files
        message = 'sonicwi2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Aero Fighters 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Aero Fighters 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sonicwi2" in each line
                 line = line.replace("GameFolder/", "sonicwi2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sonicwi2 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'sonicwi3'):
        # open both files
        message = 'sonicwi3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Aero Fighters 3.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Aero Fighters 3.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "sonicwi3" in each line
                 line = line.replace("GameFolder/", "sonicwi3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("sonicwi3 not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'spinmast'):
        # open both files
        message = 'spinmast success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Spinmaster.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Spinmaster.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "spinmast" in each line
                 line = line.replace("GameFolder/", "spinmast")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("spinmast not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ssideki'):
        # open both files
        message = 'ssideki success'
        print (message)
        with open('template3.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Super Sidekicks.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Super Sidekicks.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ssideki" in each line
                 line = line.replace("GameFolder/", "ssideki")
                 line = line.replace("0xCTOLINK", "0x00000001")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ssideki not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ssideki2'):
        # open both files
        message = 'ssideki2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Super Sidekicks 2 The World Championship.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Super Sidekicks 2 The World Championship.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ssideki2" in each line
                 line = line.replace("GameFolder/", "ssideki2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ssideki2 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ssideki3'):
        # open both files
        message = 'ssideki3 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Super Sidekicks 3 The Next Glory.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Super Sidekicks 3 The Next Glory.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ssideki3" in each line
                 line = line.replace("GameFolder/", "ssideki3")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ssideki3 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ssideki4'):
        # open both files
        message = 'ssideki4 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Ultimate 11, The The SNK Football Championship.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Ultimate 11, The The SNK Football Championship.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ssideki4" in each line
                 line = line.replace("GameFolder/", "ssideki4")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ssideki4 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'stakwin'):
        # open both files
        message = 'stakwin success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Stakes Winner.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Stakes Winner.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "stakwin" in each line
                 line = line.replace("GameFolder/", "stakwin")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("stakwin not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'stakwin2'):
        # open both files
        message = 'stakwin2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Stakes Winner 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Stakes Winner 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "stakwin2" in each line
                 line = line.replace("GameFolder/", "stakwin2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("stakwin2 not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'strhoop'):
        # open both files
        message = 'strhoop success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Street Hoop.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Street Hoop.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "strhoop" in each line
                 line = line.replace("GameFolder/", "strhoop")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("strhoop not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'superspy'):
        # open both files
        message = 'superspy success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Super Spy, The.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Super Spy, The.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "superspy" in each line
                 line = line.replace("GameFolder/", "superspy")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00280000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("superspy not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'tetrismn'):
        # open both files
        message = 'tetrismn success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Tetris.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Tetris.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "tetrismn" in each line
                 line = line.replace("GameFolder/", "tetrismn")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("tetrismn not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'svc'):
        # open both files
        message = 'svc success'
        print (message)
        with open('template1.json','r') as firstfile, open ('./Mazamars312.NeoGeo/SNK vs. Capcom.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/SNK vs. Capcom.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "svc" in each line
                 line = line.replace("GameFolder/", "svc")
                 line = line.replace("0xPVC-Cart", "0x00000001")
                 line = line.replace("0xSMA-Cart", "0x00000000")
                 line = line.replace("0xCMC-Chip", "0x00000002")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("svc not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'svcplus'):
        # open both files
        message = 'svcplus success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/SNK vs. Capcom Plus.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/SNK vs. Capcom Plus.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "svcplus" in each line
                 line = line.replace("GameFolder/", "svcplus")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("svcplus not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'tophuntr'):
        # open both files
        message = 'tophuntr success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Top Hunter.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Top Hunter.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "tophuntr" in each line
                 line = line.replace("GameFolder/", "tophuntr")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("tophuntr not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'tphuntrh'):
        # open both files
        message = 'tphuntrh success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Top Hunter (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Top Hunter (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "tphuntrh" in each line
                 line = line.replace("GameFolder/", "tphuntrh")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("tphuntrh not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'totc'):
        # open both files
        message = 'totc success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Treasure of the Caribbean.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Treasure of the Caribbean.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "totc" in each line
                 line = line.replace("GameFolder/", "totc")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("totc not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'tpgolf'):
        # open both files
        message = 'tpgolf success'
        print (message)
        with open('template2.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Top Players Golf.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Top Players Golf.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "tpgolf" in each line
                 line = line.replace("GameFolder/", "tpgolf")
                 line = line.replace("0xPCM", "0xFFFFFFFF")
                 line = line.replace("0xOFFSET", "0x00200000")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("tpgolf not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'trally'):
        # open both files
        message = 'trally success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Thrash Rally.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Thrash Rally.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "trally" in each line
                 line = line.replace("GameFolder/", "trally")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("trally not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'turfmast'):
        # open both files
        message = 'turfmast success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Neo Turf Masters.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Neo Turf Masters.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "turfmast" in each line
                 line = line.replace("GameFolder/", "turfmast")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("turfmast not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'twinspri'):
        # open both files
        message = 'twinspri success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Twinkle Star Sprites.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Twinkle Star Sprites.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "twinspri" in each line
                 line = line.replace("GameFolder/", "twinspri")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("twinspri not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'tws96'):
        # open both files
        message = 'tws96 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Tecmo World Soccer 96.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Tecmo World Soccer 96.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "tws96" in each line
                 line = line.replace("GameFolder/", "tws96")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("tws96 not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'twsoc96'):
        # open both files
        message = 'twsoc96 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Tecmo World Soccer 96 (Set 2).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Tecmo World Soccer 96 (Set 2).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "twsoc96" in each line
                 line = line.replace("GameFolder/", "twsoc96")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("twsoc96 not found")     

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'viewpoin'):
        # open both files
        message = 'viewpoin success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Viewpoint.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Viewpoint.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "viewpoin" in each line
                 line = line.replace("GameFolder/", "viewpoin")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("viewpoin not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wakuwak7'):
        # open both files
        message = 'wakuwak7 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Waku Waku 7.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Waku Waku 7.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wakuwak7" in each line
                 line = line.replace("GameFolder/", "wakuwak7")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wakuwak7 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wh1'):
        # open both files
        message = 'wh1 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/World Heroes.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/World Heroes.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wh1" in each line
                 line = line.replace("GameFolder/", "wh1")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wh1 not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wh1h'):
        # open both files
        message = 'wh1h success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/World Heroes (AES).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/World Heroes (AES).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wh1h" in each line
                 line = line.replace("GameFolder/", "wh1h")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wh1h not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wh1ha'):
        # open both files
        message = 'wh1ha success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/World Heroes (set 3).json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/World Heroes (set 3).json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wh1ha" in each line
                 line = line.replace("GameFolder/", "wh1ha")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wh1ha not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wh2'):
        # open both files
        message = 'wh2 success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/World Heroes 2.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/World Heroes 2.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wh2" in each line
                 line = line.replace("GameFolder/", "wh2")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wh2 not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wh2j'):
        # open both files
        message = 'wh2j success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/World Heroes 2 Jet.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/World Heroes 2 Jet.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wh2j" in each line
                 line = line.replace("GameFolder/", "wh2j")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wh2j not found") 
     
#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'whp'):
        # open both files
        message = 'whp success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/World Heroes Perfect.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/World Heroes Perfect.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "whp" in each line
                 line = line.replace("GameFolder/", "whp")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("whp not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wjammers'):
        # open both files
        message = 'wjammers success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Windjammers.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Windjammers.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wjammers" in each line
                 line = line.replace("GameFolder/", "wjammers")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wjammers not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'wjammss'):
        # open both files
        message = 'wjammss success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Windjammers Supersonic.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Windjammers Supersonic.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "wjammss" in each line
                 line = line.replace("GameFolder/", "wjammss")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("wjammss not found") 

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'XenoCrisis'):
        # open both files
        message = 'XenoCrisis success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Xeno Crisis.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Xeno Crisis.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "XenoCrisis" in each line
                 line = line.replace("GameFolder/", "XenoCrisis")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("XenoCrisis not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'zedblade'):
        # open both files
        message = 'zedblade success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Zed Blade.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Zed Blade.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "zedblade" in each line
                 line = line.replace("GameFolder/", "zedblade")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("zedblade not found")      

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'zintrckb'):
        # open both files
        message = 'zintrckb success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/ZinTricK.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/ZinTricK.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "zintrckb" in each line
                 line = line.replace("GameFolder/", "zintrckb")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("zintrckb not found")  

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'zupapa'):
        # open both files
        message = 'zupapa success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Zupapa!.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Zupapa!.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "zupapa" in each line
                 line = line.replace("GameFolder/", "zupapa")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("zupapa not found")   

#compares and makes .json file for game        
def find_string(file_name, word):
   with open(file_name, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(word),line):
             return True
             return False

if find_string('Gamelist.txt', 'ct2k3sa'):
        # open both files
        message = 'ct2k3sa success'
        print (message)
        with open('template.json','r') as firstfile, open ('./Mazamars312.NeoGeo/Crouching Tiger Hidden Dragon.json','w') as secondfile:
        
                 # read content from first file
                 for line in firstfile:
                 
                          # write content to second file
                          secondfile.write(line)
                 
        # This for loop scans and searches each line in the file
        # By using the input() method of fileinput module
        for line in fileinput.input("./Mazamars312.NeoGeo/Crouching Tiger Hidden Dragon.json", inplace=True):
                 
                 # This will replace string "GameFolder/" with "ct2k3sa" in each line
                 line = line.replace("GameFolder/", "ct2k3sa")
                 # write() method of sys module redirects the .stdout is redirected to the file
                 sys.stdout.write(line)
else:
     print("ct2k3sa not found")  
     
     
os.remove('./template.json')    
os.remove('./template1.json')
os.remove('./template2.json')
os.remove('./template3.json')
os.remove('./template4.json')
os.remove('./template5.json')
os.remove('./Gamelist.txt') 

  
print("Analogue Pocket Neogeo game.json files created successfully in " , dirName ,"folder")      
print("Script Created by Terminator2k2 - Enjoy")    