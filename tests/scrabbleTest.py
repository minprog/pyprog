import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts


@t.test(0)
def checks_compute_score(test):
    def testMethod():
        compute_score = lib.getFunction("compute_score", test.fileName)
        if (compute_score("WORD") == compute_score("word") and
            compute_score("Test") == 4 and
            compute_score("abcdefghijklmnopqrstuvwxyz") == 87):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'compute_score' werkt correct."

@t.test(1)
def check_S1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["Pizza", "Kaas"],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Speler 1 wint!")

    test.test = testMethod
    test.description = lambda : "Als speler 1 'Pizza' zegt en speler 2 'Kaas', dan wint speler 1."

@t.test(2)
def check_S2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["Hotel", "Kamperen"],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Speler 2 wint!")

    test.test = testMethod
    test.description = lambda : "Als speler 1 'Hotel' zegt en speler 2 'Kamperen', dan wint speler 2."

@t.test(3)
def check_gelijkspel(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["Vrijdag", "Zaterdag"],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Gelijkspel!")

    test.test = testMethod
    test.description = lambda : "Als speler 1 'Vrijdag' zegt en speler 2 'Zaterdag', dan is er een gelijkspel."
