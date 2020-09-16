def breakingRecords(scores):
    _min = _max = scores[0]
    max_count = min_count = 0
    for score in scores[1:]:
        if score > _max:
            _max = score
            max_count += 1
        elif score < _min:
            _min = score
            min_count += 1

    return (max_count,min_count)

# 5 20 20 4 5 2 25 1


    
