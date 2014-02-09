# -*- coding: ISO-8859-1 -*-
import sys, string, os, json, re

directory = os.getcwd()

data = {}
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.tkd'):
            f = open(file, 'r')
            lines = f.readlines()
            match = {}
            for counter, line in enumerate(lines):
                    words = string.split(line)
                    if words:
                        #print str(counter) + ': ' + lines[counter]
                        if words[0] == 'MATCH':
                            match_number = str(words[3])
                            
                        if words[1] == 'THRESHOLD':
                            match['Impact'] = str(words[3])

                        if words[0] == 'START':
                            match['Start'] = str(words[3])
                
                        if words[0] == 'RED':
                            match['Red'] = words[3]
                            #print 'Rauður: ' + words[3]

                        if words[0] == 'BLUE':
                            match['Blue'] = words[3]
                            #print 'Blár: ' + words[3]
                        if (len(words) > 2):
                            if words[0:4] == 'SCORE':
                                time = {}
                                time['Time'] = words[0]
            
                        if words[0] == 'END':
                            match['End'] = words[3]
                            match['Results'] = string.split(lines[counter-2])[-1]

                        if words[0] == 'WINNER':
                            match['Winner'] = words[6]
                        
                            
                        
            #data.update(match)
            data[match_number] = match
                            #print 'Úrslit: ' + string.split(lines[counter-2])[-1]
                        
            #if words[0] == 'TIME':
                #print words

                
        #label = string.split(line, ':')
        
print data
with open("matches.json", "w") as outfile:    
    json.dump(data, outfile, indent=4, sort_keys=True, encoding='ISO-8859-1')
