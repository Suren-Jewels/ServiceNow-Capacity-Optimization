-- Server Migration Planning Query
-- Fully sanitized example used for demonstrating SQL-based analysis
-- of server readiness, POD distribution, and workload classification.

SELECT 
    server_id,
    pod_location,
    workload_type
FROM 
    server_inventory
WHERE 
    status = 'ReadyForMigration'
ORDER BY 
    pod_location,
    workload_type;
