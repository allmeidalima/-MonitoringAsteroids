from Func.Functions import *
import json


#Open file .josn to get url
with open('config.json') as json_file:
   file = json.load(json_file)


_URL = file['url'].replace('{@start_date}', '2023-06-15').replace('{@end_date}', '2023-06-22')

#Accessing the Nasa url for get file json
data = request_url_string(_URL)


asteroids = data['near_earth_objects']

asteroid_list = []
closest_asteroids_dict = {}


#Scrolling through the information
for day in asteroids:
   for asteroid in asteroids[day]:
      name = asteroid['name']
      distance = asteroid['close_approach_data'][0]['miss_distance']['kilometers']
      asteroid_list.append((name , distance))

asteroid_list.sort(key=lambda x: x[1])

for i in range(10):
    closest_asteroids_dict[asteroid_list[i][0]] = asteroid_list[i][1]


create_asteroid_label(closest_asteroids_dict, 'Asteroids', 'Names', 'Kilometers', 'document_asteroids')

