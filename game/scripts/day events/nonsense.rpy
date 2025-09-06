label day_event_nonsense:
    image nonsense_cubicle = "gui/day intro/clock in base.png"
    $ nonsense_right = True
    scene bg clinic bed
    n "Oh hey, your eyes are open. You've been out of it since your lunch break."
    n "If you're feeling alright, you can get up, get another coffee, and get back to work."
    scene bg clinic checkup door
    show aikha neutral
    aikha "Feeling I treasurer promise pollution? Young personality herd carry."
    player "Sorry, could you repeat that?"
    aikha pensive "Bend obligation bridge owner. Frown houseplant order."
    n "Surely you're fine, you're not feeling any pain. You just need another cup of coffee."
    player "Uhhhh, yeah, I'm fine."
    aikha talk "Oven, joke bend."
    show aikha at disappear
    n "And they're gone. Great, now all you have to do is get out."
    n "Wow, your head hurts. Guess whatever knocked you out hit you pretty hard."
    n "You're hoping that now that you've convinced Dr. Aikha that you're fine, there are no obstacles between you and all the work you haven't gotten done today. Unfortunately, Dr. Firewal shoots that hope in the foot."
    show firewal neutral
    wal "Costume base quote! Gregarious shoot service?"

    menu: 
        n "Makes sense that the head of security would be worried about that. Good thing you remember exactly what happened."
        "My cubicle.":
            jump nonsense_wrong1
        "The lounge.":
            jump nonsense_right1
        "The vents.":
            jump nonsense_wrong1

    label nonsense_wrong1:
        $ nonsense_right = False
        n "What are you-"
        wal surprise "Lean car threat dead walk, echo. Lock scrape place walk teach aisle. Belt nervous claim fuss stool ancestor manage."
        show firewal at disappear
        n "And now he's gone. Whatever, he'll figure it out eventually. Maybe next time, actually communicate what's going on."
        jump nonsense_plutoes
       



    label nonsense_right1:
        wal surprise "Lean car threat dead walk, echo. Lock scrape place walk teach aisle."
        n "If he's so worried about that, maybe he should keep them in a Wal-let."
        if "anendophasia" in seen_events:
            n "Nothing? Whatever, guess I'll just see myself out."
            n "Ha! Like you could handle that again."
        else:
            n "Nothing? Fine, tough crowd today, huh."
        wal talk "Stool line payment slow clerk, feather. Belt nervous claim fuss stool ancestor manage."
        n "Yeah, makes sense to inform him of this."
        show firewal at disappear
        jump nonsense_plutoes

    label nonsense_plutoes:    
        scene bg hallway
        n "As you make your way towards the exit, you feel an itch on your ear. Shit, is something growing on there?"
        show plutoes happy
        n "Oh Plutoes is here, which means that any growths are probably fine and safeish."
        n "{sc}{color=#009900}It's good to see that you're doing well after that skateboard accident.{/color}{/sc}"
        player "Thank you?"
        n "{sc}{color=#009900}I hope this doesn't cause you to stop hanging out with me in the future.{/color}{/sc}"
        n "What is with this guy? He's just always unintelligible."
        show plutoes at disappear
        n "After imparting that incredible wisdom to you, Plutoes walks off, probably to bombard some other poor staff member with gibberish."
        n "Well as fun as that was, you're not getting anything done just standing around, and that task Dr. Firewal gave you sounded pretty important."
        n "Now comes the hard part: where would our glorious Founder be at this time of day?"
        n "You wander the halls as you ponder that question."
        show bg lounge kitchen cook
        n "And, look at that, your feet led you to the thing you love best here, the coffee machine."
        show alex neutral
        n "...And the Founder himself."
        n "Maybe that addiction is good for something after all."
        alex "Hang hemisphere mechanical, career?"
        n "Alright. Just pass on the message from Dr. Firewal and you can go back to drinking coffee and whatever else it is that you do all day."
        menu:
            player "Founder Alex, I've come to warn you about an anomaly that..."
            "...is trying to steal mugs.":
                jump nonsense_mug_thief
            "...is trying to free other anomalies from containment.":
                jump nonsense_jailbreak
            "...can move through walls and looks kind of like a snail.":
                jump nonsense_snail

        label nonsense_mug_thief:
            n "You know, now that I hear it from you, that does sound ridiculous."
            alex fury "Import taste? Drop, nonremittal wine fill disaster us!"
            n "But apparently, this is a pretty big deal to the Founder, seeing how he sprints out of the room, clutching his mug."
            show alex at disappear
            n "On the bright side, this means more coffee for you."
            scene 
            show nonsense_cubicle
            n "A few hours pass. Your headache subsides, you get a little work done, and you drink five cups of coffee."
            n "All in all, a pretty good day for you."
            n "The last thing to do is check your email to make sure you didn't miss anything."
            n "Hmm, one email from the security department."
            if nonsense_right==True:
                n "\"Thank you for your assistance in preventing the loss of the Founder's prized mug collection. Had it not been for your sharp memory, we may not have caught the thief before it could escape.\""
                $ update_character_points({"firewal": 1, "alex": 1})
            else:
                n "\"Thank you for your assistance in preventing the loss of the Founder's prized mug collection. Although we were unable to find the thief, your warning to the Founder allowed us to prevent the thief from accessing his collection.\""
                $ update_character_points({"firewal": -1, "alex": 1})
            return

        label nonsense_jailbreak:
            n "I guess if you're trying to make sure a big deal is made of it, that might stir up some more panic."
            alex "Veil?"
            n "Is that not a concern? You think it sounds like a pretty big deal."
            player "Yes, isn't that, like, a big, foundation-wide problem?"
            n "He laughs and takes a swig of his coffee."
            alex happy "Enfix abbey hill folk frown nap candidate expertise inhabitant block reduction, lane fair deck."
            n "Oookay then, I guess maybe that thing isn't so big of a deal."
            hide alex
            scene
            show nonsense_cubicle
            n "You return to your cubicle."
            n "A few hours pass. Your headache subsides, you get a little work done, and you drink five cups of coffee."
            n "All in all, a pretty good day for you."
            n "The last thing to do is check your email to make sure you didn't miss anything."
            n "Hmm, one email from the security department."
            if nonsense_right==True:
                n "\"Thank you for your assistance in preventing the total loss of the Founder's prized mug collection. Due to your recollection, we were able to track down the thief, although a few mugs were damaged in the process.\""
                $ update_character_points({"firewal": 1, "alex": -1})
            else:
                n "\"Your failure to provide proper information or warning has led to the total loss of the Founder's prized mug collection. Although we understand that your injury may have affected your judgement, we are disappointed in your performance.\""
                $ update_character_points({"firewal": -1, "alex": -1})
            return
            
        label nonsense_snail:
            n "What the hell? Why would the Founder be bothered with that?"
            alex "Gaffe if example abandon?"
            n "The Founder is staring at you. After a few moments, he quickly turns around and heads to the door."
            show bg lounge kitchen door
            alex unique "Possibility contempt. Railcar play, peasant text image peasant, {i}plan settlement{/i}"
            show alex at disappear
            n "He exits, scanning his surroundings. That was weirdly intense."
            scene
            show nonsense_cubicle
            n "You return to your cubicle."
            n "A few hours pass. Your headache subsides, you get a little work done, and you drink five cups of coffee."
            n "All in all, a pretty good day for you."
            n "The last thing to do is check your email to make sure you didn't miss anything."
            n "Hmm, one email from the security department."
            if nonsense_right==True:
                n "\"Thank you for your assistance in preventing the total loss of the Founder's prized mug collection. Due to your recollection, we were able to track down the thief, although a few mugs were damaged in the process.\""
                $ update_character_points({"firewal": 1, "alex": -1})
            else: 
                n "\"Your failure to provide proper information or warning has led to the total loss of the Founder's prized mug collection. Although we understand that your injury may have affected your judgement, we are disappointed in your performance.\""
                $ update_character_points({"firewal": -1, "alex": -1})
            return