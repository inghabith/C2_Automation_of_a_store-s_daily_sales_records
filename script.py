#The user is asked to enter the sale information
def sales_record(products):
    add = "yes"

    while add == "yes":
        print()
        print("                   ----NEW PRODUCT----")
        print()

        #Here the sales information is requested from the user.
        product_name = input("Enter the product name:               ")
        product_quantity = int(input("Enter the quantity of the product:     "))
        product_price = int(input("Enter the unit price of the product:   "))

        #This dictionary stores the sales data entered by the user.
        products_dictionary = {
            "name": product_name,
            "quantity": product_quantity,
            "price": product_price
        }
        #
        products.append(products_dictionary) #----> This method adds the information of all the sales to the ‘products’ list
        print("-"*60)
        add = input("Would you like to enter another sale? yes/no: ") #---> This line of the code controls the loop, it asks the user if they want to register another sale. If the answer is yes, the program requests new data and stores it in the dictionary; if not, it continues with the code
    
#Sales summary print
def total_results(products, total_a):

    print("="*60)
    print("                DAILY SALES SUMMARY")
    #Here a variable iterates through the list with the sales values and prints them to the console.
    for sell in products:
        print("Product:                   ", sell["name"])
        print("Unite price:              $", sell["price"])
        print("Amount sold today:         ", sell["quantity"], "units")

        #It performs a brief multiplication to calculate the subtotal of the sale for each product and the values are added to a new list called total_a
        a = (sell["quantity"] * sell["price"])
        total_a.append(a)
        print("Subtotal sold by product: $", a)
        
        print("="*60)

        

# TOTAL COLLECTED TODAY
def calculator(total_a):
    #Here the total_a list is used to sum all the subtotals it contains, which gives the total sales for the day. The result is then printed to the console. 💻
    print("               TOTAL COLLECTED TODAY: $", sum(total_a))
    print("="*60)



"""This project is a command-line application that allows store owners to store the sales of the day and have
a resume of them, showing names, amounts of products, amounts of sales, and the total of all daily sales.
This project is a tool built for small store owners who need a fast and organized way to record their daily sales.
The objective of this project is to apply fundamental programming concepts such as modular programming, use of dictionaries, and lists."""""
