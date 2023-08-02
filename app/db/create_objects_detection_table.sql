-- Create a table named 'objects_detection' in the 'mobileye' database (if it doesn't already exist).
CREATE TABLE IF NOT EXISTS mobileye.objects_detection (
    -- 'vehicle_id' column to store the ID of the vehicle associated with the detection.
    vehicle_id String,
    
    -- 'detections' column to store an array of JSON objects representing the detections made by the vehicle.
    detections Array(JSON),
    
    -- 'detection_time' column to store the timestamp when the detections were made (in UTC time zone).
    detection_time DateTime('UTC')
) ENGINE = MergeTree()  -- Define the storage engine for the table as MergeTree.
ORDER BY (vehicle_id, detection_time)  -- Define the sorting order for the data based on vehicle_id and detection_time.
PARTITION BY toYYYYMM(detection_time);  -- Partition the data by year and month based on the detection_time.
