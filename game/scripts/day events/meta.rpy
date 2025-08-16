image meta_reloading_script = Image("images/cgs/reloading script.png", ypos=1082)

label day_event_meta:
    scene bg hallway
    n "You knock on the door to Dr. Ryz's office, samples in hand."
    ryz "Come in."
    n "You open the door and enter."
    show bg office_ryz
    show ryz at appear
    player "Dr. Aikha told me to drop off these samples for you."
    ryz fury "You can just leave it over there on the desk- the fuck you mean \"Parsing the script failed?\""
    n "You glance over to his computer screen. You see a bunch of text on a gray background that reads:"
    n "\"File \"game/scripts/day events/meta.rpy\", line 8: end of line expected.\""
    n "\"ryz \"You can just leave it over there on the desk- the fuck you mean \\\"Parsing the script failed?\\\""
    n "...Wait what-" 
    ryz surprise "Hey! You're not supposed to be looking at this!"
    player "Uhh, okay..."
    player "Well, the samples are over here. Dr. Aikha also said to report to her at the end of the day."
    ryz neutral "Got it, got it. Oh, I just forgot a quotation mark."
    show bg halway 
    show ryz at disappear
    n "You leave his office and-"
    hide ryz
    n "..."
    n "...Where's the hallway?"
    show bg hallway
    ryz "Oops. \"hallway\", not \"halway\"."
    n "..."  
    n "You continue walking back to your cubicle, as planned."
    show bg cubicle
    n "Luckily, it's intact. No gray screens here. For now, at least."
    n "{w=3}{nw}"
    show black_screen onlayer top
    window hide
    pause 4.0
    window show

    hide black_screen onlayer top
    show black_screen
    ryz "Okay, back on the grind."
    hide black_screen
    n "Welp{nw}"
    show meta_reloading_script onlayer top
    pause 0.5
    hide meta_reloading_script onlayer top

    n "Welp{fast}, back to sper{nw}" 

    show meta_reloading_script onlayer top
    pause 0.7
    hide meta_reloading_script onlayer top

    n "Welp, back to spre{fast}adsheets you go.{nw}"
    n "You beg{nw}"

    show meta_reloading_script onlayer top
    pause 0.7
    hide meta_reloading_script onlayer top

    n "You beg{fast}in talkicng the spreadsh{nw}"

    show meta_reloading_script onlayer top
    pause 0.3 
    hide meta_reloading_script onlayer top

    n "You begin tackling the spreadsh{fast}eets like you're life depensd on{nw}"

    show meta_reloading_script onlayer top
    pause 0.4
    hide meta_reloading_script onlayer top

    n "You begin tackling the spreadsheets like your life depensd on{fast} it."
    show meta_reloading_script onlayer top
    pause 1.0
    hide meta_reloading_script onlayer top

    n "You begin tackling the spreadsheets like{fast} your life depends on it."
    n "It's{w=0.3}{nw}"

    show meta_reloading_script onlayer top
    pause 0.6
    hide meta_reloading_script onlayer top
     
    n "Okay, what is going on??"
    n "You stand up fast, determined to find out."
    n "You remember Dr. Ryz acting sketchily, and decide to find him."
    show bg hallway
    n "You walk over to his office and knock hard."
    ryz "What is it?"
    player "Can I come in?"
    ryz "Yeah, sure. Remember to close the door."
    show bg office_ryz
    show ryz at appear
    player "Dr. Ryz, what are you doing?"
    ryz "Hmm? What do you mean?"
    player "Your computer. What are you doing on it?"
    ryz "Just a bit of writing, you could say. Why?"
    player "Well-"
    ryz "\"Something's off today, and...\" {nw}"
    player "Something's off today, and I think you have something to-"
    ryz "\"Wait, what?\" {nw}"
    player "Wait, what?"
    ryz "\"How did you-\" {nw}"
    player "How did you-"
    ryz "Perfect. This'll do."
    player "Okay, what the hell are you doing? How are you predicting what I'm about to say?"
    ryz happy "Predict? Intern, I'm not predicting. I {i}wrote{/i} you."
    player "You...what?"
    ryz "Take a look at this computer!"
    player "I- what am I looking at?"
    ryz "The code for the game." # add cg when complete
    player "Game??"
    ryz "Yeah. You're just a character in the game. To your credit, though, you're the main character."
    ryz "Here, try changing this line. \"show bg office_ryz\". Change it to, I don't know, \"show lounge\" or something."
    # update cg
    ryz "And n{nw}"
    show meta_reloading_script onlayer top
    pause 0.6
    hide meta_reloading_script onlayer top
    show bg lounge
    ryz "And n{fast}ow: voila!"
    ryz "Everything in this world is controlled by this computer!"
    ryz "It's all code. Always has been, always will be."
    ryz "Now if you excuse me, I need to keep writing this event. La de la~"
    n "..."
    menu:
        n "..."
        "Hijack the computer.":
            jump meta_hijack
        "Leave.":
            jump meta_leave
    

