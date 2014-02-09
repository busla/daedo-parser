# -*- coding: ISO-8859-1 -*-
import sys, string, os, json, re

directory = os.getcwd()

score_header = ['TIME',
                'PERIOD', 
                'EVENT', 
                'R-J1', 
                'R-j2', 
                'R-j3', 
                'R-HGU', 
                'B-J1', 
                'B-j2', 
                'B-j3', 
                'B-HGU', 
                'P-RED', 
                'P-BLUE', 
                'SCORE']
data = {}
start_matrix = False
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.tkd'):
            f = open(file, 'r')
            lines = f.readlines()
            match = {}
            score = {} # Dict fyrir hverja tímasetning
            
            for counter, line in enumerate(lines):
                    words = string.split(line)                    
                    # Ef línan er ekki tóm haltu þá áfram
                    if words:
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
                        # ber saman score_header við staðsetningu í lúppu til að athuga hvort stigatafla sé að hefjast                        
                        if start_matrix:
                            if words[2] == 'SCORE':
                                point = {} # Sub-dict af score sem inniheldur body&head og stig sem var gefið
                                point['Time'] = words[0]
                                point['Round'] = words[1]
                                point['Event'] = words[2]
                                point['Total'] = words[-1]
                                score[key] = point
                                match['Score'] = score
                                key += 1
                                            
                        if words[0] == 'END':
                            match['End'] = words[3]
                            match['Results'] = string.split(lines[counter-2])[-1]
                            start_matrix = False

                        if words[0] == 'WINNER':
                            match['Winner'] = words[6]

                        if set(words) == set(score_header):
                            start_matrix = True
                            key = 1
                        
                            
                        
            #data.update(match)
            data[match_number] = match
                            #print 'Úrslit: ' + string.split(lines[counter-2])[-1]
                        
            #if words[0] == 'TIME':
                #print words

                
        #label = string.split(line, ':')
        
print data
with open("test.json", "w") as outfile:    
    json.dump(data, outfile, indent=4, sort_keys=True, encoding='ISO-8859-1')
