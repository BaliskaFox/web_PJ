class SageCalculator:

    def safe_divide(self, a, b):
        try:
            return f'✅ {a/b}'
        except ZeroDivisionError:
                return '❌ Ошибка: деление на ноль!'
        except TypeError:
                return '❌ Ошибка: оба аргумента должны быть числами!'

calc = SageCalculator()
print(calc.safe_divide(10, 2))
print(calc.safe_divide(10, 0))
print(calc.safe_divide(10, 'abc'))

        