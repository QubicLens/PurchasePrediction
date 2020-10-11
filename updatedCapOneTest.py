import requests
import json

customerId = 'Pothyn'
apiKey = '2bd4021425dbdbbb6aafac992c0ad0a8'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

customer = {
  "first_name": "Hunter",
  "last_name": "Davis",
  "address": {
    "street_number": "99",
    "street_name": "MLKJR",
    "city": "Miami",
    "state": "FL",
    "zip": "22323"
  }
}

# Clears all prior data
print(requests.delete(url = "http://api.reimaginebanking.com/data?type=Customer&key=2bd4021425dbdbbb6aafac992c0ad0a8").status_code)

# response = requests.get(url = url)
# print(response.status_code)
# print(response.text)

# response = requests.post(url = url, data = json.dumps(customer), headers = {'content-type':'application/json'})
# print(response.status_code)

PriceList = ("$4.86  $17.01  $16.49  $19.10  $210.83  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $113.07  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $220.50  $5.94  $6.57  $17.01  $16.49  $19.10  $4.86  $210.83  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $113.07  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $17.01  $16.49  $19.10  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $113.07  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50").split()

PlaceList = ("Dunkin_Donuts Netflix Hulu Amazon_Prime Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix  Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix  Anaya_Coffee McDonalds Netflix Hulu Amazon_Prime Dunkin_Donuts Publix  Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Netflix Hulu Amazon_Prime Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix").split()

DateList = ("11/1/20 11/1/20 11/1/20 11/1/20 11/1/20 11/2/20 11/2/20 11/3/20 11/3/20 11/4/20 11/4/20 11/4/20 11/5/20 11/5/20 11/6/20 11/6/20 11/6/20 11/6/20 11/6/20 11/6/20 11/8/20 11/8/20 11/9/20 11/9/20 11/10/20 11/10/20 11/11/20 11/11/20 11/11/20 11/12/20 11/12/20 11/13/20 11/13/20 11/14/20 11/14/20 11/15/20 11/15/20 11/16/20 11/16/20 11/17/20 11/17/20 11/18/20 11/18/20 11/18/20 11/19/20 11/19/20 11/20/20 11/20/20 11/20/20 11/20/20 11/20/20 11/20/20 11/22/20 11/22/20 11/23/20 11/23/20 11/24/20 11/24/20 11/25/20 11/25/20 11/25/20 11/26/20 11/26/20 11/27/20 11/27/20 11/28/20 11/28/20 11/29/20 11/29/20 11/30/20 11/30/20 12/1/20 12/1/20 12/1/20 12/1/20 12/1/20 12/2/20 12/2/20 12/2/20 12/3/20 12/3/20 12/4/20 12/4/20 12/4/20 12/4/20 12/4/20 12/4/20 12/6/20 12/6/20 12/7/20 12/7/20 12/8/20 12/8/20 12/9/20 12/9/20 12/9/20 12/10/20 12/10/20 12/11/20 12/11/20 12/12/20 12/12/20 12/13/20 12/13/20 12/14/20 12/14/20 12/15/20 12/15/20 12/16/20 12/16/20 12/16/20 12/17/20 12/17/20 12/18/20 12/18/20 12/18/20 12/18/20 12/18/20 12/18/20 12/20/20 12/20/20 12/21/20 12/21/20 12/22/20 12/22/20 12/23/20 12/23/20 12/23/20 12/24/20 12/24/20 12/25/20 12/25/20 12/26/20 12/26/20 12/27/20 12/27/20 12/28/20 12/28/20 12/29/20 12/29/20 12/30/20 12/30/20 12/30/20 12/31/20 12/31/20 1/1/21 1/1/21 1/1/21 1/1/21 1/1/21 1/1/21 1/1/21 1/1/21 1/1/21 1/3/21 1/3/21 1/4/21 1/4/21 1/5/21 1/5/21 1/6/21 1/6/21 1/6/21 1/7/21 1/7/21 1/8/21 1/8/21 1/9/21 1/9/21 1/10/21 1/10/21 1/11/21 1/11/21 1/12/21 1/12/21 1/13/21 1/13/21 1/13/21 1/14/21 1/14/21 1/15/21 1/15/21 1/15/21 1/15/21 1/15/21 1/15/21 1/17/21 1/17/21 1/18/21 1/18/21 1/19/21 1/19/21 1/20/21 1/20/21 1/20/21 1/21/21 1/21/21 1/22/21 1/22/21 1/23/21 1/23/21 1/24/21 1/24/21 1/25/21 1/25/21 1/26/21 1/26/21 1/27/21 1/27/21 1/27/21 1/28/21 1/28/21 1/29/21 1/29/21 1/29/21 1/29/21 1/29/21 1/29/21 1/31/21 1/31/21").split()

# print(DateList)
# print(PlaceList)
# print(PriceList)

purchase = []
for i in range(len(PriceList)):
  purchase.append([PriceList[i],PlaceList[i],DateList[i]])

p = []
for i in range(len(purchase)):
  p.append({
  "merchant_id": purchase[i][1],
  "medium": purchase[i][0],
  "purchase_date": purchase[i][2],
  "amount": 1,
  "status": "pending",
  "description": "string"
})
