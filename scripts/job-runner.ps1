<#
.SYNOPSIS
    Orchestrates the ServiceNow capacity pipeline.

.DESCRIPTION
    Runs metric collection, normalization, and forecasting as a single
    end-to-end job. Intended to be wired into a scheduler (Task Scheduler, etc.).
#>

param(
    [string]$PythonExe = "python",
    [string]$RepoRoot = "$PSScriptRoot\.."
)

$ErrorActionPreference = "Stop"

function Invoke-Step {
    param(
        [string]$Name,
        [scriptblock]$Action
    )

    Write-Host "=== [$Name] START ===" -ForegroundColor Cyan
    try {
        & $Action
        Write-Host "=== [$Name] COMPLETE ===`n" -ForegroundColor Green
    }
    catch {
        Write-Error "Step [$Name] failed: $_"
        exit 1
    }
}

Set-Location $RepoRoot

Invoke-Step -Name "Collect Metrics (Python)" -Action {
    & $PythonExe "scripts/collect-metrics.py"
}

Invoke-Step -Name "Normalize Data" -Action {
    & $PythonExe "scripts/data-normalization.py"
}

Invoke-Step -Name "Run Forecasting Engine" -Action {
    & $PythonExe "scripts/forecasting-engine.py"
}

Write-Host "All pipeline steps completed successfully." -ForegroundColor Green
