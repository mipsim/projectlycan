# script.rpy

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define tv = Character("Television")

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

    "It is a cool October night in the city as I roam its crowded streets."
    "The sky is lit by the orange incandescent lights and a moon waning in the sky above me."
    "Noisy people walk along the paved concrete, as I sadly spend yet another Friday night alone."
    "Another soul lost within the big atmosphere of the downtown district."
    "All of my friends are out with their partners, and I can’t blame them."
    "Tomorrow is Halloween! Of course everyone’s gonna go out and party!"
    "That or they're all making last-minute costume arrangements or whatever else couples do!"
    "All without me…"
    "Maybe I should go back home and watch some horror movies…"
    "It would be better than just wandering aimlessly like some stooge…"
    "But on the other hand, the night is still young! Filled with possibility, and life!"
    "There might even be some hotties with bodies on the prowl!"

    jump choice_1

menu choice_1:
    "So what should I do?"

    "Go back home and watch some horror movies.":
        jump m_route_after_choice_1

    "Go on an adventure.":
        jump a_route_after_choice_1

label m_route_after_choice_1:
    "You know… I’ve just realized..."
    "I really don’t need to go out today."
    "Going back home and watching a cheesy horror flick ain’t that bad of an idea!"

    #scene ---
    "Back at the apartment..."
    
    "A few hours have passed, the sky has gotten darker, and the lights are off in my humble abode."
    "All of them, save the glimmering light of my television screen, as it plays the end of Death Gun 4: One Last Bullet."
    "I am alone, with nothing but a comfy blanket on top of me and a big bowl of popcorn in my nervous palms."
    tv "\"No Tommy, you can’t shoot Death with his own Death Gun. Who knows what’ll happen?\""
    tv "\"If you do, the cycle of violence won’t stop! You have to end it here and now!\""
    tv "\"No, Mary. The Death Gun is nearly empty, all except for One. Last. Bullet.\""
    tv "\"And it’s got his name written all over it.\""
    tv "BANG!!!"
    "The gunshot causes me to lurch backward, throwing popcorn everywhere."
    "What a twist! I never expected Tommy to be so bold and brash! A truly gripping plot twist!"
    "As the credits roll, I grab the remote, getting ready to put on Death Gun 5: The New Reaper, when I hear a howling from outside."
    "Which is odd, to say the least… I can’t remember the last time a wolf was so close to the city…"
    "But I shrug it off. That’s someone else’s problem, not mine."
    "I grab another fistful of popcorn and press play."
    "Oh yeah. Tonight is gonna be perfect."

    jump end_game

label a_route_after_choice_1:
    "Taking in a deep breath, I continue walking along the streets, trying to find something of interest."
    "I refuse to let this wonderful night go to waste. I can always watch those movies some other time."
    "I’m already here, so why waste the opportunity?"
    "As I wander and maneuver the city streets, it just occurs to me how many different sights and sounds the nightlife has to offer."
    "The glowing of neon and cacophony of motor vehicles assault my eyes and ears until I become numb to the overstimulation."
    "That is, until one sign, in particular, catches my eye."
    "It has a neon green sign, with a cartoony drawing of an unbalanced table covered in a variety of drinks nearly spilling over."
    "The bar’s name is the Tipsy Table and a pair of descending staircases invite me to venture inside."
    "The place is humming with a certain energy to it, and the sound of a large ensemble band performing can be heard from inside."
    "Figuring that a drink may help calm my nerves and prepare me for what I expect to be one hell of a night, I make my way downwards."
    "Prepared for just about anything, I open the door."

label end_game:

    return
