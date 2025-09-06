label day_event_tea_party:
    image giant = "images/cgs/friendly_giant.png"
    image purple = "images/day events/purple screen.png"
    scene bg hallway
    n "You're walking down the hallway for what seems like the seventh time this shift for a meeting."
    n "What's the meeting about? You don't remember, but you know that there'll be free coffee."
    n "The better kind. Not the cheap instant brand at the lounge."
    n "As you're walking, you examine the few decorations in the hallway." 
    n "There's a poster advertising a cult meeting. A suspicious potted plant sits further down. A large mass with several eyes leering over you. A stray coupon." 
    player "...Wait a minute." 
    show giant:
        alpha 0.0
        xalign 0.5
        yalign 0.0
        zoom 0.5
        easein 0.9 alpha 1.0
    show purple behind giant:
        alpha 0.0
        block:
            linear 2.0 alpha 0.5
            linear 2.0 alpha 0.15
            repeat
    n "You look up to see the large mass staring at you." 
    n "You can almost see your own reflection in its large glossy eyes. It doesn't seem to be aggressive."
    n "You know that you should probably ring the anomaly outbreak alarm, but you hesitate to doom it to the hands of the Walbot security team."
    n "Perhaps, you can talk to it and it'll return to containment on its own?"
    player "...Hi there. Can I help you?" 
    n "The looming mass leans closer to you."
    n "The anomaly extends a hand, as if to shake yours. What a dapper fellow."
    n "You ignore the huge poster on the wall that says: {b}\"DO NOT make physical contact with unknown anomalies!!!\"{/b} and take the hand."
    unknown "{nw}{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFRIEND!!!!!!{/sc}"
    player "{nw}Hu-? UaghAaauuAAAAAAUUGGGHHHHHHHHHH?!"

    show purple onlayer top:
        alpha 0.0
        easein 0.9 alpha 1.0
    pause 0.5
    scene bg teaparty meeting
    show purple onlayer top:
        alpha 1.0
        easein 1.5 alpha 0.0 
    n "By the time your vision returns, your surroundings have completely transformed." 
    hide purple onlayer top
    n "Your head is spinning and you look around to try and get your bearings."
    n "The only thing you recognize is Dr. Jessie, who's pouring cups of tea for you, herself, and the dapper anomaly from the hallway." 
    n "It's curled up on a frog chair, leaning over the cup of tea. It doesn't seem to have a mouth to drink it." 
    show jessie at appear()
    jessie "Oh, hey [player_name]! I see you've been invited!" 
    player "Uh...What's going on?" 
    jessie "A tea party, of course!"
    jessie happy "Would you like some red pepper tea? Or some red pepper cookies? Or red pepper muffins?"
    player "Uh, I'm good for now."
    show jessie at disappear
    n "You gaze around the room. Some familiar faces are also here."
    hide jessie
    n "In particular, you notice Founder Alex, who is supposed to lead the metting that is happening in about...one minute."
    n "He's sat down eating a red pepper muffin leisurely while humming a little tune." 
    show alex at appear (x_align=0.75)
    alex happy "Oho! More guests!" 
    alex upset "Do not take from this plate of muffins, I called dibs on these."
    player "Founder Alex, don't we have a meeting in...30 seconds?"
    alex neutral "..."
    alex "Well, you see, I am unfortunately occupied with an anomalous incident here."
    alex "It's only natural that I cannot make it to the meeting as I, the benevolent founder, am lending a hand in resolving anomaly outbreaks."
    show alex happy
    n "He dips a cookie in the tea and takes a crisp bite out of it, then takes a slow sip of the pepper tea. He doesn't seem at all urgent in resolving the situation."
    show alex happy at disappear
    n "Sitting opposite to the Founder is someone you would never expect in such a setting."
    hide alex
    show b6:
        xzoom -1.0
        appear(x_align = 0.25)
    n "The head of the Deep Sea Department sits solemnly in front of a plate of red peppers."
    n "You haven't seen him eat before, actually."
    player "...{i}Can{/i} he even eat?"
    n "Oops. Didn't mean to say that out loud."
    n "It seems the mechanical fish heard you. b6 rapidly turns his head towards you."
    b6 "Fool."
    n "He picks up a red piece of pepper that seems a bit different then the rest and unhinges his metallic jaw."
    n "The elongated pepper is quickly minced between gears and wires. The pieces slips down his \"throat\"."
    n "Suddenly, the usual mechanical hums emitting from b6 slows down. He stays as still as a marble statue."
    player "?"
    b6 "..."
    b6 ".."
    b6 "."
    b6 "Fool."
    n "His humming completely stops."
    show b6 at disappear
    n "Seeing how enjoyable the Founder and b6 seem to find the snacks, you take a curious piece and try it."
    hide b6
    hampter_unknown "UAUGHHHHHHHHHH."
    n "It tastes..."
    show shock onlayer top:
        alpha 0.8
    $ shake_screen(layers="top", duration=0.1, strength=4, repeat=True)
    show hampter fury at appear
    hampter "Disgusting!"
    show shock onlayer top:
        alpha 0.0
    n "You turn to see Hampter already sitting in the chair that you were about to sit onto. She scoffs at the piece of cookie you're holding."
    player "Oh, hello, Hampter. What are you doing here?"
    hampter upset "I was abducted! Forced to be at this horrid excuse of a tea party that only serves peppers!"
    player "If you don't like it, can't you leave?"
    hampter "I wish I could! Watch!"
    show hampter upset at disappear
    n "Hampter stands up and hops off the chair."
    $ shake_screen(duration=0.1,strength=4,repeat=True,interval=0)
    unknown "{nw}{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEDOOOOOOOOO{/sc}"
    show purple onlayer top:
        alpha 0.0
        block:
            linear 2.0 alpha 0.4
            linear 2.0 alpha 0.1
            repeat
    unknown "{nw}{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEENOTTTTTTTTTTT{/sc}"
    unknown "{nw}{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEELEAVEEEEEEEEEEE{/sc}"
    show hampter panic at appear
    n "Hampter hops back on the chair."
    show purple onlayer top:
        linear 0.9 alpha 0.10
        linear 0.5 alpha 0.0
    unknown "{sc}SCREE-{sc}"
    $ shake_screen(duration=0)
    hide purple onlayer top
    unknown "{b}Scree.{/b}"
    hampter upset "See. It makes a really irritating screeching noise if you leave your chair."
    hampter sad "I also tried teleporting, but it also knows how to teleport, so it simply chased me and brought me here again."
    player "...Surely the tea party will be over soon..?"
    hampter panic "That was also what Jessie said."
    hampter "Five hours ago."
    hampter "She insists that we treat this anomaly gently and play with it until it's tired, so she can take it back to containment."
    show shock onlayer top:
        alpha 0.8
    $ shake_screen(layers="top", duration=0.1, strength=4, repeat=True)
    hampter fury "Which I would be happy to do otherwise if it weren't for its bad taste in tea parties!"
    show shock onlayer top:
        alpha 0.0
    player "...The pepper snacks aren't {i}that{/i} bad-"
    show shock onlayer top:
        alpha 0.8
    hampter "Not only is its taste in snacks awful, the guests it invites are also atrocious!"
    hide hampter
    show b6:
        xzoom -1.0
        xalign 0.1
        yalign 1.0
    show alex happy:
        xalign 0.9
        yalign 1.0
    show jessie happy:
        xalign 0.5
        yalign 1.0

    n "You look around again. Surely Hampter doesn't mean Dr. Jessie or Dr. Alex or b6, right?"
    n "Unless...She meant you..?"
    hide alex
    hide jessie
    hide b6
    show shock onlayer top:
        alpha 0.0
    show hampter panic
    show haze green onlayer top:
        alpha 0.0
        linear 2.5 alpha 0.5
    n "You feel a little offended. You're about to protest to Hampter when an {i}atrocious{/i} smell hits your nose."
    player "Aughhhhhh."
    hampter upset "AUGHHHHHHH- Not again-"
    hampter "[player_name], since you haven't sat down, can you do me a favor and grab some of those flowers off the wall for me?"
    show hampter upset at disappear
    show haze green onlayer top:
        linear 1 alpha 0.4
    n "Holding your breath, you do as Hampter asked. The fragrance of the flowers make it a little bit better."
    show haze green onlayer top:
        linear 1 alpha 0.3
    n "Hampter picks up the flower you got with her mouth and chucks them across the room into a corner barricaded with chairs."
    show haze green onlayer top:
        linear 1 alpha 0.2
    n "The flowers land on Paul Demure Johnson, who's evidently the source of the smell. The flowers wilt upon contact with him."
    show haze green onlayer top:
        linear 1 alpha 0.1
    n "It appears that Hampter has attemped to contain him with chairs and flowers."
    hide haze green onlayer top
    show hampter upset at appear
    hampter "[player_name]! Please help me shut this down! You're the only one who can freely move right now!"
    show alex upset at appear(x_align = 0.9)
    show hampter upset:
        xzoom -1.0
        move_to(x_align = 0.25)
    alex "Hold on now. You can't shut down this tea party."
    alex "That would be infringing upon the rights of foundation employees!"
    n "You have a {i}slight{/i} feeling \"foundation employees\" means \"Dr. Alex\", and \"rights\" refers to \"not going to the meeting\"."
    show giant behind hampter:
        alpha 0.0
        xalign 0.5
        yalign 0.0
        zoom 0.5
        easein 0.9 alpha 1.0
    unknown "{sc}SCREEE-{/sc}"
    show jessie at appear
    jessie surprise "Now, now, there's no need to argue! You're making our friend here anxious!"
    jessie fury "Please don't do anything that will hurt its feelings! It worked very hard to make this tea party!"
    n "The four personnel around the table all look at you, the only person still standing up. Their eyes are filled with anticipation."
    menu:
        n "What will you do?"
        "Find a way to shut down the tea party":
            jump tp_shut
        "It's out of your pay range. Just let it be.":
            jump tp_be
    
    label tp_shut:
        n "You've resolved to shut this tea party down."
        n "You have a feeling that Dr. Alex would stay here forever at this tea party if he could."
        n "But you really want that premium coffee they offer at the meeting."
        n "And to have that meeting, you need to get Dr. Alex to host it."
        show alex panic
        show jessie upset
        show hampter happy
        player "Sorry, I don't think this tea party should go on."
        alex upset "Nonsense. I don't think that's up to you!"
        show alex upset at disappear
        n "Founder Alex ignores you and continue to enjoy his red tea and red muffins."
        hide alex
        show hampter neutral
        unknown "{sc}No...tea...paaaaaaaaaaaaarty?{/sc}"
        unknown "{sc}SCREEEE-{/sc}"
        jessie surprise "No, no! It's okay! Do not worry, we {i}will{/i} have a tea party!"
        show jessie at disappear
        show giant at disappear
        n "Dr. Jessie panickedly pours more tea for the anomaly to try to calm it down."
        hide jessie
        hide giant
        show hampter happy at move_to(x_align = 0.5)
        hampter happy "Yippie! Time to crash this pathetic party!"
        hampter neutral "I have a plan, [player_name]. And I'll need your help for it."
        hampter "I need you to distract it while I teleport out to get my flamethrower."
        hampter pensive "I forgot where I put it, so I'll need some time to find it before it comes and kidnaps me again."
        hampter happy "Then I'll set this party on fire! {i}That'll{/i} shut it down for good!"
        n "You have never felt so much rage from a hamster. She must {i}really{/i} dislike the red peppers and Johnson."
        show hampter neutral
        n "You look back at Dr. Jessie, who's trying her best to comfort the anomaly. The anomaly seems more content now and is drinking the tea poured for it, despite not having a mouth."
        n "The tea spills onto the ground and it desperately tries to clean it up with the ends of Dr. Jessie's labcoat."
        n "You feel a little bad, looking at the neat decorations the anomaly put up around the room."
        n "You look back at Hampter, who's looking at you with hope in her big, cute eyes. You also feel a bit bad for her, having been stuck here for five hours."
        menu:
            hampter "So, are you ready?"
            "Become Hampter's accomplice in Arson.":
                jump tp_arson
            "Perhaps you can find a more peaceful way.":
                jump tp_talk
        

        label tp_arson:
            player "Okay, I'll help you."
            hampter happy "Yippie!!!!"
            hampter "Okay, go quickly! I'll teleport out once it's distracted!"
            show hampter at disappear
            n "You walk over to Dr. Jessie and the anomaly."
            show jessie surprise at appear(x_align = 0.7)
            show giant behind jessie:
                alpha 0.0
                xalign 0.5
                yalign 0.0
                zoom 0.5
                alpha 1.0
            show jessie fury
            n "Dr. Jessie glares at you, as if warning you to not do anything."
            menu:
                jessie "Can I help you, [player_name]?"
                "Critique the snacks.":
                    jump tp_arson_snacks
                "Discuss the guest list.":
                    jump tp_arson_guests
                "Give the anomaly a handshake":
                    jump tp_arson_hand
                
            label tp_arson_hand:
                n "You go up to the anomaly and extend a hand, just as it did earlier to bring you here."
                show jessie neutral
                unknown "..?"
                n "It extends its arm and you shake hands. What a dapper moment."
                jessie "Well I'm glad you two are getting along!"
                jessie "We should get Hampter here too! So we can all make up and have a nice tea party together!"
                unknown "!!!"
                n "Uh oh. It seems like the anomaly noticed Hampter's absence."
                show giant at disappear
                show jessie surprise
                n "It teleports away."
                hide giant
                show hampter upset at appear(x_align = 0.4)
                show giant behind hampter:
                    zoom 0.5
                    appear(x_align = 0.5, y_align = 0.0)
                n "A moment later, it's back, with Hampter in its arms."
                hampter fury "Ough! I got got!"
                unknown "{sc}DONT...LEAVE...PARTY!!!{/sc}"
                jessie "Oh, I'm so sorry, Hampter. I'm still trying to teach it consent."
                show jessie neutral
                hampter upset "I couldn't find my flamethrower in time...but I got something else!"
                show hampter happy
                n "Hampter pulls out a phone tucked in her fur."
                hampter pensive "If I can't shut this party down myself, I'll just get someone else to do it!"
                show jessie surprise
                n "She dials a number quickly with her paws."
                hampter neutral "Hello yes, inspector? I've encountered an event with healthcode violations!"
                hampter "{b}There are rodents at this tea party!!!{/b}"
                show shock onlayer top:
                    alpha 0.6
                $ shake_screen(layers='top', preset='rumble', repeat='True')
                speaker "{color=#F54927}{nw}WEEEEEEEEEEEEEEEEEEE-WOOOOOOOOOOOOOOOOOO-WEEEEEEEEEEEEEEEEEEE-WOOOOOOOOOOOOOOOOO{/color}"
                n "The emergency alarm rings. You didn't know this classifies as an emergency."
                speaker "{color=#F54927}HEALTHCODE VIOLATION DETECTED. NEUTRALIZATION PROTOCOL INITIATED FOR TARGET ROOM.{/color}"
                n "Fire sprinklers on the ceiling begin to release an unknown mist that smells like disinfectant."
                show shock onlayer top:
                    alpha 0.0
                $ shake_screen(duration=0.1,strength=4,repeat=True,interval=0)   
                unknown "{nw}{sc}NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOooooOOooo{/sc}"
                show jessie sad
                hide shock onlayer top
                show giant at disappear
                $ shake_screen(duration=0)
                show alex fury at appear(x_align = 1.1)
                alex "My cookies!!!!"
                hide giant
                n "He attempts to bag as many as he can into the teapot before dashing out with it."
                show jessie upset
                show alex upset at disappear
                hampter happy "Well, health inspectors say that they will be here in a minute. Can't be caught here as a rodent!"
                show hampter at disappear
                n "Hampter teleports away in a blink."
                jessie "Ah. Now all my progress is undone."
                jessie "That must have scared \"Friendly\" off. It was opening up to me!"
                jessie "I will have to go find it before it gets itself in danger."
                show jessie upset at disappear
                n "Without a teleporting anomaly, you should be free to leave now."
                hide jessie
                hide hampter
                hide alex
                n "On your way out of the room, you see a very {i}pristine{/i} figure by the corner."
                #cg, maybe
                n "Surrounded by chairs and flowers, a very {i}clean{/i} Johnson sits sedately. You can almost say the air around him smells good."
                n "Well, at least someone got something good out of this havoc."
                $ update_character_points({"hampter":1, "alex":-1, "jessie":-1})
                return
         
            label tp_arson_snacks:
                n "You think back to what Hampter complained about earlier. Right, the pepper snacks."
                player "I have some questions about the snacks."
                jessie neutral "Oh, did you try them? How did you find them?"
                player "...Why red bell peppers?"
                jessie "I don't know actually."
                unknown "{sc}Like...Jessie...Bell......Color...Red...Like...{/sc}"
                jessie surprise "Oh! Is it because of my bells?"
                n "The anomaly nods and points at the bell peppers."
                jessie happy "Aw, that's so sweet! Thank you!"
                jessie neutral "Sorry, [player_name]. So you were saying?"
                n "You feel a little bad. But still, the pepper snacks do taste awful, even though you're okay with peppers."
                n "You decide to be honest."
                player "I didn't like them. They were bad."
                show jessie sad
                unknown "{sc}Snacks....not....like...?{/sc}"
                player "...Well, at least they look pretty impressive for being made by an anomaly."
                jessie "Oh."
                jessie "I made them."
                n "Whoops. Now that's awkward."
                unknown "{sc}Jessie...snacks...like...{/sc}"
                player "Uh...I mean, they're okay. I just don't like peppers."
                jessie "No, it's okay. Thank you for your honesty."
                jessie fury "I shall strive to make them better next time! I will make the ultimate red pepper tea party!"
                show jessie neutral
                n "Next time...?"
                n "Just as you are about to suggest a better substitution for red peppers, you hear tiny footsteps behind you."
                jump tp_arson_end

            label tp_arson_guests:
                n "You think back to what Hampter complained about earlier. Right, the guests."
                player "So why was I \'invited\' here?"
                jessie neutral "Hm? I'm not sure, actually."
                jessie "Friendly, why did you invite [player_name]?"
                friendly "{sc}Looks...lonely...{/sc}"
                player "..."
                n "You can't help but feel a little offended, again."
                friendly "{sc}Many...lonely...many...friends...!{/sc}"
                player "...I'm not lonely. I'm at work."
                friendly "{sc}Work...suffer...lonely...{/sc}"
                n "There's no reasoning with \"Friendly\", is there? Though, it's not exactly wrong."
                player "What about the other guests? Are they also invited because they seem...lonely?"
                n "The anomaly nods."
                player "...Even Johnson?"
                n "The anomaly nods again. "
                friendly "{sc}Finance...man...extra...lonely...{/sc}"
                jessie happy "Hahahaha."
                n "She looks over at the barricade of chairs and flowers in the corner."
                jessie "...Yea maybe we should select our guests for our next tea party more carefully, Friendly."
                friendly "?"
                jessie neutral "Friendly here...doesn't have a nose."
                jessie "Or a mouth."
                jessie "So it doesn't understand and see people the way we do. Please understand."
                player "...I see."
                n "You're out of things to say. You can see \"Friendly's\" attention starts to shift off you and towards the tea table."
                n "Then you hear small rapid footsteps come up behind you."
                jump tp_arson_end

        label tp_arson_end:
            show hampter happy at appear(x_align = 0.25)
            show haze orange onlayer top:
                alpha 0.0
                linear 0.5 alpha 0.5
                block:
                    ease 0.5 alpha 0.3
                    ease 0.5 alpha 0.5
                    repeat
            hampter "BAHAHAHAHAH!"
            show jessie surprise
            hampter "Thank you, [player_name]!"
            n "The fire alarm blares. You turn around to see everything on fire."
            n "The smell of roasted bell peppers is actually not half bad."
            jessie "Oh no! What's going on??"
            unknown "{sc}NOOOOOO...TEA...PARTY!!!!!!{/sc}"
            show jessie surprise at disappear
            show giant at disappear
            n "Dr. Jessie and the anomaly scramble to salvage what little can be saved from the fire. You hear a quiet {sc}screee...{/sc} sobbing from the anomaly."
            hampter "Surely they won't come and get me now! Bye bye!"
            show hampter at disappear
            n "Hampter teleports away."
            show alex fury at appear(x_align = 0.8)
            alex "My tea party!"
            alex sad "Why is this happening to me!"
            n "You watch Dr. Alex shove as many cookies as possible into his labcoat pocket."
            n "He sighs as he walks towards the exit, not before taking the teapot with him."
            show alex sad at disappear
            n "Well, that should wrap things up. Hamp and Dr. Alex are gone, and you're sure Dr. Jessie can take care of herself."
            $ shake_screen(persist=0.5, delay=1.0)
            n "You also make your way towards the exit when an explosion goes off behind you. Uh oh."
            show paul at appear(x_align = 0.8)
            n "You turn and realize you have forgotten about the two other personnel in the room."
            "The air around Johnson seems to be {i}extra{/i} flammable. The chairs were all blown away in the explosion, yet he sits unbothered in the sea of fire."
            show b6:
                xzoom -1.0
                appear(x_align = 0.2)
            n "b6 remains unresponsive in the face of the rising flames. Still savouring that chili pepper, perhaps."
            n "You switch on the water sprinkler before leaving the room. Surely they'll be fine, right?"
            $ update_character_points({"hampter":1, "alex":-1, "jessie":-1})
            show haze orange onlayer top:
                linear 0.25 alpha 0.5
                linear 0.25 alpha 0.0
            pause 0.5
            hide haze orange onlayer top
            return

        label tp_talk:
            player "That seems a bit extreme. I think we should find another way."
            hampter panic "What? What's wrong with a bit of arson??"
            player "...Many things. Anyways, I'll try talk to Dr. Jessie and the anomaly, okay?"
            hampter upset "Fine."
            show hampter upset at disappear
            n "You walk over to Dr. Jessie and the anomaly."
            show jessie surprise at appear(x_align = 0.7)
            show giant behind jessie:
                alpha 0.0
                xalign 0.5
                yalign 0.0
                zoom 0.5
                alpha 1.0
            show jessie fury
            n "Dr. Jessie glares at you."
            jessie "Can we help you, [player_name]?"
            player "Hampter wants to leave the tea party."
            show jessie neutral
            unknown "{sc}LEAVEEEEEEEEEEEEEEEEEEEEEEEE?{/sc}"
            unknown "{sc}DO...NOT...LEAVEEEEEEEEEEEEEEE{/sc}"
            unknown "{nw}{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{/sc}"
            n "You feel sadness radiating from the anomaly. Is it...sobbing?"
            jessie "There, there, {i}Friendly{/i}. It's okay."
            unknown "!!!"
            show giant at disappear
            show jessie surprise
            n "Suddenly, the anomaly disappears."
            n "You look around to see that Hampter is gone as well. Another soon-to-be-failed escape attempt."
            jessie upset "Please be gentle with Friendly, [player_name]."
            jessie "Since it can teleport, regular containment methods can't really restrain it."
            jessie neutral "So I've been trying to get it to trust me, and to teach it to not cause trouble."
            jessie "It's not an evil entity. In fact, it's pretty {i}friendly{/i}. Quite innocent, too."
            jessie fury "And it was going so well until you threatened to shut down its tea party!"
            player "But, you can't just kidnap people for a tea party."
            jessie sad "I know, I know. I've been trying to teach it consent. It's not easy, you know."
            jessie "...At least it's not force feeding the food down your throat anymore. Or dangling you by your legs when grabbing you."
            n "You can see the fatigue behind Dr. Jessie's eyes. You gain an appreciation for her work."
            jessie happy "So just hold on for a bit longer, yeah?"
            jessie neutral "I'll get it under control soon."
            jessie "I hope."
            show hampter upset at appear(x_align = 0.4)
            show giant behind hampter:
                zoom 0.5
                appear(x_align = 0.5, y_align = 0.0)
            show jessie surprise
            n "Friendly reappears, with Hampter in their grasp."
            hampter "NOOOOOOOOOOO"
            show hampter at disappear
            n "Friendly places an unwilling Hampter into her seat. She lies face down on the chair, defeated."
            show jessie upset
            n "You hear a light sigh from Dr. Jessie. Perhaps you can help her."
            menu:
                n "You think of what to say to Friendly."
                "Compliment the tea party.":
                    show jessie neutral
                    player "I like the tea party. The decorations are very, uh, cute."
                    friendly "!!!"
                    n "You feel like it's blushing."
                    n "It takes a flower off the wall and hands it to you."
                    friendly "Friend...nice..."
                "Give feedback on the snacks":
                    show jessie neutral
                    player "The pepper snacks...are interesting."
                    friendly "!!!"
                    n "The anomaly bobs excitedly."
                    jessie happy "Oh! I made them! But Friendly was the one who picked the red bell peppers and also taste tested them!"
                    player "...How does it eat?"
                    jessie neutral "..."
                    jessie "Don't worry about it!"
            menu:
                n "It seems interested in you. What's next?"
                "Ask it why it hosted this tea party":
                    player "So why did you host this tea party?"
                    friendly "{sc}Feel...lonely...{/sc}"
                    friendly "{sc}See...other...lonely...{/sc}"
                    friendly "{sc}Many...lonely...many...friends...!{/sc}"
                    jessie "It's been in our foundation for quite a long time. Only recently did I get permission to let it socialize."
                "Take its snacks.":
                    n "The snacks suddenly look very appetizing."
                    show jessie surprise
                    n "You take the cookies placed in front of the anomaly. It's not eating them anyways."
                    n "You regret it the moment your taste buds feel the peppers. You can't help but cough."
                    friendly "!!!!"
                    n "The anomaly brings you something to drink. It's pepper tea. You cough more."
                    show jessie sad
                    friendly "Snacks...bad..?"
            menu:
                n "Now, to wrap it up."
                "Tell it that it's wrong for kidnapping people.":
                    show jessie neutral
                    player "But, it's wrong to kidnap people and force them to stay."
                    friendly "..?"
                    friendly "But...tea...party...!"
                    player "What if I don't want a tea party, so I kidnap you and won't let you be here?"
                    jessie upset "Hey, [player_name]-!"
                    friendly "!!!"
                    n "The anomaly seems to be lost in thought."
                    n "It reluctantly shakes it head."
                    n "Friendly lets out a sad {sc}scree{/sc} as it begins to pack up the cups and teapot."
                    show giant at disappear
                    jessie surprise "Woah."
                    jessie happy "I can't believe that worked."
                    jessie "Maybe I was too nice to it, haha."
                    jessie neutral "You're pretty good at this, [player_name]. Are you interested in more husbandry work?"
                    n "You look back and forth between the anomaly and a very tired Dr. Jessie."
                    player "I think I'm alright. Thanks for the offer."
                    jessie happy "Okay then! Let me know if you change your mind anytime!"
                    show jessie at disappear
                    n "She joins Friendly in tidying up the party."
                    show alex at appear(x_align = 0.8)
                    alex panic "Hey! Why are you taking my food?"
                    player "The party is over, Dr. Alex."

                "Distract it with hide and sneak.":
                    show jessie neutral
                    player "Wanna play a game?"
                    friendly "?"
                    player "I'll be the seeker, and you hide so that I don't find you."
                    friendly "!!"
                    n "The anomaly looks very excited."
                    player "Okay, I'll start counting."
                    player "3...2...1..."
                    show giant at disappear
                    show jessie surprise
                    jessie "Oh no! Where did Friendly go?"
                    player "To hide, probably."
                    jessie "But that doesn't help it! I still need to teach it consent!"
                    jessie neutral "...But I suppose that solves our tea party problem."
                    n "The fatigue seems to be catching up to Dr. Jessie. She sits back down in her chair."
                    jessie "Maybe I'll take a quick nap...Surely I can just go look for Friendly later."
                    show jessie at disappear
                    n "She passes out the moment her head is on the table."
                    show alex at appear(x_align = 0.8)
                    alex "Dr. Jessie! I finished the snacks. Can I have more?"
                    jessie "..."
                    alex pensive "Dr. Jessie?"
                    player "She's asleep."
                    alex "Oh? Then what about the anomaly? \"Frenzy\", was it?"
                    player "It's Friendly. It has gone to play hide and sneak."

            alex panic "What?"
            player "...Dr. Alex, we have a meeting."
            alex "Huh? Didn't I say I'm dealing with an anomaly?"
            player "There's no more anomaly."
            show alex fury
            alex "..."
            alex "Very well!"
            show alex fury at disappear
            n "You watch as Founder Alex storms out of the room."
            n "Finally! You can get your preminum coffee from that meeting."
            $ shake_screen(strength=4)
            n "You skip after Founder Alex when a tea cup misses your head by an inch."
            show haze green onlayer top:
                alpha 0.0
                linear 1 alpha 0.3
            n "You instintively cover your head. An awful smell suddenly hits your nose."
            show paul at appear(x_align = 0.9)
            show hampter fury at appear(x_align = 0.2)
            n "You turn to see that Johnson has broken free of his containment of chairs and flowers. Perhaps he got up when the anomaly no longer screeches at people leaving their seats."
            hampter "FIEND! STAY AWAY!"
            $ shake_screen(strength=4, interval=0.8, repeat=3)
            n "Hampter chucks another teacup at Johnson. Then a teapot. And then a chair."
            n "Johnson on the other hand doesn't seem bothered at all, as he makes his way towards the other exit that Hampter just so happens to be in front of."
            n "In fact, you can almost swear he walks with pride in the new red pepper tea stain on his blazar."
            show hampter fury at disappear
            show paul at disappear
            n "Right before you escape the room, you see a poor b6 from the corner of your eye. He lies unresponsive on the ground, with a teapot next to his head."
            n "You turn the other way and run after Dr. Alex."
            n "As far as events at the foundation go, this went pretty well."
            $ update_character_points({"hampter":-1, "alex":-1, "jessie":1})
            hide haze green onlayer top
            return


    label tp_be:
        show jessie neutral
        show alex neutral
        show hampter upset
        n "You give them a shrug. It's not really up to you whether this tea party runs or not."
        n "You're just a powerless intern, after all."
        show hampter upset at disappear
        n "Hampter shoots you a disapproving look before teleporting out."
        show giant at disappear
        n "The anomaly immediately teleports out after her."
        show jessie happy
        show alex happy
        n "Dr. Jessie pours you another cup of tea. Founder Alex continues to munch on the snacks."
        show jessie happy at disappear
        show alex happy at disappear
        n "Your phone vibrates. You turn on the screen to see the notification for the meeting you're supposed to attend."
        n "It's been postponed by ten minutes. You can still make it if you leave now. The premium coffee awaits."
        n "You look up to find Dr. Jessie and the anomaly staring warmly at you. Hampter has been recaptured and is now back in the chair opposite to you."
        n "Or maybe you can stay. You don't {i}really{/i} want to go back to work, do you?"
        menu:
            n "To stay or to leave, that is the question."
            "Stay":
                n "You decide to stay. This tea party beats sitting at your cubicle and staring at old files for the next 4 hours."
                n "You sit down in your designated seat. The anomaly beams at you, and pours you another cup of red bell pepper tea."
                n "You now have four cups in front of you."
                n "You pick a up a pepper muffin and take a small bite out of it."
                n "It's not actually {i}that{/i} bad, if you wash it down with the tea."
                n "Ooh. Nevermind. There's also pepper in the tea."
                n "Surely you can get use to it if you eat more. You continue to torture your tastebuds."
            
                with default_fade
                n "So it's been...5 hours."
                n "You have gotten used to the taste of bell peppers snacks."
                n "And by \"gotten used to\" I mean \"became numb to the taste of\"."
                n "You gaze out the window. It's dark."
                n "You check your phone. It's 10:36 pm."
                n "You should probably go home now, if you still want to sleep more than four hours before work tomorrow."
                n "You dust off the crumbs on your coat and stand up from your seat."
                show giant behind hampter:
                    alpha 0.0
                    xalign 0.5
                    yalign 0.0
                    zoom 0.5
                    easein 0.9 alpha 1.0
                show purple onlayer top:
                    alpha 0.0
                    block:
                        linear 2.0 alpha 0.35
                        linear 2.0 alpha 0.1
                        repeat
                unknown "{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE{/sc}"
                unknown "{sc}DONT...LEAVE!!!{/sc}"
                show purple onlayer top:
                    linear 0.5 alpha 0.0
                n "You quickly sit back down. Nope. Your eardrums can't take that."
                show giant at disappear
                n "Just as you're wondering what you should do, you hear shuffling next to you."
                show alex at appear(x_align = 0.7)
                n "You watch as the Founder pulls out a sleeping bag from his inner pocket."
                n "He has lined up six chairs so that he can lie comfortably across them in his sleeping bag."
                alex "Goodnight, everyone!"
                show alex at disappear
                n "He puts on an eye mask (over his goggles) and snuggles into his pouch."
                n "You look around. Dr. Jessie is already asleep on the table. She seems exhausted."
                n "Hampter is also passed out on her chair. Teleporting must take a lot of energy."
                n "b6 is still sat in his seat. He has not moved an inch this entire time."
                n "Johnson is...you can't really see him, since he's still behind the wall of chairs."
                show giant behind hampter:
                    alpha 0.0
                    xalign 0.5
                    yalign 0.0
                    zoom 0.5
                    alpha 1.0
                n "The anomaly, though, seems as awake as ever. It notices you and Dr. Alex."
                unknown "{sc}Need...lights...off...?{/sc}"
                show giant at disappear
                n "It mindfully waddles over to the light switch and turns it off."
                show black_screen onlayer master:
                    alpha 0.6
                n "Guess you're spending the night here. Company sleepover!"
                n "You pull four nearby chairs side next to yours and lie down across them."
                n "It's not very comfortable, but the pepper snacks and pepper water in your stomache is making your drowsy."
                show black_screen onlayer master:
                    linear 3 alpha 1.0
                n "You shut your eyes. You can feel your conciousness drifting away."
                show haze green onlayer top:
                    alpha 0.0
                    linear 5 alpha 0.15
                n "..."
                show haze green onlayer top:
                    linear 5 alpha 0.25
                n "Something doesn't feel right."
                n "You were never one to sleep earlier than 12:00. You shouldn't be sleepy right now."
                show haze green onlayer top:
                    linear 5 alpha 0.35
                n "You didn't even do much today, so you can't be tired."
                n "This isn't post food coma either. You literally took a nap for that an hour ago."
                show haze green onlayer top:
                    linear 5 alpha 0.5
                n "Something feels {i}very{/i} wrong."
                n "You wince your nose."
                n "Wait. Your nose."
                n "You haven't been able to smell anything since a few hours ago."
                n "The peppers snacks must have numbed your sense of smell, too."
                n "But now that you've stopped eating, your senses are coming back."
                n "You can now {i}very strongly{/i} smell an atrocious scent from a certain corner."
                show black_screen onlayer master:
                    alpha 0.6
                n "Your eyes shoot open, but it is already too late."
                n "You can barely see through the drowsiness and dizziness from the combination of the smell and the food in your stomache."
                show black_screen onlayer master:
                    alpha 0.6
                    linear 40 alpha 1.0
                n "Hampter and Jessie did not pass out from tiredness; they were taken out by the smell after Hampter ceased maintaining her containment cell for Johnson."
                n "The Founder was spared because of his immortality."
                n "And you were saved temporarily by the peppers, but now it is too late."
                n "You lament that you gave up the premium coffee for this awful end."
                $ update_character_points({"hampter":-1, "alex":1, "jessie":-1})
                return

            "Leave":
                n "You decide to leave. This party really isn't for you."
                n "Since you haven't sat down, surely the anomaly wouldn't screech and re-kidnap you if you leave, right?"
                n "You confidently walk out of the room."
                jessie "Wait, [player_name]-!"
                n "{nw}"
                scene bg room hall
                n "You give yourself a pat on the back for being a hardworking employee."
                show purple onlayer top:
                    alpha 0.0
                    easein 0.9 alpha 1.0
                pause 0.5
                scene bg teaparty meeting
                show giant:
                    alpha 0.0
                    xalign 0.5
                    yalign 0.0
                    zoom 0.5
                    alpha 1.0
                show purple onlayer top:
                    alpha 1.0
                    easein 1.5 alpha 0.0 
                n "Dammit."
                unknown "{sc}DONT...LEAVE...{/sc}"
                n "Nuh uh. You're leaving."
                show giant at disappear
                n "You run out the room again."
                show purple onlayer top:
                    alpha 0.0
                    easein 0.9 alpha 1.0
                pause 0.5
                scene bg teaparty meeting
                show giant:
                    alpha 0.0
                    xalign 0.5
                    yalign 0.0
                    zoom 0.5
                    alpha 1.0
                show purple onlayer top:
                    alpha 1.0
                    easein 1.5 alpha 0.0 
                n "Dammit. Again."
                player "Hey, I need to go back to work."
                unknown "{sc}DONT...LEAVE...{/sc}"
                n "It's like a broken record."
                n "You see across the table that Hampter has just teleported out."
                player "Look! Hampter is gone!"
                unknown "!!!"
                show giant at disappear
                n "Perfect. The anomaly should be occupied with Hampter."
                n "You dash out of the tea party room, once again."
                scene bg room hall
                n "Your plan seems to have worked. You're already three turns away from that cursed room."
                n "The meeting is just on the left. You're almost the-"
                show purple onlayer top:
                    alpha 0.0
                    easein 0.9 alpha 1.0
                pause 0.5
                scene bg teaparty meeting
                show giant:
                    alpha 0.0
                    xalign 0.5
                    yalign 0.0
                    zoom 0.5
                    alpha 1.0
                show purple onlayer top:
                    alpha 1.0
                    easein 1.5 alpha 0.0 
                n "..."
                unknown "{sc}DONT...LEAVE-{/sc}"
                player "SHUT UP."
                show jessie fury at appear(x_align = 0.8)
                jessie "Hey!"
                show alex:
                    xzoom -1.0
                    yalign 1.0
                    appear(x_align = 0.3)
                alex "...One must imagine Sisyphus happy-"
                player "I am NOT Sisiphus. OR happy."
                alex "...Live laugh love, my dear Sisyphus."
                alex pensive "You know what, come over here. I'll offer you a deal."
                show giant at disappear
                show jessie at disappear
                player "You go up to Founder Alex. Still sipping his tea, he turns towards you."
                alex "Seeing you're so desperate to get out, I'll lend you a hand."
                alex "Because I am the great and benevolent Founder Alex."
                player "You stare at him to continue."
                alex "So I wasn't completely prepared when I first came to the tea party."
                alex "I am missing my favourite \"#1 Best Majestic Regal Benevolent Founder Alex mug\". It's in my office."
                alex "If you can find it and bring it to me, I'll help you leave."
                player "How will I have enough time to get it?"
                alex "Hohoho. I will distract the anomaly. Watch."
                n "Founder Alex climbs onto the table."
                show jessie surprise at appear(x_align = 0.8)
                show giant behind jessie:
                    alpha 0.0
                    xalign 0.5
                    yalign 0.0
                    zoom 0.5
                    alpha 1.0
                jessie "Founder Alex???"
                alex unique "HOHOHO! I declear this the best tea party in the name of Founder Alex!"
                unknown "??"
                jessie "Dr. Alex, can you please get off the table???"
                n "Founder Alex grabs a few muffins and starts juggling. He's not the best at it, though."
                n "Everytime he drops a muffin, he grabs another. When he ran out of muffins in his immediate vicinity, he starts grabbing teacups."
                jessie upset "Dr. Alex, please!"
                show jessie upset at disappear
                show alex unique at disappear
                show giant at disappear
                n "You take this chance to escape the room."

    label tp_mug_minigame:            
        scene bg office enter
        n "You actually made it into Dr. Alex's office. You don't want to think about what he must be doing right now to keep the anomaly entertained."
        n "You found a drawer that is labeled in huge, bold text: {size=*3.5}{b}MUGS{/b}{/size}"
        n "You open the drawer. There are about fifty mugs."
        n "Time is of essence. Which mug do you take?"
        $ tp_mug = False
        menu:
            n "Pick a mug."
            "#1 Best Amazing Benevolent Founder in the world":
                jump tp_continue
            "#1 Best Glorious Majestic Regal Founder Alex":
                jump tp_continue
            "#1 Best Majestic Regal Benevolent Founder Alex":
                $ tp_mug = True
                jump tp_continue
            "#1 Best Miraculous Regal Beautiful Founder Alex":
                jump tp_continue
                    
        label tp_continue:
            n "You barely have time to grab the mug when your vision became a purple blur again."
            show purple onlayer top:
                alpha 0.0
                easein 0.9 alpha 1.0
            pause 0.5
            scene bg teaparty meeting
            show giant:
                alpha 0.0
                xalign 0.5
                yalign 0.0
                zoom 0.5
                alpha 1.0
            show purple onlayer top:
                alpha 1.0
                easein 1.5 alpha 0.0 
            unknown "{sc}DONT...LEAVE-{/sc}"
            player "Founder Alex, I got your mug!"
            show alex happy at appear(x_align = 0.8)
            alex "Wonderful!"
            show giant at disappear
            n "He grabs the mug off your hand and inspects it."
            if tp_mug == False:
                alex pensive "This isn't the right mug."
                player "Huh?"
                alex "I wanted my \"#1 Best Majestic Regal Benevolent Founder Alex mug\"."
                player "Oh."
                alex "Tch. Go get the right mug!"
                show alex unique at disappear
                n "He climbs onto the table again."
                n "You better get going."
                jump tp_mug_minigame
            else:
                alex happy "Oho! You're actually capable!"
                player "Can I leave now?"
                alex neutral "Of course, of course."
                show alex at disappear
                n "Dr. Alex, with his new mug in hand, got off his chair and walks over to the one appointed as yours."
                $ shake_screen()
                n "He grabs the chair and yeets it out the window."
                show jessie surprise at appear(x_align = 0.5)
                jessie "Dr. Alex!!!!"
                show alex at appear(x_align = 0.8)
                alex "Whoops. My hands slipped."
                jessie upset "..."
                show jessie upset at disappear
                player "...So what does that do?"
                alex "Hm? Well, you have no more chair, so you cannot be at this tea party!"
                player "Is it that simple?"
                alex pensive "Well, that anomaly is simple."
                player "I could've done that myself."
                alex neutral "Nope. That would be property damage. Your paycheck for the entire internship doesn't even cover a quarter of that window."
                player "..."
                alex "Well then, off you go!"
                show alex at disappear
                n "Founder Alex turn back and continue enjoying his food."
                n "You turn and leave, half expecting to be teleported again."
                scene bg room hall
                n "But you made it all the way outside. No screeching, no teleports."
                n "You quickly run to the meeting, hoping there are still that premium coffee left."
                $ update_character_points({"hampter":-1, "alex":1, "jessie":-1})
                return