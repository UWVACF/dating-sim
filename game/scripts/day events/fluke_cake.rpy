init python:
    fc_topdown_dialogue = "Who do you want to sit with?"

screen fluke_cake_lounge_topdown:
    fixed:
        image "images/cgs/lounge_topdown.png":
            zoom 0.8
            xpos 112
            ypos -25
        image "images/cgs/lounge_topdown_ah.png":
            zoom 0.8
            xpos 112
            ypos -25
        image "images/cgs/lounge_topdown_au.png":
            zoom 0.8
            xpos 112
            ypos -25
        image "images/cgs/lounge_topdown_cm.png":
            zoom 0.8
            xpos 112
            ypos -25
        
        button: # alex hamp
            background None
            xpos 500
            ypos 100
            xsize 400
            ysize 170
            action Jump("fluke_HA")
            hovered SetVariable("fc_topdown_dialogue", "Sit with Founder Alex and Hampter.")
            unhovered SetVariable("fc_topdown_dialogue", "Who do you want to sit with?")
        button: # caffi meme
            background None
            xpos 1100
            ypos 55
            xsize 400
            ysize 170
            action Jump("fluke_CM")
            hovered SetVariable("fc_topdown_dialogue", "Sit with Caffi and Meme.")
            unhovered SetVariable("fc_topdown_dialogue", "Who do you want to sit with?")
        button: # ai uriel
            background None
            xpos 1130
            ypos 500
            xsize 400
            ysize 170
            action Jump("fluke_AU")
            hovered SetVariable("fc_topdown_dialogue", "Sit with Dr. Aikha and Uriel.")
            unhovered SetVariable("fc_topdown_dialogue", "Who do you want to sit with?")
        
    window:
        id "what"
        text fc_topdown_dialogue style "say_dialogue"
        background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

