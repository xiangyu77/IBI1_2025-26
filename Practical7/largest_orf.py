seq = 'AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG'
start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

orfs = []
for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        for j in range(i+3, len(seq) - 2, 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                orf = seq[i:j+3]
                orfs.append(orf)
                break

if orfs:
    longest = max(orfs, key=len)
    print("Longest ORF:", longest)
    print("Length (nucleotides):", len(longest))
else:
    print("No ORF found.")