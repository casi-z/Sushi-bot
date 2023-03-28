from geopy.distance import geodesic
from data import data
def find_nearest_restaurant(user_geolocation):
    
    restaurants_distance = []
    for item in data.restaurants:
        restaurants_distance.append(geodesic(
            user_geolocation, 
            (
                int(tuple(item['geolocation'])[0]),
                int(tuple(item['geolocation'])[0])
             
            )
        ).m)

    return data.restaurants[restaurants_distance.index(min(restaurants_distance))]['address']

