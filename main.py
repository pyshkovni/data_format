import json
from collections import Counter

def extract_wind_directions(data):
    wind_directions = []
    
    if isinstance(data, dict):
        if 'wind_dir' in data:
            wind_directions.append(data['wind_dir'])
        for value in data.values():
            wind_directions.extend(extract_wind_directions(value))
    
    elif isinstance(data, list):
        for item in data:
            wind_directions.extend(extract_wind_directions(item))
    
    return wind_directions

