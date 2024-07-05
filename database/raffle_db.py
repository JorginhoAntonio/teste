import sqlite3

def init_db():
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tickets
                 (name TEXT, email TEXT, ticket_number INTEGER)''')
    conn.commit()
    conn.close()

def save_raffle(name, email, tickets):
    conn = sqlite3.connect('raffle.db')
    c = conn.cursor()
    for ticket in tickets:
        c.execute("INSERT INTO tickets (name, email, ticket_number) VALUES (?, ?, ?)", (name, email, ticket))
    conn.commit()
    conn.close()
