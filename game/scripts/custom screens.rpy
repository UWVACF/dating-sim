# This file is for defining and styling custom screens, separate from the built-in ones
# Also includes whatever functions are necessary

screen honing_survey(question, answers_and_actions):
    default selected_answer = -1

    $ answers = [item["answer"] for item in answers_and_actions]
    $ actions = [Function(update_honing_points, {key: value}) for item in answers_and_actions for key, value in item["personnel"].items()]

    frame:
        padding (20, 20)
        xalign 0.3 yalign 0.3
        xsize 0.6 ysize 0.5 
        vbox:
            yfill True
            xfill True
            text question:
                color "#ffffff"
                size 50
            textbutton answers[0]:
                style "honing_survey_answer_button"
                action [actions[0], SetScreenVariable("selected_answer", 0), Return(0)]
                selected (selected_answer == 0)
                sensitive (selected_answer == -1)
            textbutton answers[1]:
                style "honing_survey_answer_button"
                action [actions[1], SetScreenVariable("selected_answer", 1), Return(1)]
                selected (selected_answer == 1)
                sensitive (selected_answer == -1)
            textbutton answers[2]:
                style "honing_survey_answer_button"
                action [actions[2], SetScreenVariable("selected_answer", 2), Return(2)]
                selected (selected_answer == 2)
                sensitive (selected_answer == -1)
            textbutton answers[3]:
                style "honing_survey_answer_button"
                action [actions[3], SetScreenVariable("selected_answer", 3), Return(3)]
                selected (selected_answer == 3)
                sensitive (selected_answer == -1)

style honing_survey_answer_button:
    xfill True
    size_group "honing_survey_answer_button"
    background "#000000"
    hover_background "#0000ff"
    selected_background "#00cc00"

style honing_survey_answer_button_text:
    color "#dddd00"
    selected_color "#000000"


define config.mouse = { }
define config.mouse["monitor"] = [("gui/mouse/mouse default.png", 10.0, 0.0)]
define config.mouse["monitor button"] = [("gui/mouse/mouse button.png", 24, 0.0)]


screen day_intro:
    frame:
        xsize 1920
        ysize 1080
        xpadding 0
        ypadding 0
        xpos 0
        ypos 0
        image "gui/day intro/clock in base.png"

        button:
            background None
            area (410, 5, 1100, 680)
            mouse "monitor"
            action NullAction()

        frame:

            image "gui/day intro/clock in monitor.png"
            xsize 0
            ysize 0
            xpos 395
            ypos -5

            textbutton "Clock in!":
                idle_background "gui/day intro/clock in idle button.png"
                hover_background "gui/day intro/clock in hover button.png"
                action Jump(today_event_label)
                # hovered Function(set_cursor_button)
                
                xpos 340
                ypos 384
                xsize 444
                ysize 107
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5
                text_size 40
                mouse "monitor button"
        
        