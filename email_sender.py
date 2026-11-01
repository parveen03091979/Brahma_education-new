import smtplib
from email.message import EmailMessage
def send_email(from_gmail, app_pass, to_email, course, code, invoice_file):
    msg = EmailMessage()
    msg['Subject'] = f'{course} - Invoice + Code'
    msg['From'] = from_gmail
    msg['To'] = to_email
    msg.set_content(f"Course: {course}\nCode: {code}\nInvoice attached.\nTeam Brahma")
    with open(invoice_file, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=invoice_file)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_gmail, app_pass)
        smtp.send_message(msg)