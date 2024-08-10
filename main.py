import re

# Load the book
with open(file='miracle_in_the_andes.txt', encoding='utf-8') as f:
    book = f.read()

# Find number of chapters in the book
pattern = re.compile('Chapter [0-9]+')
result = re.findall(pattern=pattern, string=book)
print(len(result))

# Find sentences where the word 'love' is mentioned
pattern = re.compile('[A-Z][^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.')
result = re.findall(pattern=pattern, string=book)
print(len(result))

# Find most used word in the book
pattern = re.compile('[a-zA-Z]+')
result = re.findall(pattern=pattern, string=book.lower())
word_dict = {}
for word in result:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
word_list = [(count, word) for word, count in word_dict.items()]
word_list.sort(reverse=True)
print(word_list[0])

# extract paragraph where love was used
pattern = re.compile('[^\n]+love[^\n]+')
result = re.findall(pattern=pattern, string=book)
print(result[:1])

# extract the chapter titles
pattern = re.compile('([a-zA-Z ]+)\n\n')
result = re.findall(pattern=pattern, string=book)
print(result)


# function that finds occurrence of any word
def find_word_occurrence(word_):
    pattern_ = re.compile('[a-zA-Z]+')
    result_ = re.findall(pattern=pattern_, string=book.lower())
    word_dict_ = {}
    for w in result_:
        if w in word_dict_:
            word_dict_[w] += 1
        else:
            word_dict_[w] = 1
    if word_ in word_dict_.keys():
        print(f'The word {word_} occurred {word_dict_[word_]} times.')
    else:
        print(f'The word {word_} was not found in the book.')


# call the function
find_word_occurrence('hermit')
