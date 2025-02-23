def check(func):
    def wrapper(a, b):
        try:
            c=func(a,b)
            return [c,int(c)][int(c)==c]
        except ZeroDivisionError:
            return "Denominator can't be zero"
        except TypeError:
            return "Arguments must be numbers"
        except Exception:
            return f"Something went wrong"
    return wrapper

@check
def div(a, b):
    return a / b

print(div(10, 0))
print(div(10, 'a'))
print(div(6, 4))
print(div(6, 2))