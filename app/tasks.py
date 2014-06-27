from __future__ import absolute_import

from app.celery import app
from app.send_mail import send

@app.task
def send_mail( target_email, subject, message ):
  try:
    send(target_email,subject, subject)
  except Exception, e:
    print "error"
    print e
    return False
  finally:
    pass
  return True
