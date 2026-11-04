from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Paciente

bp_pacientes = Blueprint('bp_pacientes', __name__)


@bp_pacientes.route('/')
def index():
    pacientes = Paciente.query.all()
    return render_template('pacientes/index.html', pacientes=pacientes)


@bp_pacientes.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nuevo_paciente = Paciente(nombre=request.form['nombre'],
                                  telefono=request.form['telefono'])
        db.session.add(nuevo_paciente)
        db.session.commit()
        flash('Paciente registrado correctamente', 'success')
        return redirect(url_for('bp_pacientes.index'))
    return render_template('pacientes/crear.html', paciente=None)


@bp_pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    paciente = db.get_or_404(Paciente, id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.telefono = request.form['telefono']
        db.session.commit()
        flash('Paciente actualizado correctamente', 'info')
        return redirect(url_for('bp_pacientes.index'))
    return render_template('pacientes/crear.html', paciente=paciente)


@bp_pacientes.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    paciente = db.get_or_404(Paciente, id)
    for cita in list(paciente.citas):
        db.session.delete(cita)
    db.session.delete(paciente)
    db.session.commit()
    flash('Paciente eliminado', 'danger')
    return redirect(url_for('bp_pacientes.index'))
