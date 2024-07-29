from flask import Flask, request, render_template
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visits.db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15))
    timestamp = db.Column(db.String(19))
    user_agent = db.Column(db.String(255))
    qr_value = db.Column(db.String(3))

@app.route('/', methods=['GET'])
def record_visit():
    db.create_all()
    qr_value  = request.args.get('qr')

    new_visit = Visit(ip_address=request.remote_addr, 
                      timestamp=datetime.datetime.now().strftime("%m-%d-%Y %H:%M"),
                      user_agent=request.user_agent.string, qr_value=qr_value)
    db.session.add(new_visit)
    db.session.commit()

    return render_template('index.html')
    
@app.route('/view_visits')
def view_visits():
    user_value  = request.args.get('user')
    key_value  = request.args.get('key')
    visits_output = ""
    
    if user_value == 'alteredminds' and key_value == 'uQzWNTR5r2DrR5ddCjkS5py09frfkVczwZ0am1CgaxHe2bveABHtE':
        query = db.session.query(Visit).all()
        for visit in query:
            visits_output += f'<p><b>Timestamp:</b> {visit.timestamp}, <b>IP Address:</b> {visit.ip_address}, <b>User-Agent:</b> {visit.user_agent}, <b>QR Value:</b> {visit.qr_value}</p>'
        return visits_output
    else:
        return ('Access Denied')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)