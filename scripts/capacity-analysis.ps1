<#
.SYNOPSIS
    Analyze capacity across ServiceNow POD servers.

.DESCRIPTION
    Reads a list of servers, retrieves CPU/RAM metrics using a sanitized
    placeholder function, and outputs a summarized capacity report.

    This script is fully sanitized and demonstrates PowerShell automation
    patterns used in enterprise capacity analysis workflows.
#>

param(
    [string]$ServerList = "server_list.txt"
)

function Get-CapacityMetrics {
    param([string]$ServerName)

    <#
        Placeholder for actual metric retrieval logic.
        In real usage, this would call:
        - ServiceNow API
        - Monitoring tools
        - CMDB relationships
        - Performance collectors
    #>

    return [pscustomobject]@{
        CPU = Get-Random -Minimum 10 -Maximum 90
        RAM = Get-Random -Minimum 20 -Maximum 95
    }
}

if (-not (Test-Path $ServerList)) {
    Write-Error "Server list not found: $ServerList"
    exit 1
}

$servers = Get-Content $ServerList

foreach ($server in $servers) {
    $metrics = Get-CapacityMetrics -ServerName $server
    Write-Output ("{0}: CPU={1}%, RAM={2}%" -f $server, $metrics.CPU, $metrics.RAM)
}

Write-Host "Capacity analysis completed." -ForegroundColor Green
