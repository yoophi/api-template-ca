import random
import time

from flask import current_app
from flask_mail import Message

from app.extensions import mail
from app.tasks import celery


@celery.task
def send_async_email(msgd):
    """Background task to send an email with Flask-Mail."""
    msg = Message(msgd['subject'], sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[msgd['to']])
    msg.body = 'This is a test email sent from a background Celery task.'
    mail.send(msg)


@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={
                              'current': i,
                              'total': total,
                              'status': message,
                          })
        time.sleep(1)
    return {
        'current': 100,
        'total': 100,
        'status': 'Task completed!',
        'result': 42,
    }
