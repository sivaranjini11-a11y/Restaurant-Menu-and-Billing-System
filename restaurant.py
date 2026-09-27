import mysql.connector

# Connecting Python with MySQL
mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="restaurant"
)

mycursor = mycon.cursor()


# Function to display menu
def display_menu():
    print("\n========== RESTAURANT MENU ==========")

    mycursor.execute("SELECT * FROM menu")
    data = mycursor.fetchall()

    print("Item No.\tItem Name\t\tPrice")
    print("---------------------------------------")

    for row in data:
        print(row[0], "\t\t", row[1], "\t\t", row[2])


# Function to place order
def place_order():

    customer_name = input("\nEnter customer name: ")

    grand_total = 0

    while True:

        display_menu()

        item_no = int(input("\nEnter item number (0 to finish): "))

        if item_no == 0:
            break

        mycursor.execute(
            "SELECT item_name, price FROM menu WHERE item_no = %s",
            (item_no,)
        )

        data = mycursor.fetchone()

        if data is None:
            print("Invalid item number!")
            continue

        item_name = data[0]
        price = data[1]

        quantity = int(input("Enter quantity: "))

        total = price * quantity

        grand_total = grand_total + total

        # Store order in database
        sql = """INSERT INTO orders
                 (customer_name, item_name, quantity, price, total)
                 VALUES (%s, %s, %s, %s, %s)"""

        values = (
            customer_name,
            item_name,
            quantity,
            price,
            total
        )

        mycursor.execute(sql, values)
        mycon.commit()

        print("\nItem added successfully!")
        print("Item:", item_name)
        print("Quantity:", quantity)
        print("Total:", total)

    if grand_total > 0:

        print("\n================================")
        print("           BILL")
        print("================================")
        print("Customer Name:", customer_name)
        print("Grand Total:", grand_total)
        print("================================")
        print("Thank you for visiting!")
    else:
        print("\nNo items were ordered.")


# Function to display past orders
def past_orders():

    print("\n========== PAST ORDERS ==========")

    mycursor.execute("SELECT * FROM orders")
    data = mycursor.fetchall()

    if data:
        print("Order ID\tCustomer\tItem\t\tQuantity\tPrice\tTotal")
        print("---------------------------------------------------------------")

        for row in data:
            print(row[0], "\t\t", row[1], "\t", row[2],
                  "\t", row[3], "\t\t", row[4], "\t", row[5])
    else:
        print("No past orders found.")


# Main program
while True:

    print("\n\n========== RESTAURANT BILLING SYSTEM ==========")
    print("1. Display Menu")
    print("2. Place Order")
    print("3. View Past Orders")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        display_menu()

    elif choice == 2:
        place_order()

    elif choice == 3:
        past_orders()

    elif choice == 4:
        print("\nThank you! Visit again.")
        break

    else:
        print("\nInvalid choice!")

mycon.close()
