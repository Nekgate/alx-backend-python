#!/usr/bin/env python3
""" Module that contains a coroutine named async_generator
that takes no arguments.
Coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
