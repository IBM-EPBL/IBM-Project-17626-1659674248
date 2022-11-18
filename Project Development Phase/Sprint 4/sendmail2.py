import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


sg = sendgrid.SendGridAPIClient(api_key=('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'))
from_email = Email("roshinisri1234@gmail.com")  # Change to your verified sender

def sendgridmail(TEXT, email):
    to_email = To(email)  # Change to your recipient
    subject = "ALERT From Personal Expense Tracker Application"
    content = Content("text/plain", TEXT)
    mail = Mail(from_email, to_email, subject, content)
    
    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)