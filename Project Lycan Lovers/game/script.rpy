# script.rpy

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define tv = Character("Television")
define who = Character("???")
define whoo = Character("??? #2")
define p = Character("Prose")

define pov = Character("[povname]")
define j = "[job]"

# ATL
transform zoom_dissolve:
    xalign 0.5 yalign 1.0
    alpha .0 zoom .75
    linear .25 alpha 1.0 zoom 1.0
    on hide:
        xalign 0.5 yalign 1.0
        alpha 1.0 zoom 1.0
        linear .25 alpha .0 zoom .75

# Opening
label start:

    play music "audio/bensoundjazz.mp3" fadein 2.0

    #Location: Street
    scene bg room

    "It is a cool October night in the city as I roam its crowded streets."
    "The sky is lit by the orange incandescent lights and a waning moon in the sky above me."
    "Noisy people walk along the paved concrete, as I solemnly spend yet another Friday night alone."
    "Yet another soul lost within the downtown district."
    "God I’m sooooooooooo pathetic!"
    "All of my friends are out with their partners, and I’m just all alone!"
    "The worst part is that tomorrow is Halloween! So of course everyone’s gonna go out and party!"
    "That or they're all making last-minute costume arrangements or whatever else couples do!"
    "All without me…"
    "Maybe I should go back home and watch some horror movies…"
    "It would be better than just wandering aimlessly like some mindless stooge…"
    "But on the other hand, the night is still young and filled with possibilities. I’m sure I’ll find {i}something{/i} I can enjoy!"
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
    scene bg apartment
    "{i}Back at the apartment{/i}..."
    
    "A few hours have passed, the sky has gotten darker, and the lights are off in my spacious living room."
    "The glimmering light of my television screen plays the end of {i}Death Gun 4: One Last Bullet{/i}."
    "I am alone, with nothing but a comfy blanket on top of me and a bowl of buttery popcorn on my lap."
    tv "\"No Johnny, you can’t shoot Death with his own Gun! Who knows what’ll happen?\""
    tv "\"If you do, the cycle of violence won’t stop! You have to end it here and now!\""
    tv "\"No, Lisa. The Death Gun is nearly empty, all except for One. Last. Bullet.\""
    tv "\"And it’s got {i}his{/i} name written all over it.\""
    tv "BANG!!!"
    "The gunshot causes me to lurch backward, throwing popcorn everywhere."
    "What a twist! I never expected Johnny to be so bold! A truly gripping plot twist!"
    "As the credits roll, I grab the remote, getting ready to put on {i}Death Gun 5: The New Reaper{/i}, when I hear a howling from outside."
    "Which is odd, to say the least… I can’t remember the last time a wolf was so close to the city…"
    "But I shrug it off. That’s someone {i}else’s{/i} problem, not mine."
    "I grab another fistful of popcorn and press play."
    "Oh yeah. Tonight is gonna be {i}perfect{/i}."

    "Death Gun Ending Complete."

    jump end_game

