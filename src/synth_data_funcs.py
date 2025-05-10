# Beginning of "synth_data_funcs.py"
#######################################################################
# A collection of functions and dictonaries to create synthetic data
# for the personal finance app.
#######################################################################
# Import necessary libraries and modules
import pandas as pd
import random
import time
from datetime import datetime, timedelta

# VARIABLES
desc_and_cat = {
    "McBob's": "eating out",
    "Star Coffee": "eating out",
    "Applebee's": "restaurant",
    "Circuit City": "electronics",
    "Mezcal": "restaurant",
    "DoubleTree": "hotel",
    "Total Wine & More": "drinks",
    "Pandora Jewelry": "gift",
    "Tuber": "rideshare",
    "California Pizza Kitchen": "restaurant",
    "Pickup": "rideshare",
    "Dohls": "apparel",
    "Dubber's Oldtown Bar & Grill": "drinks",
    "East of Eden": "meds",
    "Lighthouse Publications": "miscellaneous",
    "Nob Hill Foods": "groceries",
    "Some Barbershop": "haircut",
    "Vans": "apparel",
    "Saint Joe's Improv": "entertainment",
    "TicketNet": "entertainment",
    "Webflix": "subscription",
    "Clown Liquors": "drinks",
    "7-Eleven": "groceries",
    "The Carrotcake Factory": "restaurant",
    "Local Watering Hole": "drinks",
    "Wendal's": "eating out",
    "Shell": "fuel",
    "Checkmark": "fuel",
    "HorsePower": "fuel",
    "Racing Fuel": "fuel",
    "Open Road": "fuel",
    "Town Mart": "miscellaneous",
    "Fancy Liquor": "drinks",
    "Urban Pantry": "groceries",
    "City Garden Grocers": "groceries",
    "The Daily Harvest": "groceries",
    "Sunrise Supermarket": "groceries",
    "The Corner Grocer": "groceries",
    "CJ's Restaurant": "restaurant",
    "California Pizza Kitchen": "restaurant",
    "El Frijol Coffee Shop": "eating out",
    "CVS/pharmacy": "groceries",
    "Quick Stop": "miscellaneous",
    "MYO": "eating out",
    "Clay Markey": "drinks",
    "Amazon Prime Membership": "subscription",
    "Flamming Fajitas": "restaurant",
    "Jack in the Box": "eating out",
    "The Otter's Den": "drinks",
    "Circle K": "fuel",
    "Microsoft": "subscription",
    "In-N-Out": "eating out",
    "Southwest Airlines": "travel",
    "UA Outlet": "apparel",
    "Polo Ralph Lauren": "apparel",
    "Relative - Venmo": "miscellaneous"
}

# A dictionary that contains necessities like rent and debts.
necessities = {
    'Description': [
        "The Property Management Company",
        "US Dept. of Education",
        "Some Auto Insurance",
        "Workout World",
        "Coparent - Venmo"
    ],
    'Category': [
        "rent",
        "student loans",
        "auto insurance",
        "gym membership",
        "child support"
    ]
}

# FUNCTIONS
# Random date function
def random_date(
        start_date,
        end_date
):
    """
    Generate a random datetime object between 2 dates.
    
    Args:
        start_date: Start date as a datetime object.
        end_date: End date as a datetime object.
    
    Returns:
        A randome datetime object between start_date and end_date.
    """
    start_time = time.mktime(
        datetime.strptime(start_date, "%Y-%m-%d").timetuple()
    )
    end_time = time.mktime(
        datetime.strptime(end_date, "%Y-%m-%d").timetuple()
    )
    random_timestamp = random.uniform(start_time, end_time)
    return datetime.fromtimestamp(random_timestamp)

# Function to pick random key-value pair from dictionary
def pick_random_item(data):
    """
    Pick a random key-value pair (item) from a dictionary.

    Args:
        data (dict): The dictionary to pick from.

    Returns:
        A tuple containing the randomly picked key-value pair, or None if the dictionary is empty.   
    """
    if not data:
        return None
    return random.choice(list(data.items()))

