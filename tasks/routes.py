from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from tasks import tasks_bp
from forms.task_forms import TaskForm
from services.task_service import get_tasks_for_user, get_task_by_id, create_task, update_task, delete_task

@tasks_bp.route('/')
@login_required
def index():
    status_filter = request.args.get('status')
    tasks = get_tasks_for_user(current_user.id, status_filter)
    return render_template('tasks/list.html', tasks=tasks, current_filter=status_filter)

@tasks_bp.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        create_task(
            title=form.title.data,
            description=form.description.data,
            status_name=form.status.data,
            user_id=current_user.id
        )
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('tasks.index'))
    return render_template('tasks/form.html', form=form, action='Nova Tarefa')

@tasks_bp.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = get_task_by_id(task_id, current_user.id)
    if not task:
        abort(404)
        
    form = TaskForm()
    if request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.status.data = task.status.name
        
    if form.validate_on_submit():
        update_task(
            task_id=task_id,
            user_id=current_user.id,
            title=form.title.data,
            description=form.description.data,
            status_name=form.status.data
        )
        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('tasks.index'))
        
    return render_template('tasks/form.html', form=form, action='Editar Tarefa')

@tasks_bp.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def destroy_task(task_id):
    # O form do CSRF é garantido pelo WTF validando a request via proteção global
    if delete_task(task_id, current_user.id):
        flash('Tarefa excluída!', 'success')
    else:
        flash('Não foi possível excluir a tarefa.', 'danger')
    return redirect(url_for('tasks.index'))
