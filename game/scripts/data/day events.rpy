# this file is for storing the metadata of day events and other related variables: day.rpy is for the code

init python:
    import copy
    # variables
    day_number = 1
    
    day_threshold = 11 # max number of days
    
    # the chance of getting an ending event instead of a day event
    ending_chance = 1.0 
    
    current_ending = None # set to a personnel name if in the process of reaching an ending

    character_point_threshold = 6 # required amount of points to see an ending gate

    # TODO: determine if we just want a fixed chance of having an event with one of the three (e.g. 75% the event guaranteed has one of them)
    base_weight = 10 # the base weight value of an event
    bonus_weight_for_honed = 2 # the bonus weight given to events with honed personnel
    bonus_weight_per_point = 1 # the bonus weight per point given to events with certain personnel

    current_tags = {} # dictionary of how many tags have been gotten

    seen_events = [] # SORTED array of seen events, where the last entry is the most recently seen

    # day event class declaration just to hold values easily
    # EVENTS ARE CONSTANTS, TO BE MODIFIED BY HAND ONLY, NOT VIA CODE
    class Event():
        def __init__(
            self,
            label = "not_found", # the label of the event WITHOUT day_event_: MUST BE snake_cased
            personnel = None, # an array of personnel names involved in the event, route-able or not
            see_before = 0, # the day during and before which the event can be viewed (the last day this can be viewed, inclusive)
            see_after = 0, # the day during and after which the event can be viewed (the first day this can be viewed, inclusive)
            prereqs = None, # an array of prerequisite labels
            prereq_tags = None, # a dictionary of prereq tags {tag: min_count_to_see_event} - can also be variables (incidents_resolved, character points)
            antireqs = None, # an array of antirequisite labels
            antireq_tags = None, # a dictionary of antireq tags: if you see x or more, you are locked out {tag: x} - can also be variables
            chain = "", # a SINGLE label indicating the event that must directly precede this one
            intro_label = "", # the label of the custom intro, if any
            outro_label = "", # the label of the custom outro, if any 
            tags = None # an array of tags used for categorization for prereq tags and antireq tags
        ):
            self.label = str(label)
            self.see_before = see_before
            self.see_after = see_after
            self.chain = str(chain)
            self.intro_label = str(intro_label)
            self.outro_label = str(outro_label)

            self.personnel = list(personnel) if personnel is not None else []
            self.prereqs = list(prereqs) if prereqs is not None else []
            self.antireqs = list(antireqs) if antireqs is not None else []
            self.tags = list(tags) if tags is not None else []

            self.prereq_tags = dict(prereq_tags) if prereq_tags is not None else {}
            self.antireq_tags = dict(antireq_tags) if antireq_tags is not None else {}

    # returns an array of events with the following properties
    # all parameters are optional - you probably only want to use one or two filters at a time, MAYBE three
    def filter_events(
        events = None, # can also specify it to be day_events (instead of remaining day events) or character_events
        label = "", # should probably only be used for character_events
        personnel = None, # array, finds event with ALL listed personnel
        viewable_on_day = 0, # finds events viewable on this day, according to see_before and see_after
        prereqs = None, # array, finds events with ALL listed prerequisite labels
        prereq_tags = None, # dictionary, finds events with ALL listed prereq tags of value at LEAST x
        antireqs = None, # array, finds events with ANY listed antireq labels
        antireq_tags = None, # dictionary, finds events with ANY listed antireq tags of value GREATER THAN x
        chain = "", # finds the UNIQUE event with that chain
        tags = None # array, finds events with ALL listed tags
    ):
        if events is None:
            events = remaining_day_events
        
        filtered = []

        label = label.replace(" ", "_")
        
        for event in events:
            if label and event.label != label:
                continue

            if personnel and not all(p in event.personnel for p in personnel):
                continue
                
            if viewable_on_day > 0:
                if event.see_before != 0 and viewable_on_day > event.see_before:
                    continue
                if event.see_after != 0 and viewable_on_day < event.see_after:
                    continue
            
            if prereqs and not all(req in event.prereqs for req in prereqs):
                continue
                
            if prereq_tags:
                if not event.prereq_tags:
                    continue
                if not all(tag in event.prereq_tags for tag in prereq_tags):
                    continue
            
            if antireqs and any(antireq in event.antireqs for antireq in antireqs):
                continue
                
            if antireq_tags:
                if any(tag in event.antireq_tags for tag in antireq_tags):
                    continue
            
            if chain and event.chain != chain:
                continue
                
            if tags and not all(tag in event.tags for tag in tags):
                continue
                
            filtered.append(event)
        
        return filtered
            
    ################################# DAY EVENTS #################################

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
        )
        Event(
            label="escape",
            personnel=["ryz", "aikha", "firewal"],
            tags=["personnel"],
        )
    ]

    # replace all spaces in labels with underscores
    for event in day_events:
        event.label = event.label.replace(" ", "_")

    remaining_day_events = copy.deepcopy(day_events)

    day_complete_remarks = [
        "Another day survived at this crazy place.",
        "Check that day off.",
        "Phew. Tough day.",
        "aughhhhHHHHHHHHHhhhh",
        "Not a bad day, I suppose.",
        "Could've been worse.",
        "At least it's over.",
        "..."
    ]

    heading_home_remarks = [
        "Well, I should get going.",
        "Home time!",
        "I'm off the clock.",
        "Signing off.",
        "Welp, let's go.",
        "At least I'm free now.",
        "Get me out get me oug getm ouget mgetou mteot"
    ]

    showcase_events = [
        filter_events(label="the_big_chase")[0],
        filter_events(label="ethics_presentation")[0],
        filter_events(label="the_bingo_card_1")[0],
        filter_events(label="staring_contest")[0],
        filter_events(label="the_common_fridge")[0],
        filter_events(label="pokanom")[0],
        filter_events(label="the_bingo_card_2")[0],
        filter_events(label="in_the_dark")[0],
        filter_events(label="fire")[0],
        filter_events(label="didnt_do_it")[0],
    ]

    ## inter-event variables here
    didnt_miku_bingo2 = 0