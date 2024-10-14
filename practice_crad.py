# practice for CRAD(Create read add and delete)
""" with open("newfile_python.txt", "w") as new_file:
    new_file.write("Hi everyone\nwe are learning File I/O\nusing Python.\nI like programming in Python and Javascript") """

""" text = ""
with open("newfile_python.txt", "r") as new_file:
    text = new_file.read()

text = text.replace("Python", "Javascript")

with open("newfile_python.txt", "w") as new_file:
    new_file.write(text) """


""" def search_word(search_for):
    with open("newfile_python.txt", "r") as new_file:
        txt = new_file.read()
        if search_for in text:
            print(search_for, "word exists")
        else:
            print(search_for, "word doesn't exists")

search_word(input("Enter the word you wanna search in newfile_python.txt: ")) """


""" def search_word_line(search_for):
    with open("newfile_python.txt", "r") as new_file:
        data = True
        line_no = 1
        while data:
            data = new_file.readline()
            if search_for in data:
                return search_for, "exist in line no", line_no
            else:
                print("loading")
            line_no += 1
        else:
            return "not found"
            
            
print(search_word_line(input("Enter the word you wanna search for getting the line no in newfile_python.txt: "))) """


""" count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(", ")
    for val in nums:
        if int(val) % 2 == 0:
            count += 1
print("even numbers exist", count, "times in the file") """
