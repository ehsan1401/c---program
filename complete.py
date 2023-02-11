import string

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.down = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append_in_next(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def spliter(self,data):
        for x in data:
            file_list= []
            file_list.append(x)
            file_list2= []
        for i in file_list:
            i = i.replace(",", " ")
            i = i.replace(".", " ")
            i = i.replace("\n", " ")
            file_list2.append(i)
        file_list3 = []
        for i in file_list2:
            i = i.split(" ")
            file_list3.append(i)
        return file_list3
    

alpha_link=linked_list()
link = alpha_link.head

file = input("Enter the file name: ")
f = open(file, "r")
file = alpha_link.spliter(f)

for i in list(string.ascii_lowercase):
    alpha_link.append_in_next(i)

counter =0 
for i in file:
    counter +=1
    for x in i:
        if (len(x) > 1):
            one = x[0].lower()
            while link.next != None:
                if link.data != one:
                    link = link.next
                else:
                    break;
            if link.next != None:
                while link.down != None:
                    if link.down.data == x.lower():
                        link.dwon.next = node(counter)
                        break;
                    else:
                        link = link.down   

search = input("Enter the word to search: ")
search_let = search[0].lower()

while link.next != None:
    if link.data != search_let:
        link = link.next
    else:
        break;
if link.next != None:
    while link.down != None:
        if link.down.data == search.lower():
            while link.down.next != None:
                print(link.down.next.data)
                link.down = link.down.next