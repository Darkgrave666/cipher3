from snake_case import to_snake_case
from camel_case import to_camel_case


class NameConverter:
    def __init__(self, c: str, s: str, cf: bool):
        self.c = c
        self.s = s
        self.cf = cf
        if c == "snake":
            self.s = to_snake_case(s)
        elif c == "camel":
            self.s = to_camel_case(s, cf)

    def __str__(self):
        return self.s


if __name__ == '__main__':
    sn = NameConverter("snake", "Snake Case", True)
    ca = NameConverter("camel", "camel case", True)
    print(sn)
    print(ca)
    print(NameConverter("snake", str(ca), True))
    print(NameConverter("camel", str(sn), False))
