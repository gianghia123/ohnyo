chapter1 = open("chapter2.html", "a")
test = open("chap2.txt", "r")

harry = test.read().split('\n')
result = ""
for i in harry:
    if i != "":
        result += '<p class="content">' + i + "</p>" + '\n'

chapter1.write(result)
print("Done!")

chapter1.close()
test.close()