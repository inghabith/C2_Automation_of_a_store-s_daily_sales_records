# Automation of a stores daily sales records
This code is for store owners, it allows them to store the sales of the day and have a resume of them showing names, amounts of products, amounts of sales and the total of the sales of all day.
The objective of this project is to apply fundamental programming concepts such as modular programming, use of dictionaries, and lists.

## Process and analysis
First, we analyzed the problem and the customer's needs. In this case, we took as a reference the owner of a typical store, who said that it was difficult to quickly capture and calculate sales information because he collected it by hand on paper.

Once the needs were identified, a flowchart was developed to organize and help understand the logic of what our system would be.
## Flowchart for the Sales Record Sistem.

<img width="560" height="1680" alt="Diagramas de flujo" src="https://github.com/user-attachments/assets/09bd0020-5da7-4ed2-ad28-c533ad577549" />

Subsequently, we proceeded to create the code that would help us make the client's requests functional.

## How it works
The code is based on the use of dictionaries and lists that help us collect the information that the user enters as the program requests it.

The code is divided into three main functions:
The first is the product request menu (sales_record). where the user is asked to enter the name, quantity, and value of the product sold. This information is stored in a dictionary, and the user is asked if they need to enter another sale. If so, the program requests the sale data again, and this new sale is also stored in the dictionary. If not, it moves on to the next part of the code.


The second is the sales summary (total_results). This part of the code is responsible for displaying all the data for all the products entered in an organized way (names, number of product sales) on the terminal. It also calculates the total amount sold per product and prints it in the same way on the terminal.


The third part calculates the total sales for the day. The program adds all the subtotals for the sales of each product to a new list, then adds them up and displays them to the user via the terminal.
