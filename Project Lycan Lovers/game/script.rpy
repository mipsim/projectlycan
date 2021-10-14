# script.rpy

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # Opening [1-12]

    mc "It is a cool October night in the city as I roam its crowded streets."

    mc "The sky is lit by the orange incandescent lights and a moon waning in the sky above me."

    mc "Noisy people walk along the paved concrete, as I sadly spend yet another Friday night alone."

    mc "Another soul lost within the big atmosphere of the downtown district."

    mc "All of my friends are out with their partners, and I can’t blame them."

    mc "Tomorrow is Halloween! Of course everyone’s gonna go out and party!"

    mc "That or they're all making last-minute costume arrangements or whatever else couples do!"

    mc "All without me…"

    mc "Maybe I should go back home and watch some horror movies…"

    mc "It would be better than just wandering aimlessly like some stooge…"

    mc "But on the other hand, the night is still young! Filled with possibility, and life!"

    mc "There might even be some hotties with bodies on the prowl!"

    jump choice_1

menu choice_1:
    mc "So what should I do?"

    "Go back home and watch some horror movies.":
        jump m_route_after_choice_1

    "Go on an adventure.":
        jump a_route_after_choice_1

label m_route_after_choice_1:
    mc "Reached M Route"

    jump end_game

label a_route_after_choice_1:
    mc "Reached A Route"

label end_game:
    return
