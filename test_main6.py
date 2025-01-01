from main6 import square

def main():
    test_main6()

def test_main6():
    # if square(2) != 4:
    #     print ("2 squared was not 4")
    # if square(3) != 9:
    #     print ("3 squared was not 9")
    
    # Another way

    assert square(2) == 4
    assert square(3) == 9
if __name__ == "__main__":
    main()                 