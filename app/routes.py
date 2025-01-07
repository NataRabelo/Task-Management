from flask import Blueprint, render_template, flash, redirect, url_for
from app import db
from app.models import Task
from app.forms import TaskForm

bp = Blueprint('routes', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully')
        return redirect(url_for('routes.index'))
    return render_template('add_task.html', form=form)
