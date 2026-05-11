# largest_orf.py
# Finds the longest open reading frame in an RNA sequence

seq = 'AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG'
start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

orfs = []

# Scan each position as a potential start
for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        # From the next codon, step by 3
        for j in range(i+3, len(seq) - 2, 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                orf = seq[i:j+3]   # include stop codon
                orfs.append(orf)
                break               # first stop gives the shortest ORF from this start

if orfs:
    longest = max(orfs, key=len)
    print("Longest ORF:", longest)
    print("Length (nucleotides):", len(longest))
else:
    print("No ORF found.")