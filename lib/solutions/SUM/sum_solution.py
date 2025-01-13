# noinspection PyShadowingBuiltins,PyUnusedLocal
class IllegalParameter(Exception):

    def __init__(self, error_msg: str, *args: object) -> None:
        super().__init__(*args)
        self.error_msg = error_msg

    def __repr__(self) -> str:
        return f'Error: {self.error_msg}'


LEGAL_RANGE_INPUT = list(range(100 + 1)) # range is not inclusive


def compute(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise IllegalParameter(f'x or y are illegal! x={x} y={y}')
    if x not in LEGAL_RANGE_INPUT or y not in LEGAL_RANGE_INPUT:
        raise IllegalParameter(f'x or y are out of range! x={x} y={y}')
    return x + y
