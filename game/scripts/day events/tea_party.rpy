label day_event_tea_party:
    scene bg hallway
    with default_fade

    n "You're walking down the hallway for what seems like the seventh time this shift for a meeting."
    n "What's the meeting about? You don't know and you don't care. All you know is that there'll be free coffee."
    n "The better kind. Not the cheap instant brand at the lounge."
    n "As you're walking, you examine the few decorations in the hallway." 
    n "There's a poster advertising a cult meeting. A suspicious potted plant sits further down. A large mass with several eyes leering over you. A stray coupon." 
    player "...Wait a minute." 
    # display anomaly
    n "You look up to see the large mass staring at you." 
    n "It doesn't seem to be aggressive... Maybe it's lost?" 
    n "Wait, aren't there procedures for escaped anomalies?" 
    player "...Hi there. Can I help you?" 
    n "The looming mass leans closer to you."
    player "I'm on my way to a meeting right now. Do you, uh, need something?" 
    n "The anomaly extends a hand, as if to shake yours." 
    n "Well, it's actually more of a tendril, but semantics."
    player "Oh, nice to meet you too. My name is [player_name]. Where are you from-?" # auto skip 
    "???" "SCREEEEEEEEEEEEEEEEEEEEEE"
    player "Hu-? UaghAaauuAAAAAAUUGGGHHHHHHHHHH?!"
    n "Before you know it, you are sucked into a rift in reality."

    # ANIMATION: scene bg tea party / black fade 
    scene bg lounge 
    n "By the time you're spat out, the hallway's completely transformed." 
    n "Your head is spinning and you look around to try and get your bearings."
    n "The only thing you see is Dr. Jessie, pouring a cup of tea for you, her, and the anomaly in the hallway." 
    n "It's curled up on a frog chair, leaning over the cup of tea. It doesn't seem to know how to drink it." 
    show jessie at appear(x_align=0.3)
    jessie "Oh, hey [player_name]! What brings you here?" 
    player "Uh..." 
    show alex at appear (x_align=0.6)
    n "You take a closer look at the room. Dr. Alex, beloved founder of the foundation as you know it, is sitting eating croquettes." 
    alex "Yo what up?" 
    n "Isn't he supposed to be at the meeting?!" 
    alex "Have you seen my phone? I dunno where I put it." 
    player "Neither do I?!" 
    n "Whatever. ONE of you has to be at that meeting, and it might as well be you."

    menu:
        n "How are you going to get out of this?" 
        "Mr. Founder, don't you have, uh... business to attend to?":
            jump bidness
        "So, Dr. Jessie. Who's this friend of yours?":
            jump friendship 
        "Wait, what's that under the table?": 
            jump jhamp_scare

    label bidness:
        alex "..."
        alex "What business?" 
        player "You know. The meeting business." 
        n "Dr. Alex pours another cup of coffee. There isn't a pot of coffee on the table, so you're not sure where he's getting it from."
        alex "A meeting?" 
        player "That's the one..." 
        n "It's not as if you're doing anything else as an intern anyway."  
        alex "I didn't plan for a meeting today." 
        player "...Wait, really?" 
        alex "I would've gotten a notif."
        player "On your phone?" 
        n "Dr. Alex sips his coffee." 
        player "Then who sent that email?!" 
        jessie "Um, excuse me. Sorry to interrupt, but if you're going to talk about work, I'd prefer it if you did it outside." 
        # anomaly CG appears 
        "???" "..." 
        jessie "Don't worry! I'm sure they're not trying to be rude." 
        "???" "..."
        "???" "...Rude."
        jessie "No, no! It's okay." 
        n "That doesn't sound good... Mr. Founder, don't you think it's time to get going?" 
        show jessie at disappear 
        # show snail 
        alex "..." 
        player "They have free snacks."
        show alex panic 
        alex "..."
        player "Mr. Founder?" 
        n "The look on his face could only be described as a generational horror talked about only in legends and folk tales."
        n "You look down to see what could inspire such fear on a man that's impervious to every disaster life can offer him."
        n "A small snail slowly inches its way towards him." 
        alex "...Welp! Smell ya later everyone!" 
        n "It leaves a trail of slime, trailing all the way from a cellphone in the corner of the room." 
        n "The cellphone is open to the Outlook app, displaying a sent email addressing everyone. Including you." 
        player "Wh- hey!"
        n "Dr. Alex shoves you aside in search for an exit." 
        n "...There is no exit."
        alex "Darn."
        n "Dark black tendrils seize Dr. Alex and hoist him into the air, dangling him by his shoes."
        n "With your luck, it's only natural that you're restrained too and are now struggling to breathe as the anomaly looms over you." 
        player "...So I'm guessing there's no meeting today." 
        "???" "Don't. Leave." # make text big and bold
        alex "Hrg."
        "???" "Lonely?"
        player "Uh. Not at the moment, no." 
        n "The anomaly rises, seeming to fill the entire room. The lights dim." 
        "???" "Leave. Rude." 
        menu: 
            n "What do you do?!"
            "HELP!!!": 
                jump rescue
            "HELP!!!":
                jump rescue
            "HELP!!!":
                jump rescue    

        label rescue: 
            # fading to black
            n "The light is fading in front of your eyes. Do they have coffee in heaven? You hope so."
            player "Espresso, here I come..."
            alex "I'm too young to die!"
            show deceased at (x_align=0.8)
            deceased "Aren't you, like... half a century old, Mr. Founder?"
            player "!!!"
            n "You're saved! Screw holy espressos, you can get shitty instant coffee here for free."
            deceased "Woah. What's going on here?"
            n "You struggle to speak around the giant anomaly crushing your windpipe."
            # make small text 
            player "Kind of... dying..."
            alex "The snail's here."
            deceased "Ah. I got you Mr. Founder."
            n "Dr. Deceased walks over to the small snail and picks it up."
            n "It immediately begins to shrivel up in their gloves, emitting a shrill sound that almost sounds like a scream."
            n "When the sound is "


label friendship:
    n "whuzz good"

label jhamp_scare:
    n "Hampter appears from underneath the table."
    hampter "Hallo!"
    n "She scampers up the tablecloth and begins to pour you tea." 
    n "...Wait, how is she doing that without opposable thumbs?" 
    player "Hey Hamp. I'm supposed to be at a meeting right now. D'you know where the exit is?" 
    hampter "Exit?"
    player "Yeah. This place has one. Right?"
    n "Hampter blinks at you."
    hampter "I can teleport."
    player "Oh. Right." 