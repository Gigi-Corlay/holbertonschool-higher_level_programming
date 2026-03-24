#!/usr/bin/python3

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.

    Parameters:
        template (str): A string containing placeholders like {name}, {event_title}, {event_date}, {event_location}.
        attendees (list): A list of dictionaries with keys 'name', 'event_title', 'event_date', 'event_location'.

    Behavior:
        - Checks input types and validity.
        - Replaces missing values with "N/A".
        - Creates output files named output_X.txt where X starts at 1.
        - Prints error messages and stops if input is invalid or empty.
    """

    # Check if template is a string
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return

    # Check that each item in the list is a dictionary
    for person in attendees:
        if not isinstance(person, dict):
            print("Error: attendees must be a list of dictionaries")
            return

    # Check if template is empty
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Loop over each attendee and generate their invitation
    for i, person in enumerate(attendees, start=1):
        # Copy the template to avoid modifying the original
        content = template

        # Get values from the dictionary, replace None or missing keys with "N/A"
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        # Replace placeholders in the template with actual values
        content = content.replace("{name}", name)
        content = content.replace("{event_title}", event_title)
        content = content.replace("{event_date}", event_date)
        content = content.replace("{event_location}", event_location)

        # Create the output filename (output_1.txt, output_2.txt, ...)
        filename = f"output_{i}.txt"

        # Write the personalized invitation to the file
        with open(filename, "w") as file:
            file.write(content)

        # Optional: print confirmation message
        print(f"{filename} generated successfully")
