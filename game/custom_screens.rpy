# This file is for defining and styling custom screens, separate from the built-in ones


screen honing_survey(question, answer1, action1, answer2, action2, answer3, action3, answer4, action4):
    default selected_answer = 0
    frame:
        padding (20, 20)
        xalign 0.3 yalign 0.3
        xsize 0.6 ysize 0.5 
        vbox:
            yfill True
            xfill True
            text question:
                size 50
            textbutton answer1:
                style "honing_survey_answer_button"
                action [action1, SetScreenVariable("selected_answer", 1), Return(1)]
                selected (selected_answer == 1)
                sensitive (selected_answer == 0)
            textbutton answer2:
                style "honing_survey_answer_button"
                action [action2, SetScreenVariable("selected_answer", 2), Return(2)]
                selected (selected_answer == 2)
                sensitive (selected_answer == 0)
            textbutton answer3:
                style "honing_survey_answer_button"
                action [action3, SetScreenVariable("selected_answer", 3), Return(3)]
                selected (selected_answer == 3)
                sensitive (selected_answer == 0)
            textbutton answer4:
                style "honing_survey_answer_button"
                action [action4, SetScreenVariable("selected_answer", 4), Return(4)]
                selected (selected_answer == 4)
                sensitive (selected_answer == 0)

style honing_survey_answer_button:
    xfill True
    size_group "honing_survey_answer_button"
    background "#000000"
    hover_background "#0000ff"
    selected_background "#00cc00"

style honing_survey_answer_button_text:
    color "#dddd00"
    selected_color "#000000"
