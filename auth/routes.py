from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from auth import auth_bp
from forms.auth_forms import LoginForm, RegistrationForm
from services.auth_service import register_user, authenticate_user

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        user = register_user(form.username.data, form.password.data)
        flash('Registro completo! Faça o login agora.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate_user(form.username.data, form.password.data)
        if user:
            login_user(user)
            flash(f'Bem-vindo, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('tasks.index'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')
            
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('auth.login'))
