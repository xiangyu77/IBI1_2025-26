import matplotlib.pyplot as plt

# Initial dictionary
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}

print("Initial gene expression dictionary:")
print(gene_expression)

# Add MYC
gene_expression['MYC'] = 11.6
print("\nAfter adding MYC:")
print(gene_expression)

# Bar chart
genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.bar(genes, values, color='skyblue')
plt.xlabel('Gene')
plt.ylabel('Expression level')
plt.title('Gene Expression Levels')
plt.show()

# Query a gene (example: BRCA1)
gene_of_interest = 'BRCA1'
if gene_of_interest in gene_expression:
    print(f"\nExpression of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"\nError: Gene '{gene_of_interest}' not found.")

# Average expression
average = sum(gene_expression.values()) / len(gene_expression)
print(f"Average expression level: {average:.2f}")