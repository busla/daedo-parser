# -*- coding: ISO-8859-1 -*-
import sys, string, os, json, re
from random import randrange

directory = os.getcwd()

score_header = [
                'TIME',
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
                'SCORE',
                ]
                
event_options = [
                'Hogu',
                'SCORE',
                'TA_PENL',
                ]

def find_point(point):
    point_type = {
                    'BODY': 'Body',
                    'HEAD': 'Head',
                    'PUNCH': 'Punch',
                    'TA_PENL': 'Penalty',
                    }
    
    return point_type.get(point)
    
def find_competitor(protector):
    position = {
                    76: 'Blue',
                    48: 'Red',
                    27: 'Red',
                    34: 'Red',
                    41: 'Red',
                    55: 'Blue',
                    62: 'Blue',
                    69: 'Blue',
                    83: 'Red',
                    91: 'Blue',           
    }
    
    return position.get(protector)
               
data = {}
start_matrix = False
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.tkd'):
            try:
                f = open(file, 'r')
                lines = f.readlines()
                match = {}
                score = {} # Dict fyrir hverja tímasetning
                ikey = 0
                impact = []
            
                for counter, line in enumerate(lines):
                        words = string.split(line)

                        # Ef línan er ekki tóm haltu þá áfram
                        if words:
                            if words[0] == 'MATCH':
                                #if len(words) == 3  :
                                    #if words[3] == 'match':
                                        #match_number = randrange(1000,10000)
                                    #else: 
                                    #match_number = str(words[3])
                                #else:
                                match_number = randrange(1000,10000)
                            
                            if words[0] == 'DATE':
                                match['Date'] = str(words[2])
                                                        
                            if words[1] == 'THRESHOLD':
                                match['Threshold'] = str(words[3])

                            if words[0] == 'START':
                                match['Start'] = str(words[3])
                
                            if words[0] == 'RED':
                                if len(words) == 2:
                                    match['Red'] = words[3]
                                #print 'Rauður: ' + words[3]

                            if words[0] == 'BLUE':
                                if len(words) == 2:
                                    match['Blue'] = words[3]
                                #print 'Blár: ' + words[3]
                            # ber saman score_header við staðsetningu í lúppu til að athuga hvort stigatafla sé að hefjast                        
                            if start_matrix:
                                point = {}
                            
                                if words[2] in event_options:
                                    # Fall til að prenta skottið á færslunni sem er alltaf eins.
                                    def print_score_info():
                                        point['Time'] = words[0]
                                        point['Round'] = words[1]                            
                                        point['Total'] = words[-1]
                                        score[key] = point
                                        match['Score'] = score                                        #point = 0

                                    if words[2] == 'Hogu':                                    
                                        if int(words[3]) < int(match['Threshold']):
                                            point['Point'] = '0'
                                            point['Impact'] = words[3]
                                            point['Competitor'] = find_competitor(line.index('BODY')) # Hvað er char index´ið í línunn
                                            point['Event'] = 'Body'
                                            print_score_info()
                                        
                                        else:
                                            impact.append(words[3]) # Ekki prenta ef höggið af stig heldur safna í lista
                                        
                                        #match['Impact'] = event[1]
                                    
                                    
                                    if words[2] == 'SCORE':
                                        if impact:
                                            point['Impact'] = impact[0] # Prenta höggþunga með stigi úr lista
                                            del impact[0] # Getur innihaldið mörg spörk, eyða fyrsta höggþunga í listanum, þannig færast færslurnar upp þar til allt hefur verið prentað og öllu eytt.
                                        elif not impact:
                                            point['Impact'] = '-'
                                        
                                        point['Competitor'] = find_competitor(line.index(words[3]))    
                                        point['Event'] = find_point(words[3])
                                        point['Point'] = words[-2]
                                        print_score_info()
                                
                                    if words[2] == 'TA_PENL': # Ef keppandi fékk mínus stig
                                        point['Point'] = words[-2]
                                        point['Competitor'] = find_competitor(line.index(words[-2]))
                                        point['Event'] = find_point(words[2])
                                        point['Impact'] = '-'
                                        print_score_info()

                                    if words[2] == 'SW_STOP':
                                        red_p = words[3].split('-')[0]
                                        blue_p = words[3].split('-')[1]
                                        if red_p > blue_p:
                                            match['Winner'] = match['Red']
                                        else:
                                            match['Winner'] = match['Blue']                                    
                                    
                                    
                                        #if impact < match['Impact']:
                                
                                    key += 1

                                            
                            if words[0] == 'END':
                                match['End'] = words[3]
                                match['Results'] = string.split(lines[counter-2])[-1]
                                start_matrix = False
                        
                            # Síðasta færslan í matrix hefur kóðann SW_STOP og á endanum eru úrslitin


                            if set(words) == set(score_header):
                                start_matrix = True
                                key = 1
                f.close()
                
            except IOError:
                print 'Eftirfarandi skrá fannst ekki: ', file
                
                            
                        
            #data.update(match)
            data[match_number] = match
                            #print 'Úrslit: ' + string.split(lines[counter-2])[-1]
                        
            #if words[0] == 'TIME':
                #print words

                
        #label = string.split(line, ':')
        
#list(reversed(sorted(data.keys())))
print data


with open("test.json", "w") as outfile:    
    json.dump(data, outfile, indent=4, encoding='ISO-8859-1')
outfile.close()
