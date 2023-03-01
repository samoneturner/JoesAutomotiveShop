import Joes_Automotive_class as ja

name = input("Enter name : ")
address = input("Enter address : ")
phone = input("Enter phone : ")
customer = ja.Customer(name, address, phone)

make = input("Enter manufacturer : ")
model = input("Enter car model : ")
year = int(input("Enter year of manufacture : "))
car = ja.Car(make, model, year)

pcharge = float(input("Enter parts charges : "))
lcharge = float(input("Enter labour charges : "))
charges = ja.ServiceQuote(pcharge, lcharge)
print()
print("------------------------------")
print("Customer Details")
print()
print(
    f"Customer : {customer.get_name()}   Address : {customer.get_address()}   Phone: {customer.get_phone()}"
)
print(
    f"Car Make: {car.get_make()}   Car Model : {car.get_model()}   Car Year : {car.get_year()}"
)
print()
print("------------------------------")
print()
print("Service Quote")
print()
print(f"Parts: ${charges.get_parts_charges()}")
print(f"Labour: ${charges.get_labour_charges()}")
print(f"Sales Tax: ${charges.get_sales_tax()}")
print(f"Total Charges: ${charges.get_total_charges()}")
