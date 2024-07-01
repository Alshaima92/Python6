"""file = open ('ex1.txt' , 'w')
file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n ")
file.close()"""
    

x = list(range(1,10+1))
y = "\n".join(map(str, x))
print(y)



with open("ex1.txt", "w+")  as fh:
   for i in range (1, 11):
      fh.write(f"{i}\n")

