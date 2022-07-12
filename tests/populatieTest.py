import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts


@t.test(0)
def checks_calculate_years(test):
    def testMethod():
        calculate_years = lib.getFunction("calculate_years", test.fileName)
        if (calculate_years(1200, 1300) == 1 and calculate_years(20, 100) == 20
            and calculate_years(100, 1000000) == 115 and calculate_years(50, 600) == 32):
            return True
        else:

            return False

    test.test = testMethod
    test.description = lambda : "De functie 'calculate_years' werkt correct."

@t.test(1)
def check_overall2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[6, 9, 5, -6, 18],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip()[-1], "8")

    test.test = testMethod
    test.description = lambda : "Je programma werkt volledig: wanneer incorrecte input wordt gegeven, wordt geprompt totdat er correcte input is. Waarna correct het aantal jaar wordt geprint."
