def students():
    names = names = ["Dave", "Jazper",  "Andy", "Corey", "Samuel", "Cesar", "Darius", "Demetri", "Janaye", "Donald", "Marco"]
    print(names)
    
    #ads elements
    names.append("Donald") 
    
    #travel the list 
    for name in names:
        print(name)
    # A) how many names in the list
    print(len(names))
    
def products():
    prices = [23, 234, 34, 672, 77, 214, 756, 76, 500, 479, 629, 325, 389, 29, 101, 50, 67, 800, 54]
    
    # A) print every price 
    # B) summ of all prices
    # C) how many prices are lower than 500
    # D) how many are greaer or equal to 500 

    
    # for loop
    total = 0
    count = 0
    expensive = 0
    for price in prices:
        print(price)
        #total = total + price 
        total = total + price

        if price < 500:
            #count = count + 1
            count = count + 1
            count += 1
        
        if price >=500:
            count += 1
    print(total)
    print(count)
    print(expensive)
    
    
def art():
    colors = ["red", "blue", "pink", "blue", "white", "blak", "green", "blak", "red", "white", "blue", "yellow"]
    # how many colors are there in the list
    print(len(colors))
    # how many are blue
    blue = 0
    black_white = 0
    
    for color in colors:
        if color =="blue":
            blue += 1
        if color == "white" or color =="blak":
            black_white += 1
            
    print("blues" + str (blue))
    print("Whites or blacks" + str (black_white))
    # how many are white or black 
#calls
#students()
products()
art()