import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_xaxis(test):
    def testMethod():
        check_xaxis = lib.getFunction("check_xaxis", test.fileName)
        xaxis_overlap = check_xaxis(1,2, 4,4, 2,3, 5,8)
        xaxis_no_overlap = check_xaxis(1,2, 4,4, 4,4, 5,8)
        if xaxis_overlap and not xaxis_no_overlap:
            return True
        else:
            if not xaxis_overlap:
                return False, f"De functie 'check_xaxis' heeft False als output terwijl er een overlap is."
            else:
                return False, f"De functie 'check_xaxis' heeft True als output terwijl er geen overlap is."

    test.test = testMethod
    test.description = lambda : "De functie 'check_xaxis' werkt correct."


@t.test(1)
def checks_yaxis(test):
    def testMethod():
        check_yaxis = lib.getFunction("check_yaxis", test.fileName)
        yaxis_overlap = check_yaxis(1,2, 4,4, 2,3, 5,8)
        yaxis_no_overlap = check_yaxis(1,2, 4,4, 4,4, 5,8)
        if yaxis_overlap and not yaxis_no_overlap:
            return True
        else:
            if not yaxis_overlap:
                return False, f"De functie 'check_yaxis' heeft False als output terwijl er een overlap is."
            else:
                return False, f"De functie 'check_yaxis' heeft True als output terwijl er geen overlap is."

    test.test = testMethod
    test.description = lambda : "De functie 'check_yaxis' werkt correct."


@t.test(2)
def checks_overlap(test):
    def testMethod():
        overlap_check = lib.getFunction("check_overlap", test.fileName)
        overlap = overlap_check(True, True)
        no_overlap = overlap_check(True, False)
        if overlap and not no_overlap:
            return True
        else:
            if not overlap:
                return False, f"De functie 'check_overlap' heeft False als output terwijl er een overlap is."
            else:
                return False, f"De functie 'check_overlap' heeft True als output terwijl er geen overlap is."

    test.test = testMethod
    test.description = lambda : "De functie 'check_overlap' werkt correct."
