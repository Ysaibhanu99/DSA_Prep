def climbingLeaderboard(ranked, player):
    # Step 1: Get unique ranked scores in descending order
    unique_ranked = []
    for score in ranked:
        if not unique_ranked or unique_ranked[-1] != score:
            unique_ranked.append(score)
            
    result = []
    # Start pointer at the lowest score on the leaderboard
    l_idx = len(unique_ranked) - 1
    
    # Step 2 & 3: Iterate through player scores (ascending order)
    for p_score in player:
        # Move the pointer up the leaderboard while player score is better
        while l_idx >= 0 and p_score >= unique_ranked[l_idx]:
            l_idx -= 1
            
        # Step 4: Current rank is the pointer position + 1
        if l_idx < 0:
            result.append(1)  # Player is at the absolute top
        else:
            result.append(l_idx + 2) # +1 for 0-indexing, +1 because they sit right below l_idx
            
    return result