label meta_hijack:
    if "company_issued_gun" not in seen_events:
        n "You slowly pull out your handgun while Dr. Ryz goes back to typing at the computer."
        ryz "Ooh, maybe I can show Helco and Uriel this..."
    else:
        n "You quietly scan the room for any possible weapons."
        n "On the side counter, you see Dr. Ryz's gun. Perfect."

    n "If the computer is really as powerful as he says, then the ends justifies the means."
    n "You pull the trigger."
    hide ryz
    $ shake_screen(preset="strong")
    n "...? He's gone. Vanished into thin air."
    n "Still, you have no time to lose. You quickly hop into his chair and skim the code."
    n "You search through folders and folders, containing everything from information about every single personnel to every single word they'd possibly say."
    n "You have no idea what you're searching for, but you keep opening file after file, PNG after PNG, RPY after RPY."
    n "You eventually find yourself looking through the personnel information. You see a plethora of photos on every single one."
    show aikha upset at appear(x_align = 0.3)
    n "\"aikha upset\"..."
    
    show firewal fury at appear
    n "\"firewal fury\"..."

    show b6 neutral at appear(x_align = 0.7)
    n "\"b6 neutral\"..."

    show aikha upset at disappear
    show firewal fury at disappear
    show b6 neutral at disappear

    n "But something's wrong. Something's missing."
    n "...You."
    n "It says here your \"default name\" is [default_name], but what does that mean?"
    n "You have no sprites. You don't appear in any drawings."
    n "Have you seen yourself in the mirror??"
    n "...Are there even mirrors here?"
    n "You search through the entire codebase, but there's nothing."
    n "Nothing about what you look like. What you sound like. What you do for fun, or for work, even."
    n "You see one singular comment in some random file: \"addicted to coffee,\" but that's it."
    n "Who..."
    n "...Or what are you?"
    ryz "SURPRISE ATTACK!"
    show ryz unique at appear
    show black_screen:
        alpha 0.0
        linear 4.0 alpha 1.0
    n "Those are the last words you hear before you feel your body hit the floor, now missing a bullet-shaped chunk of your face."
    show black_screen:
        alpha 1.0
    hide ryz
    n "...Not that you knew what your face looked like anyways."
    pause 3.0
    show bg cubicle
    show black_screen:
        alpha 0.0
        linear 4.0 alpha 1.0
    aikha "Hey! New recruit!!!"
    n "...You slowly open your eyes."
    aikha "WAKE UP!!"
    n "You feel someone slapping your face lightly."
    aikha "WAKE UP!!!!!!"
    n "And now they're-"
    player "Ow, ow, OW, OW! I'm up, I'm up!"
    aikha "I told you to deliver these samples to Ryz hours ago!!"
    player "Huh? What?"
    aikha "C'mon, it's almost home time! Hurry it up!"
    n "You hurry to your feet, grab the samples and scamper over to Dr. Ryz's office."
    n "You knock on the door to Dr. Ryz's office, samples in hand."
    ryz "Come in."
    n "You open the door and enter."
    show bg office_ryz
    show ryz at appear
    player "Dr. Aikha told me to drop off these samples for you."
    ryz fury "You can just leave it over there on the desk- the fuck you mean \"Parsing the script failed?\""
    player "..."
    n "Uh-"
    ryz neutral "Oh, I just forgot a quotation mark."
    ryz happy "Anyways, thanks for these samples."
    player "Y-yeah. Dr. Aikha also said to report to her at the end of the day. Which is now, I guess."
    ryz "Yeah, I'll be just a moment. Why isn't this working?"
    player "Well then, see you."
    show bg hallway
    n "You quickly but quietly leave the room. As you're closing the door shut behind you, you hear him say:"
    ryz "Oops. \"hallway\", not \"halway\"."
    n "...You quicken your pace."

    $ update_character_points({"ryz": -1})
    return

