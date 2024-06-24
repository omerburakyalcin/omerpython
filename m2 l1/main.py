# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()