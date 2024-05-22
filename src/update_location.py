import json
import os
import math
import time

# Constants
EARTH_RADIUS = 6371000  # in meters
CELL_SIZE = 100  # cell size in meters

def encode_geohash(latitude, longitude, cell_size):
    """
    Simple geohash function to divide the Earth's surface into a grid of cell_size x cell_size meters.
    """
    lat_cell = int((latitude + 90) * (EARTH_RADIUS * 2 * math.pi / 360) / cell_size)
    lon_cell = int((longitude + 180) * (EARTH_RADIUS * 2 * math.pi / 360 * math.cos(math.radians(latitude))) / cell_size)
    return f"{lat_cell}_{lon_cell}"

def lambda_handler(event, context):
    # Extracting details from the event
    driver_id = event['driver_id']
    updated_at = event['updated_at']
    status = event['status']
    latitude = event['latitude']
    longitude = event['longitude']
    
    # Generating geohash
    geohash = encode_geohash(latitude, longitude, CELL_SIZE)
    
    # Constructing file paths
    geohash_file_path = f"/tmp/{geohash}.json"
    driver_file_path = f"/tmp/{driver_id}.json"
    
    # Creating driver location data
    driver_data = {
        "driver_id": driver_id,
        "updated_at": updated_at,
        "status": status,
        "latitude": latitude,
        "longitude": longitude
    }
    
    # Writing data to geohash file
    with open(geohash_file_path, 'w') as geohash_file:
        json.dump(driver_data, geohash_file)
    
    # Writing data to driver ID file
    with open(driver_file_path, 'w') as driver_file:
        json.dump(driver_data, driver_file)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Location updated successfully')
    }
