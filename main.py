import ast

def main():
    code_file_1 = open(input("Enter a code file name (code file 1): "), 'r')
    code_file_2 = open(input("Enter a code file name (code file 2): "), 'r')

    code_lines_1 = code_file_1.readlines()
    code_lines_2 = code_file_2.readlines()

    # code_ast_1 = ast.parse(code_lines_1)
    # print(ast.dump(code_ast_1))

    print("\n------------------CODE FILE 1------------------")
    for line in code_lines_1:
        print(line, end = '')
    print("\n------------------CODE FILE 2------------------")
    for line in code_lines_2:
        print(line, end = '')

if __name__ == "__main__":
    main()
