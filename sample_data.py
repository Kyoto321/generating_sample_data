import pandas as pd
import numpy
import random
import datetime
import calendar

# product to price dictionary mapping
products = {
   # Product: [Price, weight(value - based on sales)]
  'iPhone': [700, 10],
  'Google Phone': [600, 8],
  'Vareebadd Phone': [400, 3],
  '20in Monitor': [109.99, 6],
  '34in Ultrawide Monitor': [379.99, 9],
  '27in 4K Gaming Monitor': [389.99, 9],
  '27in FHD Monitor': [149.99, 11],
  'Flatscreen TV': [300, 7],
  'Macbook Pro Laptop': [1700, 7],
  'ThinkPad Laptop': [999.99, 6],
  'AA Batteries (4-pack)': [3.84, 30],
  'AAA Batteries (4-pack)': [2.99, 30],
  'USB-C Charging Cable': [11.95, 30],
  'Lightning Charging Cable': [14.95, 30],
  'Wired Headphones': [11.99, 26],
  'Bose SoundSport Headphones': [99.99, 19],
  'Apple Airpods Headphones': [150, 22],
  'LG Washing Machine': [600.00, 1],
  'LG Dryer': [600.00, 1]
}

# To generate a date in format mm/dd/year H:m
def generate_random_time(month):
   # Amount of days in a month
   day_range = calendar.monthrange(2021,month)[1]
   # To select a random day
   random_day = random.randint(1, day_range)
   if random.random() < 0.5:
      date = datetime.datetime(2021, month, random_day, 12, 0)
   else:
      date = datetime.datetime(2021, month, random_day, 20, 0)
   
   time_offset = numpy.random.normal(loc=0, scale=180)
   final_date = date + datetime.timedelta(minutes=time_offset)

   return final_date.strftime("%m/%d/%y %H:%M")


# To generate a random address for each row in the dataset
def generate_random_address():
    street_names = ['Main', '2nd', '1st', '4th', '5th', 'Park', '6th', '7th', 'Maple', 'Pine', 'Washington', '8th', 'Cedar', 'Elm', 'Walnut', '9th', '10th', 'Lake', 'Sunset', 'Lincoln', 'Jackson', 'Church', 'River', '11th', 'Willow', 'Jefferson', 'Center', '12th', 'North', 'Lakeview', 'Ridge', 'Hickory', 'Adams', 'Cherry', 'Highland', 'Johnson', 'South', 'Dogwood', 'West', 'Chestnut', '13th', 'Spruce', '14th', 'Wilson', 'Meadow', 'Forest', 'Hill', 'Madison']
    cities = ['San Francisco', 'Boston', 'New York City', 'Austin', 'Dallas', 'Atlanta', 'Portland', 'Portland', 'Los Angeles', 'Seattle']
    weights = [9,4,5,2,3,3,2,0.5,6,3]
    zips = ['94016', '02215', '10001', '73301', '75001', '30301', '97035', '04101', '90001', '98101']
    state = ['CA', 'MA', 'NY', 'TX', 'TX', 'GA', 'OR', 'ME', 'CA', 'WA']

    street = random.choice(street_names)
    index = random.choices(range(len(cities)), weights=weights)[0]

    return f"{random.randint(1,999)} {street} St, {cities[index]}, {state[index]}, {zips[index]}"

def write_row(order_id, product, order_date, address):
   price = products[product][0]
   # the amount ordered is inversly proportional to the price, using numpy geometric distribution
   quantity_ordered = numpy.random.geometric(p=1.0-(1.0/price), size=1)[0]
   return[order_id, product, quantity_ordered, price, date, address]


product_list = [product for product in products]
weights = [products[product][1] for product in products]

columns = ['Order ID', 'Products', 'Quantity Ordered', 'Price Each', 'Ordered Date', 'Purchase Address' ]

order_id = 14365

# To generate a simple csv
#df = pd.DataFrame(columns=columns)
"""
# To randomly select rows
for i in range(1000):
	product = random.choice(list(products.keys()))
	price = products[product]
	df.loc[i] = [i, product, 1, price, "NA", "NA"]

#df.to_csv('test_data.csv')
"""
"""
# To make more purchased products show up on data
# add a weight value to the price list
for i in range(1000):
	product_list = [product for product in products]
	weights = [products[product][1] for product in products]

	product = random.choices(product_list, weights=weights)[0]
	price = products[product]
	df.loc[i] = [i, product, 1, price, "NA", "NA"]

print(product_list)
print(weights)
df.to_csv('test_data.csv')

"""

# Creating different csv_data from the same source
for month_value in range(1,13):

   # To make a particular set of month the high value
   if month_value <= 10:
      orders_amount = int(numpy.random.normal(loc=12000, scale=4000))

   if month_value == 11:
      orders_amount = int(numpy.random.normal(loc=20000, scale=3000))

   if month_value == 12:
      orders_amount = int(numpy.random.normal(loc=26000, scale=3000))

   df = pd.DataFrame(columns=columns)

   i=0
   while orders_amount > 0:

      address = generate_random_address()
      date = generate_random_time(month_value)
      product = random.choices(product_list, weights=weights)[0]
      
      df.loc[i] = write_row(order_id, product, date, address)

      if product=='iPhone':
         if random.random() < 0.15:
            df.loc[i] = write_row(order_id, "Lightning Charging Cable", date, address)
            i += 1

         if random.random() < 0.05:
            df.loc[i] = write_row(order_id, "Apple Airpods Headphones", date, address)
            i += 1

         if random.random() < 0.07:
            df.loc[i] = write_row(order_id, "Wired Headphones", date, address)
            i += 1 

      elif product == "Google Phone" or product == "Vareebadd Phone":
         if random.random() < 0.18:
            df.loc[i] = write_row(order_id, "USB-C Charging Cable", date, address)
            i += 1
         if random.random() < 0.04:
            df.loc[i] = write_row(order_id, "Bose SoundSport Headphones", date, address)
            i += 1
         if random.random() < 0.07:
            df.loc[i] = write_row(order_id, "Wired Headphones", date, address)
            i += 1 

         if random.random() <= 0.02:
            product_choice = random.choices(product_list, weights)[0]
            df.loc[i] = write_row(order_id, product_choice, date, address) 
            i += 1

         if random.random() <= 0.002:
            df.loc[i] = columns
            i += 1

         if random.random() <= 0.003:
            df.loc[i] = ["","","","","",""]
            i += 1

      


      order_id += 1
      orders_amount -= 1

   month_name = calendar.month_name[month_value]
   df.to_csv(f"{month_name}_data.csv")

# To generate a random address for each row in the dataset