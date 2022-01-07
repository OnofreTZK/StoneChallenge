# expenseTotalCost return the total of the expense given  
def expenseTotalCost(expense):
    return expense['unit'] * expense['quantity']

# calculateBillParts return the debtors list
def calculateBillParts(bill, names):

    if len(bill) == 0 or len(names) == 0:
        return {}

    # Getting bill's total
    totalValue = 0
    for expense in bill:
        totalValue += int(expenseTotalCost(expense) * 100)

    print("Total: R${:.2f}".format(totalValue/100))

    totalForSplit = len(names)
    part = int(totalValue/totalForSplit)
    remainder = totalValue%totalForSplit

    debtors = {}
    for name in names:
        # I'll assume that the first name will be the card owner
        # only the debtors will be added in the dict
        # unless the only debtor is the card owner
        if name == names[0] and len(names) > 1:
            continue
        elif name == names[len(names)-1]:
            debtors.update({name: 'R${:.2f}'.format((part+remainder)/100)})
        else:
            debtors.update({name: 'R${:.2f}'.format(part/100)})

    return debtors


