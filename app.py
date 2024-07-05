from flask import Flask, request, jsonify, render_template, send_file
from utils.pix import generate_pix_qr_code
from database.raffle_db import init_db, save_raffle
import random
import io

app = Flask(__name__)

available_tickets = list(range(1, 101))  # 100 bilhetes disponíveis
purchased_tickets = {}  # Dicionário para rastrear os bilhetes comprados por email
tickets = []

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/raffle/buy', methods=['POST'])

def buy_raffle():
    data = request.get_json()
    name = data['name']
    email = data['email']
    quantity = int(data['quantity'])

    if email in purchased_tickets:
        total_tickets = purchased_tickets[email] + quantity
    else:
        total_tickets = quantity

    if total_tickets > 10:
        return jsonify({'error': 'Máximo de 10 bilhetes por pessoa.'}), 400
    
    if len(available_tickets) == 0:
        return jsonify({'error': 'Todos os bilhetes foram vendidos.'}), 400
    
    tickets = []
    for _ in range(quantity):
        if len(available_tickets) == 0:
            return jsonify({'error': 'Todos os bilhetes foram vendidos.'}), 400
        random_ticket = pick_random_ticket()
        tickets.append(random_ticket)
        actual_ticket = random_ticket

    purchased_tickets[email] = total_tickets
    save_raffle(name, email, tickets)

    # Gerar QR Code Pix
    qr = generate_pix_qr_code()
    
    img_byte_arr = io.BytesIO()
    qr.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return jsonify({'ticket': str(actual_ticket), 'ticketCount': len(available_tickets), 'qr_code': img_byte_arr.read().decode('ISO-8859-1')})

    #return send_file(img_byte_arr, mimetype='image/png')

def pick_random_ticket():
    global available_tickets
    if len(available_tickets) > 0:
        random_ticket = random.choice(available_tickets)
        available_tickets.remove(random_ticket)
        return random_ticket
    return None

if __name__ == '__main__':
    app.run(debug=True)
