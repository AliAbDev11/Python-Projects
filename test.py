def transpose(lst):
    # Initialize an empty list for the transposed matrix
    transposed = []
    
    # Iterate over the range of the number of columns in the original list
    for col in range(len(lst[0])):
        # Create a new row for the transposed list
        new_row = []
        # Iterate over each row in the original list
        for row in lst:
            # Append the element at the current column to the new row
            new_row.append(row[col])
        # Append the new row to the transposed list
        transposed.append(new_row)
    
    return transposed

# Example usage:
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose(lst)
print(transposed)