#Program for processing every word from pick.txt file
def write_file():
  f1=open("pick.txt","a")
  line="file handling"
  f1.write(line)
  f1.close()

def read_file():
  f1=open("pick.txt","rb+")
  print(f1.tell())
  print(f1.read(7)) # read seven characters
  print(f1.tell())
  print(f1.read())
  print(f1.tell())
  f1.seek(9,0) # moves to 9 position from begining
  print(f1.read(5))
  f1.seek(4,1) # moves to 4 position from current location
  print(f1.read(5))
  f1.seek(-5,2) # go to 5 byte before end of file
  print(f1.read(5))
  f1.close()



