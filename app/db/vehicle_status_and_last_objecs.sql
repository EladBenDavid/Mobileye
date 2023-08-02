SELECT
    vs.report_time AS last_report_time,
    vs.status,
    vs.vehicle_id,
    od.detection_time,
    od.detections
FROM (
    select report_time, status, vehicle_id
    from(
        select report_time, status, vehicle_id,
        rank() OVER (PARTITION BY vehicle_id ORDER BY report_time DESC) AS time_rank
        from mobileye.vehicles_status
    ) as sort_vs
    where sort_vs.time_rank = 1
 ) as vs
ASOF LEFT JOIN mobileye.objects_detection od
ON vs.vehicle_id = od.vehicle_id AND vs.report_time >= od.detection_time


