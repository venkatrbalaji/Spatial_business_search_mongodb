#
# Assignment5 Interface
# Name: Venkataramana Balaji Rajendran
# ASU ID: 1219328539
#

import traceback, math


def DistanceFunction(lat2, lon2, lat1, lon1):
    R = 3959
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lat_delta_rad = math.radians(lat2-lat1)
    lon_delta_rad = math.radians(lon2-lon1)
    a = math.sin(lat_delta_rad/2)*math.sin(lat_delta_rad/2) + math.cos(lat1_rad)*math.cos(lat2_rad)*math.sin(lon_delta_rad/2)*math.sin(lon_delta_rad/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d


def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    try:
        cityToSearch = cityToSearch.upper()
        with open(saveLocation1, 'w') as f:
            for business in collection.find():
                if (business['city'].upper() == cityToSearch):
                    bus_name = business['name'].upper()
                    bus_address = business['full_address'].upper()
                    bus_city = business['city'].upper()
                    bus_state = business['state'].upper()
                    f.write(f"{bus_name}${bus_address}${bus_city}${bus_state}\n")
    except Exception as e:
            traceback.print_exc()
    

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    try:
        search_categories_as_set = set(categoriesToSearch)
        with open(saveLocation2, 'w') as f:
            for business in collection.find():
                common_categories = list(search_categories_as_set.intersection(business['categories']))
                if (len(common_categories)>0):
                    distance = DistanceFunction(float(business['latitude']), float(business['longitude']), float(myLocation[0]), float(myLocation[1]))
                    if (distance <= maxDistance):
                        bus_name = business['name'].upper()
                        f.write(f"{bus_name}\n")
    except Exception as e:
            traceback.print_exc()
