

with open ('ex2', 'a') as file2:
  while True:
   x= input ("Please Enter anything you need to the file: ")
   
   if x.lower() == "stop":
      break
   file2.write(x+ "\n")
  