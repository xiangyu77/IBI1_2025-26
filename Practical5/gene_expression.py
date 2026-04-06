# 创建包含5个基因及其表达水平的字典
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}

# 打印初始字典
print("初始基因表达字典：")
print(gene_expression)
# 添加基因 'MYC' 及其表达值
gene_expression['MYC'] = 11.6

# 打印更新后的字典
print("添加 MYC 后的字典：")
print(gene_expression)
import matplotlib.pyplot as plt

# 提取基因名称和表达值列表
genes = list(gene_expression.keys())
values = list(gene_expression.values())

# 创建条形图
plt.bar(genes, values, color='skyblue')
plt.xlabel('基因')
plt.ylabel('表达水平')
plt.title('基因表达水平条形图')
plt.show()
# 定义感兴趣的基因（你可以修改这个变量来测试不同基因）
gene_of_interest = 'BRCA1'  # 例如查询 BRCA1

# 检查基因是否在字典中
if gene_of_interest in gene_expression:
    print(f"{gene_of_interest} 的表达值为：{gene_expression[gene_of_interest]}")
else:
    print(f"错误：基因 {gene_of_interest} 不在数据集中。")
    # 计算平均值
average_expression = sum(gene_expression.values()) / len(gene_expression)

# 打印平均值
print(f"所有基因的平均表达水平为：{average_expression:.2f}")