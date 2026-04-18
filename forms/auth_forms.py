from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models.user import User

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=4, max=64)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nome de usuário já está em uso.')

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')
