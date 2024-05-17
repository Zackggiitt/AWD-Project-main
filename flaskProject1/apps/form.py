import wtforms
from wtforms.validators import Email, DataRequired, Length


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(), Length(min=3, max=25)])
    password = wtforms.PasswordField(validators=[DataRequired()])
    checkbox = wtforms.BooleanField(label='Remember Me')
