class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self): #<self = Tanda bantu
        self.headval = None  

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode #<~ new node = NODE / Field baru 

list = SLinkedList()
list.headval = Node("100")
e2 = Node("200")
e3 = Node("300")
e4 = Node("400")
e5 = Node("500")


list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtBegining("50") #insert di awal node 

list.listprint()



#Memasukkan elemen dalam linked list  melibatkan penugasan kembali pointer dari node yang ada ke node yang baru dimasukkan. 
#Bergantung pada apakah elemen data baru dimasukkan di awal atau di tengah atau di akhir linkedlist , kami memiliki skenario di bawah ini.
#Memasukkan di head linkedlist
#Ini melibatkan mengarahkan pointer berikutnya dari simpul data baru ke kepala saat ini dari linked list .
# Jadi head saat ini dari linked list  menjadi elemen data kedua dan simpul baru menjadi kepala dari linked list .