import json
from datetime import date
import re
import random
import time

try:
    with open('bank_data.json','r') as f:
        bank_data=json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    bank_data={}


def main():
    print('Open bank account: 1\nCreate net banking profile: 2\nLogin: 3')
    ask=int(input('Choice: '))
    if ask==1:
        register()
    elif ask==2:
        net_banking()
    elif ask==3:
        login()
    else:
        print('Invalid choice')




















def net_banking():

    while True:
        email=input('Enter your email: ').strip()
        user=None
        for acc_no, details in bank_data.items():
            if details['email'] == email:
                user=details
                break

        if user is None:
            print('Email not found. Try again.')
            continue
        password=valid_password()
        while True:
            password_test=input("Enter password again: ").strip()
            if password!=password_test:
                print('Password not matched\nTry again')
            else:
                user['password']=password
                print('Net banking profile created successfully')
                print('Generating bank pin...')
                banking_pin=random.randint(1000,9999)
                user['pin']=banking_pin
                print(f'Your Banking pin: {banking_pin}')
                data_save()
                return


def login():
    while True:
        print('Login')
        while True:
            phone_no_inp=input('Enter your phone number: ').strip()
            user=None
            for acc_no, details in bank_data.items():
                if details['phone_number']==phone_no_inp:
                    user=details
                    break
            password_check(user,acc_no)
            if user is None:
                print('Phone number not found. Try again.')
                continue

def password_check(user,acc_no):
    while True:
        password_inp = input('Password: ')
        if password_inp!=user['password']:
            print('Invalid password')
            continue
        else:
            print('ACCESS ALLOWED')
            logged_in(acc_no)
            return

def logged_in(acc_no):
    while True:
        print('''====== ACCOUNT INFO ======''')
        print(f'Account number: {acc_no}')
        print('Withdraw: 1\nDeposit: 2\nTransfer: 3\nShow balance: 4')
        choice=input('Enter your choice: ').strip()
        if choice=='1':
            ...
        elif choice=='2':
            ...
        elif choice=='3':
            transfer(acc_no)
        elif choice=='4':
            print(bank_data[acc_no]['balance'])
        else:
            print('Invalid choice')
            continue



    
    



    

def withdraw(user, acc_no):
    amount = int(input("Enter the amount: "))
    while amount <= 0:
        amount = int(input("Enter valid amount: "))
    if amount > user["balance"]:
        print("INSUFFICIENT BALANCE")
        return
    user["balance"] -= amount
    bank_data[acc_no]["balance"] = user["balance"]
    print("Withdrawal successful")
    print("Remaining balance:", user["balance"])
    data_save()

def deposit(user, acc_no):
    amount = int(input("ENTER AMOUNT: "))

    while amount <= 0:
        amount = int(input("ENTER VALID AMOUNT: "))    
    if "balance" not in user:
        user["balance"] = 0
    user["balance"] += amount
    print("AMOUNT SUCCESSFULLY ADDED!")
    print("CURRENT BALANCE:", user["balance"])

    data_save()



    
    
    
def transfer(acc_no):
    to_acc_no=input('Enter receiver\'s account number: ').strip()
    try:
        amount=int(input("Enter amount: $").strip())
    except ValueError:
        print("Invalid amount")
        return
    if bank_data[acc_no]['balance']<amount:
        print("Insufficient balance")
        return
    ask_pin=int(input('Enter your pin: ').strip())
    if ask_pin!=bank_data[to_acc_no]['pin']:
        print('Incorrect pin')
    bank_data[acc_no]['balance']-=amount
    if to_acc_no in bank_data:
        bank_data[to_acc_no]['balance']+=amount
    else:
        pass
    print('Transfer complete')




















def register():
    print('Register')
    name=name_input()
    dob=valid_dob().isoformat()
    email=valid_email()
    phone_number=number()
    address_=address()
    income_=income()
    occupation=input('Enter occupation: ').strip()
    account_no=get_account_no()
    bank_data[account_no] = {
        'name': name,
        'dob': dob,
        'email': email,
        'phone_number': phone_number,
        'address': address_,
        'income': income_,
        'occupation': occupation
    }

    data_save()



