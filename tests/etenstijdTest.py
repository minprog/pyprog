import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_convert(test):
    def testMethod():
        converted = lib.getFunction("convert", test.fileName)
        time = converted("11:15")
        if time == 11.25:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'convert' werkt correct."


@t.test(1)
def checks_breakfast(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["7:25"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Het is tijd voor ontbijt")

    test.test = testMethod
    test.description = lambda : "7:25 is tijd voor ontbijt."


@t.test(2)
def checks_lunch(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["13:00"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Het is tijd voor lunch")

    test.test = testMethod
    test.description = lambda : "13:00 is tijd voor lunch."


@t.test(3)
def checks_dinner(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["18:01"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Het is tijd voor avondeten")

    test.test = testMethod
    test.description = lambda : "18:01 is tijd voor avondeten."


@t.test(4)
def checks_nomeal(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["19:01"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "")

    test.test = testMethod
    test.description = lambda : "19:01 is niet een tijdstip voor een maaltijd."
