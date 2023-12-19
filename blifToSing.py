def parse_blif_file(file_path):
    """
    Parses the BLIF file and extracts information about gates, inputs, and outputs.

    Args:
    file_path (str): Path to the BLIF file.

    Returns:
    tuple: A tuple containing a list of gates and sets of primary inputs and outputs.
    """
    gates, inputs, outputs = [], set(), set()
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('.gate'):
                parts = line.split()
                gate_type = parts[1]
                # Replace 'new_n' with 'n' in inputs and output names
                gate_inputs = [p.split('=')[1].replace('new_n', 'n') for p in parts[2:-1]]
                gate_output = parts[-1].split('=')[1].replace('new_n', 'n')
                gates.append((gate_type, gate_inputs, gate_output))
                outputs.add(gate_output)
                inputs.update(gate_inputs)
            elif line.startswith('.inputs'):
                inputs.update([i.replace('new_n', 'n') for i in line.split()[1:]])
            elif line.startswith('.outputs'):
                outputs.update([o.replace('new_n', 'n') for o in line.split()[1:]])
    return gates, inputs - outputs, outputs

def topological_sort(gates, primary_inputs):
    """
    Performs a reverse topological sort on the gates to determine the order of variables.

    Args:
    gates (list): List of gates extracted from the BLIF file.
    primary_inputs (set): Set of primary input variables.

    Returns:
    list: Sorted list of variables in reverse topological order.
    """
    graph = {gate_output: set(gate_inputs) for _, gate_inputs, gate_output in gates}
    order, visited = [], set()
    
    def visit(node):
        if node not in visited:
            visited.add(node)
            if node in graph:
                for n in graph[node]:
                    visit(n)
            order.append(node)

    for output in graph:
        visit(output)
    return [o for o in order if o not in primary_inputs] + list(primary_inputs)

def generate_ring_declaration(sorted_vars):
    """
    Generates the ring declaration line for the .sing file.

    Args:
    sorted_vars (list): Sorted list of variables.

    Returns:
    str: Ring declaration string.
    """
    return f"ring r = 2, ({', '.join(sorted_vars)}), lp;"

def blif_gate_to_singular(gate_type, inputs, output):
    """
    Converts a BLIF gate to its corresponding polynomial in Singular.

    Args:
    gate_type (str): Type of the gate (nand2, inv1x, xor).
    inputs (list): List of input variables to the gate.
    output (str): Output variable of the gate.

    Returns:
    str: Polynomial equation representing the gate.
    """
    if gate_type == 'nand2':
        return f"{output} - {inputs[0]} * {inputs[1]}"
    elif gate_type == 'inv1x':
        return f"{output} - 1 + {inputs[0]}"
    elif gate_type == 'xor':
        return f"{output} - {inputs[0]} - {inputs[1]} + 2 * {inputs[0]} * {inputs[1]}"
    else:
        raise ValueError(f"Unsupported gate type: {gate_type}")

def write_singular_file(gates, sorted_vars, primary_inputs, ring_size, output_path):
    """
    Writes the converted information to a .sing file.

    Args:
    gates (list): List of gates extracted from the BLIF file.
    sorted_vars (list): Sorted list of variables.
    primary_inputs (set): Set of primary input variables.
    ring_size (int): Size of the ring.
    output_path (str): Path to save the .sing file.
    """
    with open(output_path, 'w') as file:
        file.write("// Singular file generated from BLIF\n")
        file.write(generate_ring_declaration(sorted_vars) + "\n")
        poly_names = []
        for i, (gate_type, inputs, output) in enumerate(gates):
            poly_name = f"f{i}"
            poly_names.append(poly_name)
            poly = blif_gate_to_singular(gate_type, inputs, output)
            file.write(f"poly {poly_name} = {poly};\n")

        file.write(f"ideal J = {', '.join(poly_names)};\n")

        # Generate and write the vanishing polynomials for primary inputs
        exponent = ring_size + 1
        vanishing_polys = [f"{var}^{exponent}-{var}" for var in primary_inputs]
        file.write(f"ideal J0 = {', '.join(vanishing_polys)};\n")

def main():
    """
    Main function to orchestrate the conversion from BLIF to .sing format.
    """
    blif_file_path = input("Enter the path to the BLIF file: ")
    output_singular_path = input("Enter the desired output path for the .sing file: ")

    gates, primary_inputs, _ = parse_blif_file(blif_file_path)
    sorted_vars = topological_sort(gates, primary_inputs)
    
    ring_size = 2  # Update this as needed for your specific use case

    write_singular_file(gates, sorted_vars, primary_inputs, ring_size, output_singular_path)
    print(f"Conversion complete. The .sing file has been saved to {output_singular_path}")

if __name__ == "__main__":
    main()
