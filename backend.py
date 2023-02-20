import time
import webbrowser
from fpdf import FPDF
import os


class PDFReport:
	def __init__(self, **kwargs):
		self.pdf = FPDF()
		self.pdf.add_page()

		self.pdf.image('misc_files/house.png', w=30, h=30)

		self.pdf.set_font('Arial', 'B', 24)
		self.pdf.cell(40, 10, txt=f"Flatmates Bill", ln=3)
		for value in kwargs.values():
			for index, lv in enumerate(value):
				self.pdf.set_font('Helvetica', 'B', 12)
				self.pdf.cell(40, 10, f"Person {int(index) + 1} Amount: ", border=True)
				self.pdf.cell(40, 10, txt=str(round(float(value[index]), 2)), border=True, ln=1)

		self.pdf.cell(40, 10, txt=f"Billed at {time.strftime('%H:%M:%S - %d/%m%Y')}.")

		os.chdir('misc_files')
		self.pdf.output("report.pdf")
		webbrowser.open('report.pdf')


class Bill:
	def __init__(self, amount):
		self.amount = amount

	def calc_amount(self, **kwargs):
		person_list = []
		for value in kwargs.values():
			if value:
				if type(value) == list:
					for index, lv in enumerate(value):
						int_value = float(value[index] / sum(value) * self.amount)
						person_list.append(str(int_value))
				else:
					int_value = value / 30 * self.amount
					person_list.append(int_value)
		return person_list
