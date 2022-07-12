import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_count(test):
    def testMethod():
        count_values = lib.getFunction("count_values", test.fileName)
        if (count_values("Hello, this sentence contains words.") == (30, 5, 1) and
            count_values("Hello world. The wheather is great today!") == (33, 7, 2) and
            count_values("Sentence, with; loads: of characeters. Let's make it two!")
            == (43, 9, 2)):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'count_values' werkt correct."

@t.test(1)
def checks_coleman_liau(test):
    def testMethod():
        coleman_liau = lib.getFunction("coleman_liau", test.fileName)
        if coleman_liau(537, 4.2) == 15:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'coleman_liau' werkt correct."

@t.test(2)
def checks_calculate_grade(test):
    def testMethod():
        calculate_grade = lib.getFunction("calculate_grade", test.fileName)
        if calculate_grade(119, 5, 639) == 15:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'calculate_grade' werkt correct."

@t.test(3)
def checks_tekst1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Grade 7")

    test.test = testMethod
    test.description = lambda : "Geeft de correcte grade bij een test tekst."


@t.test(4)
def checks_tekst2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "Grade 10")

    test.test = testMethod
    test.description = lambda : "Geeft de correcte grade bij een test tekst."
