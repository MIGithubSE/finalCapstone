# Capstone Project
import math

# Using simple interest function to calculate the simple interest rate
def simple_interest(amount_to_invest, interest_rate, years_to_invest): # calculate_simple_interest takes 3 arguments p, r and t

    r = (interest_rate / 100)
    p = amount_to_invest
    t = years_to_invest
    total_amount = p * (1 + r * t)  # calculating the total_amount for simple interest A = p * (1 + r * t) 
    return total_amount

def compound_interest(amount_to_invest, interest_rate, years_to_invest): # calculate_compound_interest takes 3 arguments p, r and t
    # Function to calculate compound interest
    r = (interest_rate / 100)
    total_amount = amount_to_invest * math.pow((1 + r), years_to_invest) # calculating the total_amount = A = p * (1 + r * t)
    return total_amount

# calculate_bond_repayment takes 3 arguments house_present_value, interest_rate, monthly_repayment
def calculate_bond_repayment(house_present_value, interest_rate, months): 

    # Function to calculate bond repayment
    monthly_interest_rate = (interest_rate / 100) / 12
    bond_repayment = (monthly_interest_rate * house_present_value) / (1 - (1 + monthly_interest_rate)**(-months)) # calculating the repayment
    return bond_repayment

def interest_calculator():

    ''' Main function to manage user input and call the appropriate calculator function
        User will be able to choose which calculation he/she wants to perform:") '''

    print("  - Investment: Calculate the amount of interest you'll earn on your investment")
    print("  - Bond: Calculate the amount you'll have to pay on a home loan")

    # Get input from the user and convert it to lowercase to avoid case-insensitivity errors
    user_calculator_choice = input("Please Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if user_calculator_choice == "investment":
        # Using input method to get user input for investment
        amount_to_invest = float(input("Please enter the amount of money you are depositing: ")) # the initial amount the user is willing to invest
        interest_rate    = float(input(" Please enter the interest rate (as a percentage): ")) # Only the number of the interest rate should be entered 
        years_to_invest  = int(input("Enter the number of years you plan on investing: "))
        
        # Using input method to get user input for the type of interest (simple or compound)
        interest_type = input("Do you want 'Simple' or 'Compound' interest? ").lower() # using the lower() to convert the input from the user to lower case 

        # check and validate the input from the user and calculate the appropriate interest (Simple or Compound)
        if interest_type   == 'simple':
            total_amount   = simple_interest(amount_to_invest, interest_rate, years_to_invest) # calculate the simple interest using the following formula A = p * (1 + r * t)
        elif interest_type == 'compound':
            total_amount   = compound_interest(amount_to_invest, interest_rate, years_to_invest) # # calculate the compund interest using the following formula A = P * math.pow((1+r),t)
        else:
            print("Invalid choice for interest type. Please reenter either 'simple' or 'compound'.") # if the user input is not Simple neither Compound
            return

        print(f"\nThe total amount after {years_to_invest} years of {interest_type} interest is: R{total_amount:.2f}") # This is a placeholder for the value of the variable total_amount.

    elif user_calculator_choice == 'bond':
        # Get user input for bond
        house_present_value = float(input("Enter the present value of the house: "))       # The present value of the house is taken from the user and converted to Float
        interest_rate       = float(input("Enter the annual interest rate (as a percentage): ")) # The interest_rate is taken from the user and converted to Float
        monthly_repayment   = int(input("Enter the number of months to repay the bond: "))   # interest_rate

        # Calculate bond repayment
        bond_repayment = calculate_bond_repayment(house_present_value, interest_rate, monthly_repayment)
        print(f"\nThe monthly bond repayment amount is: R{bond_repayment:.2f}") # This is a placeholder for the variable bond_repayment and .2f is a formatting specifier. 

    else:
        print("Invalid input. Please enter either 'investment' or 'bond'.") # If a user enters anything other than investment or Bond it will return an error message

# Run the interest calculator
interest_calculator()