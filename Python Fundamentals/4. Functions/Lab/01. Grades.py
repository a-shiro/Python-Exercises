def grades(grade):
    if 2 <= grade < 3:
        return "Fail"
    elif 3 < grade < 3.5:
        return "Poor"
    elif 3.5 <= grade < 4.50:
        return "Good"
    elif 4.50 <= grade < 5.50:
        return "Very Good"
    elif 5.50 <= grade <= 6:
        return "Excellent"

num_input = float(input())

print(grades(num_input))