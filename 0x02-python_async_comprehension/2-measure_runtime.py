#!/usr/bin/env python3
"""Module that contains a coroutine named measure_runtime
that will execute async_comprehension four times in parallel
using asyncio.gather.
Coroutine will measure the total runtime and return it.
Explanation for how the total runtime is 10 seconds or less
should be included in the documentation."""

import asyncio
import time
from importlib import import_module as using


async_comprehension = using("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times and measures the
    total execution time."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
