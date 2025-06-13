print("Please enter your password to check its strength and criteria")
password = input()

def check_pass_strength(password: str):
    pass_count = 0
    uppercaseval = False
    lowercaseval = False
    digitval = False
    specialchar = False
    dcount = 0
    scount = 0

    for char in password:
        pass_count += 1
        ascii_val = ord(char)  # Using unicode value of characters

        if 65 <= ascii_val <= 90:          # Uppercase A-Z
            uppercaseval = True
        elif 97 <= ascii_val <= 122:       # Lowercase a-z
            lowercaseval = True
        elif 48 <= ascii_val <= 57:        # Digits 0-9
            digitval = True
            dcount=dcount+1
        else:
            specialchar = True            # Any non-alphanumeric character 
            scount=scount+1

    # Output results
    if uppercaseval:
        print("Your password has uppercase letters.")
    if lowercaseval:
        print("Your password has lowercase letters.")
    if digitval:
        print(f"Your password has {dcount} digit(s).")
    if specialchar:
        print(f"Your password has {scount} special character(s).")
    if pass_count < 8:
        print(f"The length of the password should be at least eight characters or more, current length is {pass_count}.")

    #Criteria for pass strength
    if uppercaseval and lowercaseval and digitval and specialchar and pass_count >= 8 and dcount >=1 and scount >=1:
        return True
    else:
        return False
    
feedback = check_pass_strength(password)
if feedback == True:
    print("You have a strong password which has atleast eight characters both in upper and lowercase along with atleast one digit and special character.")    
else:
    print("You have weak password which does not meet critera of atleast Eight characters length in upper and lowercase along with atleast one digit and special character.")
    print("Feedback: Create a password atleast Eight characters of length along with one digit and special characters like @,#,$ etc to make it strong")



    
   


      


