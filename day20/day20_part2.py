# (c) Copyright 2023 Marcel
import numpy


class FlipFlop:

    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = "off"

    def reset(self):
        self.state = "off"

    def on_pulse_received(self, pulse, sender):
        if pulse == "high":
            return []
        else:  # It's a low pulse
            if self.state == "off":
                self.state = "on"
                return [(self.name, "high", output) for output in self.outputs]
            else:  # State was on
                self.state = "off"
                return [(self.name, "low", output) for output in self.outputs]


class Conjunction:

    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.memory = {}

    def init_memory(self, list_of_modules):
        for _, module in list_of_modules.items():
            if self.name in module.outputs:
                self.memory[module.name] = "low"

    def on_pulse_received(self, pulse, sender):
        self.memory[sender] = pulse

        # Check that in all the memory there's all highs
        for memory_pulse in self.memory.values():
            if memory_pulse == "low":  # If there's a low, send a high
                return [(self.name, "high", output) for output in self.outputs]

        # Otherwise send a low (all of them are high)
        return [(self.name, "low", output) for output in self.outputs]


class Broadcaster:

    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs


    def on_pulse_received(self, pulse, sender):
        return [(self.name, "low", output) for output in self.outputs]


def main():
    with open("day20/input.txt") as f:
        raw_modules = f.readlines()

    modules = {}
    for module in raw_modules:
        module = module.replace("\n", "")
        name, destination = module.split(" -> ")

        if name.startswith("%"):  # Flip-flop
            modules[name[1:]] = FlipFlop(
                    name=name[1:],
                    outputs=destination.split(", ")
                )
        elif name.startswith("&"):  # Conjunction
            modules[name[1:]] = Conjunction(
                    name=name[1:],
                    outputs=destination.split(", ")
                )
        
        else:  # Broadcaster
            modules[name] = Broadcaster(
                    name=name,
                    outputs=destination.split(", ")
                )

    for _, module in modules.items():
        if isinstance(module, Conjunction):
            module.init_memory(modules)

    # Whenever these have sent a high together to "lv", the latter will send a low
    # to "rx". So finding the cycle to each high and then the lcm
    nodes = ["st", "tn", "hh", "dt"] 
    presses_to_send_high = {name: None for name in nodes}
    times = 0
    while any([value is None for value in presses_to_send_high.values()]):
        times += 1
        pulses = [("button", "low", "broadcaster")]
        while pulses:
            sender, pulse, receiver = pulses.pop(0)
            if receiver not in modules.keys():
                continue

            if receiver == "lv" and pulse == "high":
                if presses_to_send_high[sender] is None:
                    presses_to_send_high[sender] = times
                    print(presses_to_send_high)

            pulses.extend(modules[receiver].on_pulse_received(pulse, sender))

    print(f"Part 2 result: {numpy.lcm.reduce(list(presses_to_send_high.values()))}")


if __name__ == "__main__":
    main()
