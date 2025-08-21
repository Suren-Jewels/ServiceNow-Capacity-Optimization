-- SQL snippet for planning DARE/Clotho server migrations
-- Sanitized for confidentiality

SELECT server_id, pod_location, workload_type
FROM server_inventory
WHERE status = 'ReadyForMigration'
ORDER BY pod_location;
