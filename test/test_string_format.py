def print_formatted(number):
    spaces = len(bin(number)) - 2
    format_string = (f'{{:>{spaces}}} {{:>{spaces}}} '
                     f'{{:>{spaces}}} {{:>{spaces}}}')
    for n in range(1, number + 1):
        print(format_string.format(str(n), oct(n)[2:], hex(n)[2:].upper(), bin(n)[2:]))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
