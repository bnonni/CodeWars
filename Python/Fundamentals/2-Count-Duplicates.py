def duplicate_count(text):
    dupes = 0
    alphNum = "abcdefghijklmnopqrstuvwxyz1234567890"
    for char in alphNum:
        count = text.lower().count(char)
        if count > 1:
            dupes+=1
        else:
            dupes+=0
    return dupes

print(duplicate_count("abcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("abdcea"))
print(duplicate_count("abdBcea"))