from typing import Any


class ErrorDetail:
    @staticmethod
    def unknown(func_name: str, error: Any):
        return f"Unknown error at function {func_name}: {error}"