label day_event_fluke_cake:
    scene bg hallway
    n "You're on your way back after a conference when you hear loud cheering from the direction of your office."
    $ shake_screen(duration=1.0, preset="rumble", persist=2)
    crowd "HAPPY BIRTHDAY!!!"
    n "Oh shoot. It's Josh's birthday today."
    n "You know, Josh? The one who treated you to 50 coffees? The one who covered for you the day your cat was sick? Also the day that the newest Mimtemdo Swap 2 arrived and you wanted to go home early?"
    n "You remember them? Right?? Right???"
    n "They told you it's their birthday today and even invited you to their birthday party!"
    n "Listen, they're cheering. Which means it's happening right now."
    n "You have to do something. You can't show up empty handed. That would make you a horrible person."
    n "Perhaps you can go scramble for a gift card during your break, which is now. Showing up late with a gift is better than on time without one."
    n "You look for the closest Timothy Hort on your phone. Two hours away. This is what you get for working in the middle of nowhere."
    n "Or, maybe you can do some arts and crafts in the lounge. Print out a birthday card and sign it. No one will know."
    n "You hurry into the lounge, praying that no one is there."

    scene bg lounge
    # cg cake
    n "Just as you're trying to get the printer to work, you notice a mysterious cake on the counter."
    n "You check the label to see who the owner is, but there isn't one."
    n "You look back at the printer, which is still refusing to turn on. An idea forms in your head."
    n "As the old saying goes: Finders keepers! This is the perfect solution to your gift problem."

    with default_fade
    n "You barely manage to sign your name on the cake box when the crowd migrates into the lounge."
    show aikha at appear(x_align = 0.75)
    show alex happy:
        xzoom -1.0
        appear(x_align = 0.25)
    show syg:
        xzoom -1.0
        appear(x_align = -0.05)
    show uriel at appear(x_align = 1.05)
    person "Ohh!! Is that cake you brought, [player_name]?"
    show aikha pensive
    player "...Yep!!"
    n "You feel Dr. Aikha's forty-six pairs of eyes scan you and squint. You do your best to ignore it."
    alex "Oooo. What flavour is it?"
    player "It's...birthday cake flavoured?"
    alex "Oho! Hilarious!"
    n "You force a smile. Maybe you should've sneaked a bite in earlier instead of spending the time doing a fancy signature."
    josh "Thank you so much, [player_name]!"
    n "You flash Josh a smile as you watch them make their way to the cake. You will now be remembered as a great person."
    # cake slice cg 
    n "Josh cuts the cake and the crowd gasps."
    josh "Wow, you must have put in a ton of effort into making this! There're so many flavours!!"
    josh "No wonder you said it's birthday cake flavour! It was a surprise all along!"
    n "You feel a bead of sweat slide down from your forehead. You're starting to have a bad feeling about this."
    josh "[player_name], since you made it, you should be the one to cut this! Tell us what flavours are there!"
    n "You reluctantly shuffle over in front of the cake. The crowd forms an organized line behind you."
    $ cake_list = ["Blood Velvet", "Dirt (organic topsoil)", "Eyeball (filling)", "Turnip", "Egg", "Strawberry Tallcake", "Sponge (the washing kind) cake", "Cinco Leche (almond, soy, woolly mammoth, walnut, expired)", "Angel Dust (cocain)", "Sheet cake (papersheets)", "Black Forest (with wood, sawdust and rice crispies)", "Ice Cube cake (now just water)", "Invisible And Incorporeal cake (air)", "Pineapple Right-side-up cake", "Pop cake (with jam filling and a popsticle stick)", "Chocolate Coke Cake (the other coke)", "Dehydrated cake (0% water)", "Bun cake (a bun that is cake shaped)", "Butter cake (a block of unsalted butter)", "Pound cake (british currency)", "Catepilliar cake (no catepilliars are harmed in the process of making this)", "Cheesecake (a wheel of brie, not for those latose intolerant)", "Coffee cake (just coffee grounds with whipped cream on top)", "Marble cake (hollow cake with round marble filling)", "Singlular confetti cake (with a singular sprinkle)"]
    $ cake_this_list = random.sample(cake_list, 5)
    n "You cut a slice. It perfectly seperates a slice of flavour. Weird."
    player "This is... [cake_this_list[0]!l]?"
    n "You have no idea what it actually is."
    player "And this is, uh, a [cake_this_list[1]!l]."
    n "The cake flavours are looking weirder. You're unsure if what you made up would even be tasty."
    player "This one here, it's...[cake_this_list[2]!l]? I think."
    n "The crowd looks delighted, though."
    player "Here, a smaller slice of [cake_this_list[3]!l] for you."
    n "You would never eat that."
    player "Uh, this one? Are you allergic to [cake_this_list[4]!l]..?"

    scene bg lounge
    with default_fade
    show alex at appear
    n "Your hands shake as you scoop up the last piece and serve it to the Founder himself."
    n "At least this cake looks normal. Just a regular birthday cake with sprinkles."
    alex "Ooo. What is this cake?"
    player "...Birthday cake."
    alex happy "Haha! If you say so."
    n "He gives you a wink. Or, you think he gave you a wink behind those opaque goggles."
    n "You watch as Dr. Alex takes a bite out of the cake. Then he starts coughing and sputtering."
    $ shake_screen(duration=0.3, strength=7, repeat=7, interval=0.3)
    alex panic "{i}SCOFF{/i} I'm {i}COUGH{/i} suffocat- {i}COUGH{/i} -ting!"
    $ shake_screen(duration=0.3, strength=7, repeat=5, interval=0.6)
    alex "You're right {i}COUGH{/i}...It is birthday {i}COUGH{/i} cake...I'm allergic to {i}SCOFF{/i} sprinkles..."
    show alex panic at disappear
    n "He collapses on the ground."
    n "Oh shit. Did you just kill the Founder??"
    n "The immortal Founder. Killed by mere sprinkles."
    n "You look around, but everyone else seems unbothered."
    show hampter panic at appear
    pause 0.5
    hampter panic "Oh no! Am I too late for cake??"
    n "Hampter teleports in front of you out of nowhere."
    player "Uh, Dr. Alex just got the last slice. But he uh..."
    hampter surprise "Oh!"
    show hampter surprise at disappear
    # dr alex on the floor cg
    n "You see Hampter hop towards Dr. Alex, still ragdolled and hyperventillating."
    n "She jumps right over his head and lands next to the plate of unfinished birthday cake."
    show hampter happy at appear
    hampter "Don't mind if I do!"
    n "Hampter swallows the leftover cake in one mouthful. She rolls onto her back and lies contentedly next to Dr. Alex's shaking arm."
    player "...Is the Founder okay..?"
    hampter "Hm? Oh, he's immortal, so he'll be fine!"
    n "He doesn't {i}look{/i} fine."
    show hampter happy at disappear
    player "..."
    n "Out of the corner of your eye, you spot a diligent snail making its way over to Dr. Alex."
    $ shake_screen(duration=0.1, repeat=5, interval=0.3)
    n "You're about to comment on it when Dr. Aikha punts it like a soccer ball before whipping their gun out and shooting it repeatedly."
    show aikha at appear
    aikha "Don't mind me! I'll take care of it!"
    show aikha at disappear
    $ shake_screen(duration=0.1, repeat=5, interval=0.3)
    n "...Just another day at the foundation."
    n "You look around at everyone eating their slice of cake. You didn't even get one."
    n "You decide to join a group. It would look really sad if you just stood around alone with no cake."

    call screen fluke_cake_lounge_topdown
    # monster con hangout style chibi head cg for pairs of people

    label fluke_HA:
        n "You're still worried for the Founder, so you decided to stay with Hampter and Dr. Alex."
        alex "Help me..."
        n "He's still splayed out on the floor, while Hampter is happily licking the crumbs of the cake off her lips."
        hampter "Yum yum!"
        alex "Augh..."
        n "Suddenly, you hear a loud \"pop!\""
        n "You see Hampter stand up on two legs, front paws interlaced."
        hampter_quotes "Huzzah! I have defeated my sprinkles allergy!"
        alex_quotes "HELP ME!!!"
        hampter_quotes "Wait a moment. Why are you so big?"
        player "Uh..."
        hampter_quotes "Why am I so small?"
        alex_quotes "HELP!!! {i}*cough cough*{/i} HELP ME!!!"
        hampter_quotes "[player_name]! What is going on?"
        alex_quotes "AAAAAAAAAA"
        n "This is bad. It seems the cake caused Founder Alex and Hampter to switch bodies."
        n "Logically speaking, the best way to cure them is to feed them the opposite of cake."
        n "Unfortunately for you, you don't know what is."
        n "You turn to the most reliable resource on the Internet, Wroteit."
        n "You find a post from about a year ago. \"Having a debate with my mom and daughter and extended it to friends.\""
        n "You skim the answers."
        n "\"No cake.\" Clever. However, not very helpful to you right now."
        n "\"Rocks. Cake is the end result of 600 thousand years of human civilization, Rocks is no civilization at all.\" You see a major flaw in the logic but you don't have time to make a post about it. "
        n "\"The opposite of frogs is cinnamon.\""
        n "...You have neither frogs nor cinnamon right now."
        alex_quotes "HELPMHELPHMEHLMPEHLMPEHPHELPME {i}*cough*{/i} HELPPPPP"
        hampter_quotes "Why do I have the sudden urge to eat wires??"
        n "Your time is running low. You skim faster."
        n "You finally find a post by u/Interesting-Swimmer1, who claims the opposite of cake would be Jelli."
        n "Seems reasonable enough. One is baked in the oven, one is cooled in the fridge."
        n "At the very least, it's better than rocks. Or frogs."
        n "You rush over to the pantry in search of some Jelli powder."
        n "Sitting at the very back of the top shelf is a box of Zero Sugar Jelli, apricot flavoured."
        n "You look over the box. It expired 12 years ago."
        n "Surely Jelli doesn't expire. It's all chemicals, anyways."
        n "Regrettably, the instructions on the back of the box have faded."
        n "But everybody has made Jelli at least once, right? You probably remember."
        $ fluke_cake_jelli_minigame_step = ""
        menu:
            n "What's the first step?"
            "Preheat the oven.":
                $ fluke_cake_jelli_minigame_step = "oven"
                n "You preheat the oven to 190 degrees Celsius."
            "Boil some water.":
                $ fluke_cake_jelli_minigame_step = "water"
                n "You grab a pot from the cupboards and fill it with a few cups of water before placing it onto the stove."
            "Preheat the microwave.":
                $ fluke_cake_jelli_minigame_step = "microwave"
                n "You unplug the microwave and place it into the oven, taking extra care to place it on the middle rack."
                n "You then preheat the oven to 190 degrees Celsius."

        menu:
            n "What's next?"
            "Put the Jelli powder in.":
                if fluke_cake_jelli_minigame_step == "oven":
                    n "You open the box and pour the Jelli powder directly into the oven."
                    n "You start to smell something burn."
                elif fluke_cake_jelli_minigame_step == "water":
                    n "You open the box, pour the Jelli powder into the boiling water and give it a stir."
                    n "The powder dissolves, and the mixture homogenizes."
                else:
                    n "You open the box and pour the Jelli powder into the unplugged microwave."
                    n "You start to smell something burn."
            "Pour the powder into your mouth.":
                $ fluke_cake_jelli_minigame_step = "mouth"
                n "You tear open the package and start to ravenously devour the Jelli powder."
                n "It tastes very faintly of expired apricot. It's sickeningly sweet."
                n "You manage to swallow all the powder."
                n "...Oh shit. You were supposed to give Founder Alex and Hampter the Jelli to cure them of their circumstances."
                n "You walk over to them and offer them whatever remains: the faded packaging."
                alex_quotes "AHHHHHHHHHHHHHHHHHH"
                hampter_quotes "What? What is this?"
                player "It's Jelli. Well, the packaging, at least."
                hampter_quotes "What do I do with this?"
                player "...Eat it?"
                hampter_quotes "Oho! Okay!"
                n "You watch in half-horror, half-amazement as Hampter Alex unhinges his jaw and devours the entire cardboard packaging."
                player "Does it taste good?"
                hampter_quotes "No! And it doesn't seem to have done anything, either."
                n "You glance over at Founder Hampter and see her still writhing in anaphylactic shock."
                hampter_quotes "At the very least, I've been cured of my sprinkles allergy! Huzzah!"
                hampter_quotes "[player_name], could you do me a favour and get a cupcake FILLED with sprinkles?"
                # show hampter happy
                hampter_quotes "I've been dying to try them out!"
                hampter_quotes "Haha! Dying! Get it?"
                $ update_character_points({"alex": 1, "hampter": -1}) 
                return

            "Pour the powder into a centrifuge.":
                $ fluke_cake_jelli_minigame_step = "centrifuge"
                n "You find a conveniently placed centrifuge next to the stovetop and put the Jelli powder in."
                n "You turn it on, and the powder begins spinning rapidly."
                n "Hmm. Nothing happens."
                n "You notice another conveniently placed centrifuge next to the original, this time large enough to fit both a certain Founder and a Hampter inside."
                n "This gives you an idea. Maybe you could mix Founder Alex and Hamp together and like, rescramble their consciousnesses or something. It's still a work in progress."
                n "You walk over to them. Alex is gnawing on spoons, and Hampter is still writhing in endless agony."
                alex_quotes "AHHHHHHHHHHHHHHHHHHHHHHH"
                hampter_quotes "Delicious. Quite delicious."
                n "You casually drag them both over to the centrifuge and throw them in."
                alex_quotes "?????????????"
                n "You retrieve the Jelli powder from the smaller centrifuge, pour the powder in, and press the start button."
                n "You're about 30 seconds in when it hits you that centrifuges are for {i}separating{/i}, not for {i}mixing{/i}."
                n "Eh. It should be fine."
                n "After another minute or two, the centrifuge lets out a little \"Ding!\" and pops open."
                n "You glance inside eagerly and see..."
                n "...Two jellies."
                n "One has a mustache with a mug on top, and the other has small ears. They both wobble in your general direction."
                alex_quotes "{bt}HELP ME! HELP ME!!!{/bt}"
                hampter_quotes "{bt}Where am I? What happened?{/bt}"
                n "Oh hey! They can talk."
                alex_quotes "{bt}AHHHHHHHH{/bt}"
                n "...And feel pain!"
                hampter_quotes "At the very least, I've been cured of my sprinkles allergy! Huzzah!"
                n "Logically speaking, the best way to cure them is to feed them the opposite of Jelli."
                n "...Which would be cake."
                n "Unfortunately, the last slice was eaten long ago."
                n "You leave the lounge in search for more cake."
                $ update_character_points({"alex": 1, "hampter": -1})
                return
        
        if fluke_cake_jelli_minigame_step != "mouth" and fluke_cake_jelli_minigame_step != "centrifuge":
            menu:
                n "What's the last step?"
                "Turn the heat up.":
                    if fluke_cake_jelli_minigame_step == "oven":
                        n "You raise the oven temperature to 225 degrees Celsius."
                        n "The burning smell has become more prominent."
                        n "After a few minutes, you see flames erupt from the powder."
                        n "You frantically turn the oven off, and when the flames die down, you retrieve your now-charred Jelli powder."
                        n "It's probably best to serve while still hot. You make your way over to Founder Alex and Hampter."
                        jump fluke_cake_serve
                    elif fluke_cake_jelli_minigame_step == "microwave":
                        n "You raise the oven temperature to 225 degrees Celsius."
                        n "The burning smell has become more prominent."
                        n "After a few minutes, you hear a small explosion come from within the oven."
                        n "...That's not good. You open the oven and are greeted with a face full of black smoke."
                        n "Coughing and sputtering, you manage to retrieve the burned ashes of your Jelli powder."
                        n "...Well, best served hot. You make your way over to Founder Alex and Hampter."
                        jump fluke_cake_serve
                    else:
                        n "You crank the stove all the way up. You can feel the heat blasting your face, but you need this thing to cook fast."
                        n "After a few minutes, you look into the pot and see that all the liquid has evaporated."
                        n "The only thing left is a grayish pile of ashes sitting in the middle of the pan, still sparking."
                        n "You make your way over to Founder Alex and Hampter to serve them your creation."
                        $ fluke_cake_jelli_minigame_step = "microwave"
                        jump fluke_cake_serve

                "Place it into the fridge.":
                    if fluke_cake_jelli_minigame_step == "water":
                        n "You take the pot off the stove and place it into the fridge, in perfect accordance to the instructions."
                        n "The instructions that faded 10 years ago, at least."
                        n "You have some time to kill while the mixture cools and solidifies, so you decide to check in on the two."
                    else:
                        n "You take the pot of ashes out of the oven and place it into the fridge. They're bound to look more appetizing chilled, right?"
                        n "You have some time to kill while the ashes cool, so you decide to check in on the two."
                    n "Founder Hampter is, as expected, still suffocating on the floor, while Hampter Alex is happily gnawing on everything in sight."
                    hampter_quotes "This cupboard's wood is of most excellent quality! I must remember to order more..."
                    alex_quotes "{i}*hack{/i}* AUGHHHHHH"
                    player "Don't worry guys! I have some Jelli cooling in the fridge. Once it solidifies, you guys can go back to normal!"
                    hampter_quotes "Jelli? Why Jelli?"
                    player "Because it's the opposite of cake, obviously."
                    hampter_quotes "...That makes no sense. Wouldn't the opposite of cake be savoury?"
                    player "Hm?"
                    hampter_quotes "Cake is a sweet solid. Thus, it only makes sense that the opposite of cake would be a savoury liquid. Soup, for example."
                    player "That's not what they said on Wroteit!"
                    hampter_quotes "Wroteit? When was Wroteit a reliable source? You should be using Basefook!"
                    player "Basefook? That's so outdated!"
                    hampter_quotes "Old but reliable! Wroteit is anything but!"
                    hampter_quotes "I'll even prove it to you. I'll prove that Jelli isn't the opposite of cake by eating it right now!"
                    n "Before you can stop him, he bolts past you towards the fridge."
                    if fluke_cake_jelli_minigame_step == "water":
                        n "By the time you catch up to him, he's already standing in the middle of the pot of half-solid Jelli with a defiant look on his face."
                        hampter_quotes "I'll eat this, and nothing will happen! Watch!"
                        n "He devours the entire pot of Jelli. He finishes it in mere seconds, before standing up on his hind legs, placing his front legs on his hips and looking at you smugly."
                    else:
                        n "By the time you catch up to him, he's already standing in the middle of the pot of burnt Jelli ashes with a defiant look on his face."
                        hampter_quotes "I'll eat this, and nothing will happen! Watch!"
                        n "He devours the entire pot. He finishes it in mere seconds, before standing up on his hind legs, placing his front legs on his hips and looking at you smugly."
                    hampter_quotes "Huzzah! Basefook reigns sup-"
                    n "Suddenly, you hear a loud \"POP\", and before you know it, Hampter is back on all fours, while Founder Alex's cries grow more agonized."
                    alex "NOOOOOOOOOO {i}*cough*{/i} NOT AGAIN-"
                    hampter "Huh? What am I doing here?"
                    n "Hampter looks around, confused, before noticing the pot she's standing in. Her eyes light up as she devours it whole."
                    n "You walk over to Founder Alex, who is once more convulsing on the floor."
                    player "...Wroteit wins!"
                    $ update_character_points({"alex": -1, "hampter": 1})
                    return 

                "Serve while hot.":
                    if fluke_cake_jelli_minigame_step == "oven":
                        n "You take the now-charred ashes of the Jelli powder out of the oven and make your way over to Founder Alex and Hampter."
                        jump fluke_cake_serve
                    elif fluke_cake_jelli_minigame_step == "microwave":
                        n "You take the now-charred ashes of the Jelli powder out of the microwave in the oven."
                        n "Looks like some bits of the microwave got mixed inside the ashes."
                        n "Surely this won't cause any health problems."
                        n "You make your way over to Founder Alex and Hampter."
                        jump fluke_cake_serve
                    else:
                        n "You take the mixture off the stove and make your way over to Founder Alex and Hampter."
                        jump fluke_cake_serve
        
        label fluke_cake_serve:
            if fluke_cake_jelli_minigame_step == "water":
                alex_quotes "HELPHEHLEPHEPHLEPHL {i}*cough cough*{/i}"
                hampter_quotes "Oh? What's this?"
                player "I made some Jelli to try to cure your... predicament."
                n "He takes a look at your offering. His face contorts."
                hampter_quotes "Are you sure this is Jelli?"
                n "You glance down your pot of brownish-orange liquid."
                player "..."
                player "...I mixed some sprinkles into it-"
                hampter_quotes "SAY LESS!"
                n "You watch in astonishment as Hampter Alex downs the liquid in your pot."
                hampter_quotes "So this is what sprinkles taste like? Marvelous! Truly marvelo-"
                n "Suddenly, you hear a loud pop, followed by the intensified cries of Founder Alex."
                alex "NOT AGAIN!! {i}*cough cough*{/i} NOOO!!!!!"
                hampter "Oh! I'm back! What's this brown goo?"
                n "Hampter samples a bit of the mixture, shakes her head and decides to eat the pot instead."
                alex "CURSES! CUR- {i}*cough*{/i} CURSE YOU [player_name]!"
                n "Founder Alex chucks his \"#1 FOUNDER\" mug at you. It narrowly misses your head, sails through the air and smacks against the wall."
                n "Somehow, some way, the mug doesn't break, but instead leaves a large mug-shaped dent in the wall."
                alex "[player_name]!!"
                n "You see him reach into his lab coat and pull out another mug. It's a \"#1 BOSS\" mug."
                n "You decide to take this as a sign to leave and book it out of the room while the sounds of mugs cracking the walls echo behind you."
                $ update_character_points({"alex": -1, "hampter": 1})
                return
            else:
                n "Back at the table, Founder Hampter is still on the floor in pain, but Hampter Alex is nowhere to be seen."
                n "You glance down at the ashes of what used to be Jelli powder."
                n "You decide to test out your creation by putting some Jelli into Founder Hampter's mouth."
                n "You can't quite spoon the powder in, given how she's flailing around wildly."
                n "Instead, you decide to just dump the entire pot onto her head."
                n "The good news is that she seems to have swallowed some of the powder."
                n "The bad news is that she's now coughing even more uncontrollably."
                alex_quotes "HRK- {i}*cough cough*{/i} GRRK- AUGH-"
                n "But slowly, the coughing dies down, until she goes completely silent."
                n "Woah. It seems your cure actually worked. You ought to give some credit to Wroteittor u/Interesting-Swimmer1."
                player "Hampter?"
                n "No response."
                n "You tap her shoulder lightly. Still no response."
                n "You shake her. Her body is completely still."
                n "...Uh oh."
                hampter_quotes "What did you do?!"
                n "You turn around and see Hampter Alex staring at you in shock, wires still in his mouth."
                n "He runs over to his old body and start shaking it frantically, to no avail."
                n "Out of the corner of your eye, you see a small gray snail diligently making its way over to Hampter Alex."
                n "Suddenly, it stops, looking at the both of them, confused, before crawling in circles."
                hampter_quotes "Huh? AUGUHHU"
                n "At the sight of the snail, Hampter Alex lithely jumps onto the spinning ceiling fan, shaking in fear."
                hampter_quotes "MY BODY!"
                n "...They'll be fine, right?"
                n "You casually check the time on your watch. 2:17."
                n "You should probably get back to work."
                hampter_quotes "D-DO SOMETHING, [player_name!u]!"
                n "Oh, maybe you could grab a coffee before heading back."
                n "Can't be caught sleeping on the job. Don't want to risk getting fired, do you?"
                hampter_quotes "[player_name!u]! [player_name!u][player_name[-1]!u][player_name[-1]!u][player_name[-1]!u][player_name[-1]!u][player_name[-1]!u][player_name[-1]!u][player_name[-1]!u][player_name[-1]!u]!"
                $ update_character_points({"alex": -1, "hampter": -1})
                return
        # hampter and alex start crashing out
        # alex wouldn't want to go back to their old body (sprinkle allergy)
        # hampter wants to go back
        # choice of helping them or not helping them with Jelli(?) 
        # Jelli cooking minigame!!!


    label fluke_CM:
        n "You decide to hang out with \"Dr.\" Caffi and Meme."
        show caffi at appear(x_align = 0.33)
        show meme happy at appear(x_align = 0.66)
        meme happy "Hey Caffi! Are you interested in a one-of-a-kind never-before-seen deal?"
        caffi "I'm listening."
        meme "It's simple, really! We're selling a brand new product: Demonic Rejuvenating Ultimate Glorious Stimulants!"
        meme "Just one gram of this is enough to power you through the entire day!"
        caffi pensive "Oh?"
        meme neutral "Yup! 100% organically grown, with money back guarantee!"
        n "...Maybe you can find a new group of people to hang out with."
        show caffi pensive at disappear
        show meme happy at disappear
        n "As you turn to leave, though, you get jumpscared by Dr. Syg, who appeared out of nowhere behind you."
        show syg at appear
        player "Oh! Hey, Dr. Syg."
        syg "...Hello."
        player "..."
        syg "..."
        player "Well then!"
        $ shake_screen()
        hide syg
        n "Suddenly, you hear a loud \"CRACK!\" and you feel the room shake."
        n "When the shaking stops, you look around and see..."
        # show cg
        show syg happy at appear
        n "Dr. Syg."
        n "He looks remarkably...bonita."
        n "This feels terribly wrong."
        syg happy "HELLOOOOO [player_name!u]!!!"
        player "...Hi?"
        n "He happily runs over to the pantry and pulls out a box of strawberry Bocky's."
        syg happy "Do you want one?"
        n "You mumble some half-assed excuse, anxious to get away from whatever the hell possessed Dr. Syg."
        show syg happy at disappear
        n "Unfortunately, this leads you straight into Caffi and Meme."
        show meme happy at appear(x_align = 0.35)
        show caffi pensive at appear(x_align = 0.65)
        meme "🚨⚠️TRADE OFFER⚠️🚨\nI RECEIVE: Your money!\nYOU RECEIEVE: Demonic Rejuvenating Ultimate Glorious Stimulants!"
        caffi "{cps=*0.8}Speak up. These ears don't work like they used to.{/cps}"
        meme "But! You also need to make sure you find three other people willing to join the scheme- err, business.\nBottom text"
        n "Caffi turns to you slowly, squinting and slightly hunched over."
        caffi "{cps=*0.8}Youngster. I don't understand what they're saying. Could you be a dear and help me out?{/cps}"
        meme "Yo [player_name]! Help me "
        meme "Bruh, am I not clear enough? Chat, is this real?"
        menu:
            n "What will you do?"
            "Help Meme sell their D.R.U.G.S.":
                jump fc_drugs
            "Help Caffi avoid this obvious Ponzi scheme.":
                jump fc_avoid

        label fc_drugs:
            player "They're saying that if you sign your name in that box, you'll get a free cruise trip to the Bahamas."
            meme "Get [player_name] a \"True!\""
            caffi "{cps=*0.8}Eh? The Bahamas? Let me tell you a story{/cps}"
            caffi "{cps=*0.8}I remember back in 1968 when I went with my lads to the Bahamas.{/cps}"
            caffi "{cps=*0.8}It was crazy, I'll tell you that much! We...{/cps}"
            n "Caffi embarks on a long tangent about how she and her mates stole a ceiling light from Malwart."
            n "You have a feeling most of this isn't true..."
            caffi "{cps=*0.8}And then the cops showed up, and I thought we were goners! But then-{/cps}"
            meme fury "SYBAU. SYBAU. So do you want to buy it or not??"
            caffi "{cps=*0.8}Hmmm...{/cps}"
            caffi "{cps=*0.8}What say you, youngster?{/cps}"
            player "I think you should buy it."
            caffi "{cps=*0.8}Well, if the kind lad says so. Where do I sign?{/cps}"
            meme happy ""
            $ update_character_points({"meme": 1, "caffi": -1})
            return
            
        label fc_avoid:
            
            $ update_character_points({"meme": -1, "caffi": 1})
            return

        caffi "Is this more effective than coffee?"
        meme "Definitely! But if you want coffee, we're also offering a discount on our Premium Shroom Blend! Only $9.98 per cup!"
        caffi "Uh huh."
        caffi "So back to the... \"Goodness Simulant\" or whatever. You're saying I just need to get other people to sell it under me to get a reward?"
        meme "Mhm!"

