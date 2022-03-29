from src.instabot import InstaBot
from src.front import run_front


def call_back(arg):
    insta_bot = InstaBot(arg)
    if type in ['message', 'file']:
        insta_bot.run_message()    
    if type == 'video':
        insta_bot.run_video()


if __name__ == "__main__":
    run_front()




