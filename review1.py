def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    
    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive
            if total <= b:
                max_spent = max(max_spent, total)
    
    return max_spent  # it is for hacker13.py
