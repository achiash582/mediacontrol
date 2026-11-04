@echo off
chcp 65001 >nul
echo ===== MediControl: instalacion automatica =====

where python >nul 2>nul
if %errorlevel%==0 (set PY=python) else (set PY=py)

if not exist venv (
    echo Creando entorno virtual...
    %PY% -m venv venv
)

call venv\Scripts\activate.bat

echo Instalando librerias...
python -m pip install -r requirements.txt

if not exist migrations (
    echo Inicializando migraciones...
    python -m flask --app run db init
    python -m flask --app run db migrate -m "migracion inicial"
)
python -m flask --app run db upgrade

echo Insertando datos de prueba...
python seed.py

echo.
echo ===== Listo. Abre http://127.0.0.1:5000 =====
python run.py
pause
