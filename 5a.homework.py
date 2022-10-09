'''
Вовочка счидя на урокуе писал подряд одинаковые слова
(слово может состоять из одной буквы). Когда Марья Ивановна
забрнала у него тетрадь, там была одна строка текста.
Напишите программу, которая определит самое короткое слово
из написанных Вовочкой.
'''
text = input("Enter text : ", )
text_part = ""
i = 0
for words in text:
    text_part += words
    if text[i + 1] == text[0]:
        break
    i += 1
print(text_part)
'''
Напишите программу для нахождения расстояния Левенштейна
между двумя строками. Расстояние Левенштейна - это минимальное количество
односимвольных изменений (вставки, удаления или замены), необходимых    
для изменения одной строки в другую.
'''
text_f = "kitten"
text_s = "sitting"
temp = 0

if len(text_s) > len(text_f):
    i = 0
    for let in text_f:
        if not text_f[i] == text_s[i]:
            temp += 1
        i += 1
    temp += len(text_s) - len(text_f)
    print("Range =", temp)
else:
    i = 0
    for let in text_s:
        if text_f[i] == text_s[i]:
            temp += 1
        i += 1
    temp += len(text_f) - len(text_s)
    print("Range =", temp)