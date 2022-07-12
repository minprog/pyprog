import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def checks_check_leap_year(test):
    def testMethod():
        fn = lib.getFunction("check_leap_year", test.fileName)
        if fn(2000) and fn(2020) and not fn(2100):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'check_leap_year' werkt correct."


@t.test(1)
def checks_days_from_1800(test):
    def testMethod():
        fn = lib.getFunction("days_from_1800", test.fileName)
        if fn(5, 2022) == 81204 and fn(8, 1996) == 71800:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'days_from_1800' werkt correct."


@t.test(2)
def checks_days_from_1800_till_year(test):
    def testMethod():
        fn = lib.getFunction("days_from_1800_till_year", test.fileName)
        if fn(2022) == 81084 and fn(1996) == 71587:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'days_from_1800_till_year' werkt correct."


@t.test(3)
def checks_days_in_month(test):
    def testMethod():
        fn = lib.getFunction("days_in_month", test.fileName)
        if fn(5, 2022) == 31 and fn(2, 2022) == 28 and fn(2, 2020) == 29:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'days_in_month' werkt correct."


@t.test(4)
def checks_days_till_month(test):
    def testMethod():
        fn = lib.getFunction("days_till_month", test.fileName)
        if fn(1, True) == 0 and fn(5, True) == 121 and fn(5, False) == 120:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'days_till_month' werkt correct."


@t.test(5)
def checks_first_day_month(test):
    def testMethod():
        fn = lib.getFunction("first_day_month", test.fileName)
        if fn(5, 2022) == 0 and fn(12, 2020) == 2:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'first_day_month' werkt correct."
