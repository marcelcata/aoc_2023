# (c) Copyright 2023 Marcel


XMAS = ["x", "m", "a", "s"]


class Rule:

    def __init__(self, string):
        """Initialize."""
        rule, destination = string.split(":")
        self.compare = rule[1]
        self.value = int(rule[2:])
        self.index_to_check = XMAS.index(rule[0])
        self.destination = destination
    
    def apply(self, intervals):
        """Return passed and not passed intervals for the input interval."""
        passed, rejected = None, None
        low, high = intervals[self.index_to_check]
        if self.compare == "<":
            if high < self.value:
                return intervals, None
            else:
                passed = intervals.copy()
                passed[self.index_to_check] = (low, self.value - 1)
                rejected = intervals.copy()
                rejected[self.index_to_check] = (self.value, high)
                return passed, rejected
        else:
            if low > self.value:
                return intervals, None
            else:
                passed = intervals.copy()
                passed[self.index_to_check] = (self.value + 1, high)
                rejected = intervals.copy()
                rejected[self.index_to_check] = (low, self.value)
                return passed, rejected


def compute_combinations_from_intervals(intervals):
    """Compute combinations given x, m, a, s ranges."""
    combinations = 1
    for i in [0, 1, 2, 3]:  # Accounting for x, m, a, s
        combinations *= intervals[i][1] - intervals[i][0] + 1
    return combinations


def main():
    with open("day19/input.txt") as f:
        raw_rules, _ = f.read().split("\n\n")

    raw_rules = [raw_rule for raw_rule in raw_rules.split("\n")]

    list_rules = {}
    for raw_rule in raw_rules:
        rule_name, rule_set = raw_rule.split("{")
        rule_set = rule_set.replace("}", "")
        rules = rule_set.split(",")
        list_rules[rule_name] = [Rule(rule) for rule in rules[:-1]] + [rules[-1]]

    state = ("in", (1, 4000), (1, 4000), (1, 4000), (1, 4000))
    queue = [state]

    result = 0
    while queue:
        rule_name, *intervals = queue.pop()
        if rule_name == "A":
            result += compute_combinations_from_intervals(intervals)
            continue
        if rule_name == "R":
            continue
        
        for rule in list_rules[rule_name][:-1]:
            passed, rejected = rule.apply(intervals)
            if passed is not None:
                queue.append((rule.destination, *passed))
            intervals = rejected
            if rejected is None:
                break

        else:
            queue.append((list_rules[rule_name][-1], *intervals))

    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    main()
