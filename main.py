from flask import Flask, request, session, redirect, url_for, render_template
from ascii_encryptor import encrypt, decrypt

import random

GENERATOR=3
MODULUS=15485863

app = Flask(__name__)

app.secret_key = b'84bvf85hf84uhfeu'

@app.route('/')
def index():
    return redirect(url_for('keygen', key=''))

@app.route('/keygen')
def keygen():
    if 'SHARED_KEY' in session:
        return redirect(url_for('start_index'))
    
    if 'PRIVATE_KEY' not in session:
        session['PRIVATE_KEY'] = random.randint(1, 1000000)
        
    if request.args['key'] == '':
        return render_template('keygen.html', key=(GENERATOR**session['PRIVATE_KEY'])%MODULUS)
    else:
        session['SHARED_KEY'] = (int(request.args['key'])**session['PRIVATE_KEY'])%MODULUS
        return redirect(url_for('start_index'))
    
@app.route('/start/')
def start_index():
    if 'SHARED_KEY' not in session:
        return redirect(url_for('keygen', key=''))
    else:
        return render_template('encryptor.html')

@app.route('/start/encrypt')
def encrypt_message():
    if 'SHARED_KEY' not in session:
        return redirect(url_for('keygen', key=''))
    else:
        return encrypt(session['SHARED_KEY'], request.args['message'])

@app.route('/start/decrypt')
def decrypt_message():
    if 'SHARED_KEY' not in session:
        return redirect(url_for('keygen', key=''))
    else:
        return decrypt(session['SHARED_KEY'], request.args['message'])
    

 app.run(host='0.0.0.0', port=8080)
