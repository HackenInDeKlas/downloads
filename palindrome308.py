import unittest

def digits(x):
    """Converteert een integer naar een lijst cijfers.

    Args:
        x: Het getal waarvan we de cijfers gebruiken.
        
    Retourneert: Een lijst cijfers in de volgorde van ''x''.
    
    >>> digits(4586378)
    [4, 5, 8, 6, 3, 7, 8]
    """
        
    digs = []
    while x != 0:
        #deel het getal door 10
        div, mod = divmod(x, 10)
        digs.append(mod)
        x = div
    digs.reverse()
    return digs

def is_palindrome(x):
    """Vaststellen of een integer een palindroom is.

    Args:
        x: Het te controleren getal.
        
    Retourneert: True als de cijfers van ''x'' een palindroom zijn, anders False.
    
    >>> is_palindrome(1234)
    False
    >>> is_palindrome(2468642)
    True
    """
    digs = digits(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
    return True

class Tests(unittest.TestCase):
    """Tests voor de functie ''is_palindrome()''."""
    def test_negative(self):
        """Controleren of False correct wordt geretourneerd."""
        self.assertFalse(is_palindrome(1234))
        
    def test_positive(self):
        """Controleren of True correct wordt geretourneerd."""
        self.assertTrue(is_palindrome(1234321))
        
    def test_single_digit(self):
        """Controleren of dit werkt bij getallen met 1 cijfer."""
        for i in range(10):
            self.assertTrue(is_palindrome(i))
            
if __name__ == '__main__':
    unittest.main()