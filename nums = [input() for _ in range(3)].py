while True:
    text = input().split(" ")
    
    if text[0] == text[1]:
        continue
    
    position = 0
    while True:
        if len(text[0]) < position+1 or len(text[1]) < position+1:
            print(text[0][-1], "_")
            break
        else:
            if text[0][position] != text[1][position]:
                print(text[0][position], text[1][position])
                break
            else:
                position += 1
                continue
    break