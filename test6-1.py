import random

rotors = [[10,16,21,18,6,12,25,3,14,24,5,9,22,17,15,0,1,20,26,4,19,11,2,23,13,8,7],[2,12,7,1,3,8,6,11,22,13,15,4,19,26,16,9,20,0,23,17,18,10,24,14,5,21,25],[5,6,26,13,11,17,22,24,8,20,16,23,7,15,14,9,10,18,0,21,12,1,2,3,19,4,25],[7,23,9,25,13,5,2,12,11,21,8,14,20,3,0,16,24,1,26,10,15,17,18,19,6,4,22],[20,2,13,14,21,18,23,6,12,26,9,15,19,24,25,7,22,8,5,11,1,3,17,0,10,16,4]]

#stores the actual rotors picked
encoder_rotors = [];
#ensures the same rotor isn't picked twice
checker = [];
#selects what row of the rotor is being used
row = 0;
#refers to the singular rotor the encoder is on, but using rotor would be confusing
column = 0;
#will hold the message once it is encoded
secret_message = [];
#temporary placeholder for a message
message = "hello world";
#stores message as a number
message_numbers = [];
#holds alphabet and symbols stored as numbers
encoder = [];
#holds alphabet and symbols used in message
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "];
#holds the value of the new letter once it is encoded before it is appended to the list secret message
transfer_number = 0

#checks length of the picked rotors to see if it has met the required number
while len(encoder_rotors) < 3:
    #picks a random rotor from those availble
    picked_rotor = random.randint(0,4)
    #checks to make sure there isn't repeated rotor then adds the rotor to the encoder rotors
    if picked_rotor not in checker:
        encoder_rotors.append(rotors[picked_rotor])
        checker.append(picked_rotor);

#debug vestigial code
print(str(encoder_rotors[0][0]) + " " + str(encoder_rotors[1][0]) + " " + str(encoder_rotors[2][0]));


#assigns a number to each letter of the alphabet and other symbols and characters that will be used in the secret message
for i in range(0, len(alphabet)):
    encoder.append(i);
#print(encoder);

#uses the length of the message to cycle though it and recreate it as a list of numbers
for i in range(0, len(message)):
    #checks the message at point i to see if that symbol is valid
    if message[i] in alphabet:
        #matches the symbol to its numeric value
        index = alphabet.index(message[i]);
        #appends the numeric value of the symbol to the list which stores the numeric message
        message_numbers.append(encoder[index]);
#print(message);
print(message_numbers);


for j in range(0, len(message_numbers)):
    #changes the letter based on the row and column starting point runs through the rotors starting from rotor 0 to rotor 1 to rotor 2 to rotor 2 again then rotor 1 and finally spits out a value from rotor 0
    transfer_number = message_numbers[j] + encoder_rotors[0][encoder_rotors[1][encoder_rotors[2][encoder_rotors[2][encoder_rotors[1][encoder_rotors[0][row]]]]]]
    #checks if transfer number is outside availible symbols
    if transfer_number > len(encoder):
        #if transfer number is outside availible symbols it corrects it
        transfer_number -= len(encoder)
    #adds letter to the secret number
    secret_message.append(transfer_number)
    #increases what row we are on
    row += 1
    #checks to make sure we are still on an availble row
    if row > len(encoder_rotors[0])-1:
        #resets row we are on if we are not on an availible row
        row = 0
        #increases column number once we reset the row number
        column += 1
    if column > len(encoder_rotors)-1:
        # resets the column number if we go past it
        column = 0;
print(secret_message);
