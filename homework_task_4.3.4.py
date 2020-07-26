with open ('book.txt') as book:
    lines = book.read().lower().replace('\n', ' ').split(' ')
    # lines_split = lines.split(' ')
    word = 0
    for i in lines:
        word += i.count('know')
        
print (lines)        
print('Количество слов: ',len(lines))
print ('Процент слова "know": ', round((len(lines) * word) / 100, ), '%')
