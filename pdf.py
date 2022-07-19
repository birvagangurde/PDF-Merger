# installed PyPDF2
# created a pdfmerger------------------------------
import PyPDF2
import sys

inputs = sys.argv[1:] #including as many pdfs as we want 
# displayed all the inputs beforehand 2----------------------------------------
# def pdf_combiner(pdf_list):
# 	for pdf in pdf_list:
# 		print(pdf)

# pdf_combiner(inputs)



def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

pdf_combiner(inputs)
















# installed PyPDF2
# 1st part----------------------------------------------------------------------
"""
with open('dummy.pdf', 'rb') as file:
	# rb is read binary
	reader = PyPDF2.PdfFileReader(file)
	page= reader.getPage(0)
	page.rotateCounterClockwise(90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)
	# print(reader.getPage(0))

"""














"""

import PyPDF2

with open('dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	print(page.rotateCounterClockwise(90))
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)
"""