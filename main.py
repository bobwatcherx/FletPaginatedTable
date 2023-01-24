from flet import *
from paginated_dt import PaginatedDataTable
import simpledt

def main(page:Page):
	page.scroll = "auto"
	# YOU LOCATION OF CSV FILE 
	csv = simpledt.CSVDataTable("Test Data/day.csv")
	pdt = PaginatedDataTable(
		datatable = csv.datatable,
		table_title="MY DATATABLE SAMPLE",
		rows_per_page=5

		)
	# ADD BORDER TO YOU DATATABLE
	pdt.datatable.border = border.all(4,"blue")


	# YOU CAN ADD BACGORUND COLOR TO SPECIFIC DATA
	# IN DATATBALE ROWS
	# FOR EXAMPLE IF THE DATA IS / 2 == 0
	# THEN ADD COLOR TO GREEN

	for i in pdt.datarows:
		rownum = i.cells[0].content.value
		if int(rownum) %2 == 0 :
			i.color = "purple"

	# AND YOU CAN ADD ICONS INSIDE TITLE OF COLUMN
	for i in pdt.datacolumns:
		i.label = Row([
			i.label,
			Icon(name="favorite")

			])

	page.add(pdt)


flet.app(target=main)
