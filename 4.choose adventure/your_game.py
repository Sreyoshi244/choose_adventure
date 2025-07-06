import pyttsx3
import pygame
import random
import time
import os

# -------- Voice Setup --------
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# -------- Sound System Setup --------
pygame.mixer.init()

def play_music(file, loop=True):
    path = os.path.join("sounds", file)
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1 if loop else 0)
    except Exception as e:
        speak(f"Background music error: {str(e)}")

def stop_music():
    pygame.mixer.music.stop()

def play_sound_effect(file):
    path = os.path.join("sounds", file)
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"{path} not found.")
        effect = pygame.mixer.Sound(path)
        effect.play()
    except Exception as e:
        speak(f"Sound effect error: {str(e)}")

# -------- Story Segments --------
def river_event():
    outcome = random.choice(["safe", "gator"])
    if outcome == "safe":
        speak("You swim across safely and feel refreshed.")
        play_sound_effect("splash.wav")
    else:
        speak("Suddenly, a wild alligator leaps at you!")
        play_sound_effect("alligator.wav")
        time.sleep(1)
        speak("Game over.")

def left_path():
    answer = input("You reach a river. Do you walk around or swim across? (walk/swim): ").lower()
    if answer == "swim":
        river_event()
    elif answer == "walk":
        speak("You start walking along the river...")
        time.sleep(1)
        play_sound_effect("dry-wind.wav")
        speak("After hours, you collapse from exhaustion. Game over.")
    else:
        speak("Not a valid option. You lose.")

def right_path():
    speak("You approach a rickety old bridge.")
    play_sound_effect("bridge-creak.wav")
    answer = input("Do you want to cross it or head back? (cross/back): ").lower()
    if answer == "back":
        speak("You go back and give up. Game over.")
    elif answer == "cross":
        speak("You bravely cross the bridge...")
        time.sleep(1)
        stranger = input("You meet a mysterious stranger. Talk to them? (yes/no): ").lower()
        if stranger == "yes":
            speak("The stranger smiles and hands you a bag of gold!")
            play_sound_effect("gold.wav")
            speak("Congratulations, you win!")
        elif stranger == "no":
            speak("The stranger disappears in smoke. You lose.")
        else:
            speak("Not a valid option. You lose.")
    else:
        speak("Not a valid option. You lose.")

# -------- Game Loop --------
def play_game():
    name = input("Enter your name: ")
    speak(f"Welcome, {name}, to your adventure!")

    play_music("spooky_forest.wav")

    while True:
        answer = input("You’re at a dirt road. Go left or right? (left/right): ").lower()

        if answer == "left":
            left_path()
        elif answer == "right":
            right_path()
        else:
            speak("Not a valid option. You lose.")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            stop_music()
            speak(f"Thanks for playing, {name}! Farewell, adventurer.")
            break

play_game()