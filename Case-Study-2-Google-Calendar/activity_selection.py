# Case Study 2: Calendar event scheduling using Greedy Activity Selection

def select_events(events):
    ordered = sorted(events, key=lambda event: event["finish"])
    selected = []
    last_finish = float("-inf")

    for event in ordered:
        if event["start"] >= last_finish:
            selected.append(event)
            last_finish = event["finish"]

    return selected


if __name__ == "__main__":
    events = [
        {"title": "DSA Lecture", "start": 9, "finish": 10},
        {"title": "Project Meeting", "start": 9.5, "finish": 11},
        {"title": "Lab Session", "start": 10, "finish": 12},
        {"title": "Lunch", "start": 12, "finish": 13},
        {"title": "Club Meeting", "start": 11, "finish": 12},
        {"title": "Study Group", "start": 13, "finish": 14},
    ]

    selected = select_events(events)
    print("GOOGLE CALENDAR - GREEDY EVENT SCHEDULING")
    print("Available events:")
    for event in sorted(events, key=lambda item: item["start"]):
        print(f'{event["title"]}: {event["start"]:g}:00 - {event["finish"]:g}:00')

    print("\nSelected non-overlapping events:")
    for event in selected:
        print(f'{event["title"]}: {event["start"]:g}:00 - {event["finish"]:g}:00')
    print("\nTotal events selected:", len(selected))
