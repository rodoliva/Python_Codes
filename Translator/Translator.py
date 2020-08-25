import translators as ts

try:
    with open('./Test.txt', mode='r') as my_file:
        text = my_file.read()
        translation= ts.google(text, 'es', 'en') # Translate form spanish to english
        with open('./Test-trans', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check file path')