label meta_leave:
    n "This is a game? You're just a character?"
    n "No. You're not having any of this. You're out of here."
    show bg hallway
    show ryz happy at disappear
    n "You quickly run out the door, in complete denial."
    n "You run down the hall, paranoid, searching for anything out of the ordinary."
    n "Suddenly, an idea hits you, and you sprint over to Dr. Helco's office."
    n "You barge through the door and shout:"
    show bg office_helco
    show helco at appear
    player "DR. HELCO!!!!!!"
    helco "Hello, [player_name]! What is the matter?"
    player "Well, you see-"
    n "You start info dumping onto him about the strange computer in Dr. Ryz's room, and how he predicted your every word."
    player "Do you happen to know anything about it?"
    helco happy "Well, you see {w=0.3}{nw}"
    show meta_reloading_script onlayer top
    pause 0.6
    hide meta_reloading_script onlayer top

    helco neutral "Very interesting! Maybe {w=0.4}{nw}"

    show meta_reloading_script onlayer top
    pause 0.5
    hide meta_reloading_script onlayer top

    helco "Not really {w=0.3}{nw}"

    show meta_reloading_script onlayer top
    pause 0.7
    hide meta_reloading_script onlayer top

    helco "Hmm... Nope!"

    n "He smiles blankly at you."
    n "Your worst nightmare has been confirmed. It seems Dr. Ryz was telling the truth."
    show helco at disappear
    show bg hallway
    n "Panicking, you sprint out of his office."
    n "You see an exit at the very end of the hallway, and run towards it."
    n "Now that you think about it, you've never actually seen anything outside of the facility."
    n "Sure, you remember clocking out, but your memory just ends there, and you reappear in front of the very same computer the next day."
    n "You reach the door and open it, and {w=0.2}{nw}"

    show meta_reloading_script onlayer top
    pause 0.5
    hide meta_reloading_script onlayer top
    show bg office_helco

    show helco at appear
    helco "Hmm... Nope!"

    n "He smiles blankly at you."
    n "Your worst nightmare has been confirmed. It seems Dr. Ryz was telling the truth."
    show helco at disappear
    show bg hallway
    n "Panicking, you sprint out of his office."
    n "You see an exit at the very end of the hallway, and run towards it."
    n "Wait-"

    show meta_reloading_script onlayer top
    pause 0.5
    hide meta_reloading_script onlayer top
    show bg office_helco

    show helco at appear
    helco "Hmm... Nope!"

    n "He smiles blankly at you."
    n "Your worst nightmare has been confirmed. It seems Dr. Ryz was telling the truth."
    show helco at disappear
    show bg hallway
    n "Okay, okay. Stop. Calm down."
    n "Do NOT sprint out of his office and out the door- okay great{nw}"

    show meta_reloading_script onlayer top
    pause 0.5
    hide meta_reloading_script onlayer top
    show bg office_helco

    show helco at appear
    helco "Hmm... Nope!"

    n "STOP. Stop."
    n "Running away's not going to work. The best course of action is probably to confront the problem directly."
    n "Go to Dr. Ryz's office."
    player "..."
    n "Go."
    n "You meekly make your way over to Dr. Ryz's office."
    n "Your mental state is deteriorating, but you manage to reach it. You enter without even bothering to knock."
    show ryz at appear
    show bg office_ryz
    ryz "Hey."
    player "...What's your deal?"
    ryz "Hm?"
    player "Why won't you let me leave?"
    ryz upset "Err, well, we don't really have assets for the outside of the foundation, so..."
    ryz "Now that you mention it, I don't think anyone knows what it's even {i}supposed{/i} to look like..."
    player "..."
    ryz neutral "..."
    ryz "Look."
    ryz "If you're {i}that{/i} upset, I guess I can...pull a few strings."
    player "...?"
    ryz "I can make it so this whole ordeal never happened."
    ryz happy "You won't remember a thing."


    $ update_character_points({"ryz": 1})
