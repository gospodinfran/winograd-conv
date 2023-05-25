from main import calc_convolution
from tests import tests

for test in tests:
    input_matrix, kernel = test
    result = calc_convolution(input_matrix, kernel)
    print(result)
