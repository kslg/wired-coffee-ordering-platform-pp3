import gspread
from google.oauth2.service_account import Credentials

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
    print("Welcome to the Wired Coffee B2B Ordering Plaform.\n")
    print("You can order one product at a time.\n")
    print(" **** Your Top 5 Products to Order: ****\n")
    print("Coffee Cup\n")
    print("Sip Lids\n")
    print("Coffee Beans\n")
    print("Suger Sticks\n")
    print("Drinks Stirrer\n")
    print("==============================\n")
    print("Please enter order details here:\n")
    user_name = input("Your Full Name:")
    branch_number = input("Enter your Branch Number:")
    product_sku = input("Enter the Product SKU:")
    product_qty = input("Enter the quantity:")
    payment_method = input("How would you like to pay? Choose either Bank Transfer or Pay on Account:")
    print("**** Order Preview: ****\n")
    print(f"Order Raised by {user_name}")
    print(f"Branch Number is {branch_number}")
    print(f"Product Name {product_sku}")
    print(f"Quantity {product_qty}")
    print(f"Payment Method {payment_method}")
    confirm_order = bool(input(f"Confirm Order? (y/n):"))

    validate_name_data(user_name)

def validate_name_data(user_name):
    """
    To allow letters only and a valid character length for the user's name
    """
    if user_name.isalpha() and (len(user_name) > 2 and len(user_name) <= 10):
        print("")
    else: 
        print("Error: Please enter valid name. We are not able to accept this order. Please try again.")





get_order_data()


