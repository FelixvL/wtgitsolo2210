# 1 Database zometeen
# 2 API
# 3 CSV - csv pandas
# 4 Scrapen
import pandas
import mariadb

print("yes")
print("mooi")

def a(paramtje):
    x = 4
    print("tekst")
    if paramtje == 7:
        return 35
    else:
        return 47

b = a(17)
print(b)

verzameling = [350, 22, 12, 50]

for getal in verzameling:
    print(getal)

eigenvar = pandas.read_csv("Pokemon.csv")
print(eigenvar.columns)

zoekterm = input("Welke Pokemon zoek je?")

for pokemon in eigenvar["Name"]:
#    print(pokemon)
    if zoekterm == pokemon:
        print("GEVONDEN")

for i, pok in eigenvar.iterrows():
    if zoekterm == pok["Name"]:
        print("YES", "zijn strength is: ", pok["Speed"])

conn = mariadb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="huizendb"
        )

     # Instantiate Cursor
cur = conn.cursor()

cur.execute("SELECT * FROM huis")
for huis in cur:
    print(huis[1])
    print("iets anders")