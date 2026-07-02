def libraryFine(d1, m1, y1, d2, m2, y2):
    # Case 1: Returned a year or more late
    if y1 > y2:
        return 10000
    # Case 2: Returned early in a completely different year
    elif y1 < y2:
        return 0
    
    # Case 3: Same year, but months late
    if m1 > m2:
        return (m1 - m2) * 500
    # Case 4: Same year, but returned in an earlier month
    elif m1 < m2:
        return 0
    
    # Case 5: Same year and month, but days late
    if d1 > d2:
        return (d1 - d2) * 15
    
    # Case 6: Completely on time or early
    return 0
