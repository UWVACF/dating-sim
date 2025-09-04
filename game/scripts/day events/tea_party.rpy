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
    show jessie at appear(x_align=0.7)
    jessie "Oh, hey [player_name]! I see you've been invited!" 
    player "Uh...What's going on?" 
    jessie "A tea party, of course!"
    jessie "Would you like some red peppers tea? Or some red peppers cookies? Or red peppers muffins?"
    player "Uh, I'm good for now."
    show jessie at disappear
    n "You gaze around the room. Some familiar faces are also here."
    n "In particular, you notice Founder Alex, whom is supposed to lead the metting that is happening in about...one minute."
    n "He's sat eating a red pepper muffin leisurely while humming a little tune." 
    show alex at appear (x_align=0.75)
    alex happy "Oho! More guests!" 
    alex upset "Do not take from this plate of muffins, I called dips on these."
    player "Founder Alex, don't we have a meeting in...30 seconds?"
    alex neutral "..."
    alex "Well, you see, I am unfortunately occupied with an anomalous incident here."
    alex "It's only natural that I cannot make it to the meeting as I, the benevolent founder, am lending a hand in resolving anomaly outbreaks."
    show alex happy
    n "He dips a cookie in the tea and takes a crisp bite out of it, then makes a slow sip of the pepper tea. He doesn't seem at all urgent in resolving the situation."
    show alex happy at disappear
    n "Sitting opposite to the Founder is someone you would never expect in such a setting."
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
    n "Seeing how enjoyable the Founder and b6 seems to find the snacks, you take a curious piece and try it."
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
    n "Hampter stands up and hop off the chair."
    $ shake_screen(duration=0.1,strength=4,repeat=True,interval=0)
    unknown "{nw}{sc}SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEDOOOOOOOOO{/sc}"
    show purple onlayer top:
        alpha 0.0
        block:
            linear 2.0 alpha 0.5
            linear 2.0 alpha 0.10
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
    hampter sad "I also tried teleporting, but it also knows how to teleport, so it simply chased me and put me here again."
    player "...Surely the tea party will be over soon..?"
    hampter panic "That was also what Jessie said. But it's been 5 hours, [player_name]."
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
    hampter "Not only is its taste in snack awful, the guests it invites are also atrocious!"
    n "You look around again. Surely Hampter don't mean Dr. Jessie or Dr. Alex or b6, right?"
    n "Unless...She meant you..?"
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
    n "It appears that Hampter has attemped to contain him with chair and flowers."
    hide haze green onlayer top
    show hampter upset at appear
    hampter "[player_name]! Please help me shut this down! You're the only one who can freely move right now!"
    show alex upset at appear(x_align = 0.9)
    show hampter upset:
        xzoom -1.0
        move_to(x_align = 0.1)
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
    jessie "Now, now, there's no need to argue! You're making our friend here anxious!"
    jessie "Please don't do anything that will hurt its feelings! It worked very hard to make this tea party!"
    n "The four personnel around the table all look at you, the only person still standing up. Their eyes are filled with anticipation."
    menu:
        n "What will you do?"
        "Find a way to shut down the tea party":
            jump tp_shut
        "It's out of your pay range. Just let it be.":
            jump tp_be
    
    label tp_shut:
        n "hehe"
        # either shut down the party by force (hamp :D, alex D:, jessie D:), or talk it out with the anomaly [not fast enough/hamp runs out of patient/paul escapes containment] (hamp D:, alex D:, jessie :D)
        
        
        
        
        
        

        
        
        
        
        
        return



    label tp_be:
        n "hehe"
        # either leave party [hamp unable you left her there, alex don't care, hurt anomaly's feelings] or stay and chill [hamp explodes, alex is chill, anomaly is chill]
        
        
        
        
        
        
        
        
        
        
        
        
        return

