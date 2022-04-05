from typing import Callable

from to_do import TODO


def guide2(script: Callable[[], list[str]]) -> str:
    return TODO(
        "Replace this 'TODO' with the variable 'result'. Do not erase the 'return' keyword"
    )
