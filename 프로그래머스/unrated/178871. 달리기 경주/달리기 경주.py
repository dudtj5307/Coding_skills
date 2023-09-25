def solution(players, callings):

    rank_dict = {rank:play for rank, play in enumerate(players)}
    play_dict = {play:rank for rank, play in enumerate(players)}
    
    for call in callings:
        idx = play_dict[call]
        
        play_dict[rank_dict[idx-1]], play_dict[rank_dict[idx]] = play_dict[rank_dict[idx]], play_dict[rank_dict[idx-1]]
        rank_dict[idx], rank_dict[idx-1] = rank_dict[idx-1], rank_dict[idx]
    
    return list(rank_dict.values())