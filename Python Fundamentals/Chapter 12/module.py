def myFunc():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return(a)

    except ValueError as v:
        print(v)
        return(v)

    except Exception as e:
        print(e)
        return(e)

    finally:
        print("I am inside else")       # Executed regardless of error!

if __name__ == "__main__":
    # if this code is directly executed by running the file its present in

    print("we are directly running this code")
    myFunc()
    print(__name__)