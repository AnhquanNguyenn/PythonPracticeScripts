def word_search(matrix, word):
    wordLength = len(word)
    wordArray = list(word)
    firstLetterToSearch = word[0]
    wordTemp = []

    if wordLength == len(matrix):
        for i in range(len(matrix)):
            if wordArray[i] == matrix[0][i]:
                wordTemp.append(matrix[0][i])
                print(wordTemp)

    if wordTemp == word:
        return True

    return False


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

word = 'FOAM'
print(word_search(matrix, word))
# True
