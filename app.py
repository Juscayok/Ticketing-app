from flask import Flask, render_template, request, redirect, url_for, session, send_file
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Load tickets from file if exists
try:
    with open('tickets.json', 'r') as f:
        tickets = json.load(f)
except FileNotFoundError:
    tickets = []

# Dummy user for login
USER = {'username': 'admin', 'password': 'pass123'}

@app.route('/')
def index():
    query = request.args.get('query', '').lower()
    status_filter = request.args.get('status', 'all')
    
    filtered = tickets
    if query:
        filtered = [t for t in filtered if query in t['description'].lower() or query in t['category'].lower()]
    if status_filter != 'all':
        filtered = [t for t in filtered if t['status'] == status_filter]
        
    return render_template('index.html', tickets=filtered, current_status=status_filter)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        ticket = {
            'id': len(tickets) + 1,
            'submitted_by': request.form['name'],
            'category': request.form['category'],
            'description': request.form['description'],
            'priority': request.form['priority'],
            'status': 'Open',
            'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'resolution_notes': '',
            'last_updated': '',
            'work_logs': []
        }
        tickets.append(ticket)
        save_tickets()
        return redirect(url_for('index'))
    return render_template('submit.html')

@app.route('/ticket/<int:ticket_id>')
def ticket_detail(ticket_id):
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    return render_template('ticket.html', ticket=ticket)

@app.route('/ticket/<int:ticket_id>/update', methods=['POST'])
def update_ticket(ticket_id):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket['status'] = request.form['status']
            ticket['resolution_notes'] = request.form['notes']
            ticket['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')
            break
    save_tickets()
    return redirect(url_for('ticket_detail', ticket_id=ticket_id))

@app.route('/ticket/<int:ticket_id>/delete', methods=['POST'])
def delete_ticket(ticket_id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    global tickets
    tickets = [t for t in tickets if t['id'] != ticket_id]
    save_tickets()
    return redirect(url_for('index'))

@app.route('/ticket/<int:ticket_id>/add_work_log', methods=['POST'])
def add_work_log(ticket_id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    work_log = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'entry': request.form['work_log_entry'],
        'logged_by': session.get('username', 'admin')
    }
    
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            if 'work_logs' not in ticket:
                ticket['work_logs'] = []
            ticket['work_logs'].append(work_log)
            ticket['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')
            break
            
    save_tickets()
    return redirect(url_for('ticket_detail', ticket_id=ticket_id))

@app.route('/export')
def export_tickets():
    save_tickets()
    return send_file('tickets.json',
                    mimetype='application/json',
                    as_attachment=True,
                    download_name='tickets.json')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USER['username'] and request.form['password'] == USER['password']:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

def save_tickets():
    with open('tickets.json', 'w') as f:
        json.dump(tickets, f, indent=2)

if __name__ == '__main__':
    app.run(debug=True)