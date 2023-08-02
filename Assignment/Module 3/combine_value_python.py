a = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]
combined_data ={}
for d in a:
    item  = d['item']
    amount = d['amount']
    if item in combined_data:
        combined_data[item]+=amount
    else:
        combined_data[item]=amount    
print("Combined_dictionary is:")
print(combined_data)        