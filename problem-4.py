# read the file into string
def read_input_file(filename):
    file = open(filename)
    content = file.readlines()
    parsed_content = ""
    for line in content:
        # since we are dealing with only single digits
        # we can remove spaces in the middle of the numbers
        # to ease iteration in future
        parsed_content += ''.join(line.split())
    return parsed_content


# convert string into matrix to represent input of the puzzle
def generate_matrix(string):
    matrix = [[0 for x in range(9)] for x in range(9)]
    for i in range(9):
        for j in range(9):
            matrix[i][j] = string[i * 9 + j]
    return matrix


def create_cnf_file(puzzle, index):
    output_file = open('sudoku' + str(index) + '.cnf', 'w')
    output_file.write("p cnf 999 999999" + "\n")
    generate_clauses_for_filled_cells(output_file, puzzle)
    generate_clauses_for_each_cell(output_file)
    generate_clauses_for_each_column(output_file)
    generate_clauses_for_each_row(output_file)
    generate_clauses_for_sub_matrix(output_file)
    output_file.close()


def generate_clauses_for_filled_cells(output_file, puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != '0':
                output_file.write(str(code(i + 1, j + 1, int(puzzle[i][j]))) + ' 0\n')


def generate_clauses_for_each_cell(output_file):
    for i in range(1, 10):
        for j in range(1, 10):
            for d in range(1, 10):
                output_file.write(str(code(i, j, d)) + ' ')
            output_file.write(' 0\n')


def generate_clauses_for_each_column(output_file):
    for i in range(1, 10):
        for d in range(1, 10):
            for j in range(1, 9):
                for index in range(j + 1, 10):
                    output_file.write("-" + str(code(i, j, d)) + " -" + str(code(i, index, d)) + " 0\n")


def generate_clauses_for_each_row(output_file):
    for j in range(1, 10):
        for d in range(1, 10):
            for i in range(1, 9):
                for index in range(i + 1, 10):
                    output_file.write("-" + str(code(i, j, d)) + " -" + str(code(index, j, d)) + " 0\n")


def generate_clauses_for_sub_matrix(output_file):
    for d in range(1, 10):
        for x_axis in range(0, 3):
            for y_axis in range(0, 3):
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(j + 1, 4):
                            index_1 = x_axis * 3 + i
                            index_2 = y_axis * 3 + j
                            index_3 = y_axis * 3 + k
                            output_file.write('-' + str(code(index_1, index_2, d)) + ' -' + str(code(index_1, index_3, d)) + ' 0\n')

                        for k in range(i + 1, 4):
                            for l in range(1, 4):
                                index_1 = x_axis * 3 + i
                                index_2 = y_axis * 3 + j
                                index_3 = x_axis * 3 + k
                                index_4 = y_axis * 3 + l
                                output_file.write('-' + str(code(index_1, index_2, d)) + ' -' + str(code(index_3, index_4, d)) + ' 0\n')


def code(i, j, d):
    return 100*i+10*j+d


if __name__ == "__main__":
    input_filenames = ["sudoku1.txt", "sudoku2.txt", "sudoku3.txt", "sudoku4.txt", "sudoku5.txt"]
    index = 1
    for input_file in input_filenames:
        string_content = read_input_file(input_file)
        input_matrix = generate_matrix(string_content)
        create_cnf_file(input_matrix, index)
        index += 1
