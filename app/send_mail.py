#! /usr/local/bin/python
import sys
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from django.conf import settings

def send(destination, subject, content):
  try:
    SMTPserver = settings.SMTP_SERVER
    sender =     settings.SENDER
    destination_list = [destination]

    USERNAME = settings.EMAIL_USERNAME
    PASSWORD = settings.EMAIL_PASSWORD


    # typical values for text_subtype are plain, html, xml
    text_subtype = 'html'

    #msg = MIMEText(content, text_subtype)

    msg = MIMEMultipart("alternative")
    msg.attach(MIMEText(content, "plain"))
    msg.attach(MIMEText(content, "html"))

   
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    print "Login by using smtp information"
    conn.login(USERNAME, PASSWORD)
    try:
      print "ok, prepare to send email"
      conn.sendmail(sender, destination_list, msg.as_string())
      print "ok. email is sent"
    finally:
      conn.close()

  except Exception, exc:
    sys.exit( "mail failed; %s" % str(exc) ) # give a error message