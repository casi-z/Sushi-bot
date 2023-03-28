from geopy.distance import geodesic
from data import data


def find_nearest_restaurant(user_geolocation):
    restaurants_distance = []
    for item in data.restaurants:
        restaurants_distance.append(
            geodesic(
                user_geolocation, item[1]
            ).m
        )

    return data.restaurants[restaurants_distance.index(min(restaurants_distance))][0]


def way_to_restaurant(user_geolocation):
    restaurants_distance = []
    for item in data.restaurants:
        restaurants_distance.append(
            geodesic(
                user_geolocation, item[1]
            ).km
        )
        
    return round(min(restaurants_distance))

def get_delivery_time(way):
    return round((way / 1000) * 11.11)
