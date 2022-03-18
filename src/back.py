from src.instabot import InstaBot

def call_back(arg):
    insta_bot = InstaBot(arg)
    if type in ['message', 'file']:
        insta_bot.run_message()    
    if type == 'video':
        insta_bot.run_video()

