import sys
read = sys.stdin.readline

def solution(letter):
    word = letter.split()
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    result = []
    
    for i in word:
        for j in morse[i]:
            if morse[i] == j:
                result.append(j)
    
    return ''.join(result)