def convert_multiplier_blif_to_singular(file_path):
    try:
        gate_map = {
            'nand2': 'nand',
            'inv1x': 'not',
            'xor2': 'xor'
        }

        with open(file_path, 'r') as file:
            lines = file.readlines()

        singular_code = ''
        for line in lines:
            line = line.strip()
            if line.startswith('.gate'):
                parts = line.split()
                gate_type = parts[1]
                gate_inputs = [part.split('=')[1] for part in parts[2:]]

                singular_gate = gate_map.get(gate_type)
                if singular_gate:
                    if gate_type == 'nand2':
                        singular_code += f"{gate_inputs[2]} = {singular_gate}({gate_inputs[0]}, {gate_inputs[1]});\n"
                    elif gate_type == 'inv1x':
                        singular_code += f"{gate_inputs[0]} = {singular_gate}({gate_inputs[1]});\n"
                    elif gate_type == 'xor2':
                        singular_code += f"{gate_inputs[2]} = {singular_gate}({gate_inputs[0]}, {gate_inputs[1]});\n"

        if singular_code:
            output_file_path = file_path.replace('.blif', '.sing')
            with open(output_file_path, 'w') as output_file:
                output_file.write(singular_code)
            print(f"Singular code written to {output_file_path}")
        else:
            print("No valid Singular code generated. Check the BLIF file content.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage for a 4-bit multiplier BLIF file
convert_multiplier_blif_to_singular('Mapped16BitMult.blif')
# Replace '4bit_multiplier.blif' with the path to your 8-bit or 32-bit multiplier BLIF file
