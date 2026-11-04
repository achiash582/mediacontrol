from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Cita, Medico, Paciente

bp_citas = Blueprint('bp_citas', __name__)


@bp_citas.route('/')
def index():
    citas = Cita.query.order_by(Cita.fecha, Cita.hora).all()
    return render_template('citas/index.html', citas=citas)


@bp_citas.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nueva_cita = Cita(fecha=request.form['fecha'],
                          hora=request.form['hora'],
                          medico_id=int(request.form['medico_id']),
                          paciente_id=int(request.form['paciente_id']))
        db.session.add(nueva_cita)
        db.session.commit()
        flash('Cita registrada correctamente', 'success')
        return redirect(url_for('bp_citas.index'))
    return render_template('citas/crear.html', cita=None,
                           medicos=Medico.query.all(),
                           pacientes=Paciente.query.all())


@bp_citas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cita = db.get_or_404(Cita, id)
    if request.method == 'POST':
        cita.fecha = request.form['fecha']
        cita.hora = request.form['hora']
        cita.medico_id = int(request.form['medico_id'])
        cita.paciente_id = int(request.form['paciente_id'])
        db.session.commit()
        flash('Cita actualizada correctamente', 'info')
        return redirect(url_for('bp_citas.index'))
    return render_template('citas/crear.html', cita=cita,
                           medicos=Medico.query.all(),
                           pacientes=Paciente.query.all())


@bp_citas.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    cita = db.get_or_404(Cita, id)
    db.session.delete(cita)
    db.session.commit()
    flash('Cita eliminada', 'danger')
    return redirect(url_for('bp_citas.index'))
