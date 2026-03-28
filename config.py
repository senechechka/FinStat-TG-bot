import json
from pathlib import Path

BOT_TOKEN = ''

DATA_FILE = Path(__file__).parent / 'data.json'

stats = {
    'total': 0,
    'earn': 0,
    'disearn': 0
}
transactions = []

def load_data():
    global stats, transactions
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                stats = data.get('stats', {'total': 0, 'earn': 0, 'disearn': 0})
                transactions = data.get('transactions', [])
        except (json.JSONDecodeError, IOError):
            stats = {'total': 0, 'earn': 0, 'disearn': 0}
            transactions = []
    else:
        save_data()

def save_data():
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({'stats': stats, 'transactions': transactions}, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Ошибка при сохранении данных: {e}")

def earn(amount):
    global stats, transactions
    try:
        amount = float(amount)
        stats['total'] += amount
        stats['earn'] += amount
        transactions.append(('+', amount))
        save_data()
    except ValueError:
        pass

def disearn(amount):
    global stats, transactions
    try:
        amount = float(amount)
        stats['total'] -= amount
        stats['disearn'] += amount
        transactions.append(('-', amount))
        save_data()
    except ValueError:
        pass

load_data()