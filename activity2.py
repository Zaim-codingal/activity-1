print("Hello, what is your name?")
name = input("I'm: ")
print("Nice to meet you, " + name + "! How are you feeling today?")
mood = input("im feeling (happy, sad, etc): ")
if mood.lower() == "happy":
    print("nice! tell me about it.")
elif mood.lower() == "sad":
    print("hope you get better soon")
elif mood.lower() == "bored":
    print("you want to play something?")
else:
    print("alright then")
weather = input("hows the weather out there?")
if weather.lower() == "sunny":
    print("nice weather!")
if weather.lower() == "cold":
    print("go have some coffee")
if weather.lower() == "rainy":
    print("has to clear up soon then!")