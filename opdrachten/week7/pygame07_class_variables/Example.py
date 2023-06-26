class Example:
    b = 100                 # class variable

    def __init__(self):
        a = 200             # local variable
        self.c = 300        # instance variable

    def __str__(self):
        return f"b:{Example.b} c:{self.c}" # 'Example.b' and 'self.c' are available in each method

def main():
    print("Example.b:", Example.b) # 'Example.b' is already available after the class is defined 
    e1 = Example()                 # create an object of type Example
    print("e1.c:", e1.c)           # 'e.c' is only available after an object is created 
                                   
    e2 = Example()                 # create another object of type Example
    e2.c = 3333                    # change 'e2.c'
    Example.b = 1111               # change 'Example.b'
    print("e1", e1)                # each object has its own 'c' but shares 'b'
    print("e2", e2)
    # as 'e1' and 'e2' go "out of scope" here, they together with their 'c' get deleted

if __name__ == "__main__":
    main()
    print("Example.b:", Example.b) # 'Example.b' is still available
