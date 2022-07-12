import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def calculatesZeroCosts(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[0, 0])
        return asserts.exact(output.strip(), "Jouw vakantie kost: 0")

    test.test = testMethod
    test.description = lambda : "Print correct: 'Jouw vakantie kost: 0' bij 0, 0 als invoer."

@t.test(1)
def calculatesTravelCosts(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[1000, 0])
        return asserts.exact(output.strip(), "Jouw vakantie kost: 260")

    test.test = testMethod
    test.description = lambda : "Print correct: 'Jouw vakantie kost: 260' bij 1000, 0 als invoer."

@t.test(2)
def calculatesSleepingCosts(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[0, 10])
        return asserts.exact(output.strip(), "Jouw vakantie kost: 600")

    test.test = testMethod
    test.description = lambda : "Print correct: 'Jouw vakantie kost: 60' bij 0, 10 als invoer."

@t.test(3)
def calculatesCosts(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[650, 7])
        return asserts.exact(output.strip(), "Jouw vakantie kost: 589")

    test.test = testMethod
    test.description = lambda : "Print correct: 'Jouw vakantie kost: 589' bij 650, 7 als invoer."

@t.test(4)
def calculatesTravelCostsWithHint(test):
  def testMethod():
    travelCosts = lib.getFunction("travel_costs", test.fileName, stdinArgs=[1000, 0])
    if travelCosts == 130:
        return False, f"Heb je erover nagedacht dat je ook terug moet rijden?"
    elif travelCosts == 260:
        return True
    else:
        return False

  test.test = testMethod
  test.description = lambda : "De funcite 'travel_costs' berekent correct de vervoerkosten."
