def create_cnf_file(n):
    total_clauses = 0
    total_literals = 100 * n + 10*n + n + 1
    output_file = open('lsquare' + str(n) + '.cnf', 'w')
    total_clauses += generate_clauses_for_each_cell(output_file, n)
    total_clauses += generate_clauses_for_each_column(output_file, n)
    total_clauses += generate_clauses_for_each_row(output_file, n)
    total_clauses += generate_clauses_for_first_cond(output_file, n)
    total_clauses += generate_clauses_for_second_cond(output_file, n)
    output_file.close()

    output_file = open('lsquare' + str(n) + '.cnf', 'r')
    temp = output_file.read()
    output_file.close()
    output_file = open('lsquare' + str(n) + '.cnf', 'w')
    output_file.write("p cnf " + str(total_literals) + " " + str(total_clauses) + "\n")

    output_file.write(temp)
    output_file.close()


def generate_clauses_for_each_cell(output_file, order):
    clauses = 0
    for i in range(1, order+1):
        for j in range(1, order+1):
            for d in range(1, order+1):
                output_file.write(str(code(i, j, d)) + ' ')
            output_file.write(' 0\n')
            clauses += 1
    return clauses


def generate_clauses_for_each_column(output_file, order):
    clauses = 0
    for i in range(1, order+1):
        for d in range(1, order+1):
            for j in range(1, order):
                for index in range(j + 1, order+1):
                    output_file.write("-" + str(code(i, j, d)) + " -" + str(code(i, index, d)) + " 0\n")
                    clauses += 1
    return clauses


def generate_clauses_for_each_row(output_file, order):
    clauses = 0
    for j in range(1, order+1):
        for d in range(1, order+1):
            for i in range(1, order):
                for index in range(i + 1, order+1):
                    output_file.write("-" + str(code(i, j, d)) + " -" + str(code(index, j, d)) + " 0\n")
                    clauses += 1
    return clauses

def generate_clauses_for_first_cond(output_file, order):
    clauses = 0
    for i in range(1, order+1):
        output_file.write(str(code(i, i, i)) + ' 0\n')
        clauses += 1
    return clauses


def generate_clauses_for_second_cond(output_file, order):
    clauses = 0
    for x in range(1, order+1):
        for y in range(1, order+1):
            for z in range(1, order+1):
                for w in range(1, order+1):
                    output_file.write("-" + str(code(x, y, z)) + " -" + str(code(y, x, w)) + " " + str(code(z, w, x)) + " 0\n")
                    clauses += 1
    return clauses

def code(i, j, d):
    return 100*i+10*j+d+1


if __name__ == "__main__":
    for n in range(4, 10):
        create_cnf_file(n)
