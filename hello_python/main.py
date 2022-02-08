#!/usr/bin/env python3

def say_hi(to_whom):
    return "Hello, {}!".format(to_whom)


def main():
    whozzat = "World"
    print(say_hi(whozzat))


if __name__ == '__main__':
    main()
