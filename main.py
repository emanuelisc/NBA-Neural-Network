from network.data import getDataFromFile, getDataFromApi, fixDuplicates, reduceData
from network.back import trainNetwork

def testas():
    print("testas")

def greeting():
    print("Sveiki atvykę į NBA rungtynių prognozavimo programą!\n\n")
    print("Toliau pasirinkite, kokius veiksmus norite atlikti:\n")

def main():
    print("\n\n1. Nuskaityti duomenis iš API")
    print("2. Nuskaityti duomenis iš failo")
    print("3. Surūšiuoti API duomenis")
    print("4. Sumažinti duomenų dimensijas")
    print("5. Apmokyti\n")

    var = input("Įveskite pasirinkimą: ")
    selection = str(var)
    if selection == "1":
        getDataFromApi()
        main()
    elif selection == "2":
        getDataFromFile()
        main()
    elif selection == "3":
        fixDuplicates()
        main()
    elif selection == "4":
        print("Įveskite pirmos komandos indeksą")
        ind1 = input("Pirmos komandos indeksas: ")
        print("Įveskite antros komandos indeksą")
        ind2 = input("Antros komandos indeksas: ")
        reduceData(ind1, ind2)
        main()
    elif selection == "5":
        trainNetwork()
        main()
    else:
        print("Neteisingas pasirinkimas")
        main()


if __name__ == "__main__":
    greeting()
    main()
