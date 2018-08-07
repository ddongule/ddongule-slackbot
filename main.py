from rtmbot import RtmBot
from rtmbot.core import Plugin

class HelloPlugin(Plugin):
    # def process_messanger(self, data):
    # print(data)
    def process_messanger(self, data):
        if "민경" in data["text"]:
            self.outputs.append([data["channel"], "불렀어?"])


config = {
    "SLACK_TOKEN": "xoxb-...",
    "ACTIVE_PLUGINS" : [main.HelloPlugin]
}

bot = RtmBot(config)
bot.start()

print ("Hello, ddongule(>.<)!")
print("What's wrong?")
print("오늘은 도시락메뉴 무엇? >.<")
print("hi")
