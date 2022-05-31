class User:
    
    def __init__(self, name, email_address, drivers_license_number):
        self.name = name
        self.email_address = email_address
        self.drivers_license_number = drivers_license_number

meredith = User('Meredith', 'mhall@gmail.com', 'TX123456')
jake = User('Jake', 'hilljake@gmail.com', 'MI12345')
mia = User('Mia', 'mia@mia.com', 'MA123456')
