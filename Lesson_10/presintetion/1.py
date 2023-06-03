def dilennya(a, b):
    try:
        res = a / b
    except ZeroDivisionError as ex:
        print(f'{ex}ділення на 0')
        return 0
    return res

print(dilennya(12, 0))

