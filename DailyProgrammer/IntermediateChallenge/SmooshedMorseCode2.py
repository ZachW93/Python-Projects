# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:15:12 2019
@author: Zach W

Smooshed Morse code means Morse code with the spaces or other delimiters between 
encoded letters left out. See this week's Easy challenge for more detail.

A permutation of the alphabet is a 26-character string in which each of the 
letters a through z appears once.

Given a smooshed Morse code encoding of a permutation of the alphabet, find the 
permutation it encodes, or any other permutation that produces the same encoding 
(in general there will be more than one). It's not enough to write a program 
that will eventually finish after a very long period of time: run your code through 
to completion for at least one example.

General Outputs:
    
smalpha(".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..")
    => "wirnbfzehatqlojpgcvusyxkmd"
smalpha(".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-")
    => "wzjlepdsvothqfxkbgrmyicuna"
smalpha("..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..")

    => "uvfsqmjazxthbidyrkcwegponl"
Again, there's more than one valid output for these inputs.

"""

from string import ascii_lowercase

morseCode_toLetters = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z'
}

letters_toMorseCode = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

def smorse(decoded):
    
    global decode_map
    encoded = []
    
    for char in decoded:
        
        encoded.append(morseCode_toLetters[char])
        
    return ''.join(encoded)

def backtrack(encoded, result, alphabet):
    
    if encoded == '':
        
        return result

    global decode_map

    candidates = []
    
    for i in range(1,5):
        
        chunk = encoded[:i]
        char = decode_map.get(chunk)
        
        if char in alphabet:
            
            candidates.append((char, len(chunk)))

    if not candidates:
        
        return []

    for candidate in candidates:
        
        alphabet.remove(candidate[0])
        result.append(candidate[0])
        candidate_result = backtrack(encoded[candidate[1]:], result, alphabet)
        
        if candidate_result:
            
            return candidate_result
        
        result.pop()
        alphabet.add(candidate[0])

def smalpha(encoded):
    
    return ''.join(backtrack(encoded, [], set(ascii_lowercase)))

