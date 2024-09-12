# Write a program that simulates a multi-threaded application where threads share resources. Use locks to manage shared data and prevent race conditions.

import threading
import time
import random

# Shared resource
shared_counter = 0

# Lock to prevent race conditions
lock = threading.Lock()


def increment_counter(thread_name):
    """Function for each thread to increment the shared counter."""
    global shared_counter

    # Simulate some work
    for _ in range(5):
        # Acquire the lock before modifying the shared resource
        lock.acquire()
        try:
            # Critical section (only one thread can execute this at a time)
            print(f"{thread_name} is incrementing the counter.")
            current_value = shared_counter
            time.sleep(random.uniform(0.1, 0.5))  # Simulate a delay
            shared_counter = current_value + 1
            print(f"{thread_name} incremented the counter to {shared_counter}.")
        finally:
            # Release the lock
            lock.release()


def main():
    # Create multiple threads
    threads = []
    for i in range(3):
        thread = threading.Thread(
            target=increment_counter, args=(f"Thread-{i+1}",))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print final value of shared counter
    print(f"Final value of shared counter: {shared_counter}")


if __name__ == "__main__":
    main()
