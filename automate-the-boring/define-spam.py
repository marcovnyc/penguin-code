def spam(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
