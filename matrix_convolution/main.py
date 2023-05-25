def calc_convolution(input_matrix, kernel):
    input_rows = len(input_matrix)
    input_cols = len(input_matrix[0])
    kernel_rows = len(kernel)
    kernel_cols = len(kernel[0])

    output_rows = input_rows - kernel_rows + 1
    output_cols = input_cols - kernel_cols + 1
    output = [[0] * output_cols for _ in range(output_rows)]

    for i in range(output_rows):
        for j in range(output_cols):
            for k in range(kernel_rows):
                for l in range(kernel_cols):
                    output[i][j] += input_matrix[i + k][j + l] * kernel[k][l]


    return output
