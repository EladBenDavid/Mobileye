-- Create a table named 'vehicles_status' in the 'mobileye' database (if it doesn't already exist).
CREATE TABLE IF NOT EXISTS mobileye.vehicles_status (
    -- 'vehicle_id' column to store the ID of the vehicle for which the status is reported.
    vehicle_id String,
    
    -- 'report_time' column to store the timestamp when the status is reported (in UTC time zone).
    report_time DateTime('UTC'),
    
    -- 'status' column to store the current status of the vehicle (e.g., "driving," "accident," "parking").
    status String
) ENGINE = MergeTree()  -- Define the storage engine for the table as MergeTree.
ORDER BY (vehicle_id, report_time)  -- Define the sorting order for the data based on vehicle_id and report_time.
PARTITION BY toYYYYMM(report_time);  -- Partition the data by year and month based on the report_time.
