def sales_record(products):
    add = "yes"

    while add == "yes":
        print()
        print("                   ----NEW PRODUCT----")
        print()
        product_name = input("Enter the product name:               ")
        product_quantity = int(input("Enter the quantity of the product:     "))
        product_price = int(input("Enter the unit price of the product:   "))

        products_dictionary = {
            "name": product_name,
            "quantity": product_quantity,
            "price": product_price
        }

        products.append(products_dictionary)
        print("-"*60)
        add = input("Would you like to enter another sale? yes/no: ")
    

def total_results(products, total_a):
    # SALES SUMMARY
    print("="*60)
    print("                DAILY SALES SUMMARY")

    for sell in products:
        print("Product:                   ", sell["name"])
        print("Unite price:              $", sell["price"])
        print("Amount sold today:         ", sell["quantity"], "units")

        a = (sell["quantity"] * sell["price"])
        print("Subtotal sold by product: $", a)

        print("="*60)

        total_a.append(a)


def calculator(total_a):
    # TOTAL COLLECTED TODAY
    print("               TOTAL COLLECTED TODAY: $", sum(total_a))
    print("="*60)
