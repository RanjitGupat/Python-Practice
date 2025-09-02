def main():
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

main()