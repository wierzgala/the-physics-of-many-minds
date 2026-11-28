@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "PY_EXE="

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    for /f "delims=" %%P in ('where python') do (
        echo %%P | findstr /i "WindowsApps\\python.exe" >nul
        if errorlevel 1 if not defined PY_EXE set "PY_EXE=%%P"
    )
)

if not defined PY_EXE (
    for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do (
        if exist "%%D\python.exe" set "PY_EXE=%%D\python.exe"
    )
)

if not defined PY_EXE (
    echo Error: Python 3 not found. Install via: winget install Python.Python.3.12 1>&2
    exit /b 1
)

"%PY_EXE%" "%SCRIPT_DIR%build_book.py" %*
exit /b %ERRORLEVEL%
