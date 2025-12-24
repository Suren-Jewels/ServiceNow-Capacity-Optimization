<#
.SYNOPSIS
    Collect ServiceNow performance and capacity metrics (PowerShell).

.DESCRIPTION
    Uses the shared ServiceNow API wrapper to pull node metrics and writes them
    as JSON for downstream analytics.
#>

param(
    [string]$OutputDir = "data/raw",
    [string]$ConfigPath = "config/baseline-config.json"
)

. "$PSScriptRoot\servicenow-api-client.ps1"

function Ensure-OutputDirectory {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
    }
}

function Get-NodeMetrics {
    param([string]$ConfigPath)

    $path = "/api/now/table/x_capacity_node_metrics"
    $params = @{ "sysparm_query" = "active=true" }
    Write-Host "Collecting node metrics from $path" -ForegroundColor Cyan

    $result = Invoke-ServiceNowGet -Path $path -ConfigPath $ConfigPath
    return $result.result
}

Ensure-OutputDirectory -Path $OutputDir

$records = Get-NodeMetrics -ConfigPath $ConfigPath
$timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
$fileName = "node_metrics_$timestamp.json"
$outPath = Join-Path $OutputDir $fileName

Write-Host "Writing $($records.Count) records to $outPath" -ForegroundColor Green
$payload = [pscustomobject]@{
    type    = "node_metrics"
    records = $records
}
$payload | ConvertTo-Json -Depth 5 | Out-File -FilePath $outPath -Encoding utf8

Write-Host "Metric collection completed successfully." -ForegroundColor Green