# ```
# trade offer
# bottom text
# corporate asked you to find the difference between these two images
# this is fine
# tfw
# drake meme

# ```

    label fluke_AU:
        n "You decide to hang out with Dr. Aikha and Uriel."
        show aikha at appear(x_align = 0.2)
        show uriel at appear(x_align = 0.8)
        aikha "So a company of a friend who"
        uriel "I know some people who are good at...covering things up."
        uriel 
        aikha "So I have a friend who got a friend, who has another friend, who has an uncle who is running an operation, who could use some legal advices."
        uriel "What kind of advice?"
        aikha ""
        n ""
        #

        #



### unnamed co-worker birthday, you find the cake and pretend it's yours (present)
### effects:
# speak/do everything backwards (uriel)
# antis ACE
# b&w (syg)
# body swap (hamp & founder alex, founder alex now on all four, hamp on 2 legs and hands together)
# egg -> gets a call, your law degree has been revoked by harvard -> ... turns into stock image of a regular fried egg
# meme -> speaks in only memes
# caffi -> boomer
#
#
# hamp, syg, alex, uriel, egg, meme, caffi, aikha
## pairs: pick someone to hang out with
    # hamp & founder - body swap problem
    # caffi & meem - translate their communication
    # ai & uriel - deal with ace (good luck soldier), help uriel..?
    # egg & syg - the egg just phases out of existance, syg is depressed (like extra depressed)..?


