# Google Calendar Event Scheduling
# Greedy Strategy - Activity Selection

events = [
    ("College Lecture", 9.0, 10.0),
    ("Team Meeting", 9.5, 11.0),
    ("Lab", 10.0, 11.5),
    ("Project Meeting", 11.0, 12.0),
    ("Seminar", 11.5, 13.0)
]


def activity_selection(events):
    events = sorted(events, key=lambda event: event[2])

    selected = []
    last_finish = -1

    for event in events:
        name, start, finish = event

        if start >= last_finish:
            selected.append(event)
            last_finish = finish

    return selected


def format_time(hour):
    h = int(hour)
    minutes = int(round((hour - h) * 60))

    return f"{h}:{minutes:02d}"


print("===== GOOGLE CALENDAR EVENT SCHEDULER =====")

selected_events = activity_selection(events)

print("\nSelected Non-Overlapping Events:")

for name, start, finish in selected_events:
    print(f"{name:<20} {format_time(start)} - {format_time(finish)}")

print("\nTotal Events Selected:", len(selected_events))
