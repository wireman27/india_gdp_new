import sys
sys.path.append('/Users/user/Documents/Python_Packages')
import pandas as pd
path = '/Users/user/Documents/Cities/India_GDP/new_gdp_data/india_gdp_new/airlinks'
import json

data = pd.read_csv(path+'/for_geojson.csv')
data.drop('Unnamed: 0',axis=1,inplace=True)
data.drop_duplicates(subset=['air1_iata','air2_iata'],keep='first',inplace=True)
data = data[data['air1_iata']!=data['air2_iata']]

print(data.shape)


air1 = data['air1_iata'].tolist()
air2 = data['air2_iata'].tolist()


finalSet = set()

for x in range(len(air2)):
    airSet = frozenset({air1[x], air2[x]})
    if(len(airSet) < 2):
        print(x)
    finalSet.add(airSet)

airPairs = [list(x) for x in list(finalSet)]

print(len(airPairs))

geojson = {
    'type': 'FeatureCollection',
    'features': []
    }

def index(air1, air2, data):
    return(data[((data['air1_iata']==air1) & (data['air2_iata']==air2)) |
         ((data['air2_iata']==air1) & (data['air1_iata']==air2))])

for row in airPairs:
##    pri£nt(row)
##    print(airPairs.index(row))
    a1 = row[0]
    a2 = row[1]
    a1a2 = 'null'
    a2a1 = 'null'
    t = 'null'
    rows = index(row[0],row[1],data).shape[0]
    if rows > 1:
        a1a2 = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['twc'].iloc[0].item()
        a2a1 = data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['twc'].iloc[0].item()
        t = a1a2 + a2a1
        rcs = str(data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['route'].iloc[0])
        a1lng = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air1_lng'].iloc[0].item()
        a1lat = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air1_lat'].iloc[0].item()
        a2lng = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air2_lng'].iloc[0].item()
        a2lat = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air2_lat'].iloc[0].item()
    else:
        if(len(data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['twc']) == 0):
            a2a1 = data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['twc'].iloc[0].item()
            rcs = str(data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['route'].iloc[0])
            t = a2a1
            a1lng = data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['air2_lng'].iloc[0].item()
            a1lat = data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['air2_lat'].iloc[0].item()
            a2lng = data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['air1_lng'].iloc[0].item()
            a2lat = data[(data['air2_iata']==row[0]) & (data['air1_iata']==row[1])]['air1_lat'].iloc[0].item()
        else:
            a1a2 = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['twc'].iloc[0].item()
            rcs = str(data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['route'].iloc[0])
            t = a1a2
            a1lng = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air1_lng'].iloc[0].item()
            a1lat = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air1_lat'].iloc[0].item()
            a2lng = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air2_lng'].iloc[0].item()
            a2lat = data[(data['air1_iata']==row[0]) & (data['air2_iata']==row[1])]['air2_lat'].iloc[0].item()
    geojson['features'].append({
        'type':'Feature',
        'properties':{
            'a1':a1,
            'a2':a2,
            'a1a2':a1a2,
            'a2a1':a2a1,
            't':t,
            'rcs': rcs
            },
        'geometry':{
            'type':'LineString',
            'coordinates':
            [
                [a1lng, a1lat],
                [a2lng, a2lat]
            ]
        }
    })

features = geojson['features']
features[0]

with open(path+'/airlinks.geojson','w') as f:
    json.dump(geojson,f)







