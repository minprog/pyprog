import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def calculatesZeroCafeine(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[0, 0, 0, 0])
        return asserts.exact(output.strip(), "Je krijgt 0 mg cafeine binnen.")

    test.test = testMethod
    test.description = lambda : "Print correct: 'Je krijgt 0 mg cafeine binnen.' bij 0, 0, 0, 0 als invoer."

@t.test(1)
def calculatesSomeCafeine(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[1, 2, 3, 4])
        return asserts.exact(output.strip(), "Je krijgt 580 mg cafeine binnen.")

    test.test = testMethod
    test.description = lambda : "Print correct: 'Je krijgt 580 mg cafeine binnen.' bij 1, 2, 3, 4 als invoer."
