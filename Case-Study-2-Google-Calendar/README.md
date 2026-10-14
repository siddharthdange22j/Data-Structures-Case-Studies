# Case Study 2: Google Calendar Event Scheduling Using a Greedy Algorithm

## 1. Introduction
Calendar applications help users organise meetings, lectures, appointments, and personal activities. When several events overlap, a user may not be able to attend every event. An algorithm can help select a maximum-size set of events that do not overlap.

This case study models a calendar schedule using the **Greedy Activity Selection** algorithm. It is an educational simulation and is not connected to Google's actual Calendar service.

## 2. Problem Statement
Given a set of events with start and finish times, select the maximum number of mutually compatible events, assuming the user can attend only one event at a time.

## 3. Objectives
- Understand the greedy algorithm design technique.
- Represent calendar events using records.
- Sort events by finishing time.
- Select a maximum-size set of non-overlapping events.
- Analyse the time complexity and limitations of the approach.

## 4. Data Structures and Algorithm Used
- **List:** Stores all events.
- **Dictionary:** Represents each event with a title, start time, and finish time.
- **Greedy Activity Selection:** Selects the compatible event that finishes earliest, then repeats the process.

## 5. Working Principle
1. Store each event's title, start time, and finish time.
2. Sort all events in increasing order of finish time.
3. Select the first event, because it finishes earliest.
4. Check each remaining event in that order.
5. Select an event if its start time is greater than or equal to the finish time of the last selected event.
6. Update the finish time and continue until all events have been checked.
7. Display the selected schedule.

## 6. Example
Suppose the available events are:

| Event | Start | Finish |
|---|---:|---:|
| DSA Lecture | 9:00 | 10:00 |
| Project Meeting | 9:30 | 11:00 |
| Lab Session | 10:00 | 12:00 |
| Club Meeting | 11:00 | 12:00 |
| Lunch | 12:00 | 13:00 |
| Study Group | 13:00 | 14:00 |

The algorithm selects a compatible schedule by considering the earliest finishing event first. Events that overlap with a selected event are skipped.

## 7. Time and Space Complexity
| Operation | Complexity |
|---|---|
| Sorting events | O(n log n) |
| Scanning events | O(n) |
| Overall time | O(n log n) |
| Extra space for selected events | O(n) |

The sorting step dominates the overall time complexity.

## 8. Applications
- Selecting non-overlapping meetings.
- Scheduling classroom activities.
- Planning appointments.
- Choosing compatible tasks in a timetable.

## 9. Advantages
- Simple and efficient.
- Easy to implement and explain.
- Produces an optimal maximum-cardinality selection for the standard activity-selection problem.

## 10. Limitations
- It maximises the number of events, not their importance or value.
- It assumes event start and finish times are known.
- Real calendar applications may need priorities, reminders, time zones, travel time, and user preferences.

## 11. Conclusion
The case study demonstrates how a greedy algorithm can select non-overlapping events efficiently. It shows how sorting by finish time leads to an optimal solution for the standard activity-selection problem.

## 12. How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python activity_selection.py
```

The sample result is saved in `output.txt`.
