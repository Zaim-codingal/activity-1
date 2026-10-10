print("Hello! I am an AI chatbot")
name=input("What is your name? ")
print("Nice to meet you, " + name + "! How are you today?")
mood=input("Please tell me your mood (happy, sad, excited, etc.): ")
if mood.lower() == "happy":
    print("That's great to hear! Keep smiling!")
elif mood.lower() == "sad":
    print("I'm sorry to hear that. Remember, it's okay to feel sad sometimes. Take care of yourself!")
elif mood.lower() == "excited":
    print("Wow! That's awesome! Enjoy your excitement and make the most of it!")
else:
    print("Thank you for sharing your mood with me. I hope you have a wonderful day!")