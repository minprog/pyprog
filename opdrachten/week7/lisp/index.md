# LISP

De programmeertaal LISP staat bekend om de vele haakjes die nodig zijn om een programma te schrijven.

    (defun factorial (n)
        (loop for i from 1 to n
            for fac = 1 then (* fac i)
            finally (return fac)))

De haakjes maken het wel mogelijk om een programma op één regel te zetten, waarna de computer het nog steeds begrijpt. Bovenstaand programma op één regel:

    (defun factorial (n) (loop for i from 1 to n for fac = 1 then (* fac i) fi...

Deze haakjes hebben dus wel een doel, maar toch is het makkelijk om fouten te maken. Jouw taak is een check te schrijven of een LISP-programma geldig is. De vraag is daarbij of het aantal haakjes klopt: voor elk haakje openen moet er ook een haakje sluiten zijn, en andersom!

## Validator class

We vragen je hier specifiek om een validator in een class te bouwen. Deze class genaamd `LispValidator` heeft een constructor met één parameter: de inhoud van het programma (een string). Daarnaast is er een methode genaamd `is_valid()` die True of False teruggeeft.

    >>> LispValidator("(defun factorial (())(] (loop))))").is_valid()
    False

    >>> LispValidator("(write (factorial 3))").is_valid()
    True

    >>> LispValidator("(defun gretting ((write-line \"let it snow\"))").is_valid()
    False

## Algoritme

Voor het checken van de geldigheid kun je door de string heen gaan en bijhouden hoeveel haakjes openen je bent tegengekomen. Vind je er één, dan tel je die bij de statistieken. Vind je een haakje sluiten, dan trek je die er vanaf. Het programma is alleen geldig als je op 0 eindigt.

## Doctests

Hierboven vind je al doctests. Deze testen het complete gebruik van de class, dus je zou ze in een docstring voor de `class` kunnen zetten, of in een docstring voor de `is_valid` methode. De doctests hierboven zijn niet de enige mogelijke tests.

## Main

Heeft dit programma een `if __name__ == '__main__'` nodig? Nee, dat is niet zo! Het mag wel, maar de class werkt ook zo en zou via een `import` in een ander programma gebruikt kunnen worden.
