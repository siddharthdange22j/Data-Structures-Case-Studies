# 📅 Google Calendar Application using Greedy Strategy

## 1. Introduction

Calendar applications are used to manage meetings, lectures, appointments, and other events.

When multiple events have overlapping timings, an activity-selection approach can be used to select the maximum number of non-overlapping events.

This case study demonstrates the **Greedy Strategy** using the **Activity Selection Algorithm**.

## 2. Problem Statement

Develop a calendar scheduling system that selects the maximum number of non-overlapping events using the Greedy Strategy.

## 3. Example

| Event | Start | Finish |
|---|---:|---:|
| College Lecture | 9:00 | 10:00 |
| Team Meeting | 9:30 | 11:00 |
| Lab | 10:00 | 11:30 |
| Project Meeting | 11:00 | 12:00 |
| Seminar | 11:30 | 13:00 |

## 4. Greedy Strategy

The algorithm selects the event that has the **earliest finishing time**.

After selecting an event, the next selected event must start at or after the finish time of the previously selected event.

## 5. Working

Events are first sorted according to their finishing time.

For the given example, the selected events are:

```text
College Lecture → 9:00 - 10:00
Lab             → 10:00 - 11:30
Seminar         → 11:30 - 13:00
```

Therefore, 3 non-overlapping events are selected.

## 6. Algorithm

```text
1. Sort events according to finish time.
2. Select the first event.
3. Store its finish time.
4. Check every remaining event.
5. If its start time >= previous finish time:
       Select the event.
6. Update the finish time.
7. Continue until all events are checked.
```

## 7. Complexity Analysis

Sorting the events requires:

```text
O(n log n)
```

The selection process requires:

```text
O(n)
```

Overall complexity:

```text
O(n log n)
```

## 8. Real-World Applications

- Calendar scheduling
- Meeting scheduling
- Classroom timetable management
- Appointment scheduling
- Conference scheduling
- Job scheduling

## 9. Advantages

- Simple to implement.
- Efficient for scheduling problems.
- Reduces conflicts between selected events.
- Works efficiently after sorting the activities.

## 10. Conclusion

The Greedy Strategy can be applied to calendar scheduling through the Activity Selection Problem. By selecting compatible events in increasing order of finishing time, the algorithm obtains a maximum-size set of non-overlapping activities for this standard scheduling problem.

## Run the Program

```bash
python activity_selection.py
```
