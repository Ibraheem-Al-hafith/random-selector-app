import random

class RandomSelector:
    def __init__(self):
        self.options = []

    def _clean_input(self, input_string):
        """Helper to convert comma-separated string into a cleaned list."""
        if not input_string:
            return []
        return [item.strip() for item in input_string.split(",") if item.strip()]

    def select_items(self, input_str, count):
        """Logic for Tab 1: Simple Selection"""
        options = self._clean_input(input_str)
        if not options:
            raise ValueError("The list of items is empty.")
        if count > len(options):
            raise ValueError(f"You only have {len(options)} items, but tried to pick {count}.")
        return random.sample(options, count)

    def assign_mappings(self, candidates_str, targets_str):
        """Logic for Tab 2: General Random Mapping"""
        candidates = self._clean_input(candidates_str)
        targets = self._clean_input(targets_str)
        
        if not candidates or not targets:
            raise ValueError("Both Candidates and Targets must have items.")
        
        # Shuffle both for maximum entropy
        random.shuffle(candidates)
        random.shuffle(targets)
        
        # Pair them (zip stops at the length of the shortest list)
        mappings = list(zip(candidates, targets))
        return mappings, len(candidates), len(targets)