label a_route_after_choice_1:
    "Taking in a deep breath, I continue walking, trying to find something to pass the time with."
    "I refuse to let this wonderful night go to waste. I can always watch those movies some other time."
    "I’m already here, so why waste the opportunity?"
    "As I wander, it just occurs to me how many different sights and sounds the nightlife has to offer."
    "The glowing of neon and cacophony of motor vehicles assault my eyes and ears until I become numb to the overstimulation."
    "Until one sign in particular catches my eye."
    "It has a neon green tint, with a cartoony drawing of an unbalanced table covered in a variety of drinks nearly spilling over."
    "The bar’s name is the Tipsy Table and a pair of descending staircases invite me to venture inside."
    "The place is humming with a certain energy to it, and the sound of a large ensemble band performing can be heard from inside."
    "Figuring that a drink may help calm my nerves and prepare me for what I expect to be one hell of a night, I make my way downwards."
    "Taking a deep breath, I open the door."

    # Location: Concert Bar
    scene bg bar

    "What greets me is an inviting, warmly lit dive-in, the kind of establishment you only ever see in movies."
    "The venue is wide and accommodating, stools lining its outer perimeter and bottles of liquor on glass shelves along the wall."
    "A pair of bartenders mix drinks at a rapid pace, pouring all kinds of spirits for eager patrons."
    "In front of me is a crowd of people, crowded around a big, front-facing stage, eager about an upcoming performance."
    "The purple spotlights are pointed at a variety of different musicians fiddling with their instruments before the set."
    "There are maybe five or so people on stage. They’re all dressed in white collared dress shirts. It seems to be some sort of…"
    "Ska band???"
    "Well, it isn’t exactly the {i}first{/i} thing I would have expected, but I won’t say no to free entertainment."
    "I grab a stool at the bar and order a beer. One of the bartenders, a younger woman with dyed red hair, nods."
    "She hands me a bottle as I get comfy, eager as I focus my attention on the stage."
    "The guitarist tunes his strings, the bassist practices a few licks, the drummer kicks his pedal…"
    "The singer taps the mic for a soundcheck and the trumpeter plays their scales."
    "There is a palpable excitement in the air, as a rather large audience crowds around the stage, eager for the show to start."
    "The outer lights begin to dim and the band is ready to begin, but there seems to be a person missing…"
    "All of a sudden, I feel someone brush my shoulder and walk by me."

    show prose happy at zoom_dissolve

    who "\"Oh, sorry about that! My bad dude.\""
    "She turns around to apologize, but I can barely see her in the darkened room."
    who "\"Hey, wait a minute… haven’t I seen you before…\""
    who "\"Taylor? No way! Dude, how’ve you been? I haven’t seen you since-\""
    whoo "\"Prose! Get your ass over here!\""
    "The lead singer, with a look of annoyance on his face, waves at the woman talking to me, beckoning her to come onstage."
    p "\"Ah, shit. My bad… I gotta go do this concert for a sec. Stay after the show and we’ll catch up and grab some drinks!\""
    "Before I get the chance to say anything, she dashes off, pushing her way through the crowd as her band members shake their heads."
    "I didn’t even have the chance to correct her…"
    "And tell her that I have no idea who Taylor is!"
    "But soon enough she’s under the spotlight and as she grabs her trombone, my heart skips a beat."

    # Location: Prose Close-up
    #scene --- 

    "Before me is, quite possibly, the most gorgeous woman I’ve ever seen."
    "She has short, dark brown hair that perfectly frames her face."
    "Her outfit is well fitted, a simple white collared shirt, a loose black tie, jeans, and a pair of shades adorning her face."
    "She moves with a certain confidence earned only after years of performing onstage."
    "She teases her other band members about their annoyance at her, to which they roll their eyes and prepare to play."
    "As the singer begins to hype up the crowd, she grabs her trombone, pulls on it a few times, and readies herself."
    "And just before she does, I see her move her head in my direction and she smiles."
    "And on the drop of a dime, they begin. And it's a beautifully chaotic mess."
    "The music is loud and cacophonous. Something to be expected of a genre like ska."
    "As they perform their opener, the band’s enthusiasm starts to penetrate the air."
    "Suddenly, the crowd starts to go wild, banging their heads to the music and singing the lyrics as they all jam together."
    "The room breathes with life, the alcohol and performance mixing together to exhilarate the attendees."
    "It's a gorgeously messy sight, yet all the while all I can do is focus on Prose."
    "Five songs in and she hasn't even broken a sweat, blowing away at her trombone like it was second nature."
    "Her shades barely contain the smug aura that she is radiating."
    "I'm absolutely mesmerized by the display. Her near endurance is superhuman to say the least."
    "Just who is this girl? And why did she just talk to me?"
    "I take another sip from my drink, when a sickly feeling comes over me…"
    "I like this girl, and she seems interested in me, but…"
    "She still doesn't know I'm not Taylor! She’s mistaken me for someone else!"
    "The last song is coming to a close, and I hear the big finale pop off."
    "The crowd goes crazy as they cheer and holler, praising the band's amazing performance. "
    "Soon enough, they all make their way offstage, likely to cool down and get ready for their next set later on in the night. "
    "The noise of the crowd starts to simmer down, and as spirits start to return to normal, I can feel my palms start to sweat."
    "I {i}know{/i} I don't want to screw this up, but I'm just so unsure about what to do."
    "How can I convince this absolute stranger to go on a date with me???"
    "She’s making her way over to me, chatting up the crowd and grabbing herself a drink the bartender had pre-made for her."
    "It seems that she goes to this place pretty often. She waves me over, takes a sip of her cocktail, and smiles."
    p "\"Hey Taylor! Happy to see you’re still here! What’d you think of the performance?\""
    "\"I thought it was super nice. There was a lot of passion in your guy’s performance.\""
    "I didn’t have the heart to tell her ska was so 20 years ago…"
    p "\"Aw shit, thanks, dude! I’m really happy to hear you say that! I mean, you heard me in band… I sucked ASS.\""
    "She flashes another grin, and my own cheeks start to get even redder."
    "But she suddenly looks at me, curious, with the slightest hint of suspicion in her eyes…"
    p "\"Hey… wait a minute, now that the lights are back on…\""
    p "\"Taylor, you don’t look anything like how I remember you do…\""

    jump choice_2

