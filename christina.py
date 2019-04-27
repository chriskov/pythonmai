from air import *


def main():
    airfleets = [ Russia(),S7(), Utair(),  Ural(), Nordstar()]
    for airfleet in airfleets:
        print(airfleet.company_name + ' имеет:')
        print(airfleet.about_aircrafts)
        print('\n')

if __name__ == "__main__":
    main()
