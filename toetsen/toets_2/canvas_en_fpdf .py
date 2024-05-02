# CANVAS Style
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    c = canvas.Canvas("example.pdf", pagesize=letter)
    c.drawString(100, 750, "Hello, world!")
    c.save()

create_pdf()

# FPDF style
from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Hello, world!", ln=True)
pdf.output("example.pdf")

# def volgend_factuurnummer():
#     try:
#         with open('factuurnummer.txt', 'r') as f:
#             factuurnummer = int(f.read()) + 1
#     except FileNotFoundError:
#         factuurnummer = 20240001

#     with open('factuurnummer.txt', 'w') as f:
#         f.write(str(factuurnummer))
#     return factuurnummer
# def pdf_maken():

