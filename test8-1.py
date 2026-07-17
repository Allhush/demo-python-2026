rotor_I = [['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b', 'r', 'c', 'j'], "q"]
rotor_II = [['a', 'j', 'd', 'k', 's', 'i', 'r', 'u', 'x', 'b', 'l', 'h', 'w', 't', 'm', 'c', 'q', 'g', 'z', 'n', 'p', 'y', 'f', 'v', 'o', 'e'], "e"]
rotor_III = [['b', 'd', 'f', 'h', 'j', 'l', 'c', 'p', 'r', 't', 'x', 'v', 'z', 'n', 'y', 'e', 'i', 'w', 'g', 'a', 'k', 'm', 'u', 's', 'q', 'o'], "v"]
rotor_IV = [['e', 's', 'o', 'v', 'p', 'z', 'j', 'a', 'y', 'q', 'u', 'i', 'r', 'h', 'x', 'l', 'n', 'f', 't', 'g', 'k', 'd', 'c', 'm', 'w', 'b'], "j"]
rotor_V = [['v', 'z', 'b', 'r', 'g', 'i', 't', 'y', 'u', 'p', 's', 'd', 'n', 'h', 'l', 'x', 'a', 'w', 'm', 'j', 'q', 'o', 'f', 'e', 'c', 'k'], "z"]
#rotor_VI = [['j', 'p', 'g', 'v', 'o', 'u', 'm', 'f', 'y', 'q', 'b', 'e', 'n', 'h', 'z', 'r', 'd', 'k', 'a', 's', 'x', 'l', 'i', 'c', 't', 'w'], "z", "m"]
#rotor_VII = [['n', 'z', 'j', 'h', 'g', 'r', 'c', 'x', 'm', 'y', 's', 'w', 'b', 'o', 'u', 'f', 'a', 'i', 'v', 'l', 'p', 'e', 'k', 'q', 'd', 't'], "z", "m"]
#rotor_VIII = [['f', 'k', 'q', 'h', 't', 'l', 'x', 'o', 'c', 'b', 'j', 's', 'p', 'd', 'z', 'r', 'a', 'm', 'e', 'w', 'n', 'i', 'u', 'y', 'g', 'v'], "z", "m"]
reflector_A = ['e', 'j', 'm', 'z', 'a', 'l', 'y', 'x', 'v', 'b', 'w', 'f', 'c', 'r', 'q', 'u', 'o', 'n', 't', 's', 'p', 'i', 'k', 'h', 'g', 'd']
reflector_B = ['y', 'r', 'u', 'h', 'q', 's', 'l', 'd', 'p', 'x', 'n', 'g', 'o', 'k', 'm', 'i', 'e', 'b', 'f', 'z', 'c', 'w', 'v', 'j', 'a', 't']
reflector_C = ['f', 'v', 'p', 'j', 'i', 'a', 'o', 'y', 'e', 'd', 'r', 'z', 'x', 'w', 'g', 'c', 't', 'k', 'u', 'q', 's', 'b', 'n', 'm', 'h', 'l']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class StringToList:
    def __init__(self, string):
        '''string takes a string as an input and then transforms it into a list which can the be called using .list'''
        self.string = string
        self.list = []
        for i in string:
            self.list.append(i)
        
class InAndOut:
    '''forward transorms a letter input from a letter into a number so that it can be passed onto the next function 
    backwards takes a number and transforms it into a letter so that it can be output legibily'''
    def forward(self, letter):
        signal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].index(letter)
        return signal
    def backward(self, signal):
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][signal]
        return letter

class Plugboard:
    def __init__ (self, pairs):
        '''self.right is the regular alphabet and should not be changed
        self.left is meant to have its letter swapped places with one another so as to better encode the message'''
        self.right = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for pair in pairs:
            #finds the letter that will be swapped
            one = pair[0]
            two = pair[1]
            #finds the positions of the letters so the function knows where to move the new letters
            pos_1 = self.left.index(one)
            pos_2 = self.left.index(two)
            #puts each letter into its new position
            self.left[pos_1] = two
            self.left[pos_2] = one
    def forward(self, signal):
        '''signal is recieved from another function and is used to find what position it should look at to find the correct letter in the regular alphabet(self.right)
        this letter is then found in the encoded alphabet (self.left) and has its position returned so that it can be passed to the rotors'''
        letter = self.right[signal]
        signal = self.left.index(letter)
        return signal
    def backward(self, signal):
        '''signal comes from the rotors and passes into the encoded alphabet denoting the position of a letter
        this letter is then found in the regular alphabet and its position is passed on'''
        letter = self.left[signal]
        signal = self.right.index(letter)
        return signal


class Rotor:
    def __init__(self, encoding, turnover):
        self.right = encoding
        self.left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.notch = turnover
    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.index(letter)
        return signal
    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.index(letter)
        return signal
    def rotate(self):
        left = self.left.pop(0)
        self.left.append(left)
        right = self.right.pop(0)
        self.right.append(right)
    def rotate_to(self, letter):
        '''letter is a string of the letter the user wants to rotate to'''
        pos_rotate = self.left.index(letter)
        self.left = self.left[pos_rotate:] + self.left[:pos_rotate]
        self.right = self.right[pos_rotate:] + self.right[:pos_rotate]


class Reflection:
    def __init__(self, encoding):
        self.right = encoding
        self.left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.index(letter)
        return signal


q = Rotor(rotor_I[0], rotor_I[1])
q.rotate_to("q")
print(q.left)
print(q.right)