menu choice_2:
    "Are you sure you're actually Taylor?"

    "Tell her that you aren’t Taylor":
        jump at_route_after_choice_2

    "Lie through your teeth":
        jump al_route_after_choice_2

label al_route_after_choice_2:
    "\"Wha- what’re you talking about? I’m definitely Taylor!\""
    "My voice cracks at the tail end of my terrible bluff."
    "She looks back, leaning in closer as she evaluates what I just said."
    "Her glare gets even closer now, her expression unchanging. It’s as if she's staring deep into my soul."
    "\"Um, aren’t you getting a little close-\""
    p "\"No shut up, I'm getting a better look at you.\""

    jump choice_3

menu choice_3:
    "Crack under the pressure":
        jump alc_route_after_choice_3

    "Keep your cool":
        jump alk_route_after_choice_3

label alc_route_after_choice_3:
    "\"Okay fine I give! I’m not actually Taylor!\""
    "She finally backs off, a swelling sense of pride showing as she figures out my ruse."

    jump at_route_after_choice_2

label alk_route_after_choice_3:
    "She gets even closer now. I can faintly hear her breathing as our eyes get closer. I can feel the droplets of sweat on my forehead."
    "She takes in an exaggerated sniff of air, closes her eyes, and collects her thoughts for a moment."
    p "\"There it is…\""
    "\"Ummm… There {i}what{/i} is exactly?\""
    p "\"The scent of a liar.\""

    jump at_route_after_choice_2

label at_route_after_choice_2:
    p "\"HA! I KNEW IT! You almost had me fooled there for a second, but I can always find out if someone isn’t telling the truth to me.\""
    "She’s gloating over me, reveling in her own self given glory. It’s a little showboaty."
    p "\"I’m sort of an ace detective if you didn’t know. I can read people like the back of my hand!\""
    p "\"So why’d you do it bub? Why’d you gotta go and lie about being someone I actually {i}knew{/i}?\""
    "\"Hey wait a second, I didn’t even {i}want{/i} to be this Taylor person or whatever. You just assumed I was them when we first started talking!\""
    "For the first time, she looks absolutely flabbergasted at what I just said."
    "For the first time, I think I’ve truly caught her at a loss for words."
    p "\"…oh shit… did I actually do that again…\""
    "She smacks her forehead with a loud thud, face flushing red after making such a fool of herself."
    p "\"Damnit! That’s my bad dude. This has been like the second time this month.\""
    p "\"I just get {i}way{/i} too excited at the prospect of meeting an old friend. Totally didn’t mean to put you on the spot there.\""
    "\"Oh, well I mean it’s not a big deal. It’s actually been rather exciting talking to you if I’m being honest.\""
    p "\"Oh really now? Huh, well if that’s the case…\""
    "She calls over the bartender for a second round of drinks. She offers one to me, which I happily receive."
    p "\"Why don’t we get to know each other a little better?\""
    "\"Wait, really? With someone like me?\""
    p "\"Well, I mean sure why not? You’re pretty cute and I got a little bit of time to kill before my next performance. And besides…\""
    p "\"It’s not like you or I have anything better to do! Hehe...\""
    p "\"So stranger, since we haven’t been properly introduced.\""

menu choice_4:
    p "\"What's your name?\""

    "Say name is Taylor":
        jump att_route_after_choice_4

    "Type in your real name":
        jump atn_route_after_choice_4

label att_route_after_choice_4:
    "\"Well, funnily enough, my name is Taylor.\""
    p "\"Wait a second, you mean to tell me that your real name is actually Taylor?\""
    "\"Yeah.\""
    p "\"And that you aren’t the Taylor I knew back in high school from band class? The Taylor I totally may or may not have had a crush on?\""
    "\"Wait a second you never said that you had a crush on this Taylor bozo.\""
    p "\"Nah I’m just teasing you. I know you’re not them.\""

    jump atn_2

