age = int(input("What is your age? "))
is_employed = bool(input("Are you employed? "))
credit_score = int(input("What is your credit score? "))
annual_income = float(input("What is your annual income? "))
has_collateral = bool(input("Do you have collateral? (True or False) "))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Please proceed.")
    if credit_score >= 750:
        print("You have a high credit score.")
        if  annual_income >= 100000:
            print("You have a high annual salary.")
            base_rate = 4.5
            print("Your base rate is",base_rate)
        else:
            base_rate = 5.0
            print("Your base rate is",base_rate)
    elif 600 <= credit_score < 750:
        print("Your credit score is less than 750.")
        if has_collateral == "True":
            base_rate = 7.0
            print("Your base rate is",base_rate)
        elif annual_income <= 40000:
            base_rate = 9.5
            print("Your base rate is",base_rate)
        else:
            base_rate = 8.0
            print("Your base rate is",base_rate)
    elif credit_score < 600:
            print("Rejected: Credit score too low.")
    else:
        print("Rejected: Fails baseline criteria.")