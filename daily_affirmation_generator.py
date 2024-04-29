print("Daily Affirmation Generator 🤩: ", "\n")

# Greeting based on name
name = input("What is your name?: ")
if name == "Emma" or name == "emma":
    print("Hi, Emma!🌼")
elif name == "Jack" or name == "jack":
    print("Hi, Jack!🎉")
elif name == "Anna" or name == "anna":
    print("Hi, Anna!🌸")
elif name == "Alex" or name == "alex":
    print("Hi, Alex! 🐶")
else:
    print("Hi, stranger! 🌼")

# Daily Affirmation based on day
day = input("What day is it today?: ")
if day == "Monday" or day == "monday":
    print("\033[3m", "It's the start of the week, you can do it! 🌼", "\033[0m")
elif day == "Tuesday" or day == "tuesday":
    print("\033[3m", "It's Tuesday, you can do it! 🎉 ", "\033[0m")
elif day == "Wednesday" or day == "wednesday":
    print("\033[3m", "It's  Wednesday,  you are a magnet for positive thoughts and good deeds! 🧘", "\033[0m")
elif day == "Thursday" or day == "thursday":
    print("\033[3m", "It's Thursday, you have the power to bring all your dreams into reality! 🌙", "\033[0m")
elif day == "Friday" or day == "friday":
    print("\033[3m", "It's Friday, you are ready to rock this day! 🎶 ", "\033[0m")
elif day == "Saturday" or day == "saturday":
    print("\033[3m", "It's Saturday, you have a ton of reasons to smile today! 😄", "\033[0m")
else:
    print("\033[3m", "It's SUNDAY!! Today is a good day to be the best version of yourself. 💖", "\033[0m")

# Affirmation and compliment based on emotion and favorite color
emotion = input("How are you feeling today?🤗: ")
if emotion == "good" or emotion == "Good":
    print("\033[3m", "Today's affirmation: I'm going to have a great day.🌼", "\033[0m")
    faveColor = input("What is your favorite color 🌈? : ")
    if faveColor == "purple" or faveColor == "Purple":
        print("\033[35m", "You are a creative person.", "\033[0m")
    elif faveColor == "pink" or faveColor == "Pink":
        print("\033[95m", "You are a wonderful person.", "\033[0m")
    elif faveColor == "blue" or faveColor == "Blue":
        print("\033[34m", "You are a smart person.", "\033[0m")
    elif faveColor == "green" or faveColor == "Green":
        print("\033[32m", "You are an optimistic person.", "\033[0m")
    elif faveColor == "black" or faveColor == "Black":
        print("\033[30m", "You are a strong person.", "\033[0m")
    else:
        print("\033[32m", "Reach for the stars!! ✨", "\033[0m")
elif emotion == "bad" or emotion == "Bad":
    print("\033[3m", "Today's affirmation: I look forward to tomorrow and the opportunities that await me 🐉", "\033[0m")
    faveColor = input("What is your favorite color 🌈? : ")
    if faveColor == "purple" or faveColor == "Purple":
        print("\033[35m", "You are a creative person.", "\033[0m")
    elif faveColor == "pink" or faveColor == "Pink":
        print("\033[95m", "You are a wonderful person.", "\033[0m")
    elif faveColor == "blue" or faveColor == "Blue":
        print("\033[34m", "You are a smart person.", "\033[0m")
    elif faveColor == "green" or faveColor == "Green":
        print("\033[32m", "You are an optimistic person.", "\033[0m")
    elif faveColor == "black" or faveColor == "Black":
        print("\033[30m", "You are a strong person.", "\033[0m")
    else:
        print("\033[32m", "Reach for the stars!! ✨", "\033[0m")
else:
    print("\033[3m", "Today's affirmation: I welcome what is, I welcome what comes. ☄️")
    faveColor = input("What is your favorite color 🌈? : ")
    if faveColor == "purple" or faveColor == "Purple":
        print("\033[35m", "You are a creative person.", "\033[0m")
    elif faveColor == "pink" or faveColor == "Pink":
        print("\033[95m", "You are a wonderful person.", "\033[0m")
    elif faveColor == "blue" or faveColor == "Blue":
        print("\033[34m", "You are a smart person.", "\033[0m")
    elif faveColor == "green" or faveColor == "Green":
        print("\033[32m", "You are an optimistic person.", "\033[0m")
    elif faveColor == "black" or faveColor == "Black":
        print("\033[30m", "You are a strong person.", "\033[0m")
    else:
        print("\033[32m", "Reach for the stars!! ✨", "\033[0m")

