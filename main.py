import ast
import numpy
import copy

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

        function_profile = [node.name, parameter_count, var_declaration_count, if_count, 
                            for_loop_count, while_loop_count, function_call_count, bin_op_count]
        self.function_profiles.append(function_profile)
        self.generic_visit(node)

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

# changes profile values based on vector scalars used to calculate function distance.
def apply_scalars(list):
    # attribute weights add up to 100%.
    # higher weight = the attribute matters more for the similarity calculation.
    # weights are used as vector scalars.
    attribute_weights = (
        0.3,    # parameter_count
        0.05,   # var_declaration_count
        0.1,    # if_count
        0.2,    # for_loop_count
        0.2,    # while_loop_count
        0.1,    # function_call_count
        0.05    # bin_op_count
    )
    for profile in list:
        for i in range(7):
            profile[i+1] *= attribute_weights[i]

def remove_name(list):
    for sublist in list:
        sublist.pop(0)

# given function profile lists, compare each function to one another
# and create a similarity matrix. 
def compare_codes(list_1, list_2):
    # apply scalars
    apply_scalars(list_1)
    apply_scalars(list_2)

    # get distance matrix
    distance_matrix = []
    distance_row = []
    similarity_matrix = []
    similarity_row = []
    for profile_1 in list_1:
        profile_1_name = profile_1.pop(0)
        for profile_2 in list_2:
            profile_2_name = profile_2.pop(0)
            #print(f"comparing {profile_1_name}() in file 1 and {profile_2_name}() in file 2")
            distance = numpy.linalg.norm(numpy.array(profile_1) - numpy.array(profile_2))
            #print(f"Distance: {distance}")
            profile_2.insert(0, profile_2_name)
            distance_row.append(distance)
            similarity = abs(distance - 1) # complement
            similarity_row.append(f"{profile_1_name}() in file 1 vs. {profile_2_name}() in file 2: {similarity:.1%}")
        profile_1.insert(0, profile_1_name)
        distance_matrix.append(distance_row)
        similarity_matrix.append(similarity_row)
        distance_row = []
        similarity_row = []

    #print("similarity matrix:")
    for row in similarity_matrix:
        for score in row:
            print(score)
    
def main():
    code_file_1 = open(input("Enter a code file name (code file 1): "), 'r')
    code_file_2 = open(input("Enter a code file name (code file 2): "), 'r')

    #print("\n------------------CODE FILE 1------------------")
    ast_1 = code_to_ast(code_file_1)
    #print("\n------------------CODE FILE 2------------------")
    ast_2 = code_to_ast(code_file_2)

    ast_1_node_visitor = functiondef_visitor()
    ast_1_node_visitor.visit(ast_1)
    function_list_1 = ast_1_node_visitor.function_profiles
    ast_2_node_visitor = functiondef_visitor()
    ast_2_node_visitor.visit(ast_2)
    function_list_2 = ast_2_node_visitor.function_profiles

    compare_codes(function_list_1, function_list_2)

if __name__ == "__main__":
    main()
