# MediControl - Sistema de Gestión Médica Modular

Proyecto desarrollado en Python (Flask) utilizando arquitectura monolítica modular con Blueprints, SQLAlchemy y Bootstrap 5 (Versión a Color).

## Requisitos
- Python 3.10+

## Instrucciones de Ejecución

1. Crear e iniciar entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Inicializar base de datos y migraciones:
```bash
flask db init
flask db migrate -m "Crear tablas iniciales"
flask db upgrade
```

4. Ejecutar la aplicación:
```bash
python run.py
```

5. Abrir el navegador en `http://127.0.0.1:5000`
