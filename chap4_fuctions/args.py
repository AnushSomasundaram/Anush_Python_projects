def echo(user,lang,sys):
    print("User:",user,"Language",lang,"Platform",sys)

echo("Mike","Python","Windows")

echo(lang="Pyhton",sys="Macos",user="anne")

def mirror(user="Carole",lang="Python"):
    print("\nUser",user,"\nLanguage",lang)

mirror()

mirror(lang="Java")
mirror(user="Tony")
mirror("susan","c++")

