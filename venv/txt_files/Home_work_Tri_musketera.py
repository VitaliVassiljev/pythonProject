with open('tri_musketera.txt', 'r', encoding='utf8') as book:
    data = book.read() .lower().replace('a', '').replace('p', '').replace('w', '').replace('x', '').replace('r', '') .replace('q', '').replace('d', '').replace('b', '').replace('k', '').replace('o', '').replace('t', '').replace('h', '').replace('n', '').replace('m', '').replace('y', '').replace('m', '') .replace('v', '').replace('u', '').replace('c', '') .replace('i', '').replace('l', '').replace(':', '').replace(';', '').replace('d', '').replace('e', '').replace('g', '').replace('f', '').replace('s', '').replace('.'," ") .replace('*', " ") .replace('"', " ") .replace('-', " ") .replace(',', " ") .replace(': ', " ") .replace('!', " ") .replace('?', " ") .replace('(', " ") .replace(')', " ")
    for x in '1234567890':
        data = data.replace(x, '')
    data = data.split()
    # print(len(data))
# with open('tri_musketera_copy.txt', 'w', encoding='utf8') as book:
#     data = book.read()
#     print(book.name)
#     print(len(data))
    unique_words = list(set(data))
    print(unique_words)
    with open('tri_musketera_copy2.txt', 'w', encoding='utf8') as result:
        result.write(f'There are {len(data)} words in {book.name} .\n')
        result.write(f'There are {len(unique_words)} unique_words in {book.name}.\n')
        unique_words.sort()

        for word in unique_words:
            result.write(word + '\n')