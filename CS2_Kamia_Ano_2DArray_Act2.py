https://www.programiz.com/online-compiler/5fA8KVuRKyKkq
# 2D array of quiz scores (rows = students, columns = subjects)
quiz_scores = [
    [85, 90, 78],   # Student 1: Math, Science, English
    [88, 80, 92],   # Student 2
    [90, 85, 85],   # Student 3
    [70, 80, 75]    # Student 4
]

print("Quiz Scores per Student:")
for i, row in enumerate(quiz_scores):
    print(f"Student {i+1}: {row}")

print("\nTotals and Averages:")
for i, row in enumerate(quiz_scores):
    total = sum(row)
    average = total / len(row)
    print(f"Student {i+1} - Total: {total}, Average: {average:.2f}")

max_score = max(max(row) for row in quiz_scores)
print(f"\nHighest score in dataset: {max_score}")
