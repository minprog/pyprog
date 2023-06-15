import bands
import io

# de bands:
the_rockets     = ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
the_dragonflies = ['The Dragonflies:', 'Lisa', 'Alexander', 'Lucas']
# het agenda:
agenda = { 'januari':[], 'februari':[]  } # lege agenda met 'januari' en 'februari'

answers=[]
answers.append(
"""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'Lisa', 'Alexander', 'Lucas']
maand: februari
""")
answers.append("""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'Lisa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week4 ['The Dragonflies:', 'Lisa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
maand: februari""")
answers.append("""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
maand: februari""")
answers.append("""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
maand: februari""")
answers.append("""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
maand: februari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']""")
answers.append("""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
maand: februari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']""")
answers.append("""==== AGENDA ====
maand: januari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
maand: februari
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas']
maand: maart
  week1 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Maya']
  week2 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas', 'Maya']
  week3 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Thomas', 'Maya']
  week4 ['The Dragonflies:', 'LiZa', 'Alexander', 'Lucas', 'Maya']
  week5 ['The Rockets:', 'Jim', 'Charlotte', 'Emma', 'Maya']""")

def print_agenda(agenda, strbuf) -> None:
    print("==== AGENDA ====",file=strbuf)
    for month, bands in agenda.items():
        print("maand:", month, file=strbuf)
        for index, band in enumerate(bands):
            print(f"  week{index+1} {band}", file=strbuf)

def is_equal(opdracht, strbuf1, strbuf2) -> bool:
    print(f"{opdracht}:",end='')
    strbuf1.seek(0)
    strbuf2.seek(0)
    lines1 = list(strbuf1)
    lines2 = list(strbuf2)
    if len(lines1) != len(lines2):
        strbuf1.seek(0)
        strbuf2.seek(0)
        print()
        print("ERROR, wrong number of lines")
        print("-------- your result:")
        print('"',strbuf1.getvalue(),'"',sep='')
        print("-------- should be:")
        print('"',strbuf2.getvalue(),'"',sep='')
        return False
    for i in range(len(lines1)):
        l1 = lines1[i].strip()
        l2 = lines2[i].strip()
        if l1 != l2:
            print()
            print(f'ERROR  your line: "{l1}"')
            print(f'       should be: "{l2}"')
            return False
    print(" correct")
    return True
        
def test_opdracht(opdracht, fun, answer) -> bool:
    strbuf_correct = io.StringIO()
    strbuf_correct.write(answer)
    strbuf = io.StringIO()
    fun(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda, strbuf)
    return is_equal(opdracht, strbuf, strbuf_correct)

if __name__ == "__main__":
    functions = [bands.opdracht1,
                 bands.opdracht2,
                 bands.opdracht3,
                 bands.opdracht4,
                 bands.opdracht5,
                 bands.opdracht6,
                 bands.opdracht7]
    for i in range(len(functions)):
        if not test_opdracht(f"opdracht{i+1}", functions[i], answers[i]):
            exit(1)
