from flask import Flask, request, redirect, url_for, render_template, session, abort
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
import re

app = Flask(__name__)
app.secret_key = "HSXEezgATXjcjXR9D9dWWFpjawDdun1gSGAuBhjAqvxh9cjp1g3Fkj3Rg8vJAaHD"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15))
    date = db.Column(db.String(10))
    time = db.Column(db.String(5))
    user_agent = db.Column(db.String(255))
    qr_value = db.Column(db.String(3))


@app.route('/', methods=['GET'])
def record_visit():
    db.create_all()
    current_time = datetime.now() - timedelta(hours=5)
    date_str = current_time.strftime("%m-%d-%Y")
    time_str = current_time.strftime("%I:%M %p")
    qr = escape(request.args.get('id'))
    
    if not re.match("^[0-9]*$", qr):
        abort(406)    

    new_visit = Visit(
        ip_address=request.headers.get('X-Forwarded-For', request.remote_addr).split(':')[0],
        date=date_str,
        time=time_str,
        user_agent=request.user_agent.string,
        qr_value=qr
    )
    db.session.add(new_visit)
    db.session.commit()

    return render_template('index.html')
    
@app.route('/adminportal', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        username = escape(request.form.get('username'))
        password = escape(request.form.get('password'))

        if not re.match("^[A-Za-z0-9]*$", username):
            return render_template('login.html', error = 'Invalid username or password')

        if username == 'alteredminds' and password == 'ce722d159038fcf981edf5be7a2f21586ba63d7cfbbd0290969a7a63bf45b815':
            session['logged_in'] = True
            try:
                visits = Visit.query.all()
                total_visits = Visit.query.count()
            except Exception:
                visits = []
                total_visits = 0
            return render_template('admin.html', visits=visits, total_visits=total_visits)
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
        
@app.route('/logout')
def logout():

    if not session.get('logged_in'):
        abort(404)

    session.pop('logged_in', None)
    return redirect(url_for('admin_page'))

@app.route('/clear_database', methods=['GET'])
def clear_database():
    key_value  = request.args.get('key')

    if not session.get('logged_in'):
        abort(404)
        
    if key_value != app.secret_key:
        abort(404)    

    try:
        db.drop_all()
        return ('Database cleared successfully')
    except Exception as e:
        return ('Database is empty')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)