'''
you hear form the distance at your cubical "happy bday!!!!'
oh no
that co-worker who has been helping you the whole time and mentored you and whom you've developed a wonderful working relationship with! it's their birthday!!! and you don't have anything to show for it you heartless bastard!
how could you forget, when they told you it's coming up soon and even invited you to their birthday party! which is happening, today!
dang it
better go scramble for a gift during lunch break. do you think a tims hortan card is good enough?
nvm, the closest tim hortan is an hour drive away, and your lunch break ends in 30 minutes.
maybe you can do some arts and crafts in the lounge. Just print out a birthday card and sign it. No on will know.
oh wait, there's a cake on the counter. You check it for a name of an owner. There is none. 
Well it's yours now! how convinient.

you're in the lounge. suddenlly you can an email telling eveyone but the person to get in the lounge for the party. roll a deception check. Nat 20!
Dr. Aikha eyes you, raising an eyebrow. But they didn't ask. What's the worse that will happen? Ace.
what flvor is it? you look down at the pristine icing on the cake. it's birthday cake flavoured. It's a birthday cake that is birthday cake flavoured, as all birthday cakes should be.
How convinient that nobody has an allergy to birthday cakes.

slice cake open, all sorts of flavours/colors
wow you must have put a lot of effort in this
start desperately listing the filling and flavours: blood velvet, dirt, eyeball filling, turnip, egg, strawberry tall cake, sponge (non-edible) cake, cinqo leche (almond, soy, expired, ), angel dust (cocain), sheet cake (paper), black forest (with wood, sawdust and rice crispies), ice cube cake (it's just ice, now water), invisible and incoporal cake (it's just air), pinapple right-side-up cake, pop cake (with jam and a popsticle stick so you can pick it up to eat it), chocolate coke cake (also cocain), dehydrated cake, bun cake (a bun that is cake shaped), butter cake (it's just butter), pound cake (british currency), catepilliar cake (no catapilliars are harmed in the process of making this), cheesecake (a wheel of brie, not for those latose intorlerant), coffee cake (it's just coffee grounds with wipped cream on top), marble cake (hallow cake with round marble filling), and...singlular confetti cake (25)

you serve the cakes. This party has gone well and you are now remembered as a great friend. Surely nothing will go wrong.
(uh oh, the founder seems to be allergic to sprinkles. luckily, it's a sprinkly free confetti cake. so it is edible to those with sprinkle allergies.) > last slice
hamp eats sprinkle leftovers
pop! uh oh.

chaos yippie

birthday person (mentor) disappears :( They'll be fine. Probably. 

'''

