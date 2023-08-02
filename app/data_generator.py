import os
import calendar
import time
import random
from datetime import datetime
from datetime import timedelta
import json


def write_objects_detection():
    """
    Continuously generates random objects detection and vehicle status data and writes it to JSON files.
    Each JSON file contains a timestamp in its name and is saved in the 'input_files' directory.
    The function runs indefinitely, with a delay of 10 seconds between each iteration.
    """
    while True:
        # Generate random values for the given JSON
        random_objects_detection = {
            "objects_detection_events": generate_random_objects_detection_events(3)
        }
        my_dir = 'input_files'
        if not os.path.exists(my_dir):
            # Create a new directory because it does not exist
            os.makedirs(my_dir)

        with open(f"{my_dir}/objects_detection_{calendar.timegm(time.gmtime())}.json", 'a') as f:
            f.write(json.dumps(random_objects_detection, indent=4))

        # Generate random values for the given JSON
        random_vehicle = {
            "vehicle_status": generate_random_vehicle_statuses(3)
        }

        with open(f"{my_dir}/vehicles_status_{calendar.timegm(time.gmtime())}.json", 'a') as f:
            f.write(json.dumps(random_vehicle, indent=4))

        time.sleep(10)


def generate_random_detections():
    """
    Generates a random list of detections with randomly selected object types and values.
    """
    detections = []
    for _ in range(random.randint(1, len(object_types))):
        object_type = random.choice(object_types)
        object_value = random.randint(1, 10)
        detections.append({"object_type": object_type, "object_value": object_value})
    return detections


def generate_random_objects_detection_events(num_events):
    """
    Generates a list of random objects detection events with random vehicle IDs, detection times,
    and a random number of detections per event.
    """
    objects_detection_events = []
    for _ in range(num_events):
        vehicle_id = random.choice(vehicle_ids)
        detection_time = generate_random_report_time()
        detections = generate_random_detections()
        event = {
            "vehicle_id": vehicle_id,
            "detection_time": detection_time,
            "detections": detections
        }
        objects_detection_events.append(event)
    return objects_detection_events


def generate_random_report_time():
    """
    Generates a random report time within a specified date range.
    """
    start_date = datetime(2022, 5, 1)
    end_date = datetime(2022, 5, 31)
    time_difference = end_date - start_date
    random_days = random.randint(0, time_difference.days)
    random_seconds = random.randint(0, 86400)
    random_datetime = start_date + timedelta(days=random_days, seconds=random_seconds)
    return random_datetime.isoformat()


def generate_random_vehicle_statuses(num_statuses):
    """
    Generates a list of random vehicle statuses with random vehicle IDs, report times, and status options.
    """
    vehicle_statuses = []
    for _ in range(num_statuses):
        vehicle_id = random.choice(vehicle_ids)
        report_time = generate_random_report_time()
        status = random.choice(status_options)
        status_entry = {
            "vehicle_id": vehicle_id,
            "report_time": report_time,
            "status": status
        }
        vehicle_statuses.append(status_entry)
    return vehicle_statuses


# Available object types for detections
object_types = ["pedestrians", "cars", "signs", "trucks", "obstacles"]

# Sample vehicle IDs for generating vehicle statuses
vehicle_ids = ['0a5e3c102ec811eebe560242ac120002', '2821a20a2ec811eebe560242ac120002',
               '318713c02ec811eebe560242ac120002']

# Available status options for vehicle statuses
status_options = ["driving", "accident", "parking"]

if __name__ == '__main__':
    write_objects_detection()
