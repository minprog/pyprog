class Greeting:

    def __init__(self):
        print("Hello")

    def __del__(self):
        print("Goodbey")

def main():
    greetings = []
    print("Creatings two Greeting objects:")
    greetings.append( Greeting() )
    greetings.append( Greeting() )
    print("List with two Greeting objects goes out of scope and get deleted:")
    
main()
