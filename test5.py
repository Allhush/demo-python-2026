alphabet = "abcdefghijklmnopqrstuvwxyz "
list = [];
for i in alphabet:
    list.append(i);


list2 = [];
for i in range(0, len(list)):
    list2.append(i);


message = "beep boop";

messagelist = [];
for q in message:
    if q in list:
        index = list.index(q)
        messagelist.append(list2[index]);
print(message);
print(messagelist);

string = "";

for w in messagelist:
    if w in list2:
        index2 = list2.index(w)
        string += list[index2];
print(string);