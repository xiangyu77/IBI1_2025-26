# count_codons.py
# 统计基因中指定终止密码子之前的框架内密码子使用频率，并生成饼图

import matplotlib.pyplot as plt

def read_fasta(filename):
    """读取 FASTA 文件，返回字典 {gene_name: sequence}"""
    genes = {}
    with open(filename, 'r') as f:
        header = None
        seq = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    genes[header] = ''.join(seq)
                header = line[1:]  # 去掉 '>'
                seq = []
            else:
                seq.append(line)
        if header:
            genes[header] = ''.join(seq)
    return genes

def find_stop_positions(seq, stop):
    """返回序列中所有 stop 密码子的起始索引列表"""
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
    """从终止密码子之前（不包括终止）开始，以3为步长向前统计密码子"""
    codon_counts = {}
    # 从终止密码子的前一个密码子开始（即索引 stop_pos - 3）
    pos = stop_pos - 3
    while pos >= 0:
        codon = seq[pos:pos+3]
        codon_counts[codon] = codon_counts.get(codon, 0) + 1
        pos -= 3
    return codon_counts

# 主程序
stop = input("Enter stop codon (TAA, TAG, TGA): ").strip().upper()
if stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid stop codon. Exiting.")
    exit()

# 读取 stop_genes.fa（由任务二生成）
genes = read_fasta("stop_genes.fa")

total_codon_counts = {}

for gene_name, seq in genes.items():
    # 检查该基因是否包含用户指定的终止密码子
    if stop in seq:
        # 找到所有出现位置
        positions = find_stop_positions(seq, stop)
        if not positions:
            continue
        # 选择产生最长 ORF 的终止位置（这里取最大索引，即最靠后的）
        best_pos = max(positions)
        # 统计该位置之前的密码子
        counts = count_codons_upstream(seq, best_pos)
        # 合并到总计数
        for codon, cnt in counts.items():
            total_codon_counts[codon] = total_codon_counts.get(codon, 0) + cnt

# 准备饼图数据
if total_codon_counts:
    # 如果密码子种类太多，可以按出现次数排序，取前20种显示
    sorted_codons = sorted(total_codon_counts.items(), key=lambda x: x[1], reverse=True)
    labels = [c[0] for c in sorted_codons]
    sizes = [c[1] for c in sorted_codons]

    # 设置图形大小
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Codon usage upstream of {stop} in yeast genes')
    plt.axis('equal')  # 保持圆形

    # 保存图片
    output_file = f'codon_usage_{stop}.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Pie chart saved as {output_file}")
else:
    print(f"No genes with stop codon {stop} found.")