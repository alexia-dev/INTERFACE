$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) {
    & py -3.11 --version
    $pythonCommand = "py"
} else {
    & python --version
    $pythonCommand = "python"
}

if (-not (Test-Path ".venv\Scripts\python.exe")) {
    if ($pythonCommand -eq "py") {
        & py -3.11 -m venv .venv
    } else {
        & python -m venv .venv
    }
}

& ".venv\Scripts\python.exe" -m pip install --upgrade pip
& ".venv\Scripts\python.exe" -m pip install -r requirements-windows.txt
& ".venv\Scripts\python.exe" main.py
