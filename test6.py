import random
import math

#wheel with offset values for the numbers
wheel = [[1,2,3,4,25],[12,13,4,5,21],[3,14,23,1,2],[4,15,10,18,3],[22,15,19,11,4],[12,21,2,4,7]]

# ensures that the row of the wheel starts at a random position, but always ensure it starts on the first column
row = random.randint(0,4);
column = random.randint(0,5);

encoder = [];

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "];

#assigns a number to each letter of the alphabet and other symbols and characters that will be used in the secret message
for i in range(0, len(alphabet)):
    encoder.append(i);
#print(encoder);

secret_message = "hello world";

cypher = "cypher";

numbered_secret_message = [];

#checks length of the secret message so the function can run through the whole string
#checks the numeric value of each letter and encodes it into numbers then appends them to the list called numbered_secret_message
for i in range(0, len(secret_message)):
    if secret_message[i] in alphabet:
        index = alphabet.index(secret_message[i]);
        numbered_secret_message.append(encoder[index]);

#prints original numbers to see difference, vestigial code
#print(numbered_secret_message);

#checks length of the secret message so that the function can cycle through it properly
for j in range(0, len(numbered_secret_message)):
    #offsets the number based on the position of the wheel row and column
    numbered_secret_message[j] += wheel[column][row]
    #makes sure that the number does not exceed the possible characters in alphabet list
    if numbered_secret_message[j] > len(alphabet) - 1:
        numbered_secret_message[j] -= len(alphabet);
    #changes which row is in use
    row += 1
    #ensure we never exceed row bounds
    if row == 5:
        row = 0;
    #changes which column is in use
    column += 1
    #ensure we never exceed column bounds
    if column == 6:
        column = 0;
#print(numbered_secret_message);

string = "";

for w in numbered_secret_message:
    if w in encoder:
        index2 = encoder.index(w)
        string += alphabet[index2];
print(string);
print(row);
print(column);