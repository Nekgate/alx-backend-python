#!/usr/bin/env python3

"""A Module that contains an asynchronous coroutine that takes an integer
argument (max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay (included float value)
seconds and eventually returns it.
"""

import asyncio
import random


async def wait_randon(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes an integer argument
    and returns it after a delay.
    """
    wait_time = randon.random() * max_delay
    await asyncio.sleep(wait_time)

    return wait_time
