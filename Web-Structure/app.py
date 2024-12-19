from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__, static_folder='public', template_folder='templates')
app.secret_key = 'your-secret-key'

# JSON file path
JSON_FILE = './Web-Stucture/database/data.json'

def load_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_item = {
            'id': len(load_data()) + 1,
            'name': request.form['name'],
            'description': request.form['description']
        }
        data = load_data()
        data.append(new_item)
        save_data(data)
        flash('Data added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    data = load_data()
    item = next((item for item in data if item['id'] == id), None)
    
    if request.method == 'POST':
        item['name'] = request.form['name']
        item['description'] = request.form['description']
        save_data(data)
        flash('Data updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    data = load_data()
    data = [item for item in data if item['id'] != id]
    save_data(data)
    flash('Data deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
