# stop_codons.py
# Filters FASTA entries containing a user‑specified stop codon

def get_gene_name(header):
    # Extract the gene name (e.g. ">YAL001C ..." -> "YAL001C")
    return header.split()[0][1:]

stop = input("Enter one of the stop codons (TAA, TAG, TGA): ").strip().upper()
if stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid input. Please enter TAA, TAG, or TGA.")
    exit()

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    current_header = None
    current_seq = []
    
    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            # Process previous gene
            if current_header is not None:
                seq = ''.join(current_seq)
                if stop in seq:
                    gene_name = get_gene_name(current_header)
                    outfile.write(f">{gene_name}_{stop}\n")
                    outfile.write(seq + "\n")
            # Start new gene
            current_header = line
            current_seq = []
        else:
            if line:
                current_seq.append(line)
    
    # Don't forget the last gene
    if current_header is not None:
        seq = ''.join(current_seq)
        if stop in seq:
            gene_name = get_gene_name(current_header)
            outfile.write(f">{gene_name}_{stop}\n")
            outfile.write(seq + "\n")

print(f"Done. Output written to {output_file}")