#my github is https://github.com/iTengfah
"ISABELLA TINABELLA TENGFAH"
"CIVIL 2"
"COMPUTER APPLICATION IN CIVIL ENGINEERING"
"6948821"
#cars that are being sold
Cars=['Tesla','Mazda','BMW','Sabaru','Porsche','Honda','Lexus','Toyota','Chrysler','Buick','Hyundai','Audi','Infiniti','Nissan','Dodge','Genesis','Mini','Volkswagon','Kia','Volvo','Mercedes benz','Cadillac','Acura','Chevrolet','Ford','GMC','Jaguar','Lincoln','Jeep','Land rover']
#prices of the cars saved in a dictionary
CarPrice={'Tesla':'500000','Mazda':'550000','BMW':'600000','Sabaru':'200000','Porsche':'30000','Honda':'20000','Lexus':'2000000','Toyota':'700000','Chrysler':'80000','Buick':'85000','Hyundai':'85000','Audi':'75000','Infiniti':'60000','Nissan':'60500','Dodge':'65000','Genesis':'200000','Mini':'550000','Volkswagon':'50000','Kia':'80000','Volvo':'80000','Mercedes benz':'70000','Cadillac':'70000','Acura':'70000','Chevrolet':'70000','Ford':'700000','GMC':'700000','Jaguar':'80000','Lincoln':'85000','Jeep':'20000','Land rover':'20000'}
print()
#asking the client to make their choice of car
BuyersChoice=input('Which car do you want: ')
#conditional statement giving the price of the chosen car
if BuyersChoice in Cars:
    print('This car costs '+CarPrice[BuyersChoice])
else:
    print('Sorry, the car you want is not available.')