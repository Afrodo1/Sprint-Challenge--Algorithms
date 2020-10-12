'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    #Returns zero if length of word is less than 2
    if len(word) < 2:
        return count
    #Checks only the first two letters of the remaining/word, then passes the rest of the word thru to do it all over again
    if word[:2] == 'th':
        count +=1
        return count_th(word[2:],count)
    #if 'th' isnt found then the remaining word is passed thru the function again
    else:
        return count_th(word[1:],count)
    

print(count_th('thethorithaticath'))
    

    # TBC
