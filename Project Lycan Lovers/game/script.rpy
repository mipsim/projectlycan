# script.rpy

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define tv = Character("Television")
define who = Character("???")
define whoo = Character("??? #2")
define p = Character("Prose")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Location: Street
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

    "Go back home and watch some horror movies":
        jump m_route_after_choice_1

    "Go on an adventure":
        jump a_route_after_choice_1

label m_route_after_choice_1:
    "You know… I’ve just realized..."
    "I really don’t need to go out today."
    "Going back home and watching a cheesy horror flick ain’t that bad of an idea!"

    #Location: Apartment
    #scene ---
    "{i}Back at the apartment{/i}..."
    
    "A few hours have passed, the sky has gotten darker, and the lights are off in my humble abode."
    "All of them, save the glimmering light of my television screen, as it plays the end of {i}Death Gun 4: One Last Bullet{/i}."
    "I am alone, with nothing but a comfy blanket on top of me and a big bowl of popcorn in my nervous palms."
    tv "\"No Tommy, you can’t shoot Death with his own Death Gun. Who knows what’ll happen?\""
    tv "\"If you do, the cycle of violence won’t stop! You have to end it here and now!\""
    tv "\"No, Mary. The Death Gun is nearly empty, all except for One. Last. Bullet.\""
    tv "\"And it’s got {i}his{/i} name written all over it.\""
    tv "BANG!!!"
    "The gunshot causes me to lurch backward, throwing popcorn everywhere."
    "What a twist! I never expected Tommy to be so bold and brash! A truly gripping plot twist!"
    "As the credits roll, I grab the remote, getting ready to put on {i}Death Gun 5: The New Reaper{/i}, when I hear a howling from outside."
    "Which is odd, to say the least… I can’t remember the last time a wolf was so close to the city…"
    "But I shrug it off. That’s someone {i}else’s{/i} problem, not mine."
    "I grab another fistful of popcorn and press play."
    "Oh yeah. Tonight is gonna be {i}perfect{/i}."

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

    # Location: Concert Bar
    #scene --- 

    "What greets me is an inviting, warmly lit bar scene, like something you only see in movies."
    "The bar is wide and accommodating, stools lining its outer perimeter and drinks lining glass shelves along the wall."
    "A pair of bartenders mix drinks at a rapid pace, pouring all kinds of spirits for eager patrons."
    "In front of me is a crowd of people, crowded around a big, front-facing stage, eager about an upcoming performance."
    "The purple spotlights are pointed at a variety of different musicians fiddling with their instruments before the set."
    "There are maybe five or so people on stage. They’re all dressed in white collared dress shirts. It seems to be some sort of…"
    "Punk ska band???"
    "Well, it isn’t exactly the {i}first{/i} thing I would have expected, but I won’t say no to free entertainment."
    "I grab a stool at the bar and order a beer. One of the bartenders, a younger woman with dyed red hair, nods."
    "She hands me a bottle as I get comfy, eager as I focus my attention on the stage."
    "The guitarist tunes his strings, the bassist practices a few licks, the drummer kicks his pedal…"
    "The singer taps the mic for a soundcheck and the trumpeter plays their scales."
    "There is a palpable excitement in the air, as a rather large audience crowds around the stage, eager for the show to start."
    "The outer lights begin to dim and the band is ready to begin, but there seems to be a person missing…"
    "All of a sudden, I feel someone brush my shoulder and walk by me."
    who "\"Oh, sorry about that! My bad dude.\""
    "She turns around to apologize, but I can barely see her in the darkened room."
    who "\"Hey, wait a minute… haven’t I seen you before…\""
    who "\"Taylor? No way! Dude, how’ve you been? I haven’t seen you since-\""
    whoo "\"Prose! Get your ass over here!\""
    "The lead singer, with a look of annoyance on his face, waves at the woman talking to me, beckoning her to come onstage."
    who "\"Ah, shit. My bad… I gotta go do this concert for a sec. Stay after the show and we’ll catch up and grab some drinks!\""
    "Before I get the chance to say anything, she dashes off, pushing her way through the crowd as her band members shake their heads."
    "I didn’t even have the chance to correct her…"
    "And tell her that I have no idea who Taylor is!"
    "But soon enough she’s under the spotlight and as she grabs her trombone, my heart skips a beat."

    # Location: Prose Close-up
    #scene --- 

    "Before me is, quite possibly, the most gorgeous woman I’ve ever seen."
    "She has short, dark brown hair that perfectly frames her face."
    "Her outfit is well fitted, a simple white collared shirt, black tie and pants, and a pair of shades adorning her face."
    "She moves with a certain confidence earned only after years of performing onstage."
    "She teases her other band members about their annoyance at her, to which they roll their eyes and prepare to play."
    "As the singer begins to hype up the crowd, she grabs her trombone, pulls on it a few times, and readies herself."
    "And just before she does, I see her move her head in my direction and she smiles."
    "And they begin to play."
    "The music is loud and cacophonous. Something to be expected of a genre like ska."
    "Yet as they perform their enthusiasm starts to penetrate the air."
    "Suddenly, the crowd starts to go wild, banging their heads to the music and screaming along the lyrics as they all jam together."
    "The room breathes with life, the alcohol and performance mixing together to exhilarate the attendees."
    "It's a beautifully messed sight, yet all the while all I can do is focus on the mystery girl."
    "Five songs in and she hasn't even broken a sweat, blowing away at her trombone like it was second nature."
    "Her shades barely contain the smug aura that she is radiating."
    "I'm absolutely mesmerized by the display. It's like she's superhuman with how much endurance she displays."
    "Just who is this girl? "
    "I take another sip from my drink, when a sickly feeling comes over me…"
    "I like this girl, and she seems interested in me, but…"
    "She still doesn't know I'm not Taylor!"
    "The last song is coming to a close, and I hear the big finale pop off."
    "The crowd goes crazy as they cheer and holler, praising the band's amazing performance. "
    "Soon enough, they all make their way offstage, likely to cool down and get ready for their next set later on in the night. "
    "The noise of the crowd starts to simmer down, and as spirits start to return to normal, I can feel my palms start to sweat."
    "I {i}know{/i} I don't want to screw this up, but I'm just so unsure about what to do."
    "How can I convince this cool as hell person to go on a date with me???"
    "She’s making her way over to me, chatting up the crowd and grabbing herself a drink the bartender had pre-made for her."
    "It seems that she goes to this place pretty often. She waves at me, takes a sip of her cocktail, and smiles."
    who "\"Hey Taylor! Happy to see you’re still here! What’d you think of the performance?\""
    "\"I thought it was super nice. There was a lot of passion in your guy’s performance.\""
    "I didn’t have the heart to tell her ska was so 20 years ago…"
    p "\"Aw shit, thanks, dude! I’m really happy to hear you say that! I mean, you heard me in band… I sucked ASS.\""
    "She flashes another grin, and my own cheeks start to get even redder."
    "But she suddenly looks at me, curious, with the slightest hint of suspicion in her eyes…"
    p "\"Hey… wait a minute, now that the lights are back on…\""
    p "\"Taylor, you don’t look anything like how I remember you do…\""

label end_game:

    return
