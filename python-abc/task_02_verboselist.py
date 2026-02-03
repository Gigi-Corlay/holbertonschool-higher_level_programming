#!/usr/bin/python3

class VerboseList(list):
    """
    A subclass of Python's built-in list that prints notifications
    whenever an item is added or removed.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.
        """
        super().append(item)  # call original list append
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with multiple items and print a notification
        with the number of items added.
        """
        x = len(iterable)
        super().extend(iterable)  # call original list extend
        print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification
        before removing.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)  # call original list remove

    def pop(self, index=-1):
        """
        Pop an item at the given index (default last) and print a notification
        before popping. Return the popped item.
        """
        item = self[index]  # get the item to pop
        print(f"Popped [{item}] from the list.")
        return super().pop(index)  # call original list pop
