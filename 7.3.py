lentoasemat = {}

while True:
    valinta = input("Haluatko uuden aseman (u), hakea (h) vai lopettaa (l)? ").lower()

    if valinta == "u":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif valinta == "h":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoasema:", lentoasemat[icao])
        else:
            print("Ei löytynyt")
    elif valinta == "l":
        break