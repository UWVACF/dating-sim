label day_event_pokanom:
    scene bg hallway
    n "The workday is over, but you're still here. That'd be admirable if you were actually working. Instead you're just looking around for your phone."
    n "Maybe it's in the lounge. You definitely had it on your lunch break."
    scene bg lounge
    n "You walk into the sounds of ripping plastic and shuffling cards."
    n "You see people around a table covered in cards and torn wrappings."
    n "Looking at one mostly intact wrapper, it says \"Pokanom\"."
    show lee talk at appear(x_align = 0.2)
    lee "They ordered a box of cards that came today. Unfortunately, until they are done with the pack opening, Dr. Chan and Egg are functionally inaccessible."
    show lee happy
    n "Well Dr. Lee looks pretty amused by the scene in front of them."
    show uriel upset at appear(x_align = 0.8)
    n "At the other side of the table, Uriel is also watching, although they seem far more impatient."
    hide lee  
    hide uriel
    show egg happy at appear(x_align = 0.2)
    show chan happy at appear(x_align = 0.5)
    show b6 neutral at appear(x_align = 0.8)
    n "Egg is just eating the tops of the card wrappers off with concerning speed, and Dr. Chan is tearing into the packs at a similar rate."
    n "Every so often, they drop a card onto an ever-growing pile in front of B6."
    n "Hmm, Magic-Carp, Tuna-Tone, Bass-Tion,...Are all of these cards just fish?"
    n "Suddenly, you hear loud screeching from something that looks like a buff demon with a scale for a head that's hovering over Dr. Chan's shoulder."
    chan "Yes! A CeleMeme! My demonics deck is finally complete."
    n "Well, at least they're having fun, right?"
    egg " Dr. Chan, have you gotten the full-art shiny card from the pack yet?"
    chan "No, have you?"
    n "Uh oh, looks like there's only one pack left. Well they're both reasonable people, you're sure they can just talk this out."
    show egg fury zorder 50:
        yalign -0.5
        xalign 0.2
        linear 0.3 xalign 0.5
    show chan fury
    n "Nope. Egg has just lunged on to Dr. Chan and Dr. Chan is pulling out a gun."

    menu: 
        n "Quick! Find a way to resolve this without your two most responsible department heads coming to blows."
        "Settle this the proper way: with a Pokanom battle.":
            jump pokanom_battle
        "A full-art card? Those are worth quite a bit. Take it for yourself.":
            jump grab_and_run

    label pokanom_battle:
        chan "Fine. We'll settle this properly."
        chan "Hey Uriel, we're going to need a moderator."
        show chan neutral
        show uriel at appear(x_align = 0.2)    
        uriel "...Fine."
        show uriel neutral
        show egg neutral
        egg "Choose your cards wisely, for this will be the greatest challenge you will ever face."
        n "Well at least they're calmer now."
        n "..."
        with default_fade
        n "It's been half an hour. They can't possible have this many cards to look through."
        chan "Okay, there's no way you're beating this deck!"
        uriel "Oh good, they're finally starting."
        n "They both place a card facedown and, at Uriel's signal, flip over the card."
        egg "There's no way your Tychanitar will gain enough energy before my Hydreggon knocks it out."
        chan "You forget that with Tychanitar's special ability, it can use an attack with one less energy when it's first placed in the Active zone. And with a Shelleus, I can add two extra energy."
        egg "But that's water energy, and Tychanitar needs psythic energy!"
        chan "That's where my Deceadueye comes in. It makes all my energy requirements neutral."
        egg "Fine, but you do realize that Hydreggon's ability allows it to survive any attack while at full health. Now all I have to use is Spricaffito and Glossifleuriel's healing abilities to bring it back to full health."
        chan "Well if I use-"
        n "Yeah, I'm just going to tune all of this out."
        n "..."
        n "Oh, someone's trying to get your attention."
        uriel "Greenhorn, Dr. Chan is taking a while to choose his next card. Just help him so this can be done."
        n "Can't hurt to try, I guess."
        n "You go over to Dr. Chan and look at his cards."
        chan "Oh good, intern, I can't choose between these two Pokanoms."
        chan "Charyzard does a ton of damage, but it takes so long to charge up."
        chan "And Styxtini gives double points for the next knock-out."

        menu:
            "Charyzard should be able to tank long enough to take down another two Pokanoms.":
                jump charyzard
            "Styxtini will end the game faster, at least.":
                jump styxtini

        label charyzard:
            chan "Good choice. Charyzard already has the type advantage, so one big attack should be enough."
            with default_fade
            n "It takes a couple turns to charge up, but  Ryzmic Toss does indeed get both of the Egg's next two Pokanoms down to zero hp in one hit."
            n "Uriel has left, muttering something about \"just forging the signatures\", but Ethy seems too enthralled by the battle to notice."
            n "At this point, it's well past midnight, but at least they're done."
            show chan happy
            show egg sad
            n "Chan has the card, and, honestly, this might be the happiest you've ever seen him."
            $ update_character_points({"uriel": -1, "chan": 1})
            return
    
        label styxtini:
            chan "Well you seem pretty sure about this. Aikhaslash should go down faster than it can get Styxtini."
            chan "After all, what are the chances of four out of four coin flips being heads?"
            show chan surprise
            show egg happy
            n "High enough, it seems, as Styxtini goes down in the next turn to a bizarrely lucky Naight Slash."
            show uriel happy
            uriel "So, since this is over, I need a few papers signed, Dr. Chan."
            show egg sad
            n "Uriel pulls out a pen and a stack of papers about as thick as your arm."
            n "Wow, way to kick a guy when he's down."
            $ update_character_points({"chan": -1, "uriel": 1})
            return
    
    label grab_and_run:
        n "You grab the pack and rush out of the room."
        hide egg
        hide chan
        scene bg hallway
        n "Good news: they're not fighting each other anymore. Bad news: they're both after you now."
        n "You speed your way down the halls, taking random lefts and rights to try to shake your pursuers."
        scene bg door
        n "Hmm, this place seems unfamiliar."
        n "Well, there's two ways out of here. You've got the doorway that you just came through and a door that you can hear faint footsteps behind."

        menu:
            n "Either you face the familiar screeching behind you, or keep going into the unknown."
            "Fuck it, it's time to turn around and face the music.":
                jump surrender
            "There's no way what's behind this door is worse than what's behind you.":
                jump keep_running

        label surrender:
            n "I'm sure you knew this couldn't go on forever."
            n "Just keep the pack in plain sight and don't make any sudden movements."
            show chan fury
            n "Dr. Chan comes to a stop in front of you, still brandishing his gun. You hope the screams are due to Dr. Chan's actions, but seeing how Ethy seems to be intensely locked onto the cards in your hand, you doubt it."
            chan "Hand over that card this instant, or I will be forced to take more extreme measures."
            n "You comply. After seeing that fight, you don't like your chances."
            n "He rips it open and you hear his delighted yell in concert with more screeching."
            show chan happy
            chan "Yes! A full-art shiny V-bass! Oh wow, it's gorgeous."
            n "You look over and are nearly blinded by the glory of the card."
            n "It's just so incredible that there's no way we could do an artistic rendition."
            # if anyone really wants one just make me do it
            n "Well with Dr. Chan distracted by the beauty of his card, you can make your escape."
            hide chan 
            n "Whatever's behind that door can wait for another day."
            $ update_character_points({"uriel": -1, "chan": 1})
            return

        label keep_running:
            show black_screen
            n "You go to open the door and suddenly fall forward as the door opens and closes behind you."
            n "Welp. Time to find out what horrors these shadows hold."
            show uriel neutral
            uriel "Are you open to negotiations over that card pack?"
            n "Just do it. If you don't, all of these people are going to give you a heart attack."
            player "Why do you want this? You didn't seem all that interested when they were fighting."
            uriel "I need Dr. Chan to sign these, and bribery seems like the best option at this point."
            n "They gesture with a file that looks like it has enough paper to print a few dictionaries."
            uriel "In exchange, you will no longer be on the hook for the act that brought our two most reasonable department heads to animalistic rage."
            n "The screeching is getting louder."
            player "Deal!"
            show uriel happy
            n "Uriel takes the pack from your hand and leaves through the door behind you."
            hide uriel
            n "Through the door, you can hear the faint sounds of conversation and one loud, aggrieved sigh from Dr. Chan."
            n "You wait until the footsteps recede into the distance before stepping out."
            show black_screen zorder 10
            n "It's a lot darker here than you remember. And slimier?"
            n "The slime's getting into your pockets, like it's searching for something. Oh this is so gross."
            n "Well this is just great. You're down a pretty expensive card, you're covered in slime, and you smell like yolk."
            n "Wait, what? Actually, hold that thought, the slime is retreating."
            scene hallway
            n "Once you open your eyes, you see a rapidly shrinking yellow and white mass."
            show egg sad
            n "Finally, it solidifies into a form you recognize as the Egg, which frowns at you and floats away."
            hide egg
            $ update_character_points({"uriel": 1, "chan": -1})
            #egg shows up?
            return






