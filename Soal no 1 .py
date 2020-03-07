class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None  #<self = Tanda bantu 

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode  #<~ new node = NODE / Field baru 

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None: #<~ none = null
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("100")
e2 = Node("200")
e3 = Node("300")
e4 = Node("400")

list.headval.nextval = e3
e3.nextval = e4

list.AtEnd("500")  #insert data di akhir node

list.listprint()


#Memasukkan di Akhir linked list 

#Ini melibatkan menunjuk pointer berikutnya dari node terakhir saat ini dari linked list  ke node data baru.
# Jadi simpul terakhir saat ini dari linked list  menjadi simpul data terakhir kedua dan simpul baru menjadi simpul terakhir dari linked list .

#keterangan
#1.Bantu = self 
#2.Printval = isi Value nya 
#3.newnode = kotak baru 
#4.none = null 