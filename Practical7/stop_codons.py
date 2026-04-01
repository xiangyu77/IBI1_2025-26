def get_gene_name(header):
    # 提取基因名，例如 ">YAL001C ..." -> "YAL001C"
    return header.split()[0][1:]

stop = input("Enter one of the stop codons (TAA, TAG, TGA): ").strip().upper()
if stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid input. Exiting.")
    exit()

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all (1).fa"
output_file = "stop_genes.fa"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    current_header = None
    current_seq = []
    
    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            # 遇到新基因标题
            if current_header is not None:
                # 处理上一个基因
                seq = ''.join(current_seq)
                if stop in seq:
                    # 写入输出
                    gene_name = get_gene_name(current_header)
                    outfile.write(f">{gene_name}_{stop}\n")
                    # 每行最多80个碱基，但这里简单写为一行
                    outfile.write(seq + "\n")
            # 开始新基因
            current_header = line
            current_seq = []
        else:
            # 序列行
            if line:  # 忽略空行
                current_seq.append(line)
    
    # 处理最后一个基因
    if current_header is not None:
        seq = ''.join(current_seq)
        if stop in seq:
            gene_name = get_gene_name(current_header)
            outfile.write(f">{gene_name}_{stop}\n")
            outfile.write(seq + "\n")

print(f"Done. Output written to {output_file}")