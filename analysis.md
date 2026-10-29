# Analysis: Stacks and Queues

A linked-list stack adds and removes items at the head because the head can be updated directly, so both operations take O(1) time. Adding or removing items at the tail would require extra traversal or a previous-node reference. An array queue must be circular so that empty spaces at the beginning of the array can be reused after items are removed. The modulo operation lets the rear position return to the start of the array when it reaches the end.
