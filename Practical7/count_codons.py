# count_codons.py
# Counts upstream in‑frame codons for the longest ORF defined by a user‑chosen stop codon

import matplotlib.pyplot as plt

def read_fasta(filename):
    """Return dict {gene_name: sequence} from a FASTA file."""
    genes = {}
    with open(filename, 'r') as f:
        header = None
        seq = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    genes[header] = ''.join(seq)
                header = line[1:]   # remove '>'
                seq = []
            else:
                seq.append(line)
        if header:
            genes[header] = ''.join(seq)
    return genes

def find_stop_positions(seq, stop):
    """Return list of all start indices of the stop codon in seq."""
    positions = []
    start = 0
    while True:
        pos = seq.find(stop, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

def count_codons_upstream(seq, stop_pos):
    """Count codons (3‑nt) upstream of stop_pos (excluding the stop)."""
    counts = {}
    pos = stop_pos - 3
    while pos >= 0:
        codon = seq[pos:pos+3]
        counts[codon] = counts.get(codon, 0) + 1
        pos -= 3
    return counts

def main():
    stop = input("Enter stop codon (TAA, TAG, TGA): ").strip().upper()
    if stop not in ['TAA', 'TAG', 'TGA']:
        print("Invalid stop codon.")
        return

    try:
        genes = read_fasta("stop_genes.fa")
    except FileNotFoundError:
        print("stop_genes.fa not found. Please run stop_codons.py first.")
        return

    total_counts = {}
    gene_count = 0

    for name, seq in genes.items():
        positions = find_stop_positions(seq, stop)
        if positions:
            # Choose the last stop (gives longest ORF)
            best = max(positions)
            counts = count_codons_upstream(seq, best)
            for codon, cnt in counts.items():
                total_counts[codon] = total_counts.get(codon, 0) + cnt
            gene_count += 1

    if not total_counts:
        print(f"No genes containing stop codon {stop} found in stop_genes.fa")
        return

    # Prepare pie chart data
    sorted_codons = sorted(total_counts.items(), key=lambda x: x[1], reverse=True)
    labels = [c[0] for c in sorted_codons]
    sizes = [c[1] for c in sorted_codons]

    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Codon usage upstream of {stop} (based on {gene_count} genes)')
    plt.axis('equal')
    outfile = f'codon_usage_{stop}.png'
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Pie chart saved as {outfile}")

if __name__ == "__main__":
    main()