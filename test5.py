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