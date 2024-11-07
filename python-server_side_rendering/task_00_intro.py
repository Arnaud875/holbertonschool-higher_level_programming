#!/usr/bin/python3
"""
Generate invitation from template
"""

from os import path


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Invalid template type")

    if not isinstance(attendees, list):
        raise TypeError("Invalid attendees type")

    if not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Invalid attendees type")

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A") \
            if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location", "N/A")

        personalized_invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_file_name = f"output_{index}.txt"

        if path.exists(output_file_name):
            continue

        try:
            with open(output_file_name, 'w') as file:
                file.write(personalized_invitation)
        except Exception as e:
            continue
