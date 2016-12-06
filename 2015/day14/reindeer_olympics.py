#!/usr/bin/python
# -*- coding: utf-8 -*-

""" --- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds,
but must rest occasionally to recover their energy.
Santa would like to know which of his reindeer is fastest,
and so he has them race.

Reindeer can only either be flying
(always at their top speed) or resting (not moving at all),
and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds,
but then must rest for 127 seconds.

Dancer can fly 16 km/s for 11 seconds,
but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km.
After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
On the eleventh second, Comet begins resting (staying at 140 km),
and Dancer continues on for a total distance of 176 km.
On the 12th second, both reindeer are resting.
They continue to rest until the 138th second,
when Comet flies for another ten seconds.
On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting,
and Comet is in the lead at 1120 km
(poor Dancer has only gotten 1056 km by that point).
So, in this situation, Comet would win
(if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input),
after exactly 2503 seconds,
what distance has the winning reindeer traveled? """


# LOGIC
# calculate the distance the reindeer travels by calculating chunks of
# the reindeer when it is (flying, then resting)
# after that, whatever time is left, use it to fly the reindeer
# for max(flight_duration).
# So for eg. time left after 10 rounds of flying and resting was 20secs,
# and the reindeer rests after 10 secs,
# all the duration for flight of another 10secs to the duration.


# read input,
# contains duration on first line
# reindeer info after that
with open('./input.txt', 'r') as f:
    problem_duration = int(f.readline())
    text = f.readlines()


# store all reindeer information in a dictionary
# with members flight_speed, flight_duration, and rest
reindeers = {}

# create reindeers from input
import re
pattern = r'(\w+) can fly (\d+) km\/s for (\d+) [\w, ]+ (\d+)'
for line in text:
    line = line.strip()  # newlines
    name, flight_speed, flight_duration, rest_duration = \
        re.match(pattern, line).groups()
    reindeers[name] = {
        'flight_speed': int(flight_speed),
        'flight_duration': int(flight_duration),
        'rest': int(rest_duration),
    }


def calculate_reindeer_run(reindeer, duration):
    """Calculate distance travelled by reindeer in specified duration"""

    # get reindeer stats
    flight_speed = reindeer['flight_speed']
    flight_duration = reindeer['flight_duration']
    rest_period = reindeer['rest']

    # get number of rounds reinder flies and rests
    rounds = duration // (flight_duration + rest_period)
    # time spent during rounds
    time_spent = rounds * (flight_duration + rest_period)
    # distance covered during rounds
    distance_covered = rounds * flight_speed * flight_duration
    # time left after rounds
    time_left = duration - time_spent

    # whatever time is left,
    # fly for a bit (until flight duration or time left runs out)
    # and add that to the total duration
    if flight_duration <= time_left:
        distance_covered += flight_speed * flight_duration
    else:
        distance_covered += flight_speed * time_left

    return distance_covered


# get maximum of all reindeer runs
print(max([
    calculate_reindeer_run(r, problem_duration) for r in reindeers.values()]))
