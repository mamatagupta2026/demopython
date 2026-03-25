class Calculator:
    """A simple calculator with history tracking."""

    def __init__(self):
        self._history: list[str] = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self._history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self) -> list[str]:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()

    def __repr__(self) -> str:
        return f"Calculator(operations={len(self._history)})"
