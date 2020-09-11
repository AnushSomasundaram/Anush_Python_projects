#dictionary is a data container that can store multiple items of data as a list of key:value pairs.
#i.e in a dictionary  data container, the values are not referenced by their index but by their assignedd keys

dict={"name":"Bob","ref":"Python","sys":"Win"}

print("\nReference:",dict["ref"])
print("\nKeys:", dict.keys())

del dict["name"]
dict["User"]="tom"
print("\n dictionary:-",dict)
print("\nIs there a name in the dictionary dict:-","name" in dict)

