print("============================")
print("    Bank Loan Calculator    ")
print("============================")

def bank_loan_calculator():
    print("\n--- Bank Loan Calculator ---")
    loan = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter loan term in years: "))

    # Convert annual interest rate to monthly
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    # Monthly payment formula
    if monthly_rate == 0:
        monthly_payment = loan / num_payments
    else:
        monthly_payment = loan * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)

    total_paid = monthly_payment * num_payments
    total_interest = total_paid - loan

    print(f"\nLoan Amount: {loan:,.2f}")
    print(f"Annual Interest Rate: {annual_rate:.2f}%")
    print(f"Term: {years} years ({num_payments} months)")
    print(f"Monthly Payment: {monthly_payment:,.2f}")
    print(f"Total Paid: {total_paid:,.2f}")
    print(f"Total Interest: {total_interest:,.2f}")

bank_loan_calculator()