label atn_route_after_choice_4:
    python:
        povname = renpy.input("Well my real name is", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Taylor"

    jump atn_3

    label atn_2:
        python:
            povname = "Taylor"
    
    label atn_3:
    p "\"[povname].\""
    "She seems to let it linger in the air, trying hard to remember it on the first go."
    "After a moment, she extends her hand with a smirk."
    p "\"The name is Prose. The pleasure is all yours.\""
    "I return the handshake, surprised by the firm grip she offers to me.."
    "That hand is gonna be sore for a bit."
    "But it really is nice to have a formal introduction with her, after all this time."
    "Hey, wait a minute. Did she call me cute a few minutes ago?"
    p "\"So, [povname], since we’re pretty much perfect strangers, why don’t you tell me a bit about yourself?\""


# Set Character Job
menu choice_5:
    p "\"What do you do when you ain’t watching shitty ska bands perform in local dives?\""

    "Say that I’m a music teacher for young kids":
        python:
            job = "musician"
        jump atnm_route_after_choice_5

    "Say that I’m a fitness instructor":
        python:
            job = "fitness instructor"
        jump atnf_route_after_choice_5

    "I’m actually unemployed...But I can’t let her know that! (Lie again)":
        python:
            job = "unemployed"
        jump atnp_route_after_choice_5

label atnm_route_after_choice_5:
    "I work at a little middle school on the outskirts of town. I help kids learn to play music."
    p "\"So you do have a history with music! That's just perfect!\""
    p "\"Maybe you can give me lessons sometime. I’d always love some more tips about my trombone playing skills.\""

    jump atnxc_route

label atnf_route_after_choice_5:
    "I’m employed at a private gym in downtown. I help people schedule workouts and meals to improve their lifestyles."
    p "\"Oh, you work out as well?\""
    "Yeah, I like to go pretty often. I can’t lift much, but I’m happy with the progress I’m making."
    p "\"Hell yeah dude. All about the journey over the destination.\""
    "If you have the time, I'd be more than happy to take you there. You know, complimentary employee guest and everything."
    p "\"I might just take you up on that.\""

    jump atnxc_route

label atnp_route_after_choice_5:
    "Oh man… I can’t disappoint her and let her know that I don’t have a job right now…"
    "What would she think of me if she found out I currently don’t have a stable source of income?"
    "I gotta say something cool, something believable…"
    "\"I like to hunt ghosts and investigate the paranormal. You know, like haunted houses and stuff like that.\""
    "OH GOD WHY DID I SAY THAT?????"
    "This noticeably catches her off guard, as she does a double take on her drink and chokes a bit."
    "She takes a moment to catch her breath, a look of disbelief on her face."
    p "\"You can’t be serious! How do you even make money?\""
    "\"Oh, you know, I record myself roaming haunted houses and post it on the internet. I’m actually rather popular on social media.\""
    "She starts to stare me down again, judging me with a harsh and unmoving glare."

    jump choice_6

menu choice_6:
    "Her gaze penetrates into my very soul. I don’t know what to do…"
        

    "Tell the truth":
        jump atnpt_route_after_choice_6

    "DOUBLE OR NOTHING":
        jump atnpd_route_after_choice_6

label atnpt_route_after_choice_6:
    "\"Okay fine I give I give! I’m really just unemployed right now! Quit staring so hard!\""
    p "\"Dude, why would you lie about that? There’s nothing to be ashamed of even if you are unemployed.\""
    p "\"To be honest, I was in-between jobs myself not too long ago myself. Trust me man, you’ll find one eventually.\""
    "Oh… thanks Prose. It means a lot to hear you-"
    p "\"But you better stop lying to me. I don’t appreciate it when people lie to me, especially if they do it {i}constantly.{/i}\""
    "\"...noted…\""
    p "\"Glad to hear it! We could probably do something cheap if we were gonna go out again…\""
    p "Maybe go to a museum or catch a movie or something… or maybe even invade some abandoned buildings…"
    p "That paranormal investigation thing you had going on was pretty cool…"

    jump atnxc_route

label atnpd_route_after_choice_6:
    "\"Okay maybe my channel isn't actually that popular, but it's getting there!\""
    p "\"Dude.\""
    p "\"That is so…\""
    p "\"Awesome! Who cares if you're not social media famous or anything! You get to check out haunted houses for a living!\""
    "Wait a minute… She’s actually {i}believing{/i} what I’m saying?"
    p "\"Wait before we go any further… do you actually believe in any of that stuff?\""
    "Uhm...what do you mean?"
    p "\"Oh, you know, like ghosts, vampires, zombies…\""

    jump choice_7

menu choice_7:
    p "\"…werewolves\""

    "Yes. I want to believe":
        jump atndy_route_after_choice_7        

    "Nah, it's all just a hoax":
        jump atndn_route_after_choice_7

label atndy_route_after_choice_7:
    "\"100 percent. There is {i}something{/i} out there, it's only a matter of time until we discover it.\""
    "Her eyes light up when she hears this."
    p "\"Hell yeah dude! You gotta take me along for one of your tours or whatever! Paranormal stuff is totally up my alley!\""
    
    jump atnxc_route

label atndn_route_after_choice_7:
    "No… not really. I don’t actually believe that there’s anything else out there."
    p "\"Oh… I see…\""
    "This is quite obviously not what she wanted to hear."
    p "\"Well then I’ll just have to change your mind the next time we meet up!\""

    jump atnxc_route

# Unifier
label atnxc_route:
    "Hey, wait a minute…"
    "\"Are you saying that you want to meet up again?\""
    p "\"I mean I thought it was obvious, but yes I’m saying exactly that.\""
    p "\"C’mon dude, you gotta learn to take a hint.\""
    "I can’t believe my luck. And to think, I was debating whether or not to go home just a few hours ago!"
    p "\"If you’re not too busy tomorrow, why don’t you show me around? I don’t have any plans for Halloween and I’d hate to spend it alone.\""
    "Oh god what do I say…"
    "\"How about we spend tomorrow together and wander around the city?\""
    p "\"That sounds like a good time. Here how about we-\""
    "Suddenly, a scream comes from the small concert stage."
    who "\"Hey Prose, we’re about to go on again! You ready or what?\""
    p "\"Five minutes Daryl! *whispers* God calm your tits man…\'"
    p "\"I’ve had a lovely time chatting with you today [povname], but I gotta go.\""
    p "\"We can meet up maybe around 10am or so at the city park?\""
    "\"Sounds perfect to me.\""
    p "\"Solid. Oh, and wait…\""
    p "\"I should probably tell you this before we meet up again, but you need to know that-\""
    who "\"Prose! Come on! The crowd is waiting!\""
    p "\"IN A SECOND!\""
    p "\"[povname], you gotta understand, that I’m not exactly {i}normal{/i}.\""
    p "\"There are a few things that aren’t quite… right about me, you understand?\""
    p "\"It’s a little hard to explain now but I promise that-\""
    who "\"PROSE!!! GET OVER HERE NOW!\""
    p "\"Shit… Listen I’ll tell you about it tomorrow morning, I’m sorry but I gotta go…\""
    p "\"See you then.\""
    "She gives me one more wink before she puts on her shades again and heads for the stage."
    p "\"OKAY DARYL YOU DICK I’M COMING OVER!\""

    hide prose happy

    "What a woman. It’s only after she's gone that I realize how late it actually is."
    "Every bone in my body is begging for me to head back home to bed, and to be quite honest, I don’t have the heart to refuse."
    
    #Location: Street
    scene bg room

    "I make my way outside as I start to hear the band launch into their next set. It’s just as energetic as before. The trombone blares loudly and Prose is having the time of her life."
    "Oh the magic of ska…"
    "I make my way back to my apartment, humming a tune from Prose’s band as I walk along, eager for tomorrow."
    "Tonight I’d met one hell of a character, and on the bright side, she was nice enough to keep me company on a day as special as Halloween."
    "No matter what I do, I hope to not disappoint her."
    "I don’t know why, but I can tell that tomorrow is gonna be unforgettable."

    "Act 1 Complete."

    #show bg logo
    #with fade
    #pause 5

    show bg logo
    $ renpy.pause(3, hard=True)

label d_route:
    "Hey you! Player! We just wanted to say thank you for playing our little dating game!"
    "This build is currently a prototype, and we hope to update the game in the future with different locations, scenes, art, and much more!"
    "If you enjoyed what you played, please give us a rating and let us know what we can improve on."
    "We are hoping to get Act 2 out by the end of the year! If you want any updates, feel free to follow @InfernoGuy13 on Twitter for more info."
    "Have a good one!"

label end_game:

    return
