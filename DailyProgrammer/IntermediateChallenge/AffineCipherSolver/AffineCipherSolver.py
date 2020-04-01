# -*- coding: utf-8 -*-
"""
Problem: You are to output what you think is the solution to a given Affine 
Cipher. In short, Affine ciphers are encoded by the following formula for each 
character in the plaintext: C ≡ aP + b (mod 26) where a and b are constants, C 
is the ciphertext letter, and P is the plaintext letter. In this case, the 
letter "a" has the value of 0, "b" 1, and so on and so forth. If you want a 
hint as to how to decode:

Decoding is done in the same fashion as encoding: P ≡ aC + b
In order to rank your decodings in terms of accuracy, I recommend you use a 
dictionary of some sort (builtin, or the popular enable1.txt -- note that 
enable1 lacks "i" and "a" as words). You can choose to not use a dictionary, 
but it will likely be harder.

Here's a sample of encoding, done with simple numbers (a = 3, b = 2) N.B. This 
is done with the letters a-z mapped to 1-26 (26≡0) instead of 0-25. This still 
is correct, just not the exact result you'd expect from following the method 
I've established previously.

foobar

First, we express our input numerically

6, 15, 15, 2, 1, 18

Then we multiply by a

18, 45, 45, 12, 3, 54

Optionally reduce to least positive residue

18, 19, 19, 12, 3, 2

Add b

20, 21, 21, 18, 5, 4

Now we change this to text again

tyyred

Input: Input will be words separated by spaces or newlines. Input will be in 
uppercase if need be (i.e. if you can't figure out a way to handle mixed cases), 
but if not, it will be provided in regular text (e.g. Lorum ipsum ... word). 
Expect only alphabetical characters. With reference to my previous equation, a 
will only be a number coprime with 26.

Test Cases: 
    
Test Case 1: NLWC WC M NECN

this is a test

Test Case 2: YEQ LKCV BDK XCGK EZ BDK UEXLVM QPLQGWSKMB

you lead the race of the worlds unluckiest

Test Case 3: NH WRTEQ TFWRX TGY T YEZVXH GJNMGRXX STPGX NH XRGXR TX QWZJDW ZK 
WRNUZFB P WTY YEJGB ZE RNSQPRY XZNR YJUU ZSPTQR QZ QWR YETPGX ZGR NPGJQR STXQ 
TGY URQWR VTEYX WTY XJGB

my heart aches and a drowsy numbness pains my sense as though of hemlock i had 
drunk or emptied some dull opiate to the drains one minute past and lethe wards 
had sunk
"""
def affineCipher(sentence):
    
    a_list = [3, 5, 7, 11, 15, 17, 19, 21, 23, 25]
    
    letter_dictionary = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25
            }
    
    number_dictionary = {
           0: 'a',
           1: 'b',
           2: 'c',
           3: 'd',
           4: 'e',
           5: 'f',
           6: 'g',
           7: 'h',
           8: 'i',
           9: 'j',
           10: 'k',
           11: 'l',
           12: 'm',
           13: 'n',
           14: 'o',
           15: 'p',
           16: 'q',
           17: 'r',
           18: 's',
           19: 't',
           20: 'u',
           21: 'v',
           22: 'w',
           23: 'x',
           24: 'y',
           25: 'z'      
            }
    
    with open("enable1.txt") as f:
        words = list(map(lambda s: s.strip().lower(), f.readlines()))
        words += ['i', 'a']
    
    sentence = sentence.lower().replace("'","").replace(".","")
    split_sentence = sentence.split()
    
    for a in a_list:
        for b in range(0,25):
        
            score = 0
        
            for word in split_sentence:
            
                split_word = list(word)

                number_list = []
                for letter in split_word:
        
                    numberedValue = letter_dictionary[letter]
                    numberedValue *= a
                    numberedValue += b
                    numberedValue %= 26
                    number_list.append(number_dictionary[numberedValue])
                
                new_word = "".join(number_list)
                
                if new_word in words:
                    score += 1
                
            if score != len(split_sentence):
                continue
            else:
                correct_a = a
                correct_b = b

    
    new_sentence = []
    
    for word in split_sentence:
            
                split_word = list(word)

                number_list = []
                for letter in split_word:
        
                    numberedValue = letter_dictionary[letter]
                    numberedValue *= correct_a
                    numberedValue += correct_b
                    numberedValue %= 26
                    number_list.append(number_dictionary[numberedValue])
                
                new_word = "".join(number_list)
                
                new_sentence.append(new_word)
                
    new_sentence = " ".join(new_sentence)
    return new_sentence


print(affineCipher('NH WRTEQ TFWRX TGY T YEZVXH GJNMGRXX STPGX NH XRGXR TX QWZJDW ZK WRNUZFB P WTY YEJGB ZE RNSQPRY XZNR YJUU ZSPTQR QZ QWR YETPGX ZGR NPGJQR STXQ TGY URQWR VTEYX WTY XJGB'))