# Rent Calculator

def calculate_rent():
    print("📊 Welcome to the Rent Calculator!\n")

    try:
        rent_per_month = float(input("Enter monthly rent amount (in ₹): "))
        months = int(input("Enter number of months: "))
        additional_charges = float(input("Enter any additional monthly charges (in ₹): "))
        
        total_monthly = rent_per_month + additional_charges
        total_rent = total_monthly * months

        print("\n--- Rent Summary ---")
        print(f"Monthly Rent: ₹{rent_per_month:.2f}")
        print(f"Additional Monthly Charges: ₹{additional_charges:.2f}")
        print(f"Total Monthly Payment: ₹{total_monthly:.2f}")
        print(f"Duration: {months} month(s)")
        print(f"Total Rent for {months} months: ₹{total_rent:.2f}")

    except ValueError:
        print("❌ Please enter valid numeric inputs.")

if __name__ == "__main__":
    calculate_rent()
