from app import create_app, db
from app.models import Medico, Paciente, Cita

app = create_app()

with app.app_context():
    if Medico.query.count() > 0:
        print("Ya existen datos; no se insertó nada.")
    else:
        medicos = [
            Medico(nombre="Dr. Carlos Mendoza", especialidad="Cardiología"),
            Medico(nombre="Dra. Ana Quispe", especialidad="Pediatría"),
            Medico(nombre="Dr. Luis Fernández", especialidad="Traumatología"),
        ]
        pacientes = [
            Paciente(nombre="Juan Pérez", telefono="70123456"),
            Paciente(nombre="María Condori", telefono="71234567"),
            Paciente(nombre="Pedro Mamani", telefono="72345678"),
        ]
        db.session.add_all(medicos + pacientes)
        db.session.commit()

        citas = [
            Cita(fecha="2026-11-10", hora="09:00", medico_id=medicos[0].id, paciente_id=pacientes[0].id),
            Cita(fecha="2026-11-10", hora="10:30", medico_id=medicos[1].id, paciente_id=pacientes[1].id),
            Cita(fecha="2026-11-11", hora="15:00", medico_id=medicos[2].id, paciente_id=pacientes[2].id),
        ]
        db.session.add_all(citas)
        db.session.commit()
        print("Datos de prueba insertados correctamente")
