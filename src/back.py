from src.instabot import InstaBot

def call_back(arg):
    insta_bot = InstaBot(arg)
    if arg['type'] in ['message', 'file']:
        insta_bot.run_message()    
    if arg['type'] == 'video':
        insta_bot.run_video()

