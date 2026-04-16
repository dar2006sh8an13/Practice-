def count_even_odd(arr):
    even = 0
    odd = 0
    
    for num in arr:
        if num % 2 == 0:
            even += 1  # Count even
        else:
            odd += 1   # Count odd
            
    return even, odd
