import sys , keyword

print("Python Version:-",sys.version)

print("Python intrepreter location:-",sys.executable)


print("Python module search path:-")
for dir in sys.path:
    print(dir)

print("Pyhton keywords:-\n")
for word in keyword.kwlist:
    print(word)


