# (c) Copyright 2023 Marcel


class Part:

    def __init__(self, string):
        string = string.replace("{","").replace("}", "")
        x, m, a, s = string.split(",")
        self.values = {
            "x": int(x[2:]),
            "m": int(m[2:]),
            "a": int(a[2:]),
            "s": int(s[2:]),
        }
    
    def sum(self):
        return sum(self.values.values())


def rule_match(rule, part):
    """Return true if part matches the rule."""
    rule = rule.split(":")[0]
    value_to_check = part.values[rule[0]]
    if rule[1] == "<":
        return value_to_check < int(rule[2:])
    if rule[1] == ">":
        return value_to_check > int(rule[2:])


def part_is_approved(part, rule_name, list_rules):
    """Apply rule_name to part."""
    for rule in list_rules[rule_name]:
        if ":" not in rule:
            if rule == "A":
                return True
            if rule == "R":
                return False
            return part_is_approved(part, rule, list_rules)
        if rule_match(rule, part):
            new_rule_name = rule.split(":")[-1]
            if new_rule_name == "A":
                return True
            if new_rule_name == "R":
                return False
            return part_is_approved(part, new_rule_name, list_rules)


def main():
    with open("day19/input.txt") as f:
        raw_rules, machine_parts = f.read().split("\n\n")

    raw_rules = [raw_rule for raw_rule in raw_rules.split("\n")]
    machine_parts = [Part(part) for part in machine_parts.split("\n")]

    list_rules = {}
    for raw_rule in raw_rules:
        rule_name, rule_set = raw_rule.split("{")
        rule_set = rule_set.replace("}", "")
        rules = rule_set.split(",")
        list_rules[rule_name] = rules
    
    approved_sum = 0
    for part in machine_parts:
        if part_is_approved(part, "in", list_rules):
            approved_sum += part.sum()
    
    print(f"Part 1 result: {approved_sum}")


if __name__ == "__main__":
    main()
