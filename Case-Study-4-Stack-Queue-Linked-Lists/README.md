# Case Study 4: Implementation of Stack and Queue Operations Using Linked Lists

## 1. Introduction
Stacks and queues are linear data structures used in many computing applications. A stack follows **Last In, First Out (LIFO)**, while a queue follows **First In, First Out (FIFO)**. Linked lists allow these structures to grow dynamically without requiring a fixed-size array.

This case study implements both structures using nodes and links.

## 2. Problem Statement
Implement stack and queue operations using a singly linked list. The stack must support push, pop, peek, and display. The queue must support enqueue, dequeue, peek, and display.

## 3. Objectives
- Understand linked-list nodes and references.
- Implement stack operations using a linked list.
- Implement queue operations using a linked list.
- Handle empty-structure cases safely.
- Compare LIFO and FIFO behaviour.
- Analyse the time complexity of the operations.

## 4. Data Structures Used
- **Node:** Contains data and a reference to the next node.
- **Stack:** Maintains a reference to the top node.
- **Queue:** Maintains references to both the front and rear nodes.

## 5. Working Principle
### Stack
1. **Push:** Create a node and connect it before the current top.
2. **Pop:** Remove the top node and move the top reference to the next node.
3. **Peek:** Return the top value without removing it.
4. **Display:** Traverse from top to bottom.

### Queue
1. **Enqueue:** Create a node and attach it after the rear node.
2. **Dequeue:** Remove the front node and move the front reference forward.
3. If the queue becomes empty, set both front and rear to `None`.
4. **Peek:** Return the front value without removing it.
5. **Display:** Traverse from front to rear.

## 6. Example
For the stack, pushing `Book-A`, `Book-B`, and `Book-C` means `Book-C` is on top and will be popped first.

For the queue, inserting `Student-101`, `Student-102`, and `Student-103` means `Student-101` is at the front and will be removed first.

## 7. Time and Space Complexity
| Operation | Time Complexity |
|---|---|
| Stack push | O(1) |
| Stack pop | O(1) |
| Stack peek | O(1) |
| Queue enqueue | O(1) |
| Queue dequeue | O(1) |
| Queue peek | O(1) |
| Display | O(n) |

The structures use O(n) space for n stored elements.

## 8. Applications
- Stack: undo operations, browser history, function-call management.
- Queue: service counters, print queues, task scheduling.
- Linked lists: dynamic collections where the number of elements changes.

## 9. Advantages
- Grows and shrinks dynamically.
- Stack push/pop and queue enqueue/dequeue are O(1).
- Does not require shifting elements as an array-based queue might.

## 10. Limitations
- Each node requires extra memory for a link.
- Accessing an arbitrary element requires traversal.
- Incorrect pointer/reference updates can lose nodes or break the structure.

## 11. Conclusion
This case study implements stack and queue operations with a linked list and demonstrates the difference between LIFO and FIFO. It also shows why maintaining top, front, and rear references makes common operations efficient.

## 12. How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python stack_queue_linked_list.py
```

The sample result is saved in `output.txt`.
