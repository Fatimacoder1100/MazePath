def count_paths(sr, sc, dr, dc):

    if sr == dr and sc == dc:
        return 1
    
    count = 0

    if sr < dr:
        count += count_paths(sr + 1, sc, dr, dc)
    if sc < dc:
        count += count_paths(sr, sc + 1, dr, dc)

    return count

print(count_paths(0,0,2,2))