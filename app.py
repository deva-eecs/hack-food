from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secret key for form security

class DonationForm(FlaskForm):
    donor_name = StringField('Donor Name', validators=[DataRequired()])
    food_type = StringField('Food Type', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    expiration_date = StringField('Expiration Date', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Submit Donation')

class ReceiverRequestForm(FlaskForm):
    receiver_name = StringField('Receiver Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Submit Request')

food_donations = []
receiver_requests = []

@app.route('/')
def home():
    return render_template('index.html', donations=food_donations, requests=receiver_requests)

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        donation = {
            'donor_name': form.donor_name.data,
            'food_type': form.food_type.data,
            'quantity': form.quantity.data,
            'expiration_date': form.expiration_date.data,
            'location': form.location.data
        }
        food_donations.append(donation)
        return redirect(url_for('home'))
    return render_template('donate.html', form=form)

@app.route('/request', methods=['GET', 'POST'])
def request_food():
    form = ReceiverRequestForm()
    if form.validate_on_submit():
        request_data = {
            'receiver_name': form.receiver_name.data,
            'location': form.location.data
        }
        receiver_requests.append(request_data)
        return redirect(url_for('home'))
    return render_template('request_food.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
