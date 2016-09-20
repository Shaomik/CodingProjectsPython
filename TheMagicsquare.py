

#  Description: Program checks if a 2-d matrix is a valid magic square.

#  Name: Shaomik Sarkar

#  Date Created:4/13/2015

#  Date Last Modified:4/13/2015

##########################################################################
# The Magic Function
##########################################################################
def isMagic(a):
  side = len(a)
  magic_sum=int((side*((side*side)+1))/2)
  #print (f)
  c_row = 0
  c_col = 0
  c_lr = 0
  c_rl = 0
 # sum of each row
  for i in range (len(a)):
    sum_row = 0
    for j in range (len(a[i])):
      sum_row = sum_row + a[i][j]
    #print (sum_row)
    if sum_row == magic_sum:
        c_row += 1
        
    #print (sum_row)

  # sum of each column
  for j in range (len(a[0])):
    sum_col = 0
    for i in range (len(a)):
      sum_col += a[i][j]
    if sum_col == magic_sum:
        c_col += 1
    #print (sum_col)
    #print (c_col)
  # sum diagonal left to right
  sum_lr = 0
  for i in range (len(a)):
    sum_lr += a[i][i]
  if sum_lr == magic_sum:
        c_lr += 1
  #print (sum_lr)
  # sum diagonal right to left
  sum_rl = 0
  for i in range (len(a)):
    sum_rl += a[i][len(a) - 1 - i]
  if sum_rl == magic_sum:
        c_rl += 1
  #print (sum_rl)
  # print(c_row)
  #print(c_col)
  #print(c_lr)
  #print(c_rl)
  #check to see if the rows,columns and diagonals sums are good
  if c_row == side and c_col == side and c_lr == 1 and c_rl == 1:
    return (True)
  else:
    return(False)
##################################################################################
# The Main Function
################################################################################
def main():
  # open files for reading and writing
  in_file = open ("squares.txt", "r")
  out_file = open("results.txt", "w")
  
  # read number of squares
  line = in_file.readline()
  line = line.strip()
  num_squares = int (line)
  out_file.write(line+"\n")
  out_file.write("\n")
  
  # read a blank line
  line = in_file.readline()

  # read and process the number of squares
  for i in range (num_squares):
    line = in_file.readline()
    line = line.strip()
    dimensions = int (line)
    # create 2-D list that is the square
    matrix = []

    # read data to populate the 2-D list
    for j in range (dimensions):
      line = in_file.readline()
      line = line.strip()
      row = line.split()
      # convert the strings to integers
      for k in range (dimensions):
        row[k] = int (row[k])
      # add row to the square
      matrix.append (row)
    #check if the square is magic and write results to out file
    if isMagic(matrix):
     out_file.write(str(dimensions) + " " +"valid"+"\n")
     for l in range(len(matrix)):
      mat_line = str(matrix[l])
      mat_line = mat_line[1:-1]
      mat_line = mat_line.replace(",","")
      out_file.write(mat_line+"\n")
    else:
     out_file.write(str(dimensions) + " " +"invalid"+"\n")
     for m in range(len(matrix)):
      mat_line = str(matrix[m])
      mat_line = mat_line[1:-1]
      mat_line = mat_line.replace(",","")
      out_file.write(mat_line+"\n")
    # read blank line
    out_file.write("\n")
    line = in_file.readline()

  # close files
  in_file.close()
  out_file.close()
  print("The output has been written to results.txt")
################################################################################

main()
################################################################################
#                                  END
################################################################################
