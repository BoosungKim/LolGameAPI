import json
from pandas import DataFrame
import pandas as pd


def make_simple_match_info(matchjsonfile):
    '''
    output : time | total_gold | position
    '''
    with open(matchjsonfile, mode='r', encoding='utf-8') as f:
        jsontext = f.read()

    data = json.loads(jsontext)

    frames = data['timeline']['frames']
    record = []
    for frame in frames:
        data_per_min = {'time': 0, 'total_gold': 0, 'pos_x': -1, 'pos_y': -1}

        time_m = frame['timestamp']//60000
        mydata = frame['participantFrames']['6']
        position = mydata.get('position', dict())

        data_per_min['time'] = time_m
        data_per_min['total_gold'] = mydata['totalGold']

        if position:
            data_per_min['pos_x'] = position['x']
            data_per_min['pos_y'] = position['y']

        record.append(data_per_min)

    df = DataFrame(record)

    order = ['time', 'total_gold', 'pos_x', 'pos_y']
    df = df[order]

    outputname = 'matchinfo.csv'
    df.to_csv(outputname, sep='\t')
    print('Complete to create match info : ', outputname)