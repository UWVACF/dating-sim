# This file is for defining and styling custom screens, separate from the built-in ones


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
