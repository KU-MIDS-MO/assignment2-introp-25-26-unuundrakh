def swap_ends(L, k):
    if not isinstance(L, list) or k <= 0 or len(L) == 0 or k > len(L) // 2:
        return (L.copy(), 0)
    new_list = L.copy()
    new_list[:k], new_list[-k:] = L[-k:], L[:k]
    num_swaps = k
    return (new_list, num_swaps)
    
    
