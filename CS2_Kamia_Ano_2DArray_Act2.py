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
#Using a 2D array made it much easier to organize the quiz scores because each student’s data was grouped together in rows. This structure allowed me to quickly calculate totals and averages using simple loops, instead of handling each score individually. The easiest part was printing and summing the rows, while finding the maximum required a bit more thought since I had to check across all rows. Overall, arrays helped simplify the process of analyzing patterns in the dataset.
