# Write a python program to implement a Random Movement Reflex Agent. (A, B, C )

import random
import time

locations = ['A', 'B', 'C']
current_location = random.choice(locations)


def move(current_location):
    new_location = random.choice(locations)
    print(f"Agent moved from {current_location} to {new_location}")
    return new_location


def random_movement(steps):
    global current_location
    for _ in range(steps):
        current_location = move(current_location)
        time.sleep(1)

steps=10

print(f"Current Location: {current_location}")
random_movement(steps)

print("Final Location: ", current_location)
