# Unit Tests Suite
from stone import *

# Setting up
empty_bills = []
empty_names = []

bills = [{
    'name': 'Almoço self-service',
    'quantity': 0.757,
    'unit': 45.99
},
         {
    'name': 'Passeio de escuna',
    'quantity': 3,
    'unit': 80.00
},
         {
    'name': 'Diária do hotel',
    'quantity': 3,
    'unit': 337.99
}]

names = ['Tiago', 'Onofre', 'Araujo']

def test_expense_total_cost_function():
    assert(expenseTotalCost(bills[0]) == 34.81443)
    assert(expenseTotalCost(bills[1]) == 240.00)
    assert(expenseTotalCost(bills[2]) == 1013.97)

def test_empty_bills_list():
    assert(calculateBillParts(empty_bills, names) == {})

def test_empty_names_list():
    assert(calculateBillParts(bills, empty_names) == {})

def test_both_list_empties():
    assert(calculateBillParts(empty_bills, empty_names) == {})

def test_only_the_card_owner_as_debtor():
    assert(calculateBillParts([bills[0]], [names[0]]) == {'Tiago' : 'R$34.81'})

def test_split_for_three_with_remainder():
    expected_dict = {'Onofre': 'R$429.59', 'Araujo': 'R$429.60'}
    assert(calculateBillParts(bills, names) == expected_dict)

def test_split_for_three_without_remainder():
    no_remainder_bill = [{
        'name' : 'Passeio de barco',
        'quantity' : 3,
        'unit' : 30.00
    }]
    expected_dict = {'Onofre': 'R$30.00', 'Araujo': 'R$30.00'}
    assert(calculateBillParts(no_remainder_bill, names) == expected_dict)
