import random

def prisoner_search(boxes,prisoner):
    i = prisoner
    nr_tries = len(boxes) // 2 
    for tries in range(nr_tries):
        box = i
        slip = boxes[box]
        if slip == prisoner:
            return True
        i = slip
    return False

def all_prisoners_search(boxes):
    for i in range(len(boxes)):
        if not prisoner_search(boxes,i):
            return False
    return True

def runs(n):
    nr_prisoners = 100
    success_count = 0
    boxes = [i for i in range(nr_prisoners)]
    for i in range(n):
        random.shuffle(boxes)
        success = all_prisoners_search(boxes)
        if success:
            success_count += 1
    print(success_count/n)

runs(1000)
