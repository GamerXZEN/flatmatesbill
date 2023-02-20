from backend import PDFReport, Bill

if __name__ == '__main__':
	total_amount = int(input("What was your total amount: "))
	bill = Bill(total_amount)
	flatmates_no = int(input("How many people live in the flat: "))
	flatmates_list = []
	for index in range(0, flatmates_no):
		flatmate = int(input(f"How many days did each person stay: "))
		flatmates_list.append(flatmate)
	calc_list = bill.calc_amount(flatmates_list=flatmates_list)
	for index, value in enumerate(calc_list):
		print(f"Person {index + 1} Amount: {value}")
	pdf = PDFReport(flatmates_list=calc_list)
