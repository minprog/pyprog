import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_convert0(test):
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("check") == "check":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'check' blijft onveranderd."

@t.test(1)
def checks_convert1(test):
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("checkInput") == "check_input":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'checkInput' wordt succesvol geconverteerd naar 'check_input'."

@t.test(2)
def checks_convert2(test):
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("checkInputFromUser") == "check_input_from_user":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'checkInputFromUser' wordt succesvol geconverteerd naar 'check_input_from_user'."
