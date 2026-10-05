
import asyncio
import time


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")


async def task3():
    print("Task 3 started")
    await asyncio.sleep(2)
    print("Task 3 completed")


async def main():
    # Run tasks sequentially
    print("\nRunning tasks sequentially:")
    start_time = time.perf_counter()

    await task1()
    await task2()
    await task3()

    sequential_time = time.perf_counter() - start_time
    print(f"Sequential execution time: {sequential_time:.2f} seconds")

    # Run tasks concurrently
    print("\nRunning tasks concurrently:")
    start_time = time.perf_counter()

    await asyncio.gather(task1(), task2(), task3())

    concurrent_time = time.perf_counter() - start_time
    print(f"Concurrent execution time: {concurrent_time:.2f} seconds")


asyncio.run(main())