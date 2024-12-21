def operation(a, b, operator):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):

        return {
            'result': None,
            'is_error': True,
            'reason': 'Оба аргумента должны быть числами.'
        }

    try:
        string = f'{a} {operator} {b}'
        result = eval(string)

        return {
            'result': result,
            'is_error': False,
            'reason': ''
        }
    except ZeroDivisionError:

        return {
            'result': None,
            'is_error': True,
            'reason': 'Делить на 0 нельзя.'
        }
    except Exception as error:

        return {
            'result': None,
            'is_error': True,
            'reason': str(error)
        }


class Calculator(object):
    def __init__(self):
        pass

    def add(self, a: int|float, b: int|float) -> dict:
        return operation(a, b, '+')

    def subtract(self, a: int|float, b: int|float) -> dict:
        return operation(a, b, '-')

    def multiply(self, a: int|float, b: int|float) -> dict:
        return operation(a, b, '*')

    def divide(self, a: int|float, b: int|float) -> dict:
        return operation(a, b, operator='/')
