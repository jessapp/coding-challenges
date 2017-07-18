# Generate a collatz sequence given a starting integer N

def find_collatz_sequence(num):
    
    sequence = [num]
    
    while num != 1: 
        
        if num % 2 == 0:
            sequence.append(num // 2)
            num = num // 2
        
        elif num % 2 != 0:
            result = (3 * num) + 1
            sequence.append(result)
            num = result
        
    if num == 1:
        return sequence 


print find_collatz_sequence(13)