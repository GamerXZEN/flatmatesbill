from wtforms.validators import DataRequired
from backend import *
from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField


app = Flask(__name__)


class HomePage(MethodView):

	def get(self):
		return render_template('index.html')


class BillFormPage(MethodView):

	def get(self):
		bill_form = BillForm()
		return render_template('bill.html', bill_form=bill_form)

	def post(self):
		bill_form = BillForm(request.form)
		amount = int(bill_form.amount.data)
		person_1_days = int(bill_form.days_in_house1.data)
		person_2_days = int(bill_form.days_in_house2.data)
		person1_name = bill_form.flatmate1.data
		person2_name = bill_form.flatmate2.data
		bill = Bill(amount)
		person1_amount, person2_amount = bill.calc_amount(person_1_days, person_2_days)
		PDFReport(person1_name, person2_name, person1_amount, person2_amount)
		result = f"{person1_name.title()} pays {person1_amount} <br> {person2_name.title()} pays {person2_amount}"
		return render_template('bill.html', bill_form=bill_form, result=result)


class BillForm(Form):
	amount = StringField('Bill Amount: ', validators=[DataRequired()])
	flatmate1 = StringField(f'Flatmate No 1: ', validators=[DataRequired()])
	days_in_house1 = StringField(f'Days in House: ', validators=[DataRequired()])
	flatmate2 = StringField(f'Flatmate No 2: ', validators=[DataRequired()])
	days_in_house2 = StringField(f'Days in House: ', validators=[DataRequired()])
	submit_button = SubmitField('Submit')


if __name__ == '__main__':
	app.add_url_rule('/', view_func=HomePage.as_view('home'))
	app.add_url_rule('/bill/', view_func=BillFormPage.as_view('bill'))
	app.run(debug=True)
