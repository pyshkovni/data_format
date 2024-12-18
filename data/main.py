import pandas as pd
import json


json_file_path = 'data/Saint-Petersburg24.09.06.json'
data = [
    {"date": "2024-09-08" , "hour": 0 , "condition": "partly-cloudy" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 1 , "condition": "clear" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 2 , "condition": "clear" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 3 , "condition": "clear" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 4 , "condition": "partly-cloudy" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 5 , "condition": "cloudy" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 6 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 7 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 8 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 9 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 10 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 11 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 12 , "condition": "overcast" , "pressure_mm": 769} ,
    {"date": "2024-09-08" , "hour": 13 , "condition": "overcast" , "pressure_mm": 768} ,
    {"date": "2024-09-08" , "hour": 14 , "condition": "overcast" , "pressure_mm": 768} ,
    {"date": "2024-09-08" , "hour": 15 , "condition": "overcast" , "pressure_mm": 768} ,
    {"date": "2024-09-08" , "hour": 16 , "condition": "cloudy" , "pressure_mm": 768} ,
    {"date": "2024-09-08" , "hour": 17 , "condition": "partly-cloudy" , "pressure_mm": 767} ,
    {"date": "2024-09-08" , "hour": 18 , "condition": "partly-cloudy" , "pressure_mm": 767} ,
    {"date": "2024-09-08" , "hour": 19 , "condition": "partly-cloudy" , "pressure_mm": 767} ,
    {"date": "2024-09-08" , "hour": 20 , "condition": "partly-cloudy" , "pressure_mm": 767} ,
    {"date": "2024-09-08" , "hour": 21 , "condition": "clear" , "pressure_mm": 767} ,
    {"date": "2024-09-08" , "hour": 22 , "condition": "clear" , "pressure_mm": 767} ,
    {"date": "2024-09-08" , "hour": 23 , "condition": "partly-cloudy" , "pressure_mm": 767} 

]


df = pd.DataFrame(data)

csv_file_path = 'data/weather_data.csv'
df.to_csv(csv_file_path, index=False)






    