def valid_password():
    while True:
        problems=[]
        code=input('Create password: ').strip()
        if len(code)!=8:
            problems.append('8 characters')
        if ' ' in code:
            problems.append('not contain spaces')
        if not any(ch.isalpha() for ch in code):
            problems.append('Alphabets')
        if not any(ch.isupper() for ch in code):
            problems.append('Uppercase alphabets')
        if not any(ch.isdigit() for ch in code):
            problems.append('Digits')
        if not any(ch in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~' for ch in code):
            problems.append('Special characters')
        if problems:
            print('Password must have '+', '.join(problems))
            continue
        else:
            return code





















































def number():
    while True:
        phone_pattern=r'^\+\d{1,3}\d{6,14}$'
        phone_number=input('Enter a Phone number: ')
        if re.fullmatch(phone_pattern,phone_number):
            return phone_number
        else:
            print('Invalid Phone Number')
            continue

def valid_dob():
    while True:
        try:
            date_today=date.today()
            dob=input("Enter your date of birth: mm/dd/yy ").split('/')
            month=int(dob[0])
            day=int(dob[1])
            year=int(dob[2])

            if year<=date.today().year%100:
                year+=2000
            else:
                year+=1900

            birth_date=date(year,month,day)

            age=date_today.year-birth_date.year
            if age<18:
                print("You must be at least 18 years old.")
                continue
            return birth_date
        except ValueError:
            print("Please enter a valid date of birth.")



def valid_email():
    while True:
        email=input("Enter your email: ").strip()
        email_pattern=r'^[\w.-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        if re.fullmatch(email_pattern,email):
            return email
        else:
            print("Please enter a valid email.")
            continue









#name
def name_input():
    name=input("ENTER YOUR NAME: ")
    while not name.replace(' ','').isalpha():
        name=input("ENTER VALID NAME: ")
    return name.title()


#address 
def address():
    input_state=input("STATE: ").lower()
    input_district=input("DISTRICT: ").lower()
    state=["jammu and kashmir", "ladakh", "himachal pradesh", "punjab",
            "haryana", "uttarakhand", "uttar pradesh", "rajasthan", "delhi", "chandigarh"]
    dist=["agar", "agra", "ahmednagar", "ajmer", "aligarh", "alipurduar", "almora", "ambala", "amethi", "amritsar", "anantnag", "araria", "auraiya", "ayodhya",
"baghpat", "bahraich", "ballia", "balrampur", "bandipora", "banda", "barabanki", "baramulla", "bareilly", "basti", "bhiwani", "bijnor", "bikaner", "bilaspur", "bulandshahr",
"chamba", "chandigarh", "charkhi dadri", "chitrakoot", "churu",
"dausa", "dehradun", "delhi central", "delhi east", "delhi new", "delhi north", "delhi north east", "delhi north west", "delhi shahdara", "delhi south", "delhi south east", "delhi south west", "delhi west", "doda",
"etah", "etawah",
"faridabad", "farrukhabad", "fatehabad", "fatehpur", "firozabad",
"ganderbal", "ghaziabad", "ghazipur", "gonda", "gorakhpur", "gurgaon",
"hamirpur", "hardoi", "haridwar", "hathras", "hisar", "hoshiarpur",
"jaisalmer", "jammu", "jaunpur", "jhajjar", "jhansi", "jind", "jodhpur",
"kangra", "kannauj", "kanpur dehat", "kanpur nagar", "kathua", "kaushambi", "khandwa", "kishtwar", "kullu", "kupwara", "kurukshetra",
"kargil", "leh",
"lakhimpur kheri", "lalitpur", "lucknow",
"mahendragarh", "mathura", "meerut", "mewat", "moradabad", "muzaffarnagar",
"nainital", "noida",
"pauri garhwal", "pilibhit", "poonch", "prayagraj", "pulwama",
"rajouri", "rampur", "reasi", "rewari", "rohtak",
"saharanpur", "samba", "shimla", "shopian", "sikar", "sirsa", "sitapur", "sirmaur", "srinagar",
"tehri garhwal", "udhampur", "una",
"varanasi",
"yamunanagar"]    
    while input_state not in state:
        input_state=input("VALID STATE: ").lower()
    while input_district not in dist:
         input_district=input("DISTRICT: ").lower()
    return ','.join([input_district,input_state])


#income range
def income():
    income_range = {
        0:"below 10000",
        1:"10000-20000",
        2:"20001-30000",
        3:"30001-50000",
        4:"50001-75000",
        5:"75001-100000",
        6:"above 100000"}
    print("\nYOUR MONTHLY INCOME RANGE:")
    for key,value in income_range.items():
        print(f"{key}.{value}")

    while True:
        try:
            choice = int(input("ENTER OPTION (0-6): "))
            if 0 <= choice <len(income_range):
                return income_range[choice]
            else:
                print("PLEASE SELECT A VALID OPTION (0-6)")
        except ValueError:
            print("PLEASE ENTER A NUMBER ONLY")


def data_save():
    with open('bank_data.json','w') as f:
        json.dump(bank_data,f,indent=4)

def get_account_no():
    last=str(random.randint(1000,9999))
    account_no='1234567890'+last
    return int(account_no)
main()



