class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.e1 = None

# Fungsi nemembahkan node baru di tengah"
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

# Print  linked list
    def listprint(self):
        printval = self.e1
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.e1 = Node("50")
e2 = Node("100")
e3 = Node("200")
e4 = Node("300")
e5 = Node("400")
e6 = Node("500")



list.e1.nextval= e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6



list.Inbetween(e2.nextval,"250") # insert node di antara 200 & 300

list.listprint()

#Memasukkan di antara dua Data Nodes

#Ini melibatkan pengejaran pointer dari simpul tertentu untuk menunjuk ke simpul baru. 
#Itu dimungkinkan dengan melewati kedua simpul baru dan simpul yang ada setelah mana simpul baru akan dimasukkan. 
#Jadi kita mendefinisikan kelas tambahan yang akan mengubah pointer selanjutnya dari node baru ke pointer berikutnya dari node tengah.
# Kemudian tetapkan node baru ke pointer berikutnya dari node tengah.