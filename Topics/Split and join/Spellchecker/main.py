dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
text = input().split()
result = ""
for word in text:
    if word not in dictionary:
        result += "{0}\n".format(word)
if result == "":
    result = "OK"
print(result)