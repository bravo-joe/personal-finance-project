# Beginning of "test_process_day_column.py"
import pandas as pd
from pandas.testing import assert_frame_equal
import sys
sys.path.append("../src")
from process_day_column import process_day_col

# The test dataframe
test_dataframe = {
    'date': [
        '2023-12-25',
        '2023-12-25',
        '2023-12-26',
        '2023-12-26',
        '2023-12-27',
        '2023-12-27',
        '2023-12-28',
        '2023-12-28',
        '2023-12-29',
        '2023-12-29',
        '2023-12-30',
        '2023-12-30',
        '2023-12-31',
        '2023-12-31'
    ],
    'day': [
        'MONDAY',
        'MonDay',
        'tuesday',
        'tuESDAY',
        'WEDNESDAY',
        'WEDnesday',
        'THursDAY',
        'thURSday',
        'friday',
        'FrIdAy',
        'sAtUrDaY',
        'SaTuRdAy',
        'Sunday',
        'SUNDAY'
    ],
    'description': [
        'Grocery Store A',
        'Grocery Store B',
        'Liquor Store A',
        'Liquor Store B',
        'Streaming Service A',
        'Streaming Service B',
        'Student Loan Provider A',
        'Student Loan Provider B',
        'Restaurant A',
        'Restaurant B',
        'Gas Station A',
        'Gas Station B',
        'Cafe A',
        'Cafe A'
    ],
    'category': [
        'groceries',
        'groceries',
        'drinks',
        'drinks',
        'subscription',
        'subscription',
        'student loans',
        'student loans',
        'restaurant',
        'restaurant',
        'fuel',
        'fuel',
        'eating out',
        'eating out'
    ],
    'amount($)': [
        1.00,
        2.00,
        3.00,
        4.00,
        5.00,
        6.00,
        7.00,
        8.00,
        9.00,
        10.00,
        11.00,
        12.00,
        13.00,
        14.00
    ]
}
test_df = pd.DataFrame(test_dataframe)

# Expected dataframe
expected_dataframe = {
    'date': [
        '2023-12-25',
        '2023-12-25',
        '2023-12-26',
        '2023-12-26',
        '2023-12-27',
        '2023-12-27',
        '2023-12-28',
        '2023-12-28',
        '2023-12-29',
        '2023-12-29',
        '2023-12-30',
        '2023-12-30',
        '2023-12-31',
        '2023-12-31'
    ],
    'day': [
        'monday',
        'monday',
        'tuesday',
        'tuesday',
        'wednesday',
        'wednesday',
        'thursday',
        'thursday',
        'friday',
        'friday',
        'saturday',
        'saturday',
        'sunday',
        'sunday'
    ],
    'description': [
        'Grocery Store A',
        'Grocery Store B',
        'Liquor Store A',
        'Liquor Store B',
        'Streaming Service A',
        'Streaming Service B',
        'Student Loan Provider A',
        'Student Loan Provider B',
        'Restaurant A',
        'Restaurant B',
        'Gas Station A',
        'Gas Station B',
        'Cafe A',
        'Cafe A'
    ],
    'category': [
        'groceries',
        'groceries',
        'drinks',
        'drinks',
        'subscription',
        'subscription',
        'student loans',
        'student loans',
        'restaurant',
        'restaurant',
        'fuel',
        'fuel',
        'eating out',
        'eating out'
    ],
    'amount($)': [
        1.00,
        2.00,
        3.00,
        4.00,
        5.00,
        6.00,
        7.00,
        8.00,
        9.00,
        10.00,
        11.00,
        12.00,
        13.00,
        14.00
    ]
}
expected_df = pd.DataFrame(expected_dataframe)

# Now, the testing function
def test_process_day_col():
    assert_frame_equal(process_day_col(test_df), expected_df) 

# End of "test_process_day_column.py"