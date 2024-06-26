import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from library import *

# function to serialize the graph
def serialize_graph(G):
    # serialized array for the result
    output = []

    # iterate over the nodes and edges of the graph we created
    for node_id, node_data in G.nodes(data=True):
        # Save node information in a variable
        node_info = f"Node {node_id}: Type={node_data['type']}, Label={node_data['label']}"
        # if the node has a value check it
        if 'value' in node_data:
            value_str = str(node_data['value'])
            # add the value to the node information
            node_info += f", Value={value_str}"
        # add it to our result
        output.append(node_info)
    
    # for each of the edges, add them to the result,
    # to keep track of the connections in the file exported
    for u, v in G.edges():
        output.append(f"Edge from Node {u} to Node {v}")
    
    return "\n".join(output)

# Global variables
parseGraph = None
draw = True
NODE_COUNTER = 0
read_file_1 = input("Enter file you want to read or press enter if you don't have a file: ")

# Tokens
tokens =(
    'NUMBER',
    "VARIABLE",
    "SETTO",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "EXP",
    "LPAREN",
    "RPAREN",
    "COMMA",
    "STRING",
    "CONNECT",
)

# Symbol table
symbol_table = dict()

# function to add node to the graph
def add_node(attr):
    global parseGraph
    global NODE_COUNTER
    attr["counter"] = NODE_COUNTER
    parseGraph.add_node(NODE_COUNTER, **attr)
    NODE_COUNTER += 1

    return parseGraph.nodes[NODE_COUNTER - 1]


# Reserved keywords
symbol_table["pi"] = 3.14159265359 
symbol_table["e"] = 2.71828182846
symbol_table["max"] = max
symbol_table["None"] = None

# openCV and numpy functions defined in our library file
symbol_table["load_image"] = load_image
symbol_table["save_image"] = save_image
symbol_table["gen_matrix"] = gen_matrix
symbol_table["gen_vector"] = gen_vector
symbol_table["show_image"] = show_image
symbol_table["multiplot_show"] = multiplot_show
symbol_table["histogram_visualization"] = histogram_visualization
symbol_table["search_cv2"] = search_cv2
symbol_table["numpy_sin"] = numpy_sin
symbol_table["numpy_cos"] = numpy_cos
symbol_table["numpy_tan"] = numpy_tan
symbol_table["numpy_arcsin"] = numpy_arcsin
symbol_table["numpy_arccos"] = numpy_arccos
symbol_table["numpy_arctan"] = numpy_arctan
symbol_table["numpy_sinh"] = numpy_sinh
symbol_table["numpy_cosh"] = numpy_cosh
symbol_table["numpy_tanh"] = numpy_tanh
symbol_table["grabcut_segmentation"] = grabcut_segmentation

# Regular expressions as variables

t_PLUS = r'\+'
t_SETTO = r'='
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'->'

# reg expressions that need more logic, expressed as functions 

def t_NUMBER(t):
    r'\d+\.?\d*'
    if t.value.find(".") > -1:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Error")
    t.lexer.skip(1)

#Build Lexer 
lexer = lex.lex()

# Grammar

def p_assignment_assigns(p):
    '''
    statement : VARIABLE SETTO expression
    '''
    node = add_node( {'type': 'ASSIGN', 'label': '=', 'value': ''} )
    node_variable = add_node( {'type': 'VARIABLE_ASSIGN', 'label': f'VAR_{p[1]}', 'value': p[1]} )
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_assignment_flow(p):
    '''
    statement : VARIABLE SETTO flow
    '''
    node = add_node( {'type': 'ASSIGN', 'label': '=', 'value': ''} )
    node_variable = add_node( {'type': 'VARIABLE_ASSIGN', 'label': f'VAR_{p[1]}', 'value': p[1]} )
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_flow_form(p):
    '''
    flow : VARIABLE CONNECT flow_functions
    '''

    connections = parseGraph.neighbors(p[3][0]["counter"])
    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            c["type"] = "VARIABLE"
            c["label"] = f'VAR_{p[1]}'
            c["value"] = p[1]
            break
    
    p[0] = p[3][-1]
    

