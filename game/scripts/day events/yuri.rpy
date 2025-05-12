label day_event_yuri:
    scene bg lounge
    with default_fade
    n "You're making your way to the lounge to get a cup of coffee when you run into two department heads."
    n "It's Dr. Aikha and Dr. Deceased! You wonder what they're talking about."
    show deceased pensive at appear(x_align = 0.33)
    show aikha pensive at appear (x_align = 0.66)
    deceased "..."
    aikha "..."
    n "...They're just staring at each other. Are you interrupting something?"
    n "You slowly slink towards the coffee machine."
    deceased "So how was your day, Dr Ai?"
    aikha "It's been fine. My patients have been doing pretty well lately."
    aikha "Maybe you could come over to the Path-Para department to meet them some time."
    deceased "Yeah! That would be..."
    deceased "..."
    aikha "..."
    player "..."
    n "...Is this some sad attempt at office romance?"
    n "Well! You have no clue what's going on, and you suspect those two don't either."
    
    menu:
        n "Maybe you can help them out?"
        "Wingman for Dr. Deceased.":
            jump wing_dece
        "Wingman for Dr. Aikha.":
            jump wing_aikha

    label wing_dece:
        player "Hey, Dr. Aikha! I heard that there're some really cool... um... diseases! That Dr. Deceased has been researching!"
        aikha surprise "Oh. Is that so? But I thought Dece specialized in..."
        aikha neutral "Huh. Dece. What {i}do{/i} you specialize in?"
        deceased happy "Oh! I'm glad you asked!"
        deceased "You see, the variety of anomalies that exist in our world go far beyond what we've chosen to classify at the Foundation.{nw}"
        deceased "Although we can easily split anomalies by their origins and functions, there are many in the world that cannot be so easily classified into such a category..."
        show black_screen:
            alpha 0.0
            linear 3.0 alpha 1.0
        deceased neutral "...all that being said, I'm basically half an expert in anomalous pathologies myself!"
        deceased "Although not as much as you, certainly. Ha. Ha."
        n "God, kill me."
        aikha "Well, if you ever have time, you're free to come by and take a peak! I'm sure Aran would be happy to see you."
        deceased "Haha, yeah! Aran..."
        aikha "Unless you're preoccupied. You've been out a lot on field studies lately, so-"
        deceased "No!"
        aikha surprise "..."
        deceased "I mean... it's been kind of slow out there lately. I can set my assistants on it for a bit. I have time! I promise."
        aikha happy "Oh. Of course! I've been meaning to hang out more, but you never seemed to have time. Heh."
        deceased "That's alright. I mean... I'll always make time for you!"
        aikha "!"
        deceased happy ":D"
        n "Barf."
        n "Well, you've already finished your coffee, so you leg it while you still can."
        player "I'll just... be going now..."
        aikha "Right! You're still here, [player_name]."
        if characters["deceased"]["points"] > 2:
            n "You see Dr. Deceased turn to look at you, goggles glinting gratefully. Score! You must've helped them out."
            n "Or maybe the lights are too bright in here? Anyway, you feel like you've done something right, so you take credit for it."
        else:
            deceased pensive "Wait, who is that?"
            n "No one important! Please leave us alone."
        aikha "Alright then! Meet at the Path-Para department for 1?"
        deceased happy "Sure thing!"
        
        n "The two skip away, hand in hand."
        n "Well, sort of. Dr. Deceased is holding the coat sleeve of Dr. Aikha's, but it's the thought that counts right?"

    label wing_aikha: 
        player "Dr. Deceased! "
# Maybe mention omni? or do something really wild like shoot aikha to get deceased invested into the anomaly might be funny sob
# against all ethics and occupational preservation, you decide to shoot dr. aikha to create an almost fanfic esque scenario. its also a good way to break your frustration over this tension
    return

# deleted
        # player "Well, if you guys are preoccupied, I'll just-"
        # deceased "Wait! You should come with, [player_name]!"
        # n "???"
        # deceased "You know! The more the merrier."
        # n "Does this guy know what a date is?!"
        
        # menu: 
        #     player "O-oh. Well..."

        # n "You've already had your coffee but you can't think of an excuse to leave."
