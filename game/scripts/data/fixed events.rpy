# this code is for storing the metadata of fixed events
# every X days, a random fixed event will be chosen from a pool separate from day events (hr checkup, group photo, company issued gun, etc)
# see event.rpy for documentation on the Event class
init python:
    fixed_events = [
    ]

    # replace all spaces in labels with underscores
    for event in fixed_events:
        event.label = event.label.replace(" ", "_")

    remaining_fixed_events = copy.deepcopy(fixed_events)