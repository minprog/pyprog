import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

"""
TODO:
- check of geod te groot en te klein wordt geprint
- check programma overall (als niet goed geraden opnieuw prompten)
"""


@t.test(0)
def checks_check_guess(test):
    def testMethod():
        check_guess = lib.getFunction("check_guess", test.fileName)
        if check_guess(10, 10) and not check_guess(5, 10):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_guess' werkt correct."

@t.test(1)
def checks_decide_number(test):
    def testMethod():
        decide_number = lib.getFunction("decide_number", test.fileName)
        if (decide_number(1000) != decide_number(1000) and decide_number(1) == 1
            and decide_number(3) <= 3):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'decide_number' werkt correct."

@t.test(2)
def check_level1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[1, 1],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Je hebt het getal goed geraden, gefeliciteerd!")

    test.test = testMethod
    test.description = lambda : "Bij level 1 wordt 1 goed geraden."

@t.test(2)
def check_overall(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip()[-14:], "gefeliciteerd!")

    test.test = testMethod
    test.description = lambda : "Bij level 10 kan het goede getal geraden worden."
