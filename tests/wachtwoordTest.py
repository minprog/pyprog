import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_length(test):
    def testMethod():
        length = lib.getFunction("check_length", test.fileName)
        if length("12345678") and length("ThisIsAtLeast8") and not length(""):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_length' werkt correct."


@t.test(1)
def checks_letter(test):
    def testMethod():
        letter = lib.getFunction("check_letter", test.fileName)
        if letter("AaBbCc") and not letter("abc") and not letter("ABC") and not letter("123"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_letter' werkt correct."


@t.test(2)
def checks_number(test):
    def testMethod():
        number = lib.getFunction("check_number", test.fileName)
        if number("123") and number("Hello123") and not number("Hello"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_number' werkt correct."

@t.test(3)
def checks_password(test):
    def testMethod():
        password = lib.getFunction("check_password", test.fileName)
        if password(True, True, True) and not password(True, False, False) and not password(False, False, False):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_password' werkt correct."
