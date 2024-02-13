#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i, name in enumerate(dir(hidden_4)):
        if name[0:2] != '__':
            if i == len(dir(hidden_4))-1:
                print(name, end=" ")
            else:
                print(name)
