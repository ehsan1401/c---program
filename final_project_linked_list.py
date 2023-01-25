import string
class node:
    def __init__(self, data=None):
        self.data = data
        self.first = None
        self.second = None
# class node_1link:
#     def __init__(self, data=None):
#         self.data = data
#         self.next=None
class linked_list:
    def __init__(self):
        self.head = node()

    def append_first(self,data):
        new_node = node(data)
        cur = self.head
        while cur.first != None:
            cur = cur.first
        cur.first = new_node
    
    def append_second(self,data,char):
        new_node = node(data)
        cur = char
        while cur.second != None:
            cur = cur.second
        cur.second = new_node
        return new_node
    

    def length(self):
        cur = self.head
        total = 0
        while cur.first != None:
            total += 1
            cur = cur.first
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.first != None:
            cur_node = cur_node.first
            elems.append(cur_node.data)
        print(elems)

    def find_in_first(self,key):
        cur_node = self.head
        while cur_node.first != None:
            if cur_node.data == key:
                return cur_node
            cur_node=cur_node.first
        return None

    def find_in_second(self,key,char):
        cur_node = char
        while cur_node.second != None:
            if cur_node.data == key:
                return cur_node
            cur_node=cur_node.second
        return None
    
    def append_first(self,key,data):
        new_node = node(data)
        cur_node = key
        while cur_node.first != None:
            cur_node = cur_node.first
        cur_node.first = new_node

    def erase(self, key):
        cur_node = self.head
        while cur_node.first != None:
            last_node = cur_node
            cur_node = cur_node.first
            if cur_node.data == key:
                last_node.first = cur_node.first
                return       
file_list= []
f = open("text.txt", "r")
for x in f:
    file_list.append(x)
file_list2= []
for i in file_list:
    i = i.replace(",", " ")
    i = i.replace(".", " ")
    file_list2.append(i)

alpha_link=linked_list()
y=alpha_link.head
for i in list(string.ascii_lowercase): #list of alphabet
    y.data=i
    y.first=node()
    y=y.first

# letter_link=linked_list()
counter=0
for line in file_list2:
    counter+=1
    for letter in line:
        letter=letter.lower()
        key=letter[0]
        target_char=alpha_link.find_in_first(key)
        p= alpha_link.find_in_second(letter,target_char)
        if p == None:
            target_letter=alpha_link.append_second(letter,target_char)
            alpha_link.append_first(target_letter,counter)
        else:
            alpha_link.append_first(p,counter)


# file_list3 = []
# for i in file_list2:
#     z=i.split()
#     file_list3.append(z)

# counter = 0
# for i in file_list3:
#     counter+=1
#     for x in i:
#         z = x.upper()
#         if len(z) > 3:
#             print(z , counter)