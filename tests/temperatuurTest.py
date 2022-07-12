import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts


@t.test(0)
def checks_change_temperature(test):
    def testMethod():
        change_temperature = lib.getFunction("change_temperature", test.fileName)
        if change_temperature("C", 10) == 50 and change_temperature("F", 9) == -12:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'change_temperature' werkt correct."


@t.test(1)
def checks_capital(test):
    def testMethod():
        change_temperature = lib.getFunction("change_temperature", test.fileName)
        if (change_temperature("C", 10) and change_temperature("c", 10) and
            change_temperature("F", 9) and change_temperature("f", 9)):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "Zowel 'C' en 'F' als 'c' en 'f' worden geaccpeteerd."


@t.test(2)
def check_overall1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["F", 0, 9, 3],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12")

    test.test = testMethod
    test.description = lambda : "De correcte tabel wordt geprint bij een omzetting van F naar C met 0 als begin temperatuur, 9 als eindtemperatuur en 3 als stapgrootte."


@t.test(3)
def check_overall2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["C", 0, 20, 5],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "C |   F\n  0 |  32\n  5 |  41\n 10 |  50\n 15 |  59\n 20 |  68")

    test.test = testMethod
    test.description = lambda : "De correcte tabel wordt geprint bij een omzetting van C naar F met 0 als begin temperatuur, 20 als eindtemperatuur en 5 als stapgrootte."
