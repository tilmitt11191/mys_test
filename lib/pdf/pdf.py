
# -*- coding: utf-8 -*-

class PDF:
	def __init__(self):
		import sys,os
		sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
		from log import Log as l
		self.log = l.getLogger()
		self.log.debug("PDF.__init__")
				
	def read_title_authors_keywords(self, by="file", var=""):
		self.log.debug("read_title_authors_keywords(by[" + by + "], var[" + var + "]) start")
		self.open_pdf_file(var)
		self.log.debug("text:\n" + self.text)

	def open_pdf_file(self, path):
		self.log.debug("open_pdf_file(path[" + path + "]) start")

		from pdfminer.pdfparser import PDFParser, PDFDocument
		from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
		from pdfminer.converter import PDFPageAggregator
		from pdfminer.layout import LAParams, LTTextBox, LTTextLine
		
		self.text = ""
		fp = open(path, 'rb')
		parser = PDFParser(fp)
		doc = PDFDocument()
		parser.set_document(doc)
		doc.set_parser(parser)
		doc.initialize('')
		rsrcmgr = PDFResourceManager()
		laparams = LAParams()
		device = PDFPageAggregator(rsrcmgr, laparams=laparams)
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		# Process each page contained in the document.
		for page in doc.get_pages():
			interpreter.process_page(page)
			layout = device.get_result()
			for lt_obj in layout:
				if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
					self.text += lt_obj.get_text()
		print(path)
		#print(doc.xrefs) #[<pdfminer.pdfparser.PDFXRef object at 0x7f53658af550>]
		print(doc.get_outlines())
		return self.text




