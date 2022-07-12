from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    username = StringField("Your Name", validators=[InputRequired()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    address = StringField("Your Address", validators=[InputRequired()])
    submit = SubmitField("Checkout")

