# this code is for storing the metadata of ending events
# see event.rpy for documentation on the Event class
init python:
    ending_events = [
        Event(
            label="aikha_1",
        ),
        Event(
            label="neutral_ending",
        )
    ]

    # replace all spaces in labels with underscores
    for event in ending_events:
        event.label = event.label.replace(" ", "_")