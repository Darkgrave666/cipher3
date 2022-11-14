class Cipher:
    def __init__(self, info: str, key: int):
        alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.info = info.upper()
        self.key = key
        self.res = ''
        for i in self.info:
            let_num = alphabet_en.find(i)
            new_let = let_num + self.key
            if i in alphabet_en:
                self.res += alphabet_en[new_let]
            else:
                self.res += i

    def __str__(self):
        return self.res


if __name__ == "__main__":
    print(Cipher('run', 4))
