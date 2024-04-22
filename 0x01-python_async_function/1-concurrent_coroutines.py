#!/usr/bin/python3

""" Module documentation """
import random
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """doc func"""
    listDelays = []
    for _ in range(n):
        listDelays.append(asyncio.ensure_future(wait_random(max_delay)))
    await asyncio.wait(listDelays)
    return sorted([task.result() for task in listDelays])
