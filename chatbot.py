# this will get a random choice from each list
from random import choice
# list what reccommendations the bot has for user input
def get_bot_reccommend(response):

    bot_reccommend_mellow = ["You probably want to listen to mellow vibes for this weather.", "Maybe listen to some Instrumental Blues music.", "Chillhop is a great playlist option for this!"]
    bot_reccommend_bright = ["You probably want to listen to some bright happy vibes, its a great day!", "Come on, you know you want to listen to some Disney music", "Some fun Pop music would be great!"]
    bot_reccommend_edgy = ["You def need something edgy for this, I mean look outside!", "I reccommend some Rock music.","Electro is a must for this kind of weather."]

    if response in ["snowing", "rainy", "foggy"]:
        return choice(bot_reccommend_mellow)
    elif response in ["sunny", "crisp", "breezy"]:
        return choice(bot_reccommend_bright)
    elif response in ["windy", "freezing", "cloudy"]:
        return choice(bot_reccommend_edgy)
    else:
        return "For that, i dont have a playlist reccommendation. Youre on your own, sorry."

print("This program's going to tell you what mood music you need.")
# this is the loop to make sure it'll ask a lot so i dont have to run it a lot
# itll also show everything that repeats: the question, user response, and the bot reccomendation
while True:

    response = input("So whats the weather? ")

    if response == "done":
        break

    print(f"Oh dang it's {response}?")

    bot_reccommend = get_bot_reccommend(response)
    print(bot_reccommend)

