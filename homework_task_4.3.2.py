import string

###
translator = str.maketrans({key: " " for key in string.punctuation})



with open ('homework_task_4.3.2.txt') as file:
    
    
    text = file.readlines()
    lines = 0
    words = 0
    symbols = 0
    text2 = []
    for line in text:    
        text2.append(" ".join(line.translate(translator).split()))
        lines += line.count('\n')
        if not line.endswith('\n'):
            lines += 1
        words += len(",".join(text2).split())
        symbols += len(line)



print(text , '\n')
print(text2, '\n')
print ('Lines: ', lines)
print ('Words: ', words)    
print ('Symbols: ', symbols)



