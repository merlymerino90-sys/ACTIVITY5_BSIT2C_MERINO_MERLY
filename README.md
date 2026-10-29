# Activity 5: Fundamental Data Structures — Stacks and Queues

## Program description
This Python program demonstrates stacks (LIFO) and queues (FIFO) using array-based and linked-list implementations. It includes a menu-driven test program, a balanced-brackets checker, and a print-queue simulation.

## Files
- `array_stack.py` — fixed-capacity stack using a Python list.
- `linked_stack.py` — stack using linked nodes.
- `array_queue.py` — fixed-capacity circular array queue.
- `linked_queue.py` — queue using linked nodes with front and rear references.
- `main.py` — menu-driven test program and application exercises.
- `analysis.md` — written analysis of linked stacks and circular array queues.
- `sample_runs.txt` — example output for common operations and errors.

## How to run
1. Put all Python files in the same folder.
2. Open a terminal in that folder.
3. Run: `python main.py`
4. Follow the menu choices.

## Notes
- The array-based stack and queue have a default capacity of 5. They can be tested for overflow by adding more than five items without removing any.
- The linked-list implementations do not have a fixed capacity, so their `is_full()` method returns `False`.
- Empty `pop()` and `dequeue()` operations raise descriptive underflow errors.
