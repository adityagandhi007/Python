class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next


llist = SLinkedList()
llist.RemoveNode("500") #node yang di hapus
llist.Atbegining("400")
llist.RemoveNode("300") #node yang di hapus 
llist.Atbegining("250")
llist.Atbegining("200")
llist.Atbegining("100")
llist.Atbegining("50")

llist.LListprint()

#Menghapus Item dari linked list 

#Kami dapat menghapus node yang ada menggunakan key untuk node itu. 
#Dalam program di bawah ini kami menemukan node sebelumnya dari node yang akan dihapus. 
#Kemudian arahkan pointer berikutnya dari node ini ke node berikutnya hingga node yang akan dihapus.


#keterangan
#1.Bantu = self 
#2.Printval = isi Value nya 