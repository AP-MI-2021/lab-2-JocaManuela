'''
Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).
'''

def get_leap_years(year_1, year_2):
    '''
    Programul afiseaza toti anii bisecti intre doi ani dati (inclusiv anii dati)
    :param year_1: int,primul numar care reprezinta primul an dat
    :param year_2: int, al doilea numar care reprezinta al doilea an dat
    :return: anii bisecti cuprinsi intre cei doi ani dati
    '''
    list = []

    # Este parcursă lista, care conține valorile cuprinse între year_1 și year_2

    for year in range(year_1, year_2):
        if year % 4 == 0:
            list.append(year)
        year = year + 1
    return list

def test_get_leap_years():
     assert (get_leap_years([1624, 1634])) == (1624,1628,1632), 'Anii bisecți cuprinși între 1624 și 1634 sunt: 1624,1628,1632'
     assert (get_leap_years([1999, 2007])) == (2000,2004), 'Anii bisecți cuprinși între 1999 și 2007 sunt: 2000,2004'
     assert (get_leap_years([2010, 2024])) == (2012,2016,2020,2024), 'Anii bisecți cuprinși între 2010 și 2024 sunt: 2012,2016,2020,2024'




'''
Afișează toate pătratele perfecte dintr-un interval închis dat.
'''

def get_perfect_squares(number_1, number_2):
    '''
    Programul afiseaza toate patratele perfecte dintr-un interval inchis dat
    :param number_1: int, primul numar din interval
    :param number_2: int, al doilea numar din interval
    :return: toate patratele perfecte din intervalul dat
    '''
    list = []

    # Este parcursă lista, care conține valorile cuprinse între number_1 și number_2

    for i in range(number_1, number_2):
        j = 1;
        while j * j <= i:
            if j * j == i:
                list.append(i)
            j = j + 1
        i = i + 1
    return list

def test_get_perfect_squares():
    assert (get_perfect_squares([10, 30])) == (16,25), 'Pătratele perfecte cuprinse între 10 și 30 sunt: 16, 25'
    assert (get_perfect_squares([19, 38])) == (25, 36), 'Pătratele perfecte cuprinse între 19 și 38 sunt: 25, 36'
    assert (get_perfect_squares([4, 12])) == (4, 9), 'Pătratele perfecte cuprinse între 4 și 12 sunt: 4, 9'


'''
Determină dacă un număr dat este palindrom.
'''
def is_palindrome(n):

    '''
    Verifica daca un numar introdus este palindrom
    :param n: numarul despre care vrem sa stim daca este palindrom
    :return: True, daca numarul este palindrom
             False, daca numarul nu este palindrom
    '''

    temp = n

    oglindit = 0

    while (n > 0):
        ultima_cifra = n % 10
        oglindit = oglindit *10 + ultima_cifra
        n = n // 10

    if (temp == oglindit):
        return True
    else:
        return False


def test_is_palindrome():
    assert (is_palindrome(121)) == True, "Numarul 121 este palindrom"
    assert (is_palindrome(245)) == False, "Numarul 245 nu este palindrom"
    assert (is_palindrome(343)) == True, "Numarul 343 este palindrom"



def print_menu():
    print('1.Afișarea tuturor anilor bisecți între doi ani dați')
    print('2.Afișarea tuturor pătratelor perfecte dintr-un interval închis dat')
    print('3.Verifică dacă numărul introdus este palindrom')
    print('x.Ieșire')

def main():
    list = []
    while True:
        print_menu()
        option = input('Alege opțiunea:')
        if option == '1':
            year_1 = int(input("\nIntroduceți un număr: "))
            year_2 = int(input("\nIntroduceți alt număr: "))
            print("\nAnii bisecți cuprinși în intervalul ", year_1, ", ", year_2, "sunt: ",get_leap_years(year_1, year_2))
        elif option == '2':
            number_1 = int(input("\nIntroduceți un număr: "))
            number_2 = int(input("\nIntroduceți alt număr: "))
            print("\nPătratele perfecte cuprinse în intervalul ", number_1, "si ", number_2, "sunt: ",get_perfect_squares(number_1, number_2))
        elif option == '3':
            n = int(input("\nIntroduceti un numar: "))
            if (is_palindrome(n)):
                print("\nNumarul", n, "este palindrom!")
            else:
                print("\nNumarul", n, "nu este palindrom")
        elif option == 'x':
            break
        else:
            print('Opțiune invalidă')
main()
