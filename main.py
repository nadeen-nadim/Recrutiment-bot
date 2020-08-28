from flask import Flask, request
from flask import render_template,request,session
import bot
app = Flask(__name__)
app.secret_key = b'xxjadahcdhs\n\xec]/'
@app.route("/")
def chat():
    bot.reload()
    session['chatData'] = {'topic': 'random'}
    return render_template('chat.html')
    #while True:
       # msg = str(input('me> '))
        #print('bot> ' + bot.chat(msg))

@app.route("/get")
def get_bot_response():
    bot.set_bot("user", session['chatData'])
    msg = request.args.get('msg')
    records = bot.chat(msg)
    session['chatData'] = bot.get_bot("user")
    return records

if __name__ == "__main__":
    app.run()
        
