'''
1. Написать функцию, которая получает строку и возвращает обработанную строку.
Если строка уже заканчивается числом, это число следует увеличить на 1.
Если строка не заканчивается числом, к исходной строке следует добавить число 1.
Если в числе есть ведущие нули, следует учитывать количество цифр.
Примеры:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
'''


import re
def increment_string(s):
    dig = re.search('\d*$',s).group(0) # ищет цифры  с конца
    if dig:
        ch = s[0:len(s)-len(dig)]
        dig_str = '{0:0>{1}}'.format(int(dig)+1,len(dig))        
        return (ch + dig_str)
    else:
        return s + '1'

def increment_string2(txt):
    head = txt.rstrip('0123456789')
    tail = txt[len(head):]
    if tail == "": return txt+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


print(increment_string("sss0099"))
print(increment_string2("sss0099"))