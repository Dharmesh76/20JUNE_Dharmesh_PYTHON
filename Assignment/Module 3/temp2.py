sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_values = {}

for d in sample_data:
    item = d['item']
    amount = d['amount']
    combined_values[item] = combined_values.get(item) + amount

print("Combined values:")
print(combined_values)
