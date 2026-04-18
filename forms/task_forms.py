from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from models.task import TaskStatus

class TaskForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    description = TextAreaField('Descrição')
    status = SelectField(
        'Status', 
        choices=[(status.name, status.value) for status in TaskStatus],
        validators=[DataRequired()]
    )
    submit = SubmitField('Salvar Tarefa')
