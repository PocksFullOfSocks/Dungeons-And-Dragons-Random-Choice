import classes
import races
import backgrounds
import random
import pyperclip


def greeting():
    # loop until works
    while True:
        get_started = input(
            "Hello, and welcome to DRC (D&D Random Choice)! \n Lets get started, shall we? \n y/n>:")
        if get_started == "y":
            print("This program will provide a random background, class, and race option for you.")
            break
        elif get_started == "n":
            print("Sorry, I guess you don't want my super cool, random and quirky stuff!")
            break
        else:
            print("Sorry that's an invalid answer.")


def user_background_choice():
    while True:
        user_input = input(
            "Are there any main backgrounds you don't want to play?\n y/n>:")
        if user_input == "y":
            unwanted_backgrounds = input("Okay list them comma separated please.\n")
            print("So, you don't want to play " + unwanted_backgrounds + ".")
            background_list = [x for x in backgrounds.total_backgrounds if x not in unwanted_backgrounds]
            random_background_choice = random.choice(background_list)
            print("The background you should play is " + random_background_choice + '.')
            return random_background_choice
        elif user_input == "n":
            random_background_choice = random.choice(backgrounds.total_backgrounds)
            print("The background you should play is " + random_background_choice + '.')
            return random_background_choice
        else:
            print("Sorry that's an invalid answer.")


def user_class_choice():
    while True:
        user_input = input(
            "Are there any main classes you don't want to play?\n y/n>:")
        if user_input == "y":
            unwanted_classes = input("Okay list them comma separated please.\n")
            print("So, you don't want to play " + unwanted_classes + ".")
            class_list = [x for x in classes.total_classes if x not in unwanted_classes]
            random_class_choice = random.choice(class_list)
            print("The class you should play is " + random_class_choice + '.')
            return random_class_choice
        elif user_input == "n":
            random_class_choice = random.choice(classes.total_classes)
            print("The class you should play is " + random_class_choice + '.')
            return random_class_choice
        else:
            print("Sorry that's an invalid answer.")


def user_race_choice():
    while True:
        user_input = input(
            "Are there any main races you don't want to play?\n y/n>:")
        if user_input == "y":
            unwanted_races = input("Okay list them comma separated please.\n")
            print("So, you don't want to play " + unwanted_races + ".")
            race_list = [x for x in races.total_races if x not in unwanted_races]
            random_race_choice = random.choice(race_list)
            print("The race you should play is " + random_race_choice + '.')
            return random_race_choice
        elif user_input == "n":
            random_race_choice = random.choice(races.total_races)
            print("The race you should play is " + random_race_choice + '.')
            return random_race_choice
        else:
            print("Sorry that's an invalid answer.")
