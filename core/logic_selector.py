import random

class RandomSelector:
    def __init__(self):
        self.options = []

    def add_options(self, input_string):
        """
        Takes a string like 'Apple, Orange, Banana' and 
        converts it into a list.
        """
        # BUG: This doesn't remove leading/trailing spaces from items.
        # Hint: Look into the .strip() method.
        self.options = input_string.split(",")

    def select_items(self, count):
        """
        Randomly selects 'count' number of items from the list.
        """
        # TODO: Add a check to ensure 'count' is not greater than len(self.options)
        
        # BUG: This currently only returns the first 'count' items, not random ones.
        # Hint: Use random.sample() for unique random selections.
        selected = self.options[:count] 
        
        return selected