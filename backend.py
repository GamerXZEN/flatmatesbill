import time
import webbrowser
from fpdf import FPDF
import os


class PDFReport:
	def __init__(self, person1, person2, amount1, amount2):
		self.pdf = FPDF()
		self.pdf.add_page()
		try:
			self.pdf.image('misc_files/house.png', w=30, h=30)
		except:
			print("Please reload")
		self.pdf.set_font('Arial', 'B', 24)
		self.pdf.cell(40, 10, txt=f"Flatmates Bill", ln=3)
		self.pdf.set_font('Helvetica', 'B', 12)
		self.pdf.cell(70, 10, f"{person1.title()}'s Amount: ", border=True)
		self.pdf.cell(40, 10, txt=str(round(float(amount1), 2)), border=True, ln=1)
		self.pdf.cell(70, 10, f"{person2.title()}'s Amount: ", border=True)
		self.pdf.cell(40, 10, txt=str(round(float(amount2), 2)), border=True, ln=1)

		self.pdf.cell(40, 10, txt=f"Billed at {time.strftime('%H:%M:%S - %d/%m%Y')}.")

		os.chdir('misc_files')
		self.pdf.output("report.pdf")
		webbrowser.open('report.pdf')

	def get_url(self):
		return self.new_file.url


class Bill:
	def __init__(self, amount):
		self.amount = amount

	def calc_amount(self, person1, person2):
		total = person1 + person2
		person1 = person1 / total * self.amount
		person2 = person2 / total * self.amount
		return person1, person2
