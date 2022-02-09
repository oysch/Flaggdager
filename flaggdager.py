import smtplib
from datetime import date, datetime, timedelta
from dateutil.easter import *

from apscheduler.schedulers.blocking import BlockingScheduler
from email.mime.text import MIMEText

# apschedulers
sched = BlockingScheduler()
email_user = 'offisiell.flaggdag@gmail.com'
server = smtplib.SMTP ('smtp.gmail.com', 587)
#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.starttls()
server.login(email_user, 'top_secret_password')

# email.mime
text_type = 'plain' # or 'html'
mottakere = 'epost1@epost.com, epost2@epost.com'

# Calculate the date of easter
aar = datetime.today().year
forste_paskedag = easter(aar)
forste_pinsedag = forste_paskedag + timedelta(days=49)

def send_email(subject, text):
    #EMAIL
    text = text
    msg = MIMEText(text, text_type, 'utf-8')
    msg['Subject'] = subject
    msg['From'] = email_user
    msg['To'] = mottakere
    server.send_message(msg)

def sjekk_om_flaggdag(dagens_dato):

    if f"{aar}-01-01"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("1. nyttaarsdag", "1. nyttaarsdag - 1. januar")

    if f"{aar}-01-21"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Prinsesse Ingrid Alexandra", "Prinsesse Ingrid Alexandra - 21. januar")

    if f"{aar}-02-26"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Kong Harald V", "Kong Harald V - 21. februar")

    if f"{forste_paskedag}"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - 1. paaskedag", "1. paaskedag - 17. april")

    if f"{aar}-05-01"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Den internasjonale arbeiderdagen", "Den internasjonale arbeiderdagen - 1. mai")

    if f"{aar}-5-8"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Frigjoringsdagen 1945", "Frigjoringsdagen 1945 - 8. mai")

    if f"{aar}-05-17"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Grunnlovsdagen", "Flaggdag - Grunnlovsdagen - 17. mai")

    if f"{forste_pinsedag}"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - 1. pinsedag", "Flaggdag - 1. pinsedag - 5. Juni")

    if f"{aar}-06-07"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Unionsopplosningen 1905", "Unionsopplosningen 1905 - 7. juni")

    if f"{aar}-07-04"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Dronning Sonja", "Dronning Sonja - 4. juli")

    if f"{aar}-07-20"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Kronprins Haakon", "Kronprins Haakon - 20. juli")

    if f"{aar}-07-29"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Olsokdagen", "Olsokdagen - 29. juli")

    if f"{aar}-08-19"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - Kronprinsesse Mette-Marit", "Kronprinsesse Mette-Marit - 19. august")

    if f"{aar}-12-25"==dagens_dato.strftime("%Y-%m-%d"):
        send_email("Flaggdag - 1. juledag", "1. juledag - 25. desember")

# The job will be executed if defined date is date today
sched.add_job(sjekk_om_flaggdag, 'date', args=[date.today()])

#sched.add_job(send_email)
sched.start()