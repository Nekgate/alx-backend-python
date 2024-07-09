#!/usr/bin/env python3

""" Module that contains a coroutine named async_comprehension
that takes no arguments.
Coroutine will collect 10 random numbers using an async comprehensing over
async_generator, then return the 10 random numbers.
"""

from typing import List
from importlib import import_module as using


asyncio_generator = using("0-async_generator").async_generator

async def async_comprehension() -> List[float]:
    """Async Coroutine function that collects 10 random numbers
    using an async comprehension over async_generator,
    then return the 10 random numbers.
    """
    return [num async for num in asyncio_generator()]
