def to_snake_case(n: str):
    if n.find(" ") == -1:
        n1 = n[1:]
        n2 = n[0].lower()
        new = ""
        for i in range(len(n1)):
            if n1[i] == n1[i].lower():
                new += n1[i]
            else:
                new += "_" + n1[i].lower()
        new = str(n2) + str(new)
    else:
        new = n.replace(" ", "_").lower()
    return new


if __name__ == "__main__":
    print(to_snake_case("ToSnakeCase"))
