def climbingLeaderboard(ranked, player):
    ranked.sort(reverse = True)
    ranks = []
    for score in player:
        I = len(ranked) + 2
        for index in range(len(ranked)):
            if ranked[index] >= score:
                I = index + 1
        ranks.append(I)


                

