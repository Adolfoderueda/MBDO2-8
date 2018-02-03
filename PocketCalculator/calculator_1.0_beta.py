import re

inp_string = '11+2+3*4'

math_regex = '^[0-9\/\*\+\-\s\.]+$'
digit_regex = '([0-9\.]+?)'
operator_regex = '([\*\/\+\-])'
one_operator_regex = '.*([\+\-\*\/]).*'
two_operators_regex = '.*([\+\-\*\/][\+\-\*\/]).*'

def get_tokenized_math_expression(inp_string):
    inp_match = re.match(math_regex, inp_string)
    if inp_match is None:
        inp_string = ''
        print('Invalid characters. Please input a valid maths expression.')
        return([], False)
    else:
        inp_string = inp_match.string
        op_list = re.split(operator_regex, inp_string)
        return(op_list, True)
    

def check_unary_minus(tk_list):
    for i in range(1, len(tk_list) - 1):
        if tk_list[i] == '-':
            left_operand = tk_list[i-1]
            lo_match = re.match(digit_regex, left_operand)
            if lo_match is None:
                print('Cannot operate on unary minus.')
                return(False)
    return(True)

def check_valid_operators(txt):
    txt_match = re.match(two_operators_regex, txt)
    #print(txt_match)
    if txt_match is None:
        return(True)
    else:
        print('Invalid input. Two consecutive operators found :', txt_match.string)
        return(False)

def solve_tokenized_expression(tk_expr):
    ans = 0.0
    operators_list = ['*', '/', '+', '-']
    for op in operators_list:
        while op in tk_expr:
            op_idx = tk_expr.index(op)
            left_operand = float(tk_expr[op_idx - 1])
            right_operand = float(tk_expr[op_idx + 1])
            int_ans = 0.0
            if op == '*':
                int_ans = left_operand * right_operand
            if op == '/':
                if right_operand == 0:
                    print('Cannot divide by zero at :', left_operand, '/', right_operand)
                    return(None)
                else:
                    int_ans = left_operand / right_operand
            if op == '+':
                int_ans = left_operand + right_operand
            if op == '-':
                int_ans = left_operand - right_operand
            del tk_expr[op_idx + 1]
            del tk_expr[op_idx]
            tk_expr[op_idx - 1] = str(int_ans)
            
    ans = float(tk_expr[0])
    return(ans)


while(True):
    text = input('>>>')
    if text == 'quit':
        break
    text = text.replace(' ', '')
    
    if False == check_valid_operators(text):
        continue
        
    tokens_list, valid = get_tokenized_math_expression(text)
    if valid == False:
        continue
        
    if False == check_unary_minus(tokens_list):
        continue
    
    print('Tokenized as :', tokens_list)
    calculated = solve_tokenized_expression(tokens_list)
    if calculated is not None:
        print('Calculated as :', calculated)
