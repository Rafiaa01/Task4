# Task 4 — Async Experiment

## Overview

This task demonstrates sequential and concurrent execution using Python's `asyncio`.

Three async functions simulate API calls, and each waits for 2 seconds using `asyncio.sleep(2)`.

## How to Run
bash
python main.py


## Expected Result

Sequential: approximately 6 seconds
Concurrent: approximately 2 seconds

Sequential execution waits for each function to finish before starting the next one. With `asyncio.gather()`, the functions run concurrently, so their waiting times overlap.

When a coroutine reaches `await`, it pauses and gives control back to the event loop, allowing other tasks to run.

## What I Learned

I learned how `async`, `await`, `asyncio.gather()`, and the event loop enable concurrent execution for I/O-bound tasks.
