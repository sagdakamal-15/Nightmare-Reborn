


define e = Character("Anabell")


image ig:
    "bg1.jpg"
    xsize 1920
    ysize 1080
    fit "cover"


image ig2:
    "scene1.png"
    xsize 1920
    ysize 1080
    fit "cover"


label start:

    play music "audio/music.mp3"

    show ig
    show ana

    e "Hello, I am Anabell"

    e "Let's start"

    "Welcome to the haunted shop"
    "You are the security guard tonight"
    "Be careful and watch out"

    "LEVEL 1"
    "You have one minute to watch the cameras. You should notice what changed."
    jump cameras

image ig3 = "scene1ch.png"

label cameras:

    scene black
    show ig2

    "Look carefully at the doll"

    hide ig2
    show ig3

    "Something has changed!"

    menu:
        "What changed?"

        "The teddy bear color":
            e "Correct! You found the change!"
            "You survived this round!"
            return

        "The doll's dress":
            e "WRONG ANSWER!"
            "The doll is behind you..."
            "You didn't survive the night."
            "GAME OVER"
            jump start

        "The doll's hair":
            e "WRONG ANSWER!"
            "The doll is behind you..."
            "You didn't survive the night."
            "GAME OVER"
            jump start

    return