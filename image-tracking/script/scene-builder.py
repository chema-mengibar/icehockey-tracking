import bpy
import json
from math import degrees

path = bpy.path.abspath("//")


# SCENE OBJECTS

# selection_names = [obj.name for obj in bpy.context.selected_objects]

frameStart = 765
frameEnd = 820


sceneName = 'game-001' + '_' + str(frameStart) + '-' + str(frameEnd)

players = [
    'PUCK',
    'P_LOC_1','P_LOC_2','P_LOC_3','P_LOC_4','P_LOC_5',
    'P_VIS_1','P_VIS_2','P_VIS_3','P_VIS_4','P_VIS_5','P_VIS_6',
]

trackers = [
    'C1',    'C2',    'C3',
    'L11',    'L12',    'L13',    'L14',
    'L21',    'L22',    'L23',    'L24',    'L25',
    'L31',    'L32',    'L33',    'L34',    'L35',    'L36',
    'L41',    'L42',
    'L51',    'L52',    'L53',    'L54',
]


data = {
    'meta':{
       'name': sceneName 
    },
    'limits':[5.04488, 2.77683],
    'ref_objects_location': [],
    'ref_players_location': [],
    'ref_objects': trackers,
    'ref_players': players
}


# ANIMATION

for tracker in trackers:
    
    objData = {
        'name': tracker,
        'coors': [],
    }
    
    
    for frameIdx in range(frameStart,frameEnd):
    
        bpy.context.scene.frame_set(frameIdx)
    
        obj = bpy.data.objects[tracker]
        loc = obj.location
        
        x = round(loc.x, 3)
        y = round(loc.y, 3)
      
        objData['coors'].append([x, y, frameIdx]) 
       
    data['ref_objects_location'].append(objData)
    
    
for player in players:
    
    obj = bpy.data.objects[player]
    
    objData = {
        'name': player,
        'num':  int(obj["NUM"]) if player is not 'PUCK' else '',
        'coors': [],
    }
    
    
    for frameIdx in range(frameStart,frameEnd):
    
        bpy.context.scene.frame_set(frameIdx)
    
        
        loc = obj.location
        
        x = round(loc.x, 2)
        y = round(loc.y, 2)
      
        objData['coors'].append([x, y, frameIdx]) 
       
    data['ref_players_location'].append(objData)
   

content = f"""
{json.dumps(data, indent=4)}
"""

with open(path + "../data/game-tracking/" + sceneName +".json",'w') as f:
    f.write(content)
    