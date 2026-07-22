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
    '''forward transforms a letter input from a letter into a number so that it can be passed onto the next function 
    backwards takes a number and transforms it into a letter so that it can be output legibily'''
    def forward(self, letter):
        letter = letter.lower()
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
        '''encoding is a list of all of the characters in the alphabet which have had their order re arraged
        turnover is what character causes the subsequent rotor on the wheel to rotate'''
        self.right = encoding
        self.left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.notch = turnover
    def forward(self, signal):
        '''essentially the same as forward in plugboard'''
        letter = self.right[signal]
        signal = self.left.index(letter)
        return signal 
    def backward(self, signal):
        '''essentially the same as backward in plugboard'''
        letter = self.left[signal]
        signal = self.right.index(letter)
        return signal
    def rotate(self):
        '''turns the rotor by removing the first letter in the rotor and appending it to the last position'''
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
        '''essentially the same as forward in plugboard'''
        letter = self.right[signal]
        signal = self.left.index(letter)
        return signal
    def backward(self, signal):
        '''not in use, was attempting to do something but it didn't work'''
        letter = self.left[signal]
        signal = self.right.index(letter)
        return signal


class Encryption:
    def __init__ (self, rotor1, rotor2, rotor3, rotor4, plugs, keys, reflect):
        #leftmost rotor
        self.r1 = rotor1
        #middle rotor
        self.r2 = rotor2
        #rightmost rotor
        self.r3 = rotor3
        #extra rotor, not in use
        self.r4 = rotor4
        #plugboard with switched plugs
        self.pb = plugs
        #is used to transform letter into number signal
        self.kp = keys
        #is the refelctor, simply reflects letter
        self.rm = reflect

    def encode_3_rotor(self, letter):
        '''uses three rotors to encode the message, and the rotors are rotated acording to each notch'''
        if self.r3.left[0] == self.r3.notch and self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r3.rotate()
            self.r2.rotate()
        else:
            self.r3.rotate()

        code = self.kp.forward(letter)
        code = self.pb.forward(code)
        code = self.r3.forward(code)
        code = self.r2.forward(code)
        code = self.r1.forward(code)
        code = self.rm.forward(code)
        code = self.r1.backward(code)
        code = self.r2.backward(code)
        code = self.r3.backward(code)
        code = self.pb.backward(code)
        code = self.kp.backward(code)
        return code

    def key(self, passkey):
        '''passkey is a three letter key that causes the wheels to rotate to those letters'''
        passkey = passkey.lower()
        self.r3.rotate_to(passkey[2])
        self.r2.rotate_to(passkey[1])
        self.r1.rotate_to(passkey[0])
        if len(passkey) == 4:
            self.r4.rotate_to(passkey[3])


#    def encode_4_rotor(self, letter):
#        if self.r4.left[0] == self.r4.notch and self.r3.left[0] == self.r3.notch and self.r2.left[0] == self.r2.notch:
#            self.r1.rotate()
#            self.r2.rotate()
#            self.r3.rotate()
#            self.r4.rotate()
#
#        elif self.r4.left[0] == self.r4.notch and self.r3.left[0] == self.r3.notch and self.r2.left[0] == self.r2.notch:
#            self.r2.rotate()
#            self.r3.rotate()
#            self.r4.rotate()
#
#        elif self.r4.left[0] == self.r4.notch and self.r3.left[0] == self.r3.notch:
#            self.r3.rotate()
#            self.r4.rotate()
#
#        else:
#            self.r4.rotate()
#
#        code = self.kp.forward(letter)
#        code = self.pb.forward(code)
#        code = self.r4.forward(code)
#        code = self.r3.forward(code)
#        code = self.r2.forward(code)
#        code = self.r1.forward(code)
#        code = self.rm.forward(code)
#        code = self.r1.backward(code)
#        code = self.r2.backward(code)
#        code = self.r3.backward(code)
#        code = self.r4.backward(code)
#        code = self.pb.backward(code)
#        code = self.kp.backward(code)
#        return code

I = Rotor(rotor_I[0], rotor_I[1])
II = Rotor(rotor_II[0], rotor_II[1])
III = Rotor(rotor_III[0], rotor_III[1])
IV = Rotor(rotor_IV[0], rotor_IV[1])
V = Rotor(rotor_V[0], rotor_V[1])
A = Reflection(reflector_A)
B = Reflection(reflector_B)
C = Reflection(reflector_C)
plugs = Plugboard(["ak", "fz", "nj", "ty"])
keys_pressed = InAndOut()

prayer = Encryption(I, II, III, IV, plugs, keys_pressed, B)

message = "jxfl rd o ngfzdbb gvhzkgb ek pqwph vnq aarhfy reiaia"
new_message = []

prayer.key('ajh')
new_message = []
message = message.lower()
for i in message:
    if not i in alphabet:
        new_message.append(i)
    else:
        new_message.append(prayer.encode_3_rotor(i))
new_string = ''
for i in new_message:
    new_string = new_string + i
print(new_string)