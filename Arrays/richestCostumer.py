def richestCostumer(accounts):
    actual_richest = 0
    for bank in accounts:
        if sum(bank) >= actual_richest:
            actual_richest = sum(bank)
    return actual_richest


accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(richestCostumer(accounts))