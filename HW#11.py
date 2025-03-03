# Положительные аргументы функции
def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Все аргументы должны быть положительными числами")
        return func(*args)

    return wrapper


@validate_arguments
def add(a, b):
    return a + b


print(add(3, 7))
print(add(5, -2))


# Вернуть число

def number_check(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print("Ошибка: результат не является числом!")
        return result

    return wrapper


@number_check
def ad(a, b):
    return a + b


@number_check
def greet(name):
    return "Привет, " + name


print(ad(2, 3))
print(greet("Мир"))


# Декоратор типов
def typed(arg_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = [arg_type(arg) for arg in args]
            new_kwargs = {k: arg_type(v) for k, v in kwargs.items()}
            return func(*new_args, **new_kwargs)

        return wrapper

    return decorator


@typed(arg_type=str)
def adding(a, b):
    return a + b


print(adding("3", 5))
print(adding(5, 5))
print(adding('a', 'b'))


@typed(arg_type=int)
def add_int(a, b, c):
    return a + b + c


print(add_int(5, 6, 7))


@typed(arg_type=float)
def add_float(a, b, c):
    return a + b + c


print(add_float(0.1, 0.2, 0.4))


# Функция кэширования *
def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            return cache_dict[key]
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Примеры использования:

print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
