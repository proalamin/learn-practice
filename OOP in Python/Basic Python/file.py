# .csv (comma-separated values) file
# .txt (text file)


# with open('message.txt', 'w') as file:
#     file.write('Hello, world!\n')
#     file.write('This is a text file.')


# with open('message.txt', 'a') as file:
#     file.write('\nHello, world!\n')
#     file.write('This is a text file.')


with open('message.txt', 'r') as file:
    text = file.read()
    print(text)
