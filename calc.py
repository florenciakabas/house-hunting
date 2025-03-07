# The intent of this branch is to create plot with multiple interest rates
# HOLAMOR !
import matplotlib.pyplot as plt
import ipdb

def calculate_monthly_payment(principal, annual_interest_rate, years):
    # Convert annual interest rate to monthly and decimal
    monthly_interest_rate = annual_interest_rate / 100 / 12
    # Total number of payments
    number_of_payments = years * 12

    # Calculate monthly payment using the formula
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    
    return monthly_payment

def calculate_amortization_schedule(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = years * 12
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    
    balance = principal
    interest_payments = []
    principal_payments = []
    balances = []

    for _ in range(number_of_payments):
        interest_payment = balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment

        interest_payments.append(interest_payment)
        principal_payments.append(principal_payment)
        balances.append(balance)

    return interest_payments, principal_payments, balances

def plot_amortization_schedule(interest_payments, principal_payments, balances):
    plt.figure(figsize=(10, 6))
    plt.plot(interest_payments, label='Interest Payment')
    plt.plot(principal_payments, label='Principal Payment')
    #plt.plot(balances, label='Remaining Balance')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.title('Amortization Schedule')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Input parameters
    #principal = float(input("Enter the loan amount (principal): "))
    #annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    #years = int(input("Enter the loan term (in years): "))
    
    principal = 500000
    annual_interest_rate = 5.0
    years= 30

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    
    # Output the result
    print(f"The estimated monthly payment is: ${monthly_payment:.2f}")

    # Calculate amortization schedule
    interest_payments, principal_payments, balances = calculate_amortization_schedule(principal, annual_interest_rate, years)
    
    # Plot amortization schedule
    plot_amortization_schedule(interest_payments, principal_payments, balances)

if __name__ == "__main__":
    main()