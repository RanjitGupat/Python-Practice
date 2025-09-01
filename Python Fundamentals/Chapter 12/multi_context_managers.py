with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    # You can now work with f1 and f2
    data1 = f1.read()
    data2 = f2.read()
    print(data1, data2)
