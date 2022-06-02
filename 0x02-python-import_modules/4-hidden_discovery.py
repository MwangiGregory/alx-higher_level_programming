#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    nm = []
    nm = dir(hidden_4)

    for str in nm:
        if (str[0] != '_') and (str[1] != '_'):
            print(str)
