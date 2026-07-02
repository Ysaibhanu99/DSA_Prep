def circularArrayRotation(a, k, queries):
    n = len(a)
    result = []
    
    for q in queries:
        # Calculate the original index before rotation
        original_index = (q - k) % n
        result.append(a[original_index])
        
    return result
