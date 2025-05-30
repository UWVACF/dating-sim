label day_event_the_common_fridge:
    scene bg hallway
    n "The clock strikes noon. Lunch time!"
    n "You Jazzercise over to the lounge, relieved at finally being able to break."
    show bg lounge
    n "As you enter the room, you realize you forgot to bring your lunch today. Damn it."
    n "However, salvation comes in the large, rectangular shape of a fridge, on which a sticky note reads, \"COMMON.\" It's not hopeless after all!"
    n "You open the fridge and see a wide assortment of... things. Some are edible, some are legal, and some are none of the above."
    n "Your stomach rumbles."
    menu:
        n "You gotta eat. What do you grab?"
        "The elephant.":
            jump tcf_elephant
        "The skull of poor Yorick.":
            jump tcf_skull
        "The instant noodles and Aloe Vera.":
            jump tcf_noodles
        "\"Frigid Friday Fridge Fries.\"":
            jump tcf_fries
    
    label tcf_elephant:
        n "So we're just not gonna question how an elephant fits in there? No? Okay."
        n "Physics be damned, you take the elephant out of the fridge. Now you have room for the giraffe!" # too obscure of a joke?
        n "The elephant looks at you, trumpets in your face and trots away happily to the lions' party."
        n "We will also disregard how the elephant fits in the hallway, let alone the doorway."
        show layer master:
            shake(preset="strong")
        n "Nevermind. It doesn't."
        show bg hallway
        n "You're devising a plan to kill and cook the elephant when you spot two people walking down the hall towards you."
        show deceased at appear(x_align = 0.3)
        show syg at appear(x_align = 0.7)
        deceased "Did I tell you about that keychain I saw the other day?"
        syg "I don't believe so."
        deceased "Oh! So it was this- who let the elephant out?"
        n "Dr. Deceased's head turns to stare at you. You feel slightly uncomfortable."
        deceased "Yeah, but anyways, I saw this Miku keychain the other day, and I just HAD to get it."
        n "You're trying to figure out what to do when you hear a faint explosion and several voices chanting:"
        "Walbot" "FOR THE WAL! FOR THE WAL!"
        syg "Please do not tell me more."
        deceased "It was like, Miku as a plague doctor! It was fate, it had to be. I'd never seen it before!"
        # gang idk what to write here


    label tcf_skull:
        n "Bone marrow is nutritious. You reach over to the skull and-"
        player "Alas, poor Yorick!" 
        n "Dear god."
        player "I knew him, Horatio - a fellow of infinite jest, of most excellent fancy. He hath bore me on his back a thousand times, and now how abhorred in my imagination it is!"
        n "You're monologuing uncontrollably."
        player "My gorge rises at it. Here hung those lips that I have kissed I know not how oft."
        n "Well, technically, you're soliloquying."
        player "Where be your gibes now? Your gambols? Your songs? Your flashes of merriment that were wont to set the table on a roar? Not one now to mock your own grinning? Quite chapfallen?"
        n "Oh, apparently the actual word is \"soliloquizing.\" Interesting."
        player "Now get you to my lady's chamber, and tell her, let her paint an inch thick, to this favor she must come. Make her laugh at that."
        n "You can't stop. You raise the skull in your hand dramatically as you continue."
        player "Prithee, Horatio, tell me one thing."
        player "HORATIO: What's that, my lord?"
        n "I don't think you're supposed to say that part..."
        player "HAMLET: Dost thou think Alexander looked o' this fashion i' th' earth?"
        player "HORATIO: E'en so."
        player "HAMLET: And smelt so? Pah! {i}[[He puts the skull down.]{/i}"
        n "You put the- Wait, that's my line!"
        player "HORATIO: E'en so, my lord."
        player "HAMLET: To what-"
        show layer master:
            shake
        syg "STOP. Please."
        show syg fury at appear(x_align = 0.3)
        show deceased at appear(x_align = 0.7)
        n "Someone slaps you. You come to your senses and realize that Dr. Deceased and Dr. Syg were standing in front of you for god knows how long, watching your monologue."
        n "You're eternally grateful for their saving you from a fate worse than death."
        syg "I could hear you from all the way down the hall. Please shut up."
        deceased "Don't you know better than to touch suspicious objects?"
        player "Right. Sorry."
        deceased "We should really put this in a containment room or something."
        n "Without thinking, they bend down to pick up the skull and-"
        deceased "Alas, poor Yorick!"
        n "FUCK."
        deceased "I knew him, Horatio - a fellow of infinite jest, of most excellent fancy."
        syg "FUCK."
        n "Dr. Syg slaps Dr. Deceased hard, causing their head to fly off from their body. As and after it sails through the air, it continues the monologue."
        deceased "Where be your gibes now? Your gambols? Your songs?"
        n "Their headless body cradles the skull close to their chest."
        menu:
            n "Should you help?"
            "Save Dr. Deceased from the clutches of Shakespeare.":
                n "You run over to Dr. Deceased's decapitated body and shake it, trying to get them to drop the skull."
                n "In response, they clutch it even more tightly."
                deceased "Now get you to my lady's chamber, and tell her, let her paint an inch thick-"
                n "You shake harder. Still no use."
                n "Suddenly, inspiration hits. You grab their arms and pull hard. Unfortunately, lack of athleticism is doing you no favours."
                n "Dr. Syg catches onto what you're doing and rushes over to help. Together, you dislodge both of Dr. Deceased arms from their shoulders."
                deceased "Prithee, Horatio, tell me one thing."
                n "Carefully, you two start smacking the skull repeatedly against the countertop. After nearly a dozen attempts, their hands finally let go, and the skull soars across the room."
                deceased "HORATIO: What's that, my- HUH? What? What happened?"
                player "You picked up the skull and starting soliloquying."
                n "It's \"soliloquizing.\""
                syg "Just leave it be. Please. You two are giving me a headache, ugh."
                n "He swiftly and coldly leaves the room, with Dr. Deceased trailing sheepishly behind."
                n "Well, you missed out on lunch, but at least you saved someone from high school English PTSD."
                $ update_character_points({"syg": 1, "deceased": 1})

            "Nah.":
                n "You're eternally grateful for their help, but not {i}that{/i} eternally grateful. You slowly turn to leave as Dr. Syg conjures up shadowy tentacles from the floor."
                syg "SHUT UP!"
                deceased "Prithee, Horatio, tell me one thing.\nHORATIO: What's that, my l- {nw}"
                show layer master:
                    shake
                extend "AHHHHHHHHHH"
                n "You can have lunch some other time..."
                $ update_character_points({"syg": -1, "deceased": -1})
                return
                
    label tcf_noodles:
        n "You grab the Shin Ramen instant noodles and two-litre bottle of Aloe Vera."
        n "Not sure why instant noodles are in the fridge, but regardless, you grab a pot and start boiling some water."
        n "..."
        n "..."
        n "Oh shit, the stove was set to simmer. You crank the heat up to high."
        n "..."
        n "..."
        n "You open the Aloe and take a sip. It reminds you of childhood memories."
        n "You also start snacking on the crumby bits of instant noodles. Good stuff."
        n "..."
        show helco at appear
        n "...?"
        helco "Oh, hello!"
        player "Hi, Dr. Helco. What're you doing here?"
        helco "I'm grasping lunch!"
        player "...Grabbing?"
        helco "Yes! Grabbing lunch. As humans do."
        n "He smiles blankly at you." # maybe another word
        n "..."
        n "You check on the water. It's finally boiling! You put the noodles in and cover it."
        player "How's your morning been?"
        helco "Oh, fine, fine. Not much to do today."
        n "Dr. Helco starts rummaging through the cupboards."
        player "What are you looking for?"
        helco "I brought a bag of burning coals today, as a treat. Have you seen it anywhere?"
        player "...Burning coals??"
        helco "Yes! A scrumptious human delicacy."
        player "Uh huh."
        n "He starts looking all around the room: in the fridge, the freezer, under the floor tiles and in the vents."
        helco "Perhaps someone else ate them...No matter! I'll just have some liquid nitrogen instead."
        n "He leaves the room, happily humming to himself."
        n "..."
        n "..."
        n "Oh yeah! You were boiling some noodles. You grab some wooden chopsticks and ." # take a bite?? or what
        n "They don't taste very good. You forgot the flavour packet."
        n "That's better."
        n "Not great, but better."
        n "You ate the Instant Noodles."
        n "You're about to finish cleaning up when you see Dr. Helco re-enter the room with a small vial surrounded by white fumes."
        helco "I found some liquid nitrogen! Would you like some?"
        player "No thanks. I'll literally die."
        helco "Oh. In that case!"
        show helco at disappear
        n "As you walk past him to return to your cubicle, you hear him mutter:"
        helco "Hmm, a little bland still."
        n "...You pick up the pace."
        $ update_character_points({"helco": 1})
        return

    label tcf_fries:
        # RAHH i don't like this
        n "Sitting on the side shelf is a package of \"Frigid Friday Fridge Fries.\""
        n "You grab the Frigid Friday Fridge Fries and find the instructions on how to prepare them."
        n "It says you should bake the Frigid Friday Fridge Fries at 425 Fahrenheit for 10 minutes."
        n "You line a tray with freshly oiled parchment paper and place the Frigid Friday Fridge Fries on top."
        show helco at appear
        helco "Oh, hello!"
        player "Oh, hi Dr. Helco!"
        helco "What are you doing there?"
        player "I'm making these Frigid Friday Fridge Fries."
        helco "In the oven? Forgive me, but I believe we have an air fryer, no?"
        n "You frown. Your friendly fellow frames facts. Shouldn't you be air frying the Frigid Friday Fridge Fries?"
        n "Frankly, you're too famished to falter. You frenziedly fit the frumpy Frigid Friday Fridge Fries into the fryer."
        n "You're fretful, fidgeting frantically for the Frigid Friday Fridge Fries to finish frying."
        helco "Oh, those look..."
        helco "..."
        n "Finally, you find that the Frigid Friday Fridge Fries finished frizzling flawlessly. Fabulous!"
        n "You fastidiously fetch the formerly frigid, currently fervent fries from the fryer, fancying a feast."
        n "Forlornly, you find the Fiery Friday Fridge Fries fare fairly frowzily, fuming a foul fetor."
        n "You forego forcing yourself to finish this fiasco."
        n "You run to the nearest trash can and throw up - figuratively, the flurry of F's, and literally, the Fetid Friday Fridge Fries."
        helco "May I try some?"
        n "..."
        menu:
            n "What do you do?"
            "Spare him from the disgust.":
                player "Believe you me, Dr. Helco, you don't want to be eating these."
                helco sad "I understand. Well then, I shall continue my search for tasteable human food elsewhere."
                helco sad "{size=[helco_text_downsize]}A shame...{/size}"
                show helco sad at disappear
                n "You feel a bit guilty, but frankly, you figure it's probably for the better if no one else tries these."
                n "Still retching, you make your way back to the cubicle."
                $ update_character_points({"helco": -1})
                return
            "Let him try some.":
                player "...Sure."
                n "Dr. Helco takes a flimsy Fiery Friday Fridge Fry and plops it into his mouth."
                show helco pensive
                n "He chews it pensively, showing complete nonchalence."
                helco "I don't taste anything. Perhaps if I try some more..."
                n "He downs the entire tray with no reaction."
                helco neutral "Hm. Still nothing."
                n "You're stunned. The fries that, frankly, flogged your fauces, failed to fructify any form of feedback from Dr. Helco."
                helco "A shame. I saw your reaction to eating these fries and thought I had finally found something I could taste. Apparently not."
                helco happy "Well then, I shall continue my search for tasteable human food elsewhere."
                show helco happy at disappear
                n "...Is this guy taste blind? Is he even human?"
                n "These thoughts run through your head as you make your way back to your cubicle, still retching."
                $ update_character_points({"helco": 1})
                return