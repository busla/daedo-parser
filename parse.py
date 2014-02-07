# -*- coding: ISO-8859-1 -*-
import sys, string, os, json

directory = os.getcwd()

data = {}
match = {}
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.tkd'):
            f = open(file, 'r')
            lines = f.readlines()
            for counter, line in enumerate(lines):
                    words = string.split(line)
                    if words:
                        #print str(counter) + ': ' + lines[counter]
                        if words[0] == 'MATCH':
                            match_number = str(words[3])
                            
                        if words[1] == 'THRESHOLD':
                            match['Minimum impact'] = str(words[3])

                        if words[0] == 'START':
                            match['Match began'] = str(words[3])
                
                        if words[0] == 'RED':
                            match['Red'] = words[3]
                            #print 'Rauður: ' + words[3]

                        if words[0] == 'BLUE':
                            match['Blue'] = words[3]
                            #print 'Blár: ' + words[3]
            
                        if words[0] == 'END':
                            match['Match ended'] = words[3]
                            match['Results'] = string.split(lines[counter-2])[-1]

                        if words[0] == 'WINNER':
                            match['Winner'] = words[6]
                        
            
            data[match_number] = match
                            #print 'Úrslit: ' + string.split(lines[counter-2])[-1]
                        
            #if words[0] == 'TIME':
                #print words

                
        #label = string.split(line, ':')
        
    #if words[0] !=
with open('my_dict.json', 'w') as f:
    json.dump(data, f, encoding='ISO-8859-1')