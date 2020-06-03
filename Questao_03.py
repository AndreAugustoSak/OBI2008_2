def overflow(num_max, string):
    resultado = eval(string)
    if num_max >= resultado:
        return True
    else:
        return False
print(overflow(323500,'42 * 35'))