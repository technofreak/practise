__author__ = 'Parthan'

"""Sum of a Triangle
Consider a list of lists in which the first list has one integer and each consecutive list has one more integer then the
last. Such a list of lists would look like a triangle. You must write a program that will help Nikola and Stephen look
for a route down the pyramid by stepping down and to the left or to the right. Your goal is to make sure this program
will find the sturdiest route, that is, the route with the highest possible sum on its way down the pyramid.

Tip: Think of each step down to the left as moving to the same index location or to the right as one index location
higher.
"""

def checkio(data):
    rows = len(data)
    sum_rows = [[0 for j in range(rows+1)] for i in range(rows)]

    for row in range(rows):
        if row == 0:
            # do nothing for the first row
            sum_rows[row][0] = data[row][0]
            continue
        for col in range(row+1):
            if col == 0:
                # for the first column just get the same col item from prev row and add to it
                sum_rows[row][col] = data[row][col] + sum_rows[row-1][col]
            elif row == col:
                # for the last item in a row, add the prev column (left) in the prev row
                sum_rows[row][col] = data[row][col] + sum_rows[row-1][col-1]
            else:
                # for anything else, add the max of previous column (left) and curr column (right) in previous row
                sum_rows[row][col] = data[row][col] + max(sum_rows[row-1][col-1], sum_rows[row-1][col])

    # when all rows are done, the last row contain the sums
    return max(sum_rows[-1])

if __name__ == "__main__":
    inp1 = [
    [1],
    [2, 3],
    [3, 3, 1],
    [3, 1, 5, 4],
    [3, 1, 3, 1, 3],
    [2, 2, 2, 2, 2, 2],
    [5, 6, 4, 5, 6, 4, 3]
    ]
    out1 = 23
    inp2 = [
    [1],
    [2, 1],
    [1, 2, 1],
    [1, 2, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1, 9]
    ]
    out2 = 15
    inp3 = [
    [9],
    [2, 2],
    [3, 3, 3],
    [4, 4, 4, 4]
    ]
    out3 = 18
    assert checkio(inp1) == out1, "First sample"
    assert checkio(inp2) == out2, "Second sample"
    assert checkio(inp3) == out3, "Third sample"