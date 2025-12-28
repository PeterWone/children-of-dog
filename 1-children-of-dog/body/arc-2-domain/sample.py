#!/usr/bin/env python3
"""
Sample Python file for testing the VS Code Print extension.

This file intentionally includes:
- imports
- classes
- functions
- type hints
- exceptions
- f-strings
- comments
- multiline strings
"""

import math
from dataclasses import dataclass

PI = math.pi  # constant for highlighting

@dataclass
class Circle:
    radius: float

    def area(self) -> float:
        return PI * (self.radius ** 2)

    def circumference(self) -> float:
        return 2 * PI * self.radius


def describe_circle(c: Circle) -> str:
    """Return a formatted description of the circle."""
    if c.radius < 0:
        raise ValueError("Radius cannot be negative")

    return (
        f"Circle:\n"
        f"  radius        = {c.radius}\n"
        f"  area          = {c.area():.3f}\n"
        f"  circumference = {c.circumference():.3f}"
    )


def main() -> None:
    # Create a few circles to test formatting
    circles = [Circle(r) for r in (1, 2.5, 5)]

    for c in circles:
        print(describe_circle(c))
        print("-" * 40)


if __name__ == "__main__":
    main()
