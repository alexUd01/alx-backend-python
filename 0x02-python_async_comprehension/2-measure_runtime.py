#!/usr/bin/python3
"""Measuring Runtime

INSTRUCTIONS:
Import async_comprehension from the previous file and write a
`measure_runtime` coroutine that will execute async_comprehension four times
in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ The async function/coroutine """
    start = perf_counter()
    res = await asyncio.gather(*[async_comprehension() for i in range(4)])
    stop = perf_counter()
    time_diff = stop - start
    return time_diff