def p_flow_functions(p):
    '''
    flow_functions : flow_function_call CONNECT flow_functions
    '''
    connections = parseGraph.neighbors(p[3][0]["counter"])
    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            parseGraph.add_edge(c["counter"], p[1]["counter"])
            break
    
    p[0] = [p[1]] + p[3]

def p_flow_function(p):
    '''
    flow_functions : flow_function_call
    '''
    p[0] = [p[1]]

def p_flow_function_call(p):
    '''
    flow_function_call : VARIABLE LPAREN params RPAREN
    '''
    node = add_node( {'type': 'FLOW_FUNCTION_CALL', 'label': f'ff_{p[1]}', 'value': p[1]} )
    pending_node = add_node({'type': 'PENDING_NODE', 'label': f'pending', 'value': ''})
    parseGraph.add_edge(node["counter"], pending_node["counter"])
    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    
    p[0] = node

def p_assignment_expression(p):
    '''
    statement : expression
    '''
    p[0] = p[1]

def p_expression_plus(p):
    '''
    expression : expression PLUS term
    '''
    node = add_node( {'type': 'PLUS', 'label': '+', 'value': ''} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    p[0] = node

def p_expression_minus(p):
    '''
    expression : expression MINUS term
    '''
    node = add_node( {'type': 'MINUS', 'label': '-', 'value': ''} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_term(p):
    '''
    expression : term 
                | string
    '''
    p[0] = p[1]

def p_string_def(p):
    '''
    string : STRING
    '''
    p[0] = add_node( {'type': 'STRING', 'label': f'STR_{p[1]}', 'value': p[1]} )

def p_term_times(p):
    '''
    term : term TIMES exponent
    '''
    node = add_node( {'type': 'TIMES', 'label': '*', 'value': ''} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_term_divide(p):
    '''
    term : term DIVIDE exponent
    '''
    node = add_node( {'type': 'DIVIDE', 'label': '/', 'value': ''} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_term_exponent(p):
    '''
    term : exponent
    '''
    p[0] = p[1]

def p_exponent_ext(p):
    '''
    exponent : factor EXP factor
    '''
    node = add_node( {'type': 'EXPONENT', 'label': '^', 'value': ''} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_exponent_factor(p):
    '''
    exponent : factor
    '''
    p[0] = p[1]

def p_exponent_paren(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    node = add_node( {'type': 'GROUP', 'label': '{}', 'value': ''} )
    parseGraph.add_edge(node["counter"], p[2]["counter"])
    p[0] = node

def p_factor_num(p):
    '''
    factor : NUMBER
    '''
    p[0] = add_node( {'type': 'NUMBER', 'label': f'NUM_{str(p[1])}', 'value': p[1]} )

def p_factor_var(p):
    '''
    factor : VARIABLE
    '''
    p[0] = add_node( {'type': 'VARIABLE', 'label': f'VAR_{str(p[1])}', 'value': p[1]} )

def p_factor_function_call(p):
    '''
    factor : function_call
    '''
    p[0] = p[1]

def p_function_call_no_params(p):
    '''
    function_call : VARIABLE LPAREN RPAREN
    '''
    p[0] = add_node( {'type': 'FUNCTION_CALL', 'label': f'FUNC_{p[1]}', 'value': p[1]} )

def p_function_call_params(p):
    '''
    function_call : VARIABLE LPAREN params RPAREN
    '''
    node = add_node( {'type': 'FUNCTION_CALL', 'label': f'FUNC_{p[1]}', 'value': p[1]} )
    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_params(p):
    '''
    params : params COMMA expression
            | expression
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_error(p):
    print("Syntax error on input!", p)

def execute_parse_tree(tree):
    root = tree.nodes[0]
    root_id = 0
    res = visit_node(tree, root_id, -1)
    if type(res) == int or type(res) == float:
        print("RESULT: ", res)

def visit_node(tree, node_id, parent_id):
    children = tree.neighbors(node_id)

    res = []
    for c in children:
        if c != parent_id:
            res.append(visit_node(tree, c, node_id))
    current_node = parseGraph.nodes[node_id]

    print(f"From Node {node_id}", res)

    print("Current Node: ", current_node["type"])

    if current_node["type"] == "INITIAL":
        return res[0]

    if current_node["type"] == "NUMBER":
        return current_node["value"]
    
    if current_node["type"] == "PLUS":
        print("adding: ", res)
        return res[0] + res[1]
    
    if current_node["type"] == "MINUS":
        print("substracting: ", res)
        return res[0] - res[1]
    
    if current_node["type"] == "TIMES":
        print("multiplying: ", res)
        return res[0] * res[1]
    
    if current_node["type"] == "DIVIDE":
        print("dividing: ", res)
        return res[0] / res[1]
    
    if current_node["type"] == "EXPONENT":
        print("exponenting: ", res)
        return res[0] ** res[1]
    
    if current_node["type"] == "GROUP":
        return res[0]
    
    if current_node["type"] == "VARIABLE":
        return symbol_table[current_node["value"]]
    
    if current_node["type"] == "VARIABLE_ASSIGN":
        return current_node["value"]
    
    if current_node["type"] == "ASSIGN":
        symbol_table[res[0]] = res[1]
        return res[1]
    
    if current_node["type"] == "STRING":
        return current_node["value"]

    if current_node["type"] == "PENDING_NODE":
        return res[0]
    
    if current_node["type"] == "FUNCTION_CALL" or current_node["type"] == "FLOW_FUNCTION_CALL":
        v = current_node["value"]
        if v in symbol_table:
            fn = symbol_table[v]
            if callable(fn):
                try:
                    res = fn(*res)
                    return res
                except Exception as e:
                    print(f"Error calling function {v}", e)
                    return "Error"
            else:
                print(f"Function {v} is not callable")
                return "Error"
        else:
            fn = search_cv2(v)
            if fn:
                if callable(fn):
                    try:
                        res = fn(*res)
                        return res
                    except Exception as e:
                        print(f"Error calling function {v}", e)
                        return "Error"
            else:
                print(f"Function {v} not found")
                return "Error"

        
# Build parser
parser = yacc.yacc()


# If File is true then read from file
if len(read_file_1) > 0:
    with open(read_file_1, "r") as file:
        for line in file:
            NODE_COUNTER = 0
            parseGraph = nx.Graph()
            root = add_node( {'type': 'INITIAL', 'label': 'INIT'})
            result = parser.parse(line)
            parseGraph.add_edge(root["counter"], result["counter"])

            labels = nx.get_node_attributes(parseGraph, 'label')

            if draw:
                pos = graphviz_layout(parseGraph, prog='dot')
                nx.draw(parseGraph, pos, with_labels=True, labels=labels)
                plt.show()

            execute_parse_tree(parseGraph)
    
    print("Finished, processed file.")

else:
    while True:
        try:
            data = input("input>> ")
            if(data == "exit"):
                break
            if(data == "symbols"):
                print(symbol_table)
                continue
            
        except EOFError:
            break

        if not data:
            continue
        
        NODE_COUNTER = 0
        parseGraph = nx.Graph()
        root = add_node( {'type': 'INITIAL', 'label': 'INIT'})
        result = parser.parse(data)
        parseGraph.add_edge(root["counter"], result["counter"])
        
        labels = nx.get_node_attributes(parseGraph, 'label')

        if draw:
            pos = graphviz_layout(parseGraph, prog='dot')
            nx.draw(parseGraph, pos, with_labels=True, labels=labels)
            plt.show()

        execute_parse_tree(parseGraph)
        serialized = serialize_graph(parseGraph)
        # write serialized graph to file
        with open("graph.txt", "w") as f:
            # write title
            f.write("Input: " + data + "\n")
            f.write(str(serialized))

    print("Finished, accepted input.")