import gspread
from google.oauth2.service_account import Credentials
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Additional Constant Variable settings to help access the spreadsheet data.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('wired_coffee_branch_orders')

def get_order_data():
    """
    Get order data input from the user
    """

    sku = [2345,5432,3456,7654,5678]
    priceExvat = (2.79,2.99,484,7.95,3.49)
    product_name = ["16oz Coffee Cup", "90mm Coffee Cup Sip Lids", "Whole Bean Coffee", "White Sugar Sticks", "Wooden Drinks Stirrer"]
    productName=[]
    productPrice=[]

    d = {"16oz Coffee Cup": [2345, 2.79, 'Pack of 25'],
    "90mm Coffee Cup Sip Lids": [5432, 2.99, 'Pack of 25'],
    "Whole Bean Coffee": [3456, 484, '6 Bags'],
    "White Sugar Sticks": [7654, 7.95, 'Pack of 1000'],
    "Wooden Drinks Stirrer": [5678, 3.49, 'Pack of 1000']
    }
    while True:
        print("Welcome to the Wired Coffee B2B Ordering Plaform.\n")
        print("You can order one product at a time.\n")
        print(" **** Your Top 5 Products to Order: ****\n")

        print ("{:<25} {:<10} {:<15} {:<10}".format('Name','SKU','Price exVAT','Shipped'))
        for name, v in d.items():
            sku, price, ship = v
            print ("{:<25} {:<10} {:<15} {:<10}".format(name, sku, price, ship))
        print("\n")    
        print("==============================\n")
        print("Please enter order details here:\n")
        user_name = input("Your Full Name:")
        branch_number = input("Enter your Branch Number:")
        product_sku = input("Enter the Product SKU:")
        product_qty = int(input("Enter the quantity (1 to 100 max):"))
        payment_method = input("How would you like to pay? Choose either 'b' = Bank Transfer or 'p' = Pay on Account:")
        date_stamp_preview = (f"Order Date: {datetime.datetime.now():%d-%m-%Y}")
        date_stamp_file = (f"{datetime.datetime.now():%d-%m-%Y}")
        print("\n")
        print("**** Order Preview: ****\n")
        print(date_stamp_preview)
        print(f"Order Raised by {user_name}")
        print(f"Branch Number is {branch_number}")
        print(f"Product SKU: {product_sku}")

        if product_sku =='2345':
            productName.append(product_name[0])
            productPrice.append(priceExvat[0]*product_qty)
        elif product_sku =='5432':
            productName.append(product_name[1])
            productPrice.append(priceExvat[1]*product_qty)
        elif product_sku =='3456':
            productName.append(product_name[2])
            productPrice.append(priceExvat[2]*product_qty)            
        elif product_sku =='7654':
            productName.append(product_name[3])
            productPrice.append(priceExvat[3]*product_qty)
        elif product_sku =='5678':
            productName.append(product_name[4])
            productPrice.append(priceExvat[4]*product_qty)
            
        print("Product Name:", *productName)
        print("Total Price exVAT:", *productPrice)
        print("Quantity:", (product_qty))
        print("Payment Method:", payment_method)
        confirm_order = (input(f"Confirm Order? (y/n):"))
        
        validate_name_data(user_name)
        validate_branch_number_data(branch_number)
        validate_product_sku_data(product_sku)
        validate_product_qty_data(product_qty)
        validate_payment_method_data(payment_method)

        order_data = (date_stamp_file, user_name, branch_number, product_sku, productName, productPrice, product_qty, payment_method)
        
        if confirm_order != 'y':
            print("Your order has been cancelled. You can place a new order below:\n")
            continue

        if validate_name_data(user_name):
            print("Data is valid")
        elif validate_branch_number_data(branch_number):
            print("Data is valid")
        elif validate_product_sku_data(product_sku):
            print("Data is valid")
        elif validate_product_qty_data(product_qty):
            print("Data is valid")
        elif validate_payment_method_data(payment_method):
            print("Data is valid")
        break
    return order_data

def validate_name_data(user_name):
    """
    To allow letters only and a valid character length for the user's name
    """
    if user_name.isalpha() and (len(user_name) > 2 and len(user_name) <= 20):
        print("")
    else: 
        print("Error: Please enter valid name. We are not able to accept this order. Please try again.")

def validate_branch_number_data(branch_number):
    """
    To allow numbers only and max four numbers long.
    """
    if branch_number.isdigit() and (len(branch_number) == 4):
        print()
    else:
        print("Error: Your Branch number is not valid and should be four numbers only. We are not able to accept this order. Please check and try again. ")

def validate_payment_method_data(payment_method):
    """
    To only allow two values to pass for payment method user input.
    """
    if payment_method == "b":
        print()
    elif payment_method == "p":
        print()
    else:
        print("Error: Payment option not valid. Please choose either 'b' for Bank Transfer or 'p' for Pay on Account.")

def validate_product_sku_data(product_sku):
    """
    To allow numbers only and max four numbers long.
    """
    if product_sku == "2345":
        print()
    elif product_sku == "5432":
        print()
    elif product_sku == "3456":
        print()
    elif product_sku == "7654":
        print()
    elif product_sku == "5678":
        print()
    else:
        print("Error: You must choose from one of the 4 product skus only. We are not able to accept this order. Please check and try again. ")

def validate_product_qty_data(product_qty):
    """
    To allow integers only between 1 to 100.
    """
    try:
        if (int(product_qty) >100):
            raise ValueError(
                f"Enter Quantity 1 to 100."
            )
        elif (int(product_qty) <1):
            raise ValueError(
                f"Enter Quantity 1 to 100."
            )
    except ValueError as e:
        print(f"Invalid Data: {e} We are not able to accept this order. Please check and try again.\n")
        return False

    return True

final_order = get_order_data()
print(final_order)
