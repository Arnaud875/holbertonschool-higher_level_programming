#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result =  a / b
    except Exception as e:
        pass
    finally:
        print("{:d}".format(result))
    return result
