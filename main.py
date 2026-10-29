from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def choose_implementation():
    print("\nChoose a data structure:")
    print("1. Array Stack")
    print("2. Linked Stack")
    print("3. Circular Array Queue")
    print("4. Linked Queue")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        return ArrayStack(), "stack"
    if choice == "2":
        return LinkedStack(), "stack"
    if choice == "3":
        return ArrayQueue(), "queue"
    if choice == "4":
        return LinkedQueue(), "queue"

    print("Invalid choice.")
    return None, None


def run_structure(structure, kind):
    while True:
        print("\nOperations:")
        if kind == "stack":
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Display structure")
        print("0. Return to main menu")

        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter a value: ")
                if kind == "stack":
                    structure.push(value)
                else:
                    structure.enqueue(value)
                print("Operation completed.")
                structure.display()

            elif choice == "2":
                if kind == "stack":
                    print("Removed item:", structure.pop())
                else:
                    print("Removed item:", structure.dequeue())
                structure.display()

            elif choice == "3":
                if kind == "stack":
                    print("Top item:", structure.peek())
                else:
                    print("Front item:", structure.peek_front())
                structure.display()

            elif choice == "4":
                print("Is empty?", structure.is_empty())
                structure.display()

            elif choice == "5":
                print("Is full?", structure.is_full())
                structure.display()

            elif choice == "6":
                structure.display()

            elif choice == "0":
                break

            else:
                print("Invalid operation. Please choose again.")

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            structure.display()


def balanced_symbols():
    expression = input("Enter a string containing brackets: ")
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = "([{"
    stack = []

    for symbol in expression:
        if symbol in opening:
            stack.append(symbol)
        elif symbol in pairs:
            if not stack or stack.pop() != pairs[symbol]:
                print("Result: The brackets are NOT balanced.")
                return

    if not stack:
        print("Result: The brackets are balanced.")
    else:
        print("Result: The brackets are NOT balanced.")


def print_queue_simulation():
    jobs = []
    number = input("How many print jobs will you add? ").strip()

    try:
        number = int(number)
        if number < 0:
            print("Please enter zero or a positive number.")
            return
    except ValueError:
        print("Please enter a whole number.")
        return

    for index in range(number):
        print(f"\nPrint job {index + 1}")
        job_id = input("Enter job ID: ").strip()
        try:
            pages = int(input("Enter number of pages: "))
            if pages < 1:
                print("Page count must be at least 1. Job skipped.")
                continue
        except ValueError:
            print("Invalid page count. Job skipped.")
            continue
        jobs.append({"job_id": job_id, "pages": pages})

    print("\nJobs will be printed in FIFO order:")
    if not jobs:
        print("There are no print jobs.")
        return

    while jobs:
        job = jobs.pop(0)
        print(f"Printing job {job['job_id']} ({job['pages']} pages)")


def main():
    while True:
        print("\n=== STACKS AND QUEUES MENU ===")
        print("1. Use a stack or queue implementation")
        print("2. Check balanced brackets")
        print("3. Simulate a print queue")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            structure, kind = choose_implementation()
            if structure is not None:
                run_structure(structure, kind)
        elif choice == "2":
            balanced_symbols()
        elif choice == "3":
            print_queue_simulation()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
