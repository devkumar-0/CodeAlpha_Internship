#Basic chatbot
def bot():
    print("Chat with bot..")
    while True:
        a = input("-->")
        if a in ["hello", "Hello", 'hi', 'Hi']:
            print("Hi!")
        elif a in ["how are you", 'How are you']:
            print("I\'m fine, thanks!")
        elif a in ["bye", 'Bye']:
            print("Goodbye!")
            break
        else:
            print("yet to develop more")
bot()
