import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_answer0(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["42"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Ja")

    test.test = testMethod
    test.description = lambda : "Het antwoord '42' leidt tot de output Ja."


@t.test(1)
def checks_answer1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["tweeenveertig"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Ja")

    test.test = testMethod
    test.description = lambda : "Het antwoord 'tweeenveertig' leidt tot de output Ja."

@t.test(2)
def checks_answer2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["tweeen veertig"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Ja")

    test.test = testMethod
    test.description = lambda : "Het antwoord 'tweeen veertig' leidt tot de output Ja."

@t.test(3)
def checks_answer3(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["TWEEENVEERTIG"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Nee")

    test.test = testMethod
    test.description = lambda : "Het antwoord 'TWEEENVEERTIG' leidt tot de output Nee."

@t.test(4)
def checks_answer4(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["53"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Nee")

    test.test = testMethod
    test.description = lambda : "Het antwoord '53' leidt tot de output Nee."
