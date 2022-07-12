import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_coin(test):
    def testMethod():
        coin = lib.getFunction("check_coin", test.fileName)
        if coin(25) and coin(10) and coin(5) and not coin(1) and not coin("10"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_coin' werkt correct."

@t.test(1)
def checks_due(test):
    def testMethod():
        due = lib.getFunction("determine_due", test.fileName)
        if due(25) == 25 and due(20) == 50 and due(10) == 40:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'determine_due' werkt correct."

@t.test(2)
def checks_main(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[25, 10, 25],
            overwriteAttributes = [("__name__", "__main__")])
        answer = "10"
        return asserts.exact(output.strip()[-2:], answer)

    test.test = testMethod
    test.description = lambda : "Het wisselgeld (10) wordt correct berekend bij het inwerpen van 25, 10, en 25 cent."
