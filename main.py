from script import sales_record, total_results, calculator
total_a = []
products = []

products = sales_record(products)

total_result = total_results(products, total_a)

total_a = total_result[1]
products = total_result[0]

calculator(total_a)
