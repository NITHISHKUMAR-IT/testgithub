rows = 5
for i in range( 0 , rows + 1 ):
  for j in range(
      rows-i,0,-1):
        print(j , end =' ')
  print()
  
  word = "python"
  x = " "
  for i in word:
    x += i + " "
    print(x)