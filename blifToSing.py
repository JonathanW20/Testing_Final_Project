def convert_blif_to_singular(blif_content):
    singular_code = ''
    gate_map = {
        'nand2': 'nand',
        'inv1x': 'not',
        'xor': 'xor'  # Adding XOR gate mapping
    }

    lines = blif_content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('.gate'):
            parts = line.split()
            gate_type = parts[1]
            gate_inputs = [part.split('=')[1] for part in parts[2:]]

            singular_gate = gate_map.get(gate_type)
            if singular_gate:
                if gate_type == 'inv1x':
                    singular_code += f"{gate_inputs[0]} = {singular_gate}({gate_inputs[1]});\n"
                else:
                    # Include XOR gate handling
                    if gate_type == 'xor2':
                        singular_code += f"{gate_inputs[2]} = {singular_gate}({gate_inputs[0]}, {gate_inputs[1]});\n"
                    else:
                        singular_code += f"{gate_inputs[2]} = {singular_gate}({gate_inputs[0]}, {gate_inputs[1]});\n"

    return singular_code

def convert_multiplier_blif_to_singular(file_path):
    with open(file_path, 'r') as file:
        blif_content = file.read()

    singular_code = convert_blif_to_singular(blif_content)

    output_file_path = file_path.replace('.blif', '.sing')

    with open(output_file_path, 'w') as output_file:
        output_file.write(singular_code)

    print(f"Singular code written to {output_file_path}")

# Example usage for a 4-bit multiplier BLIF file
# Replace '4bit_multiplier.blif' with the path to your 8-bit or 32-bit multiplier BLIF file
convert_multiplier_blif_to_singular('4bit_multiplier.blif')

