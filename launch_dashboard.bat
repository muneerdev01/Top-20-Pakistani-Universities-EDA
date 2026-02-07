@echo off
echo ==========================================
echo   University Quantum Command - Launcher
echo ==========================================
echo.
echo [1/3] Navigating to project frequency...
cd University-Quantum-Command

echo [2/3] Installing hyper-dependencies...
call npm install
if %ERRORLEVEL% NEQ 0 (
    echo Error installing dependencies.
    pause
    exit /b %ERRORLEVEL%
)

echo [3/3] Igniting thrusters (Dev Server)...
npm run dev

pause
