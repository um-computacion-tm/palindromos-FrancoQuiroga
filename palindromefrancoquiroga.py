import unittest
#funcion iterativa
def palindrome(palabra):
    listpalindrome = []
    for letra in palabra:
        listpalindrome.append(letra)
    for i in range(0, len(palabra), 1):
        if listpalindrome[i] != listpalindrome[-i-1]:
            return False
    return True
#funcion recursiva
def palindromerecursive(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return palindromerecursive(word - 1) + palindrome(word - 2)
    else:
        return False

class Testpalindrome(unittest.TestCase):
#test palindrome recursivo

#test palindrome iterativo
    def testala(self):
        resultado =  palindrome('ala')
        self.assertEqual(resultado, True)
    def testneuquen(self):
        resultado =  palindrome('neuquen')
        self.assertEqual(resultado, True)
    def testpajaro(self):
        resultado =  palindrome('pajaro')
        self.assertEqual(resultado, False)
    def testsometemos(self):
        resultado =  palindrome('sometemos')
        self.assertEqual(resultado, True)
    def testagita_falsos_usos_la_fatiga(self):
        resultado =  palindrome('agita falsos usos la fatiga')
        self.assertEqual(resultado, True)
    def testsometemosrecursivo(self):

if __name__ == '__main__':

    unittest.main()
