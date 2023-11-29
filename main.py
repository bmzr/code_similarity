import ast

def make_functiondef_list(code_ast):
    functiondef_list = []
    for object in code_ast.body:
        if isinstance(object, ast.FunctionDef):
            functiondef_list.append(object)
    return functiondef_list

def main():
    # code_file_1 = open(input("Enter a code file name (code file 1): "), 'r')
    # code_file_2 = open(input("Enter a code file name (code file 2): "), 'r')

    code_file_1 = open("file1.py", 'r')
    code_file_2 = open("file2.py", 'r')

    code_lines_1 = code_file_1.readlines()
    code_lines_2 = code_file_2.readlines()

    print("\n------------------CODE FILE 1------------------")
    code_segment_1 = ''
    for line in code_lines_1:
        code_segment_1 += line
    ast_1 = ast.parse(code_segment_1)
    print(ast.dump(ast_1, indent = 4))
    print("\n------------------CODE FILE 2------------------")
    code_segment_2 = ''
    for line in code_lines_2:
        code_segment_2 += line
    ast_2 = ast.parse(code_segment_2)
    print(ast.dump(ast_2, indent = 4))

    function_list_1 = make_functiondef_list(ast_1)
    function_list_2 = make_functiondef_list(ast_2)
    print("End.")
    
if __name__ == "__main__":
    main()
