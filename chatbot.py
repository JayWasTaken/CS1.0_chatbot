from random import choice

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

while True:

    response = input("So whats the weather? ")

    if response == "done":
        break

    print(f"Oh dang it's {response}?")

    bot_reccommend = get_bot_reccommend(response)
    print(bot_reccommend)

