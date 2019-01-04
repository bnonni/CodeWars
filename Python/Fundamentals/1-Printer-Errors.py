def printer_error(s):
    arr = []
    chars = "abcdefghijklm"
    for char in chars:
        count = s.count(char)
        arr.append(count)
        denom = len(s)
        numer = denom - sum(arr)
    print(str(numer) + "/" + str(denom))

printer_error("aaabbbbhaijjjm");