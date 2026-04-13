def calculate_protein_mass(sequence):
    """
    Calculate total mass of a protein sequence in amu.
    sequence: string of single-letter amino acid codes (e.g., "ACDEF")
    Returns: total mass as float
    Raises: ValueError if an unknown amino acid is found
    """
    # Dictionary mapping amino acid symbol to residue mass (monoisotopic)
    mass_dict = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }
    total_mass = 0.0
    for aa in sequence.upper():   
        if aa in mass_dict:
            total_mass += mass_dict[aa]
        else:
            raise ValueError(f"Unknown amino acid: '{aa}'. Valid symbols: {list(mass_dict.keys())}")
    return total_mass
if __name__ == "__main__":
    # Example 1: normal sequence
    test_seq = "ACDEFGHIKLMNPQRSTVWY"   
    mass = calculate_protein_mass(test_seq)
    print(f"Mass of {test_seq} is {mass:.2f} amu")

    # Example 2: sequence with unknown letter (should raise error)
    try:
        bad_seq = "ACDEX"
        mass2 = calculate_protein_mass(bad_seq)
        print(f"Mass of {bad_seq} is {mass2:.2f} amu")
    except ValueError as e:
        print("Error:", e)