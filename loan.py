loan_amt = float(input("enter amount: "))
years = int(input("enter years to pay: "))
month = years * 12
principal = loan_amt / month
rem_bal = loan_amt
total = 0

print("|Month\t|\tPayment\t\t|\tInterest\t|\tPrincipal\t|\tBalance\t\t|")
for x in range(1, month+1):
    rem_bal -= principal
    loan_interest = rem_bal * 0.00259 # or 0.00256 or 0.003
    monthly_pay = loan_interest + principal
    total += loan_interest
# print(x, round(monthly_pay, 2), round(loan_interest, 2), round(principal, 2), round(rem_bal, 2))
    print(f"|   {x}\t|\t {round(monthly_pay,2)}\t\t|\t   {round(loan_interest,2)}\t\t|\t{round(principal,2)}\t\t|\t{round(rem_bal,2)}\t\t|")
print(total)