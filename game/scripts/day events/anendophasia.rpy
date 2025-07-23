init python:
    anendophasia_wave_str = 0
    def wavy_text_wrapper(text):
        return f"\{{bt={anendophasia_wave_str}}} {auto_pause(text)}{{/bt}}"


label day_event_anendophasia:
    $ config.say_menu_text_filter = wavy_text_wrapper
    scene bg office
    show alex at right
    show meme at center
    alex "...which is why Meme is {i}not{/i} allowed to sell shrooms in our foundation. Is that clear, Meme?"
    meme sad "Yes, Founder Alex."
    alex "In that case, you two are both excused. Have a good day!"
    show bg hallway with fade
    meme "Man, and I almost got away with it, too."
    player "Surely there are better and more ethical ways of making money than selling drugs?"
    meme neutral "Nah, nah, you don't get it. This is the premium stuff! It's worth a lot. Wanna buy some?"
    player "Isn't there a literal child in our foundation?"
    meme happy "Naomi! Oh, I love her. She would've bought out my entire stock if frickin' Chan didn't step in."
    meme angry "Uwuhhbwuhbwuh \"You can't be selling drugs to kids!!\" uwuhhbwuhbwuhh! What a stick in the mud."
    player "..."
    meme happy "So did you want to buy some? It's only 7 bucks per gram, but I'll give you a discount-"
    player "I'm gonna grab some coffee. See you, Meme."
    meme neutral "Aww, lame! And didn't you just have a coffee?"
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
    player "It's like, a voice in your head? Kinda like a narrator, you know? It just describes everything that's going on, sometimes sarcastically-"
    show caffi at disappear
    caffi "GUYS! THE INTERN'S DELUSIONAL. I REPEAT-"
    player "GOD DAMNIT- okay, nevermind."
    player "I need to find out where they went. Shit."
    player "Shit. How do I just lose a voice in my head?"
    player "How do I even have a voice in my head?"
    player "Anyways, I need to ask someone."

    $ anendophasia_people_asked = 0
    $ anendophasia_asked_alex = False
    $ anendophasia_asked_venture = False
    $ anendophasia_asked_aikha = False
    $ anendophasia_asked_plutoes = False
    label anendophasia_choice:
        menu:
            player "Who do I ask?":
                "Founder Alex.":
                    if anendophasia_asked_alex:
                        player "I already asked him. He thinks I'm insane."
                        jump anendophasia_choice
                    else:
                        $ anendophasia_asked_alex = True
                        player "Maybe Founder Alex would know something."
                        scene bg office
                        show alex at appear
                        alex "Intern! What brings you here?"
                        player "Founder Alex! Have you seen like-"
                        player "Shit, how do I describe this."
                        player "Okay, so, basically, I have a narrator, right?"
                        player "It kinda just, well, narrates everything I do."
                        player "But for some reason, they're gone now, and it's awfully silent."
                        player "Do you know what might've happened to it?"
                        alex "..."
                        alex "You might find some help in the mental health ward."
                        player "NO- okay, nevermind, sorry to bother you."
                        alex "...Have a good day."
                        player "Yeah, you too."
                        alex "And for the record, schizophrenia {i}is{/i} covered in the company insurance-"
                        player "BYE."
                        scene bg hallway
                        player "Ugh, that was useless."
                "Dr. Venture.":
                        if anendophasia_asked_venture:
                            player "I already asked him. He thinks I'm high."
                        else:
                            $ anendophasia_asked_venture = True
                            player "Maybe Dr. Venture's alchemy can help me out here."
                            show bg office
                            show venture at appear
                            venture "Hm? What is it, [player_name]?"
                            player "So, uh, basically..."
                            player "I have - well, used to have - this voice in my head that would narrate everything, but it just randomly disappeared."
                            player "Do you know what could've caused it?"
                            venture "..."
                            venture happy "Are you high?"
                            player "Wh- no!"
                            player "...I don't think??"
                            venture neutral "I think you're high. Good talk."
                            player "I- wow, okay, he closed the door on me."
                            scene bg hallway
                            player "God damnit."
                "Dr. Aikha.":
                    if anendophasia_asked_aikha:
                        player "I already asked them. They think I'm drunk.."
                    else:
                        $ anendophasia_asked_aikha = True
                        player "Surely Dr. Aikha can help me out here. They'll understand."
                        show bg office
                        show aikha at appear
                        aikha "Oh hey! New recruit? You okay?"
                        player "Dr. Aikha, can I trust you to believe me?"
                        aikha "Oh, uh, sure! What's up?"
                        player "Okay, so, basically, I used to have this narrator who would just constantly make sassy remarks in my head."
                        player "But randomly, they've disappeared. Do you know what could've happened to them?"
                        aikha pensive "You had this voice in your head, you're saying?"
                        player "Yeah."
                        aikha "For how long?"
                        player "Since I got here. It's really weird."
                        aikha "Hmm..."
                        aikha neutral "And when was the last time you drank?"
                        player "GOD- okay, nevermind, bye."
                        aikha "Make sure to drink plenty of water!"
                        scene hallway
                        player "*sigh*"
                "Plutoes.":
                        
        $ anendophasia_people_asked += 1
        if anendophasia_people_asked < 4:
            jump anendophasia_choice
    
    $ config.say_menu_text_filter = auto_pause