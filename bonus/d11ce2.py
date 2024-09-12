def get_max():
    grades = [9.6, 9.2, 9.7]
    min_grade = min(grades)
    max_grade = max(grades)
    minmax_local = f"Max: {max_grade}, Min: {min_grade}"
    return minmax_local

minmax = get_max()
print(minmax)