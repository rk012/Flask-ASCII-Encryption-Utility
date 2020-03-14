from flask import Flask, request, session, redirect, url_for, render_template
from ascii_encryptor import encrypt, decrypt

import random

GENERATOR=3
MODULUS=15485863

app = Flask(__name__)

app.secret_key = b'84bvf85hf84uhfeu'

@app.route('/')
def index():
    return redirect(url_for('keygen'))

@app.route('/keygen', methods=['GET', 'POST'])
def keygen():
    if 'SHARED_KEY' in session:
        return redirect(url_for('start_index'))
    
    if 'PRIVATE_KEY' not in session:
        session['PRIVATE_KEY'] = random.randint(1, 1000000)
        
    if request.method == 'POST':
        session['SHARED_KEY'] = (int(request.form['PUBLIC_KEY'])**session['PRIVATE_KEY'])%MODULUS
        return redirect(url_for('start'))
    else:
        return render_template('keygen.html', key=(GENERATOR**session['PRIVATE_KEY'])%MODULUS)
    
@app.route('/start', methods=['GET', 'POST'])
def start():
    if 'SHARED_KEY' not in session:
        return redirect(url_for('keygen'))

    if request.method == 'POST':
        if 'message' in request.form:
            return render_template('start.html', message=encrypt(session['SHARED_KEY'], request.form['message']))
        else:
            return render_template('start.html', message=decrypt(session['SHARED_KEY'], request.form['encrypted_message']))
    else:
        return render_template('start.html')

@app.route('/encrypt')
def encrypt_message():
    if 'SHARED_KEY' not in session:
        return redirect(url_for('keygen'))
    else:
        return render_template('encrypt.html')

@app.route('/decrypt')
def decrypt_message():
    if 'SHARED_KEY' not in session:
        return redirect(url_for('keygen'))
    else:
        return render_template('decrypt.html')

@app.route('/newkeygen')
def newkeygen():
    session.pop('SHARED_KEY', None)
    session.pop('PRIVATE_KEY', None)
    return redirect(url_for('keygen'))

app.run(host='0.0.0.0', port=80)
