import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts


@t.test(0)
def checks_input(test):
    def testMethod():
        input_dna = lib.getFunction("check_input", test.fileName)
        if (input_dna("ATGC") and input_dna("agtc") and input_dna("AaGgCcTt")
            and not input_dna("AUGA") and not input_dna("123")):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_input' werkt correct."


@t.test(1)
def checks_convert_dna(test):
    def testMethod():
        convert = lib.getFunction("convert_dna", test.fileName)
        if (convert(["A", "T", "G", "C"]) == ["U", "A", "C", "G"]
            and convert(["a", "A", "t", "g", "c"]) == ["U", "U", "A", "C", "G"]):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'convert_dna' werkt correct."


@t.test(2)
def checks_convert_list(test):
    def testMethod():
        convert = lib.getFunction("convert_to_list", test.fileName)
        if convert("ATGCAGA") == ["A", "T", "G", "C", "A", "G", "A"]:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'convert_to_list' werkt correct."


@t.test(3)
def checks_convert_string(test):
    def testMethod():
        convert = lib.getFunction("convert_to_string", test.fileName)
        if convert(["A", "T", "G", "C", "T", "T", "G"]) == "ATGCTTG":
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'convert_to_string' werkt correct."
