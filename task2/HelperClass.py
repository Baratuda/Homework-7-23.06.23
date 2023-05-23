class HelperClass:
   def __init__(self):
       pass
   
   def print_operation_table(self, operation, num_rows=6, num_columns=6):
         for i in range(1,num_columns+1):
            print(end='\n')
            for j in range(1,num_rows+1):
               print(operation(i,j), end=' ')
    