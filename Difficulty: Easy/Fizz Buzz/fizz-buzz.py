class Solution:
    def fizzBuzz(self, n : int):
        output = []
        
        for i in range (1, n+1):
            if i % 3 == 0 and i %5 == 0:
                output.append("FizzBuzz")
            
            elif i % 3 == 0:
                output.append("Fizz")
                
            elif i % 5 == 0:
                output.append("Buzz")
                
            else:
                output.append(int(i))
                
        return output        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # code here
        # output = []
        # for i in range(1, n+1):
        #     if i % 3 and 5 != 0:
        #         output += str(i)
        #     # elif i % 5 != 0:
        #     #     output += str(i)
                
     
        #     if i % 3 == 0:
        #         output.append("Fizz")
        #     elif i % 5 == 0:
        #         output.append("Buzz")
             
        # return output
