def rev(s):
    if s == "":
        return ""
    return rev(s[1:]) + s[0]
print(rev("Husnain"))