def convert_blif_to_sing(blif_content, sing_file):
    # Initialize the Singular content with introductory remarks or comments
    sing_content = '// Converted from BLIF to Singular\n'

    # Parsing BLIF content
    lines = blif_content.split('\n')
    model_name = None
    inputs = []
    outputs = []
    logic_gates = {}

    for line in lines:
        line = line.strip()
        if line.startswith('.model'):
            model_name = line.split()[-1]
            sing_content += f'ring R = 0, ({model_name}), dp;\n'
        elif line.startswith('.inputs'):
            inputs = line.split()[1:]
            for var in inputs:
                sing_content += f'poly {var};\n'
        elif line.startswith('.outputs'):
            outputs = line.split()[1:]
            for var in outputs:
                sing_content += f'poly {var};\n'
        elif line.startswith('.names'):
            parts = line.split()
            input_vars = parts[1:-1]
            output_var = parts[-1]
            truth_table = parts[2:-1]  # Exclude input/output variables
            logic_gates[output_var] = {'input_vars': input_vars, 'truth_table': truth_table}

    # Generating Singular commands for logic gates
    for output_var, gate_info in logic_gates.items():
        sing_content += f"{output_var} = "
        for i, tt in enumerate(gate_info['truth_table']):
            if tt == '1':
                sing_content += "(" + "*".join(gate_info['input_vars'][i] for i, bit in enumerate(tt) if bit == '1') + ")"
                sing_content += "+"  # Adding "+" between minterms
        sing_content = sing_content.rstrip("+")  # Remove the last "+"
        sing_content += ";\n"

    # Writing the converted content to the Singular file
    with open(sing_file, 'w') as f:
        f.write(sing_content)

# BLIF content provided by the user
blif_content = '''
.model bcd_7seg
.inputs a b c d
.outputs seg0 seg1 seg2 seg3 seg4 seg5 seg6
.names d c b a min0
0000 1
# Remaining BLIF content...
.end
'''

# Replace 'output.sing' with your desired file path
convert_blif_to_sing(blif_content, 'output.sing')
