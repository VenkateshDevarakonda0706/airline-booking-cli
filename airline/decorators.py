from collections.abc import Callable
from functools import wraps
from time import perf_counter, sleep
from typing import Any, TypeVar


T = TypeVar("T")


def timed(func: Callable[..., T]) -> Callable[..., T]:
    """Measure and display the execution time of a function."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = perf_counter()

        result = func(*args, **kwargs)

        elapsed_time = perf_counter() - start_time

        print(
            f"[timer] {func.__name__} "
            f"completed in {elapsed_time:.4f}s"
        )

        return result

    return wrapper


def retry(
    attempts: int,
    delay: float = 0.0,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Retry a function when it raises an exception.

    attempts must be at least 1.
    delay specifies the pause between attempts.
    """

    if attempts < 1:
        raise ValueError("attempts must be at least 1.")

    if delay < 0:
        raise ValueError("delay cannot be negative.")

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_error: Exception | None = None

            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_error = exc

                    if attempt == attempts:
                        raise

                    if delay > 0:
                        sleep(delay)

            raise RuntimeError(
                f"{func.__name__} failed after {attempts} attempts."
            ) from last_error

        return wrapper

    return decorator