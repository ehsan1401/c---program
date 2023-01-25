import string
class node:
    def __init__(self, data=None):
        self.data = data
        self.first = None
        self.second = None
class linked_list:
    def __init__(self):
        self.head = node()

    def append_first(self,data):
        new_node = node(data)
        cur = self.head
        while cur.first != None:
            cur = cur.first
        cur.first = new_node
    
    def append_second(self,data):
        new_node = node(data)
        cur = self.head
        while cur.second != None:
            cur = cur.second
        cur.second = new_node

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
    y=y.first

counter=0
for line in file_list2:
    counter+=1
    for char in line:
        key=char[0]
        

    


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