def date_day_df(
        start_date,
        end_date,
        num_data_pts):
    """
    Takes a date range and number of records to create a dataframe of arbitrary size for synthetic data.

    Args:
        start_date (str): Beginning of date interval in YYYY-MM-DD format.

        end_date (str): End of date interval in YYYY-MM-DD format.
        
        num_data_pts (int): Number of records for the dataframe.

    Returns:
        dataframe
    """
    date_list = [] # Initiate an empty date list
    day_list = [] # List of days
    for x in range(num_data_pts):
        y = random_date(start_date, end_date)
        date_list.append(y.strftime("%Y-%m-%d"))
        day_list.append(y.strftime("%A"))

    s1 = pd.Series(date_list, name='Date')
    s2 = pd.Series(day_list, name='Day')

    return pd.concat([s1, s2], axis=1)

def create_desc_cat_df(
        num_of_records: int,
        trx_list: dict        
) -> pd.DataFrame:
    """
    Given a integer to represent the number of rows, will randomly pick elements from a dictionary.count

    Args:
        num_of_records (int): Number of rows for the dataframe.

        trx_list (dict): A collection of descriptions and categories for transactions.

    Returns:
        pd.DataFrame
    """
    desc_list = [] # Initiate an empty description list
    cat_list = []
    for x in range(num_of_records):
        y = pick_random_item(desc_and_cat)
        desc_list.append(y[0])
        cat_list.append(y[1])
    # Join two lists
    s1 = pd.Series(desc_list, name='Description')
    s2 = pd.Series(cat_list, name='Category')
    
    return pd.concat([s1, s2], axis=1)

def random_amount(
        low,
        high,
        decimal_nums=2
    ):
    """
    Pick a pseudo random number from a given range that is suppose to represent a typical amount spent per given category and allowed variance.

    Args:
        low (float): The minimum considered for this category for a given transaction.
        
        high (float): The maximum for this category per transaction.

        decimal_nums (int): Default at 2. Trying to represent real-world transactions.

    Returns:
        A float number tuple containing the randomly picked key-value pair, or None if the dictionary is empty.   
    """
    return(round(random.uniform(low, high), decimal_nums))

def amount(value):
    """
    Adds a new column with numerics representing money spent per record given another column, i.e. the category.append

    Args:
        value (str): The string describing the category.append

    Returns:
        A new column with numeric amounts representing money spent.
    
    """
    # Haircut
    if value == 'haircut':
        return random_amount(45, 70)
    # Eating out
    elif value == 'eating out':
        return random_amount(6, 40)
    # Miscellaneous
    elif value == 'miscellaneous':
        return random_amount(15, 120)
    # Groceries
    elif value == 'groceries':
        return random_amount(20, 80)
    # Drinks
    elif value == 'drinks':
        return random_amount(25, 125)
    # Meds
    elif value == 'meds':
        return random_amount(20, 50)
    # Student Loans
    elif value == 'student loans':
        return random_amount(120, 240)
    # Apparel
    elif value == 'apparel':
        return random_amount(30, 120)
    # Rideshare
    elif value == 'rideshare':
        return random_amount(15, 35)
    # Subscription
    elif value == 'subscription':
            return random_amount(10, 15)
    # Fuel
    elif value == 'fuel':
            return random_amount(45, 65)
    # Electronics
    elif value == 'electronics':
            return random_amount(35, 120)
    # Restaurant
    elif value == 'restaurant':
            return random_amount(60, 150)
    # Entertainment
    elif value == 'entertainment':
        return random_amount(30, 200)
    # Gifts
    elif value == 'gift':
        return random_amount(20, 120)
    # Hotels
    elif value == 'hotel':
        return random_amount(120, 300)
    # Travels
    elif value == 'travel':
        return random_amount(150, 250)
    # Rent. Googled average rent in CA for 1-bd apartment.
    elif value == 'rent':
        return random_amount(1800, 2300)
    # Auto Insurance
    elif value == 'auto insurance':
        return random_amount(60, 70)
    # Gym Membership
    elif value == 'gym membership':
        return random_amount(50, 50)
    # Child Support
    elif value == 'child support':
        return random_amount(300, 400)


# End of "synth_data_funcs.py"