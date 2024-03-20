#!/usr/bin/env python3
import asyncio
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel.
    """
    # Start time measurement
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # End time measurement
    end_time = asyncio.get_event_loop().time()

    # Return total runtime
    return end_time - start_time
