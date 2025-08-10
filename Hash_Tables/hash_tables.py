#  Una Hash Table es una estructura de datos que guarda por clave y valor,
#  hasheando la clave a un entero y  guardando los valores en un array

#  Objetivo de una hashTable
#  Buscar, Insertar y elimar en una complejidad cercana a Big O(1)

# Colisiones: cuando 2 claves diferentes se generan con el mismo hash
        # Encadenamiento (chaining) : Si se llega a hashear una clave con el mismo hash, 
        # guardamos todos los valores como una linked list

        # Direccionamiento Abierto (Open Addressing): Buscas las isguiente posicion disponible para guardar la clave

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None # Manejar colisiones como una lista enlazada


class HashTable:
    def __init__(self, size= 10):
        self.size = size
        self.buckets = [None] * size # Arrays de buckets
    
    #Funcion para hashear
    def hash(self, key):
        #retornamos el hash generado
        return sum(ord(c) for c in str(key)) % self.size
    
    #Funcion apra imprimir la tabla
    def print_table(self):
        for i , node in enumerate(self.buckets):
            print(f"Bucket {i}: " , end=" ")
            current = node
            if not current:
                print("Empty")
                continue
            while current:
                print(f"{current.key}: {current.value}", end=" -> ")
                current =current.next
            
            print("None")
    
    def insert(self, key, value):
        index = self.hash(key)
        #Obtiene el nodo inicial en el bucket
        node = self.buckets[index]

        #Si el nodo esta vacio se asigna
        if node is None:
            self.buckets[index] = HashNode(key, value)
        else:
            # Recorremos la lista en caso de colision con el
            # Chaining method

            prev = None
            while node:
                #Si si existe actualizamos el valor al nuevo valor
                if node.key == key:
                    node.value = value
                    return
                #Seguimos apuntando al siguiente
                prev = node
                node = node.next
            #Si no existe insertamos en el siguiente del ultimo valor el nuevo nodo
            prev.next = HashNode(key, value)
    
    def get(self, key):
        index = self.hash(key)
        #Encontramos el bucket en el cual esta el hash
        node = self.buckets[index]

        #Recorremos ese nodo hasta entontrar la clave correspondiente y devolvemos
        #el value, si no lo encontramos seguimos recorrendo con el .next
        while node:
            if node.key == key:
                print(node.value)
                return node.value
            
            node = node.next
        return None
    
    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    # sie es la primero vez
                    self.buckets[index] = node.next
                
                return True
            prev = node
            node = node.next
        return False #No se encontro



hash_table = HashTable()
hash_table.insert("Frutas", "Mango")
hash_table.insert("Verduras", "Chayote")
hash_table.insert("legumbres", "Frijol negro")

hash_table.remove("Verduras")

hash_table.get("Frutas")

hash_table.print_table()