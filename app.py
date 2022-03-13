from src.instabot import InstaBot
from src.utils.toolbox import check_parameters

def main(args):
    insta_bot = InstaBot(args)
    if any(x in ['message', 'file'] for x in args):
        insta_bot.run_message()
    if 'video' in args:
        insta_bot.run_video()


if __name__ == "__main__":
    args = check_parameters()
    args = ['file']
    main(args)
