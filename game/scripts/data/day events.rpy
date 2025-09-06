# this file is for storing the metadata of day events and other related variables: day.rpy is for the code

init 10 python:
    # arrays
    # when declaring events, you can omit fields
    day_events = [
        Event(
            label="fire",
            personnel=["aikha", "firewal", "uriel", "helco", "moon"],
        ),
        Event(
            label="test",
            personnel=["helco"],
        ),
        Event(
            label="paul_demure_johnson",
            personnel=["paul"]
        ),
        Event(
            label="ethics_presentation",
            personnel=["chan"],
            tags=["foundation event", "personnel"], 
        ),
        Event(
            label="staring_contest",
            personnel=["lee", "aikha"],
            tags=["break"],
        ),
        Event(
            label="the_big_chase",
            personnel=["plutoes", "syg", "chan", "hamp"],
            tags=["anomaly encounter"],
        ),
        Event(
            label="in_the_dark",
            personnel=["lee", "helco"],
            tags=["anomaly encounter"],
        ),
        Event(
            label="dr_ryz_and_the_goose",
            personnel=["ryz"],
            tags=["personnel"],
        ),
        Event(
            label="company_issued_gun",
            personnel=["alex"],
            tags=["work"],
        ),
        Event(
            label="the_bingo_card_1",
            personnel=["plutoes", "firewal", "alex", "ryz", "aikha"],
            tags=["personnel"],
        ), 
        Event(
            label="yuri",
            personnel=["aikha", "deceased"],
            tags=["personnel"],
        ), 
        Event(
            label="filing_incident_report",
            personnel=["egg", "chan", "alex"],
            tags=["work"],
        ), 
        Event(
            label="aikha_flare",
            personnel=["aikha"],
            tags=["personnel", "incident"],
        ), 
        Event(
            label="didnt_do_it",
            personnel=["syg", "deceased", "chan"],
            tags=["anomaly"],
            # outro_label="ddi_outro"
        ), 
        Event(
            label="trial_and_error",
            personnel=[],
            tags=["anomaly", "personnel", "incident"],
        ), 
        Event(
            label="the_bingo_card_2",
            personnel=["deceased", "helco", "uriel", "ryz", "caffi"],
            tags=["personnel"],
        ),
        Event(
            label="fin",
            personnel=["aikha"],
            tags=["personnel"],
        ),
        Event(
            label="the_common_fridge",
            personnel=["deceased", "helco", "syg", "firewal"],
            tags=["personnel"],
        ),
        Event(
            label="lamp",
            personnel=["venture", "firewal"],
            tags=["anomaly"],
        ),
        Event(
            label="pokanom",
            personnel=["chan", "uriel", "egg", "lee", "b6"],
            tags=["personnel"],
        ),
        Event(
            label="tea_party",
            personnel=["deceased", "alex", "hamp", "jessie"],
            tags=["anomaly"],
        ),
        Event(
            label="escape",
            personnel=["ryz", "aikha", "firewal"],
            tags=["personnel"],
        ),
        Event(
            label="skibidi",
            personnel=["ryz", "caffi", "helco", "meem"],
            tags=["personnel"],
        ),
        Event(
            label="anendophasia",
            personnel=["meme", "venture", "aikha", "plutoes", "alex"],
            tags=["personnel"],
        ),
        Event(
            label="fluke_cake",
            personnel=["hampter", "syg", "alex", "uriel", "egg", "meme", "caffi", "aikha"],
            tags=["incident"],
        ),
        Event(
            label="meta",
            personnel=["ryz"],
            tags=["incident"],
        ),
        Event(
            label="nonsense",
            personnel=["aikha", "plutoes", "firewal", "alex"],
            tags=["personnel"]
        ),
        Event(
            label="showcase",
            personnel=[],
            tags=["personnel"]
        ),

    ]

    # replace all spaces in labels with underscores
    for event in day_events:
        event.label = event.label.replace(" ", "_")

    remaining_day_events = copy.deepcopy(day_events)

    # aikha route
    showcase_events = [
        filter_events(label="fluke_cake")[0],
        filter_events(label="yuri")[0],
        filter_events(label="aikha_flare")[0],
        filter_events(events=fixed_events, label="company_issued_gun")[0],
        filter_events(label="dr_ryz_and_the_goose")[0],
        filter_events(label="anendophasia")[0],
        filter_events(label="fin")[0],
        filter_events(events=ending_events, label="alex_1")[0]
    ]

    # alex route
    # showcase_events = [
    #     filter_events(label="lamp")[0],
    #     filter_events(label="didnt_do_it")[0],
    #     filter_events(label="trial_and_error")[0],
    #     filter_events(events=fixed_events, label="company_issued_gun")[0],
    #     filter_events(label="tea_party")[0],
    #     filter_events(label="nonsense")[0],
    #     filter_events(events=ending_events, label="aikha_1")[0]
    # ]
