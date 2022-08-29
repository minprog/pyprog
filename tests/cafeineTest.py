import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

language = "en"

def expectedOutput(target, args):
    if language == "nl":
        return f"Print correct: 'Je krijgt {target} cafeine binnen.' bij {str(args)} als invoer." 
    else:
        return f"Print correct: 'Your intake is {target} of caffeine.' for {str(args)} as input."

@t.test(0)
def validFile(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[0, 0, 0, 0])
        if "krijgt" in output:
            global language
            language = "nl"
        elif not "intake" in output:
            return False, "Output not recognized; please double check examples on the assignment page."
        return asserts.fileExists(test.fileName)

    test.test = testMethod
    test.description = lambda : (
        "Het bestand is in orde."
        if language == "nl" else
        "The file is valid."
    )

@t.test(1)
def calculatesZeroCafeine(test):
    target = "0 mg"
    args = [0, 0, 0, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(2)
def calculatesCoffee(test):
    target = "90 mg"
    args = [1, 0, 0, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(2)
def calculatesTea(test):
    target = "45 mg"
    args = [0, 1, 0, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(2)
def calculatesEnergy(test):
    target = "80 mg"
    args = [0, 0, 1, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(2)
def calculatesCola(test):
    target = "40 mg"
    args = [0, 0, 0, 1]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(3)
def calculatesSomeCafeine(test):
    target = "580 mg"
    args = [1, 2, 3, 4]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)
