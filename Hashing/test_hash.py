from HashTable import HashTable

table = HashTable()  # Create a HashTable
print(table.is_empty())
table.insert("This", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Driver", 5)
table.insert("Noorul", 10)
table.insert("KM", 15)
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))
print("The value for 'Noorul' key: " + str(table.search("Noorul")))
print("The value for 'KM' key: " + str(table.search("KM")))