import csv

csv_file_path = 'Public_Restrooms.csv'

def haversine(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, sqrt, atan2

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of the Earth in kilometers
    radius = 6371.0

    # Calculate distance
    distance = radius * c

    return distance



def filter_bathrooms(csv_file_path, user_lat, user_lon, max_distance_km=5.0):
    filtered_bathrooms = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            # Handle missing or improperly formatted values
            try:
                bathroom_lat = float(row.get('lat', 0))
                bathroom_lon = float(row.get('lon', 0))
            except ValueError:
                continue

            # Calculate distance between user and bathroom
            distance_km = haversine(user_lat, user_lon, bathroom_lat, bathroom_lon)

            if distance_km <= max_distance_km:
                filtered_bathrooms.append({
                    'name': row.get('name', 'Unknown'),
                    'address': row.get('address', 'Unknown'),
                    'latitude': bathroom_lat,
                    'longitude': bathroom_lon,
                    'distance_km': distance_km
                })

    return filtered_bathrooms


for bathroom in filter_bathrooms(csv_file_path, 40.7128, -74.0060):
    print(bathroom)