class Node:
    # Pembuatan Titik
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    # Pembuatan awal dari Linked List
    def __init__(self):
        self.head = None


    def append(self,data):
        # Pembuatan wadah titik baru 
        newNode = Node(data)
        
        # Jika List nya masih kosong masukkan saja jadi anggota pertama 
        if not self.head:
            self.head = newNode
            return
            
        # Jika sudah terisi kita pergi keujung akhir list
        current = self.head
        while current.next:
            current = current.next
            
        # Taruh titik diujung akhir dari list
        current.next = newNode

    def printall(self):
        # Cek jika list kosong
        if not self.head:
            print("List ini kosong");
            return

        current = self.head
        # Cek apakah current ada atau tidak,jika ada maka kita print data didalamnya
        while current:
            print(current.data)
            current = current.next
        
listsaya = LinkedList()

for i in range(1,5):
  listsaya.append(i)
  
listsaya.printall()
