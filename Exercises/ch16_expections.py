def get_number():
    while True:
        num = (input("Please enter a number: "))
        try: 
            return float(num)
        except:
            print("Not a number try again")
        
get_number()

