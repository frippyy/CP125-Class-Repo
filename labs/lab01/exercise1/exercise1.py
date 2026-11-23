# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km, budget):
    cost = (one_way_km / 10) * 2
    if cost <= budget:
        return True
    else:
        return False

print(is_budget_sufficient(100, 40))
print(is_budget_sufficient(100, 39))