from src.instabot import InstaBot

def init(to_send):
    InstaBot(to_send)
    input("DONE")

if __name__ == "__main__":
    to_send = {'flyser' : False, 'message' : True}
    init(to_send)
