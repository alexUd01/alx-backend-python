#!/usr/bin/env python3
""" A module that contains an asynchronous coroutine that takes in
an integer argument (`max_delay`, with a default value of 10) named
`wait_random` that waits for a random delay between 0 and `max_delay`
(included and float value) seconds and eventually returns it.

Instruction: Use the random module.
"""
from random import uniform
import asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """ The fuction """
    i = uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
