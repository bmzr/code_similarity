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

# Creates a profile list from a FunctionDef based on similarity scoring attributes
# (todo: document how/what we determine similarity with)
def create_profile(function):
    # number of inputs
    input_count = 0
    for arg in function.args.args:
        input_count += 1
    # datatype of inputs
    
    # number of outputs
    #output_count = 0
    #for value in 
    # datatype of outputs
    # number of variable declarations
    # number of if statements
    # number of for loops
    # number of while loops
    # number of function calls

def compare_codes(list_1, list_2):
    for function_l1 in list_1:
        for function_l2 in list_2:
            if len(function_l2.args.args) == len(function_l1.args.args):
                print("function " + function_l1.name + "and function " + function_l2.name + "have the same function name.")
    
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

    compare_codes(function_list_1, function_list_2)
    print("End.")

if __name__ == "__main__":
    main()
