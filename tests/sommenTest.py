import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_answer0(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["3 + 5"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "8.0")

    test.test = testMethod
    test.description = lambda : "3 + 5 is gelijk aan 8.0"

@t.test(1)
def checks_answer1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["19 - 6"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "13.0")

    test.test = testMethod
    test.description = lambda : "19 - 6 is gelijk aan 13.0"

@t.test(2)
def checks_answer2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["6 - 19"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "-13.0")

    test.test = testMethod
    test.description = lambda : "6 - 19 is gelijk aan -13.0"


@t.test(3)
def checks_answer3(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["12 * 23"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "276.0")

    test.test = testMethod
    test.description = lambda : "12 * 23 is gelijk aan 276.0"

@t.test(4)
def checks_answer4(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["6 / 4"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "1.5")

    test.test = testMethod
    test.description = lambda : "6 / 4 is gelijk aan 1.5"


@t.test(4)
def checks_answer4(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["-8 * 12"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "-96.0")

    test.test = testMethod
    test.description = lambda : "-8 * 12 is gelijk aan -96.0"
