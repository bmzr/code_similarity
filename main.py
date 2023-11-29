import ast

# Given an AST, create a list of FunctionDef nodes.
def make_functiondef_list(code_ast):
    functiondef_list = []
    for object in code_ast.body:
        if isinstance(object, ast.FunctionDef):
            functiondef_list.append(object)
    return functiondef_list

# Given a code file pointer, create an AST structure.
# Pass True to print_ast to print out the AST structure to console.
def code_to_ast(code_file, print_ast = False):
    code_lines = code_file.readlines()
    code_segment = ''
    for line in code_lines:
        code_segment += line
    code_ast = ast.parse(code_segment)
    if print_ast:
        print(ast.dump(code_ast, indent = 4))
    return code_ast

def main():
    # code_file_1 = open(input("Enter a code file name (code file 1): "), 'r')
    # code_file_2 = open(input("Enter a code file name (code file 2): "), 'r')

    code_file_1 = open("file1.py", 'r')
    code_file_2 = open("file2.py", 'r')

    print("\n------------------CODE FILE 1------------------")
    ast_1 = code_to_ast(code_file_1, print_ast=True)
    print("\n------------------CODE FILE 2------------------")
    ast_2 = code_to_ast(code_file_2, print_ast=True)

    function_list_1 = make_functiondef_list(ast_1)
    function_list_2 = make_functiondef_list(ast_2)
    print("End.")

if __name__ == "__main__":
    main()
