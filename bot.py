from rivescript import RiveScript
from sqlalchemy import create_engine
import os
db = create_engine(os.getenv('DATABASE_URL'))
bot = RiveScript(utf8=True)

bot.load_directory("brain")
bot.sort_replies()


def chat(message):
    if message == "":
        return "No message found "
    else:
        responce = bot.reply("user", message)
    if responce:
        return responce
    else:
        return "No responce found"

def reload():
    bot.clear_uservars()
    query2 = "DELETE FROM internSelection"
    db.engine.execute(query2)
    query2 = "DELETE FROM jobSelection"
    db.engine.execute(query2)

def set_bot(user, data):
    bot.set_uservars(user, data)

def get_bot(user):
    return bot.get_uservars(user)