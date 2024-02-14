

def about_me():
    me = {
        "first": "Donald",
        "last": "Francois",
        "age": 37,
        "address":{
            "street": "evergreen",
            "number": "42",
            "city": "springfield",
            "zip": "12345",
        }
    }
    
    print(me)
    
    
    # read values
    print(me["first"] + " "+ me ["last"])
    print(f"I'm {me["age"]} years old")
    
    #read the address
    #print(me["address"]["street"])
    
    address = me ["address"]
    street = address["street"]
    num = address ["number"]
    city = address["city"]
    zip = address["zip"]
    print("street")
    
    #a) return to street #numb, city, zip
    print(f"Return to: {street} #{num},{city}, {zip}.")
   
   
    # fn calls
about_me()
    
    