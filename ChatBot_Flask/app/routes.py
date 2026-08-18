from flask import *
from model.model import Bot
import os

app = Flask(__name__)
bot = Bot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    try:
        p = os.path.join(os.path.dirname(__file__), '../data/academic_persona_chat.json')
        bot.train(p)
        return {'status': 'ok', 'msg': 'trainok'}
    except Exception as e:
        return {'status': 'error', 'msg': str(e)}

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get('message', '')
    r = bot.chat(msg)
    return {'response': r}