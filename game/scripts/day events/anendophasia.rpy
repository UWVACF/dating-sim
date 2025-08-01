label day_event_anendophasia:
    scene bg office
    show alex at right
    show meme sad at center
    alex "...which is why Meme is {i}not{/i} allowed to sell shrooms in our foundation. Is that clear, Meme?"
    meme sad "Yes, Founder Alex."
    alex happy "In that case, you two are both excused. Have a good day!"
    show bg hallway with fade
    show alex at disappear
    meme "Man, and I almost got away with it, too."
    player "Surely there are more profitable and ethical ways of making money than...selling drugs?"
    meme neutral "Nah, nah, you don't get it. This is the premium stuff! Wanna try some?"
    player "Isn't there a literal child in our foundation?"
    meme happy "Naomi! Oh, I love her. She would've bought out my entire stock if frickin' CHAN didn't step in."
    meme fury "Uwuhhbwuhbwuh \"You can't be selling drugs to kids!!!\" uwuhhbwuhbwuhh \"That's an ethical violation!!!\" Who shoved a stick up YOUR ass??"
    player "..."
    meme happy "So did you want to buy some? It's only 7 bucks per gram, but we have a buy-one-get-one-half-off deal right now-"
    player "I'm gonna grab some coffee. See you, Meme."
    meme sad "Aww, lame! And didn't you just have a coffee?"
    player "That one tasted weird. I need another."
    meme neutral "Oh? How do you feel?"
    player "Huh? Fine. Why?"
    meme "Oh, nevermind. See you!"
    show meme at disappear
    show bg lounge
    player "..."
    player "..."
    player "It's awfully quiet."
    player "..."
    player "Oh, the coffee's a lot better than before."
    player "..."
    menu:
        player "..."
        "Go back to work.":
            player "Well, it's time to get back to spreadsheets."
            show bg hallway
            pause 2.0
            show bg cubicle
            player "..."
        "Keep lazing around.":
            player "Maybe 5 more minutes..."
            player "..."
    player "Wait a minute."
    player "Where did the narrator go?"
    show bg hallway
    show caffi at appear
    player "Caffi, have you seen..."
    player "..."
    caffi "Have I seen what?"
    player "Okay, how do I describe this..."
    player "It's like, a voice in your head? Kinda like a narrator, you know? It just describes everything that's going on, usually sarcastically-"
    show caffi at disappear
    caffi "GUYS! THE INTERN'S DELUSIONAL. I REPEAT-"
    player "GOD DAMNIT- okay, nevermind."
    player "I need to find out where it went. Shit."
    player "And now I need to fill in for it. Ugh."

    $ anendophasia_people_asked = 0
    $ anendophasia_asked_alex = False
    $ anendophasia_asked_venture = False
    $ anendophasia_asked_aikha = False
    $ anendophasia_asked_plutoes = False
    label anendophasia_choice:
        menu:
            player "Who do I ask?"
            "Founder Alex.":
                if anendophasia_asked_alex:
                    player "I already asked him. He thinks I'm insane."
                    jump anendophasia_choice
                else:
                    $ anendophasia_asked_alex = True
                    player "Maybe Founder Alex would know something."
                    player "I make my way down the hall to Founder Alex's office."
                    scene bg office
                    show alex at appear
                    alex "Oh, hello, intern! I heard you speaking to somebody in the hall."
                    player "Yeah, I was talking to myself."
                    alex "..."
                    player "Anyways. Have you seen like-"
                    player "Shit, how do I describe this."
                    player "Okay, so, basically, since I joined the foundation, I've had, like, a narrator, right?"
                    player "It kinda just, well, narrates everything I do."
                    player "But for some reason, it's gone now, and it's awfully silent."
                    player "Do you know what might've happened to it?"
                    alex "..."
                    alex "You might be able to find something of use in the mental health ward."
                    player "...Okay, nevermind, sorry to bother you."
                    alex "...Have a good day."
                    player "Yeah, you too."
                    alex "And for the record, schizophrenia {i}is{/i} covered by the company insurance-"
                    player "BYE."
                    show alex at disappear
                    show bg hallway
                    player "Ugh, that was useless."
                    $ anendophasia_people_asked += 1
            "Dr. Venture.":
                if anendophasia_asked_venture:
                    player "I already asked him. He thinks I'm high."
                else:
                    $ anendophasia_asked_venture = True
                    player "Maybe Dr. Venture's alchemy can help me out here."
                    player "I walk down the hall towards Dr. Venture's office-"
                    show venture at appear
                    venture "Hm? What is it, [player_name]?"
                    player "Oh! He opened the door before I got here"
                    venture "Who are you talking to?"
                    player "Uh, no one. But, anyways!"
                    player "I have - well, used to have - this voice in my head that would narrate everything, but it just randomly disappeared."
                    player "Do you know what could've happened to it?"
                    venture "..."
                    venture happy "Are you high?"
                    player "Wh- no!"
                    player "...I don't think so??"
                    venture neutral "I think you're high. Goodbye!"
                    player "I'm just stressed! I'm- wow, okay, he closed the door on me."
                    show bg hallway
                    show venture at disappear
                    player "God damnit."
                    $ anendophasia_people_asked += 1
            "Dr. Aikha.":
                if anendophasia_asked_aikha:
                    player "I already asked them. They think I'm drunk."
                else:
                    $ anendophasia_asked_aikha = True
                    player "Surely Dr. Aikha can help me out here. They'll understand."
                    player "I stroll down the hall to Dr. Aikha's office."
                    player "Wait, I forgot where it was."
                    player "This way? I think?"
                    player "I take a left and- oh, it's a dead end. Shit."
                    player "Maybe this way? There's a little hallway this way."
                    player "There's a door at the end of the hallway. Oh, it says \"Office of Paul Demure Johnson.\" Whoops."
                    player "Actually, I think it was on the other side of the foundation. Ughhhhhhh."
                    player "I start the long trek to the other side of the foundation-"
                    aikha panicked "??? Oh, new recruit, that was you talking in the hallway?"
                    show aikha at appear
                    player "Dr. Aikha, there you are!!"
                    aikha "Are you okay?? Who were you talking to?"
                    player "Dr. Aikha, if I tell you something crazy, can you promise to believe me?"
                    aikha neutral "Oh, uh, sure?! What's up?"
                    player "Okay, so, basically, I used to have this narrator who would just constantly make sassy remarks in my head."
                    player "But earlier today, it disappeared randomly. Do you know what could've happened to it?"
                    aikha pensive "You had this voice in your head, you're saying?"
                    player "Yeah."
                    aikha "For how long?"
                    player "Since I got here. It's really weird."
                    aikha "Hmm..."
                    aikha neutral "And how many drinks did you have last night?"
                    player "GOD- okay, nevermind, bye."
                    aikha "Make sure to drink plenty of water!"
                    show hallway
                    show aikha at disappear
                    player "*sigh*"
                    $ anendophasia_people_asked += 1
            "Plutoes.":
                if anendophasia_asked_plutoes:
                    player "I already asked him. He started sniffing me weirdly."
                else:
                    $ anendophasia_asked_plutoes = True
                    player "Plutoes? Maybe?"
                    player "Where the hell woudl I find Plutoes? Does he even have an office?"
                    player "Oh, well. I choose a random direction and start walking-"
                    show bg office
                    show plutoes at appear
                    player "Oh! Hey Plutoes, have-"
                    player "Woah, what the hell are you doing? Why are you sniffing me??"
                    show plutoes happy
                    player "Hey, listen- OW!"
                    player "A sign? Where did this even come from?"
                    player "\"you smel good. like msuhrooms.\""
                    player "...Thanks?"
                    show plutoes happy at disappear
                    player "Oh. Okay. Bye."
                    show hallway
                    $ anendophasia_people_asked += 1

        hide aikha
        hide plutoes
        hide venture
        hide alex
        
        if anendophasia_people_asked < 4:
            jump anendophasia_choice
    
    player "Damnit, nobody knows what I'm talking about."
    player "What do I even do here?"
    player "Ugh. My head hurts. I need a coffee."
    scene bg lounge
    player "I walk into the lounge and pour myself a cup of coffee."
    player "I take a sip of the coffee. *sip*"
    player "It tastes fine. Could be a bit stronger, I think to myself."
    player "I finish my coffee and-"
    meme "Are you okay???"
    show meme at appear
    player "Oh, hi again, Meme."
    player "Meme walks up to me, looking slightly confused. Probably about my self-narration."
    meme "Yeah, spot on. Why {i}are{/i} you self-narrating?"
    player "I give them a look."
    meme "Err, yeah. You did give me a look. Now I'm giving you one."
    player "Meme is giving me a look back."
    meme "..."
    meme "Say, I left a silver coffee machine sitting next to the toaster this morning. Did you happen to drink from it?"
    player "Yeah, wasn't it the brand new coffee machine Founder Alex told us about?"
    meme "...Did you read the label?"
    player "Uh, no. Why?"
    meme "Meme sighs and starts dragging you through the hallway."
    player "Oh, I appreciate that."
    meme "Yeah, yeah."
    show bg office
    meme "Meme (the coolest person ever) opens the door to their office and pulls you inside before locking the door."
    player "Hey, if you're gonna narrate, you need to be objective!"
    player "Inside the office is-"
    meme "SHHHH! You can't go announcing what I have in here to the world!"
    player "I start whispering. Inside the office is a row of planters, each filled to the brim with soil, sitting underneath a square of fluorescent lightbulbs."
    player "Inside the planters are- are those shrooms???"
    meme "SHHHHHHHHHH!!!! You can't let anyone know about this!"
    meme happy "But isn't it great? It's like planting money!"
    meme "They're so easy to grow, too! All you need is a bit of water and light-"
    player "How the hell- nevermind. "
    player "I walk around the room a bit more. There's nothing particularly of note, except for paperwork scattered everywhere. "
    player "However, on the counter to the left is a silver coffee machine."
    meme neutral "Oh, yeah! That was mine, I accidentally left it in the lounge. Here, did you read the label?"
    player "The label it says:"
    player "\"Premium Shroom Blend, by Meme. Only $10 per cup!\""
    player "\"LIMITED TIME: We are offering a buy-two-for-the-price-of-three-and-get-one-free promotion!\""
    player "\"(While supplies last. Only at participating restaurants. By purchasing our product, you are agreeing to our Terms of Service. For more details, please contact Meme.)\""
    player "..."
    meme "So..."
    player "..."
    meme happy "You owe me $10 bucks!"
    player "You SPIKED my coffee?"
    meme neutral "Well, it wasn't {i}your{/i} coffee, per se-"
    player "Wait, is that why the narrator's disappeared??"
    meme "I still have no idea what narrator you're talking about, but you should calm down-"
    player "I AM CALM!!"
    player "*sigh* How do I, like, undo this?"
    meme "Buddy, you can't just \"undo\" drugs."
    meme happy "At least, not for free!"
    player "..."
    meme "[player_name] is giving me a look."
    player "...Meme pulls out a Ziploc bag filled with blood red mushrooms."
    meme "Not just any mushrooms! These are shrooms curated in the deeper trenches of hell!"
    meme "They're super well renowned for curing any hangover or post-acid trip crash instantly! You'll be restored to perfect condition!"
    meme "Or so rumour has it."
    player "Rumour???"
    meme "I wouldn't know. I don't experience hangovers or the likes. Nothing's strong enough for that."
    player "..."
    meme neutral "It's not that expensive, don't worry!"
    player "How much?"
    meme "$499.99 for one!"
    player "WHAT{nw}"
    meme happy "BUT! I'm willing to offer you a deal! Cuz we're friends and all that, y'know?"
    meme "Instead of that, I'll give you the cure if you advertise my...business a little bit. Catch my drift?"
    player "..."
    meme "[player_name] is giving me a look again!"
    menu:
        player "*sigh*"
        "Cough up $500.":
            jump anendophasia_pay
        "Do the advertising.":
            jump anendophasia_ad

    label anendophasia_pay:
        meme "You'll pay? That works too!"
        meme "What are you gonna pay with? Credit? Debit? Card? E-transfer? Cheque?"
        player "Uh, cash is fine, I think. I need to go to an ATM though."
        meme "Oh, well, I have one right here! Behind you!"
        player "Why???"
        meme "For times like these! See? It works out!"
        meme "So after tax and the processing fee, handling fee, delivery fee, tips, insurance fee, issuer fee, transaction fee, illegal possession of unauthorized materials fee, warranty, transaction fee 2, usage of ATM fee, a charity donation, gas fee, inflation, copyrighted material fee, excessive text in a dialogue box fee, transaction fee 3 and the hidden fee in the Terms of Service you didn't read..."
        meme "Your total is $1491.43!!"
        player "WHAT?? THAT'S ALMOST TRIPLE THE PRICE!!!"
        meme "Sorry, buddy, that's how capitalism works! You can go ahead and use the ATM now~"
        player "Maybe the narrator isn't worth it..."
        player "Sighing to myself, I type in my credentials in the ATM-"
        meme "You should narrate those!"
        player "SHUT UP!"
        player "Just- just take your money."
        meme "Pleasure doing business with you! Here's your shroom!"
        player "...Thanks. So how do I, like, you know?"
        meme "Have you never taken shrooms before?"
        player "No???"
        meme "Just eat it! It's simple."
        meme "Hehe, [player_name] eats the shroom happily."
        player "I am NOT happy!!!"
        player "...So when does it kick in?"
        meme "Oh, it should-"
        $ shake_screen(preset="strong")
        player "WHAT THE-"
        $ shake_screen(preset="strong")
        meme "...happen right now!"
        $ shake_screen(preset="strong")
        n "The world is spinning, spinning."
        player "Jesus christ, I can't-"
        player "Wait."
        player "NARRATOR?"
        n "Hi!"
        n "You quickly scramble to your feet and hug- the wall?? Why??"
        player "WHERE DID YOU GO??"
        n "Well, when you drank Meme's coffee, your mind was so warped you couldn't hear me anymore."
        n "I was here the whole time. You really need to work on your coffee addiction."
        player "HEY! Shut up!"
        meme "I didn't say anything-"
        player "Oh, not you."
        n "You still owe them $10, by the way."
        player "Owe them?? For what??"
        n "The \"Premium Shroom Blend.\""
        meme "Oh yeah! You owe me $10 bucks for the \"Premium Shroom Blend!\""
        player "..."
        player "Didn't I just give you $1500..."
        meme "Yeah, so you should have no problem giving me $10 more!"
        n "Business is business."
        meme "Business is business!!"
        player "..."
        n "You stare bullets at Meme before angrily leaving the room, slamming the door behind you. Rude."
        player "Go do your job without all the sass, please."
        n "You {i}clumsily{/i} make your way down to the lounge, no doubt to feed your coffee addiction once more. In fact, you haven't had a single productive minute since you arrived here today. Rather, you've just been running around like a headless chicken-"
        player "Shut up. Please."
        n "Hehe. All's well that ends well."
        n "And for the record, I am INSULTED that you hesitated so much!!!"
        player "IT WAS $1500!!! THAT'S ONE MONTH OF RENT!!!!"
        n "Maybe I'll disappear again if you think I'm not worth your money!"
        player "NOOOOOOOOOOO"
        return

    label anendophasia_ad:
        meme "Free advertising! Let's GO!!!"