1. # PowerShell script to analyze server capacity across PODs
# Sanitized for confidentiality

$servers = Get-Content "server_list.txt"
foreach ($server in $servers) {
    $metrics = Get-CapacityMetrics -ServerName $server
    Write-Output "$server: CPU=$($metrics.CPU)%, RAM=$($metrics.RAM)%"
}
