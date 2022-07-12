import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts


@t.test(0)
def checks_set_board(test):
    def testMethod():
        set_board = lib.getFunction("set_board", test.fileName)
        if (set_board(4) == [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]] and
            set_board(3) == [[8, 7, 6], [5, 4, 3], [2, 1, 0]]):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'set_board' werkt correct."

@t.test(1)
def checks_is_won(test):
    def testMethod():
        is_won = lib.getFunction("is_won", test.fileName)
        if (is_won([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) and not
            is_won([[1, 2, 3], [4, 5, 6], [8, 7, 0]]) and
            is_won([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'is_won' werkt correct."


@t.test(2)
def checks_move_tile(test):
    def testMethod():
        move_tile = lib.getFunction("move_tile", test.fileName)
        if (move_tile([[8, 7, 6], [5, 4, 3], [2, 1, 0]], 3) == ([[8, 7, 6], [5, 4, 0], [2, 1, 3]], True)
            and move_tile([[8, 7, 6], [5, 4, 3], [2, 1, 0]], 7) == ([[8, 7, 6], [5, 4, 3], [2, 1, 0]], False)):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "De functie 'move_tile' werkt correct."
