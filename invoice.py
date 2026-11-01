from fpdf import FPDF
import random
from datetime import datetime
def create_invoice(name, email, course, price, owner_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"{owner_name} - BRAHMA INVOICE", ln=True, align='C')
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Invoice: INV-{random.randint(10000,99999)}", ln=True)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True)
    pdf.cell(0, 10, f"Customer: {name} - {email}", ln=True)
    pdf.cell(0, 10, f"Course: {course}", ln=True)
    pdf.cell(0, 10, f"Amount: Rs.{price}", ln=True)
    filename = f"invoice_{name}.pdf"
    pdf.output(filename)
    return filename