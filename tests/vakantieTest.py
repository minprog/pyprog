import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

language = "en"

def expectedOutput(target, args):
    if language == "nl":
        return f"Print correct: 'Jouw vakantie kost: {target}' bij {str(args)} als invoer." 
    else:
        return f"Print correct: 'Your vacation costs: {target}' for {str(args)} as input."

@t.test(0)
def validFile(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[0, 0, 0, 0])
        if "vakantie" in output:
            global language
            language = "nl"
        elif not "vacation" in output:
            return False, "Output not recognized; please double check examples on the assignment page."
        return asserts.fileExists(test.fileName)

    test.test = testMethod
    test.description = lambda : (
        "Het bestand is in orde."
        if language == "nl" else
        "The file is valid."
    )

@t.test(1)
def calculatesZeroCosts(test):
    target = "0"
    args = [0, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(2)
def calculatesTravelCostsWithHint(test):
  def testMethod():
    travelCosts = lib.getFunction("travel_costs", test.fileName, stdinArgs=[1000, 0])(1000)
    if travelCosts == 130:
        return (False, 
                "Vergeet niet om de kosten voor zowel heen als terug te berekenen"
                if language == "nl" else
                "Don't forget to calculate costs for a round trip."
            )
    elif travelCosts == 260:
        return True
    else:
        return False

  test.test = testMethod
  test.description = lambda : (
    "De functie 'travel_costs' berekent correct de vervoerkosten."
    if language == "nl" else
    "The function 'travel_costs' calculates the costs of travel correctly."
  )

@t.test(2)
def calculatesTravelCosts(test):
    target = "260"
    args = [1000, 0]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(3)
def calculatesSleepingCosts(test):
    target = "600"
    args = [0, 10]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

@t.test(4)
def calculatesCosts(test):
    target = "589"
    args = [650, 7]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args)
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda: expectedOutput(target, args)

