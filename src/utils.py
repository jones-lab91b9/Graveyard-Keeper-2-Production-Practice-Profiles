# Build: 181f885d2049c4d9d7fbf6d805731e0e

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
