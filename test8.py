'''Disclaimer code of InputAndOutput, and Plugboard was copied from video by @codingcassowary6391 on youtube from his "Coding the Enigma machine - Part 1" originally released on March 26th of 2022
the rest of the code was done on my own however I did attempt to maintain a similar naming convention'''

#rotors for future use
rotor_one = ["ekmflgdqvzntowyhxuspaibrcj", "q"] 
rotor_two = ["ajdksiruxblhwtmcqgznpyfvoe", "e"]
rotor_three = ["bdfhjlcprtxvznyeiwgakmusqo", "v"]
#rotor_thre = ["abcdefghijklmnopqrstuvwxyz", "v"]
rotor_four = ["esovpzjayquirhxlnftgkdcmwb", "j"]
rotor_five = ["vzbrgityupsdnhlxawmjqofeck", "z"]
#rotor_six = ["jpgvoumfyqbenhzrdkasxlictw", "z", "m"]
#rotor_seven = ["nzjhgrcxmyswboufaivlpekqdt" "z", "m"]
#rotor_eight = ["fkqhtlxocbjspdzramewniuygv", "z", "m"]
reflector_A = "ejmzalyxvbwfcrquontspikhgd"
reflector_B = "yruhqsldpxngokmiebfzcwvjat"
reflector_C = "fvpjiaoyedrzxwgctkuqsbnmhl"


#will be used to check the inputs and the outputs of the user and match them to a numeric value
class InputAndOutput:
    def input(self, letter):
        signal = "abcdefghijklmnopqrstuvwxyz".find(letter.lower())
        return signal
    def output(self, signal):
        letter = "abcdefghijklmnopqrstuvwxyz"[signal]
        return letter
    
class Plugboard:

    def __init__(self, pairs):
        '''Pairs is the letter that will be swapped on the plugboard, the left will change, the right will be the original alphabet'''
        self.left = "abcdefghijklmnopqrstuvwxyz"
        self.right = "abcdefghijklmnopqrstuvwxyz"
        for pair in pairs:
            #A is the first letter of the swapped pair
            A = pair[0]
            #B is the second letter of the swapped pair
            B = pair[1]
            #pos_A is where to find position of A
            pos_A = self.left.find(A)
            #pos_B is where to find the position of B
            pos_B = self.left.find(B)
            #rewrites self.left as a new string with B replacing A
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            #rewrites self.left as a new string with A replacing B
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]
    
    def forward(self, signal):
        '''signal is passed into the unchanged side of the alphabet and finds the corresponding letter
        this letter is then searched for in the changed side of the alphabet to find its position
        the position is then returned so it can be used in the next set of encoding'''
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    def backward(self, signal):
        '''signal comes from the previous rotor to be passed into the encoded side of the plugboard where it is used to find the letter
        this letter is then found in the unchanged alphabet where its position is then found and returned so it can be passed on and displayed'''
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

class Rotor:
    def __init__ (self, wiring, notch, isfirst):
        '''wiring is a string contanin a single instance of all the character in the alphabet arranged in a random order
        notch is the turnover notch which will tell the rotors when to turn
        isfirst is true or false depending on if the rotor is the first in the sequence'''
        self.right = wiring
        self.left = "abcdefghijklmnopqrstuvwxyz"
        self.notch = notch
        self.first = isfirst

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward(self, signal):
        if self.first or self.right[0] == self.notch:
            new_right = self.right[0]
            self.right = self.right[1:] + new_right
            new_left = self.left[0]
            self.left = self.left[1:] + new_left
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
    
class ReflectionRotor:
    def __init__ (self, wiring):
        self.left = "abcdefghijklmnopqrstuvwxyz"
        self.right = wiring
        

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

rotor1 = Rotor(rotor_one[0], rotor_one[1], False)
rotor2 = Rotor(rotor_two[0], rotor_two[1], False)
rotor3 = Rotor(rotor_three[0], rotor_three[1], True)
rotor4 = Rotor(rotor_four[0], rotor_four[1], False)
rotor5 = Rotor(rotor_five[0], rotor_five[1], False)
reflectorA = ReflectionRotor(reflector_A)
reflectorB = ReflectionRotor(reflector_B)
reflectorC = ReflectionRotor(reflector_C)
Keypressed = InputAndOutput()
Switched_Plugs = Plugboard(["ar", "gk", "ox"])

letter = "P"
signal = Keypressed.input(letter)
signal = Switched_Plugs.forward(signal)
signal = rotor3.forward(signal)
signal = rotor2.forward(signal)
signal = rotor1.forward(signal)
signal = reflectorA.forward(signal)
signal = rotor1.backward(signal)
signal = rotor2.backward(signal)
signal = rotor3.backward(signal)
signal = Switched_Plugs.backward(signal)
letter = Keypressed.output(signal)
print(letter)