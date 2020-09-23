# this will get a random choice from each list
from random import choice
# list what reccommendations the bot has for user input
def get_bot_reccommend(response):

    bot_reccommend_mellow = ["You probably want to listen to mellow vibes for this weather.", "Maybe listen to some Instrumental Blues music.", "Chillhop is a great playlist option for this!", "Nature sounds are quite peaceful."]
    bot_reccommend_bright = ["You probably want to listen to some bright happy vibes, its a great day!", "Come on, you know you want to listen to some Disney music.", "Some fun Pop music would be great!", "Just play He-Man singing 'What's goin on' on repeat."]
    bot_reccommend_edgy = ["You def need something edgy for this, I mean look outside!", "I reccommend some Rock music.", "Electro is a must for this kind of weather.", "Listen to a little metal. Not too much tho."]

    if response in ["snow", "snowy", "nice", "rainy", "foggy", "calm"]:
        return choice(bot_reccommend_mellow)
    elif response in ["sunny", "crisp", "breezy", "clear", "great", "warm"]:
        return choice(bot_reccommend_bright)
    elif response in ["windy", "freezing", "cloudy", "bad", "stormy", "hail"]:
        return choice(bot_reccommend_edgy)
    else:
        return "For that, i dont have a playlist reccommendation. Youre on your own, sorry."

print("This program's going to reccommend music based off the weather, to meet all your vibin needs.")
print("It's got a reccomendation for almost anything, from sunny to freezing.")
print("Whenever you're finished with the program, just type 'done'.")
# this is the loop to make sure it'll ask a lot so i dont have to run it a lot
# itll also show everything that repeats: the question, user response, and the bot reccomendation
while True:

    response = input("So whats the weather? ")

    if response == "done":
        break

    print(f"Oh dang it's {response}?")

    bot_reccommend = get_bot_reccommend(response)
    print(bot_reccommend)

