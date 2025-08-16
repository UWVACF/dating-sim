image meta_reloading_script = Image("images/cgs/reloading script.png", ypos=1082)

label day_event_meta:
    scene bg hallway
    n "You knock on the door to Dr. Ryz's office, samples in hand."
    ryz "Come in."
    n "You open the door and enter."
    show bg office_ryz
    show ryz fury at appear
    player "Dr. Aikha told me to drop off these samples for you."
    ryz "You can just leave it over there on the desk- the fuck you mean \"Parsing the script failed?\""
    n "You glance over to his computer screen. You see a bunch of text on a gray background that reads:"
    n "\"File \"game/scripts/day events/meta.rpy\", line 8: end of line expected.\""
    n "\"ryz \"You can just leave it over there on the desk- the fuck you mean \\\"Parsing the script failed?\\\""
    n "...Wait what-" 
    ryz shocked "Hey! You're not supposed to be looking at this!"
    player "Uhh, okay..."
    player "Well, the samples are over here. Dr. Aikha also says to report to her at the end of the day."
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
    n "It's{nw}"

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
    ryz "\"Something's off today, and...\"{nw}"
    player "Something's off today, and I think you have something to-"
    ryz "\"Wait, what?\"{nw}"
    player "Wait, what?"
    ryz "\"How did you-\"{nw}"
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
    







