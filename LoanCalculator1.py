Loan = []

def Calculate_Loan(Principal, Annual_Interest, Loan_Tenure):
    Monthly_Interest = (Annual_Interest / 12 / 100)
    Num_Months = Loan_Tenure * 12
    Monthly_Payment_Amount = Principal * (Monthly_Interest / (1 - (1 + Monthly_Interest)**(-Num_Months)))
    Total_Payment_Amount =  Monthly_Payment_Amount * Num_Months
    return Monthly_Payment_Amount, Total_Payment_Amount

def Calculate_DSR(Monthly_Income, Monthly_Financial_Commitment):
    DSR = Monthly_Financial_Commitment / Monthly_Income
    return DSR

def Add_Loan(Principal, Annual_Interest, Loan_Tenure, Monthly_Income, Monthly_Financial_Commitment):
    Monthly_Payment_Amount, Total_Payment_Amount = Calculate_Loan(Principal, Annual_Interest, Loan_Tenure)
    DSR = Calculate_DSR(Monthly_Income, Monthly_Financial_Commitment)

    Housing_Loan = {
        "Principal" : Principal,
        "Annual Interest" : Annual_Interest,
        "Loan Tenure" : Loan_Tenure,
        "Monthly Payment Amount" : Monthly_Payment_Amount,
        "Total Payment Amount" : Total_Payment_Amount,
        "Monthly Financial Commitment" : Monthly_Financial_Commitment,
        "DSR" : DSR
    }
    Loan.append(Housing_Loan)

while True:
    print("\nHousing Loan Calculator & DSR Calculator")
    print("[1] Calculate New Loan")
    print("[2] View Previous Calculations")
    print("[3] Quit Program")

    Selection = input("Please Select 1/2/3: ")

    if Selection == "1":
        Principal = float(input("Enter Principal Amount (RM) : "))
        Annual_Interest = float(input("Enter Annual Interest Rate (%) : "))
        Loan_Tenure = float(input("Enter Loan Tenure (Yrs) : "))
        Monthly_Income = float(input("Enter Monthly Income (RM) : "))
        Monthly_Financial_Commmitment = float(input("Enter Monthly Financial Commitment (RM) : "))
        
        Add_Loan(Principal, Annual_Interest, Loan_Tenure, Monthly_Income, Monthly_Financial_Commmitment)
        print("\nCalculation Succesful")
        print(f"Monthly Installment : {Loan[-1]['Monthly Payment Amount']:.2f}")
        print(f"Total Amount : {Loan[-1]['Total Payment Amount']:.2f}")
        print(f"DSR :  {Loan[-1]["DSR"]:.2f}")

        if Loan[-1]['DSR'] < 0.7:
            print("Loan Application is Valid!")
        else:
            print("Loan Application is Invalid!")
    
    elif Selection == "2":
        print("\nCalculations History :")
        for index, Housing_Loan in enumerate(Loan):
            print(f"\nCalculations {index + 1}")
            print(f"Principal : {Housing_Loan["Principal"]}")
            print(f"Annual Interest Rate : {Housing_Loan["Annual Interest"]}")
            print(f"Loan Tenure : {Housing_Loan["Loan Tenure"]}")
            print(f"Monthly Payment Amount : {Housing_Loan["Monthly Payment Amount"]:.2f}")
            print(f"Total Payment Amount : {Housing_Loan["Total Payment Amount"]:.2f}")
            print(f"DSR : {Housing_Loan["DSR"]:.2f}")

    elif Selection == "3":
        print("Program Closed")
        break

    else:
        print("\nError. Please Select 1, 2 or 3.")

# MUHAMMAD AIMAN ZULHAKIM BIN MOHD ZAKILAH, 292042