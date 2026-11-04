from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Medico

bp_medicos = Blueprint('bp_medicos', __name__)


@bp_medicos.route('/')
def index():
    medicos = Medico.query.all()
    return render_template('medicos/index.html', medicos=medicos)


@bp_medicos.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nuevo_medico = Medico(nombre=request.form['nombre'],
                              especialidad=request.form['especialidad'])
        db.session.add(nuevo_medico)
        db.session.commit()
        flash('Médico registrado correctamente', 'success')
        return redirect(url_for('bp_medicos.index'))
    return render_template('medicos/crear.html', medico=None)


@bp_medicos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    medico = db.get_or_404(Medico, id)
    if request.method == 'POST':
        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        db.session.commit()
        flash('Médico actualizado correctamente', 'info')
        return redirect(url_for('bp_medicos.index'))
    return render_template('medicos/crear.html', medico=medico)


@bp_medicos.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    medico = db.get_or_404(Medico, id)
    for cita in list(medico.citas):
        db.session.delete(cita)
    db.session.delete(medico)
    db.session.commit()
    flash('Médico eliminado', 'danger')
    return redirect(url_for('bp_medicos.index'))
