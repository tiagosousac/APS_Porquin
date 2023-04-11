# application/frontend/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, DateField

from wtforms.validators import DataRequired, Email

'''
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class OrderItemForm(FlaskForm):
    product_id = HiddenField(validators=[DataRequired()])
    quantity = IntegerField(validators=[DataRequired()])
    order_id = HiddenField()
    submit = SubmitField('Update')


class ItemForm(FlaskForm):
    product_id = HiddenField(validators=[DataRequired()])
    quantity = HiddenField(validators=[DataRequired()], default=1)
'''
class OrcamentoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    mes = DateField('Mês', validators=[DataRequired()])
    valor_maximo = IntegerField('Valor do Orçamento', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Orçamento')