#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables
a set of wires and bitwise logic gates!
Unfortunately, little Bobby is a little under the recommended age range,
and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters)
and can carry a 16-bit signal (a number from 0 to 65535).
A signal is provided to each wire by a gate, another wire,
or some specific value. Each wire can only get a signal from one source,
but can provide its signal to multiple destinations.
A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes
how to connect the parts together:
x AND y -> z means to connect wires x and y to an AND gate,
and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the
bitwise AND of wire x and wire y is provided to wire z.

p LSHIFT 2 -> q means that the value from wire p is
left-shifted by 2 and then provided to wire q.

NOT e -> f means that the bitwise complement of the value
from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
If, for some reason, you'd like to emulate the circuit instead,
almost all programming languages
(for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet
(provided as your puzzle input),
what signal is ultimately provided to wire a? """


import logging
import re
import sys

# Set log output to console / stdout
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Wire(object):

    """Represents a wired circuit component"""

    def __init__(self):
        # signal value, default is None
        self.signal = None
        # name of the wire / circuit
        self.name = None
        # list of inputs
        self.inputs = []
        # gate in the circuit
        self.gate = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def parse_circuit(
        name=None, signal=None, gate=None, input_a=None, input_b=None):
    """Create wire with given inputs"""

    wire = Wire()
    wire.name = name
    wire.signal = signal
    wire.gate = gate
    wire.inputs = []
    # set inputs if present
    if input_a:
        wire.inputs.append(input_a)
    if input_b:
        wire.inputs.append(input_b)

    return wire


def make_wires(filename):
    """Create wires from input file"""

    # Input patterns and group names.
    #
    # The input patterns are regular expressions
    # that identify the type of statement.
    # The associated tuple contains the groups names for the regex
    # which is used to pass the extracted groups as keyword arguments
    # to the parse_circuit function to create wire objects.
    patterns = {
        # extend wire
        r'^([a-z]+) -> (\w+)': ('input_a', 'name'),
        # signal
        r'^(\d+) -> (\w+)': ('signal', 'name'),
        # single input gate
        r'^(\w+) (\w+) -> (\w+)': ('gate', 'input_a', 'name'),
        # double input gate
        r'^(\w+) (\w+) (\w+) -> (\w+)': ('input_a', 'gate', 'input_b', 'name'),
    }

    # the dictionary will hold wire / circuits
    # identified by their name
    wires = {}

    # iterate over each line in the file,
    # match regex expressions, extract groups,
    # pass to parse_circuit function as keyword arguments
    # and save the wire object to wires dict
    with open(filename, 'r') as f:
        for line in f.readlines():
            for pattern, kwargs in patterns.items():
                matches = re.match(pattern, line)
                if matches is not None:
                    # assign extracted groups to keywords
                    # from matched patterns,
                    # then construct dict to be unpacked as
                    # keyword arguments
                    wire = parse_circuit(**dict(zip(kwargs, matches.groups())))
                    wires[wire.name] = wire

    return wires


def link_wires(wires):
    """Link wires to form circuit"""

    # Iterate over saved wire objects,
    # and link inputs to wire objects.
    # This will link the entire circuit through references.
    for wire in wires.values():
        # Set inputs to empty list
        inputs = []
        # For each input,
        # try to parse it as an int,
        # if it can't be (ValueError), it's a wire object,
        # therefore, link it to the wire object in dict
        for name in wire.inputs:
            try:
                value = int(name)
                inputs.append(value)
            except ValueError:
                inputs.append(wires[name])

        wire.inputs = inputs


def get_input(input_obj, wires):
    """Get input signal for input_obj from wires if required"""

    if input_obj is None:
        return None

    # If the input is a signal, return it back
    if type(input_obj) == int:
        return input_obj

    # If the input is a wire, resolve it until we get a signal
    if type(input_obj) == Wire:
        input_obj = wires[input_obj.name]

    return input_obj


def solve_gate(wire, wires):
    """Solve the circuit formed by this wire and its gate"""

    # Always keep the result as a 16bit number
    m16 = lambda x: x & 0xFFFF

    # Extending wires have no gates
    if wire.gate is None:
        wire.signal = get_input(wire.inputs[0], wires)
        logger.debug(
            '{name} = EXTEND {signal}'.format(
                name=wire.name, signal=wire.signal))
    # NOT gates have only one input
    elif wire.gate == 'NOT':
        x = get_input(wire.inputs[0], wires)
        wire.signal = m16(~x)
        logger.debug(
            '{name} = NOT {x} = {signal}'.format(
                name=wire.name, x=x, signal=wire.signal))
    # All the other gates have two inputs
    else:
        # Get the two inputs as x, y
        x = get_input(wire.inputs[0], wires)
        y = get_input(wire.inputs[1], wires)

        if wire.gate == 'AND':
            wire.signal = m16(x & y)
            logger.debug(
                '{name} = {x} AND {y} = {signal}'.format(
                    name=wire.name, x=x, y=y, signal=wire.signal))

        elif wire.gate == 'OR':
            wire.signal = m16(x | y)
            logger.debug(
                '{name} = {x} OR {y} = {signal}'.format(
                    name=wire.name, x=x, y=y, signal=wire.signal))

        elif wire.gate == 'LSHIFT':
            wire.signal = m16(x << y)
            logger.debug(
                '{name} = {x} LSHIFT {y} = {signal}'.format(
                    name=wire.name, x=x, y=y, signal=wire.signal))

        elif wire.gate == 'RSHIFT':
            wire.signal = m16(x >> y)
            logger.debug(
                '{name} = {x} RSHIFT {y} = {signal}'.format(
                    name=wire.name, x=x, y=y, signal=wire.signal))


def solve_circuit(wires, end_point):
    """Solve the circuit formed by the wires with end_point"""

    # Create stack using a list with the end_point in it.
    # Iterate over the stack until it is empty.
    #
    # At each iteration, pop the wire off the stack,
    # and check if it has any wire inputs.
    # If it does, push it back on the stack,
    # and push all its wire inputs on the stack.
    #
    # If the wire has only signal inputs, solve the gate
    # and save the signal in the dictionary
    #
    # At the end, the entire circuit will have been sovled,
    # assuming that it is a valid circuit, and the stack
    # should be empty.
    stack = [end_point]

    while(stack):

        # uncomment the next line to see a step-by-step operation on the stack
        # logger.debug('stack:{stack}'.format(stack=stack))

        # pop a wire off the stack
        wire = stack.pop()

        # If it does not have any inputs nor any gates,
        # then it has a signal.
        if not wire.inputs and not wire.gate:
            wires[wire.name] = int(wire.signal)
            logger.debug(
                '{name} = {signal}'.format(
                    name=wire.name, signal=wire.signal))
            continue

        # Check how many other wires are attached as inputs
        wire_inputs = [
            x for x in wire.inputs
            if type(x) != int and type(wires[x.name]) == Wire]

        # If there are any, push the wire on the stack,
        # then push its wire inputs on the stack.
        if wire_inputs:
            stack.append(wire)
            stack.extend(wire_inputs)
        # Otherwise, solve the wire and save its signal
        else:
            solve_gate(wire, wires)
            wires[wire.name] = wire.signal


def get_answer(filename, target_wire):
    """Get signal for wire a"""

    # create wires from input file
    wires = make_wires(filename)

    # link wires to other wires to form circuit
    link_wires(wires)

    # set target wire from the dict with given name
    target_wire = wires.get(target_wire)
    if target_wire is None:
        logger.critical('Target wire not specified.')
        return None

    solve_circuit(wires, end_point=target_wire)

    # Unsolved wires are those who are still present
    # in the wires dict as Wire objects
    logger.debug(
        'Wires unsolved: {unsolved}'.format(
            unsolved=[
                x for x, y in wires.items()
                if type(y) != int]))

    return wires[target_wire.name]


if __name__ == '__main__':

    signal_on_a = get_answer('./input.txt', 'a')
    print(signal_on_a)
