print("hello world")

szam = 10 # egész szám
tortszam = 5.5 # nem egész szám
szoveg = "macska" # szöveg

print(szam)
print(tortszam)
print(szoveg)

# Konkatenációhoz example
vezeteknev = "Apró"
keresztnev = "Tamás"

print(vezeteknev, keresztnev) # konkatenáció v1
print(vezeteknev + " " + keresztnev) # konkatenáció v2

# Verzió 1
print("Kérem add meg a nevedet")
nev = input()
print("Szia, " + nev)

"""
#összeadás verzio 1
print("kérem adja meg az első számot")
szam1 = int(input())
print("kérem adja meg a második számot")
szam2 = int(input())

osszeg = szam1 + szam2
print("A két szám összege: " + str(osszeg))
"""
"""
#összeadás verzio 2
szam1 = int(input("kérem adja meg az első számot"))
szam2 = int(input("kérem adja meg a második számot"))

osszeg = szam1 + szam2
print(f"A két szám összege: {osszeg}")
print(f"A két szám összege: {szam1 + szam2}")

"""
#Kivonás 1
szam1 = int(input("kérem adja meg az első számot"))
szam2 = int(input("kérem adja meg a második számot"))

különbsége = szam1 - szam2
print(f"A két szám különbsége: {különbsége}")
