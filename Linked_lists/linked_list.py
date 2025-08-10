#Las listas enlazadas son una lista de nodos que siempre apuntan al siguiente nodo

#No tienen indices
#Estan relacionadas por puntero

#Inserción , eliminacion al inicio de la lista O(1)
#Inserción, eliminacion en un lugar especifico o(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Big O(N)
    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Big O(1)
    def append_start(self , val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
        else:
            #Referenciamos el siguiente del nuevo nodo al nodo actual 
            # y  referenciamos la cabeza al nuevo nodo
            new_node.next = self.head
            self.head = new_node
    
    #Big O(N)
    def append_end(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        #Accedemos al ultimo sin llegar a None 
        while current.next is not None:
            current = current.next

        #Asignamos al final el nuevo nodo
        current.next = new_node

    #Big O(N)
    def append_at_index(self, val , index):
        new_node = Node(val)
        current = self.head
        counter = 0

        while current is not None and counter < index-1:
            counter += 1
            current = current.next
        
        if current is None:
            raise IndexError("Índice fuera de rango")
        
        new_node.next = current.next
        current.next = new_node
    
    #Big O(1)
    def del_first(self):
        if self.head is None:
            print("No existe que eliminar")
        
        self.head = self.head.next

    #Big O(N)
    def del_last(self):
        current = self.head

        #Current.next.next = es dos nodos despues del current actual
        while current.next.next is not None:
            current = current.next
        
        #El siguiente del current actual que siempre sera dos nodos antes del none
        #lo desvinculamos entonces el siguiente ya seria el None
        current.next = None
    
    #Big O(N)
    def del_at_index(self, index):
        counter = 0
        current = self.head

        if self.head is None:
            print("Lista vacía, nada que eliminar")
            return

        if index == 0:
            self.head = self.head.next
            return


        while current is not None and counter < index-1:
            current = current.next
            counter += 1

        if current is None or current.next is None:
            print("Índice fuera de rango")
            return
        
        #llegamos a un nodo anterior del que queremos eliminar
        #y su siguiente sera el siguiente del nodo que eliminaremos
        current.next = current.next.next
    
    #Big O(N)
    def deleteDuplicatesInSortedLinkedList(self):
        current = self.head

        #Verificamos si el actual y siguiente del actual no son none 
        #para poder validar los values de current.next.data con el current.data
        #y cambiar el puntero de asignacion.
        while current and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
                 

linked_list = LinkedList()

linked_list.append_start(5)
linked_list.append_start(2)
linked_list.append_start(10)
linked_list.append_end(9)

linked_list.append_end(8)

linked_list.append_at_index(1, 1)

linked_list.del_first()

linked_list.del_at_index(1)

linked_list.del_last()

linked_list.append_start(1)
linked_list.append_at_index(2, 2)
linked_list.append_at_index(2, 2)


linked_list.deleteDuplicatesInSortedLinkedList()
linked_list.print_linked_list()