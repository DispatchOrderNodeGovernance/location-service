import json
import os
import math
from datetime import datetime

# Constants
EARTH_RADIUS = 6371000  # in meters
CELL_SIZE = 100  # cell size in meters

def encode_geohash(latitude, longitude, cell_size):
    """
    Simple geohash function to divide the Earth's surface into a grid of cell_size x cell_size meters.
    """
    lat_cell = int((latitude + 90) * (EARTH_RADIUS * 2 * math.pi / 360) / cell_size)
    lon_cell = int((longitude + 180) * (EARTH_RADIUS * 2 * math.pi / 360 * math.cos(math.radians(latitude))) / cell_size)
    return lat_cell, f"{lat_cell}_{lon_cell}"

def lambda_handler(event, context):
    # Extracting body from the event
    body = json.loads(event['body'])
    driver_id = body['driver_id']
    status = body['status']
    latitude = body['latitude']
    longitude = body['longitude']
    
    # Generating geohash and cell
    lat_cell, geohash = encode_geohash(latitude, longitude, CELL_SIZE)
    
    # Constructing file paths
    lat_cell_dir = f"/tmp/{lat_cell}"
    geohash_file_path = f"{lat_cell_dir}/{geohash}.json"
    driver_file_path = f"/tmp/{driver_id}.json"
    
    # Ensure the directory exists
    os.makedirs(lat_cell_dir, exist_ok=True)
    
    # Generating the current timestamp for updated_at
    updated_at = datetime.utcnow().isoformat() + 'Z'
    
    # Creating driver location data
    driver_data = {
        "driver_id": driver_id,
        "updated_at": updated_at,
        "status": status,
        "latitude": latitude,
        "longitude": longitude
    }
    
    # Check if the geohash file exists
    if os.path.exists(geohash_file_path):
        # Read existing data
        with open(geohash_file_path, 'r') as geohash_file:
            geohash_data = json.load(geohash_file)
    else:
        geohash_data = {}
    
    # Update geohash data with the new driver data
    geohash_data[driver_id] = driver_data
    
    # Write updated data back to the geohash file
    with open(geohash_file_path, 'w') as geohash_file:
        json.dump(geohash_data, geohash_file)
    
    # Writing data to driver ID file
    with open(driver_file_path, 'w') as driver_file:
        json.dump(driver_data, driver_file)
    
    # Prepare the response with all drivers in the updated geohash file
    response_data = [
        {"id": driver_id, "latitude": data["latitude"], "longitude": data["longitude"]}
        for driver_id, data in geohash_data.items()
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }

