@echo off
setlocal
cd /d "%~dp0"

echo.
echo ========================================
echo              NEXA - Windows
echo ========================================
echo.

where py >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON=py -3.11"
) else (
    set "PYTHON=python"
)

%PYTHON% --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python 3.11 nao encontrado.
    echo Instale o Python 3.11 e marque "Add Python to PATH".
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    echo [1/3] Criando ambiente virtual...
    %PYTHON% -m venv .venv
    if errorlevel 1 goto :error
)

echo [2/3] Verificando dependencias...
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto :error
".venv\Scripts\python.exe" -m pip install -r requirements-windows.txt
if errorlevel 1 goto :error

echo [3/3] Abrindo NEXA...
".venv\Scripts\python.exe" main.py
if errorlevel 1 goto :error

exit /b 0

:error
echo.
echo [ERRO] Nao foi possivel iniciar o NEXA.
echo Verifique a mensagem acima.
pause
exit /b 1
