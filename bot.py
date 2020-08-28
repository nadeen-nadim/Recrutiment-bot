from rivescript import RiveScript
from sqlalchemy import create_engine

db = create_engine('postgres://oetowqpnbuonwk:b58854c08f68596f8ca36436e93fc3e2ae5e91a77d99f054d1f27bb26e651ba8@ec2-3-216-129-140.compute-1.amazonaws.com:5432/dbhb351ushkvo3')
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