from flask import Blueprint

main = Blueprint('main', __name__)

from flask import request, render_template, session, flash, redirect, \
    url_for, jsonify

from .tasks import send_async_email, long_task


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    subject = "Hello From Flask"
    msgd = {'to': request.form['email'], 'subject': subject}
    # send the email
    if request.form['submit'] == 'Send':
        # send right away
        send_async_email.delay(msgd)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[msgd], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('.index'))


@main.route('/longtask', methods=['POST'])
def longtask():
    task = long_task.apply_async()
    headers = {'Location': url_for('.taskstatus', task_id=task.id)}
    return jsonify({}), 202, headers


@main.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
