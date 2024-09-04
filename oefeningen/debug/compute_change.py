
def compute_denomination_amount(due, denomination: int) -> int:
    """
    Berekent hoeveel van de 'denomination' we betalen om het 'due' bedrag te betalen.
    >>> compute_denomination_amount(1, 10)
    0
    >>> compute_denomination_amount(24, 10)
    2
    """
    amount = round(due / denomination) # compute the amount of 'denomination' needed to pay 'due'
    amount = max(amount, 0)            # amount may not be negative
    return amount

def compute_change(due: int, denominations: list[int]) -> list[int]:
    """
    Berekent hoeveel van de verschillende 'denominations' we betalen om het 'due' bedrag te betalen.
    >>> compute_change(1, [50, 20, 10, 5, 2, 1])
    [0, 0, 0, 0, 0, 1]
    """
    change = [] # start with empty change list
    for denomination in denominations:
        amount = compute_denomination_amount(due, denomination) # compute the amount of 'denomination'
        change.append(amount)                                   # add amount to the change list
        due -= amount                                           # update the 'due' value
    return change

def print_change(change: list[int], denominations: list[int]) -> None:
    """
    Print elke denomination in 'change'
    """
    print(f"{'Denomination':>15}: {'Amount':>8}")
    for i in range(len(denominations)):
        amount = change[i]
        if amount > 0:
            print(f"{denominations[i]:15}: {amount:8}")

if __name__ == '__main__':
    denominations = [50, 20, 10, 5, 2, 1]
    due = int(input("Welk bedrag moet je betalen? "))
    change = compute_change(due, denominations)
    print_change(change, denominations)
