import ast

class functiondef_visitor(ast.NodeVisitor):
    def __init__(self):
        self.function_profiles = []
    
    # get information for each function defined in the AST
    def visit_FunctionDef(self, node):
        parameter_count = len(node.args.args)
        var_declaration_count = 0
        if_count = 0
        for_loop_count = 0
        while_loop_count = 0
        function_call_count = 0
        bin_op_count = 0

        for stmt in node.body:
            if isinstance(stmt, ast.Assign):
                var_declaration_count += 1
                if isinstance(stmt.value, ast.Call):
                    function_call_count += 1
                if isinstance(stmt.value, ast.BinOp):
                    bin_op_count += 1
            elif isinstance(stmt, ast.If):
                if_count += 1
            elif isinstance(stmt, ast.For):
                for_loop_count += 1
            elif isinstance(stmt, ast.While):
                while_loop_count += 1
            elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                function_call_count += 1
            elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.BinOp):
                bin_op_count += 1

        function_profile = (node.name, parameter_count, var_declaration_count, if_count, for_loop_count, while_loop_count, function_call_count, bin_op_count)
        self.function_profiles.append(function_profile)
        self.generic_visit(node)

# Given a code file pointer, create an AST structure.
# Pass True to print_ast to print out the AST structure to console.
def code_to_ast(code_file, print_ast = False):
    code_lines = code_file.readlines()
    code_segment = ''
    for line in code_lines:
        code_segment += line
    print(code_segment)
    code_ast = ast.parse(code_segment)
    if print_ast:
        print(ast.dump(code_ast, indent = 4))
    return code_ast

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

    ast_1_node_visitor = functiondef_visitor()
    ast_1_node_visitor.visit(ast_1)
    function_list_1 = ast_1_node_visitor.function_profiles
    ast_2_node_visitor = functiondef_visitor()
    ast_2_node_visitor.visit(ast_2)
    function_list_2 = ast_2_node_visitor.function_profiles
    print("FUNCTION LIST 1: ", end = '')
    print(function_list_1)
    print("FUNCTION LIST 2: ", end = '')
    print(function_list_2)
    print("End.")

if __name__ == "__main__":
    main()
