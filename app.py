from flask import Flask, jsonify, request
from flask_cors import cross_origin, CORS
app = Flask(__name__)
cors=CORS(app)

app.config['CORS_HEADERS']='Content-Type'

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/stores")
@cross_origin()
def stores():
    obj=[
  {
    "storeName": "Mc Donalds",
    "storeSlug": "mcdonalds",
    "storeLogo": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/000000/external-mcdonald-corporation-an-american-fast-food-company-food-color-tal-revivo.png",
    "categories": [
      {
        "name": "Burger",
        "products": [
          {
            "name": "Big Mac",
            "price": "50",
            "qty":0
          },
          {
            "name": "Mc Aloo Tikki",
            "price": "40",
            "qty":0
          }
        ],
        "Image": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80"
      },
      {
        "name": "Meal",
        "products": [
          {
            "name": "Medium Meal",
            "price": "50",
            "qty":0
          },
          {
            "name": "Large Meal",
            "price": "40",
            "qty":0
          }
        ],
        "Image": "https://images.unsplash.com/photo-1619881589670-43629f0e90f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80"
      },
      {
        "name": "Drinks",
        "products": [
          {
            "name": "Pepsi",
            "price": "50",
            "qty":0
          },
          {
            "name": "Coke",
            "price": "40",
            "qty":0
          }
        ],
        "Image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80"
      }
    ]
  },
  {
    "storeName": "Dominos",
    "storeSlug": "dominos",
    "storeLogo": "https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/48/000000/external-dominos-an-american-multinational-pizza-restaurant-chain-food-shadow-tal-revivo.png",
    "categories": [
      {
        "name": "Veg Pizza",
        "products": [
          {
            "name": "Tandoori Paneer",
            "price": "50",
            "qty":0
          },
          {
            "name": "Veg Margherita",
            "price": "40",
            "qty":0
          }
        ],
        "Image": "https://images.unsplash.com/photo-1607290817806-e93c813ff329?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
      },
      {
        "name": "Non Veg Pizza",
        "products": [
          {
            "name": "Chicken Barbeque",
            "price": "50",
            "qty":0
          },
          {
            "name": "Chichken Dominator",
            "price": "40",
            "qty":0
          }
        ],
        "Image": "https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80"
      },
      {
        "name": "Drinks",
        "products": [
          {
            "name": "Pepsi",
            "price": "50",
            "qty":0
          },
          {
            "name": "Coke",
            "price": "40",
            "qty":0
          }
        ],
        "Image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80"
      }
    ]
  }
]

    return jsonify(obj)

@app.route("/orders")
@cross_origin()
def orders():
    obj=[
  {
    "storeName": "Mc Donalds",
    "orderDate":"29th January 2022",
    "storeSlug": "mcdonalds",
    "storeLogo": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/000000/external-mcdonald-corporation-an-american-fast-food-company-food-color-tal-revivo.png",
    "products": [
          {
            "name": "Big Mac",
            "price": "50",
            "quantity": 1,
          },
          {
            "name": "Mc Aloo Tikki",
            "price": "40",
            "quantity": 1,
          },
          {
            "name": "Medium Meal",
            "price": "50",
            "quantity": 1,
          },
          {
            "name": "Large Meal",
            "price": "40",
            "quantity": 1,
          },
          {
            "name": "Pepsi",
            "price": "50",
            "quantity": 1,
          },
          {
            "name": "Coke",
            "price": "40",
            "quantity": 1,
          }
        ],
      "total":"270",
      "address": "G-271, Hall-3",
      "paidBy":"Cash",
      "orderStatus":"Accepted",
      }
  ]


    return jsonify(obj)

@app.route("/products",methods=["POST", "GET"])
@cross_origin()
def products():
  if request.method=="GET":
    obj=[
      {
        "product":"Mc ALoo Tikki",
        "category":"Burger",
        "price":"50",
        "inStock":True,
      },
      {
        "product":"Mc Veggie",
        "category":"Burger",
        "price":"60",
        "inStock":True,
      },
      {
        "product":"Mc Flurry",
        "category":"Ice Cream",
        "price":"60",
        "inStock":True,
      },
      {
        "product":"Pepsi",
        "category":"Drinks",
        "price":"70",
        "inStock":True,
      }
    ]
    return jsonify(obj)
  
  if request.method=="POST":
    data=request.get_json()
    return data

@app.route("/categories")
@cross_origin()
def categories():
  obj=[
    {
      "title": "Pizza",
      "description": "A wide variety of mouth-watering pizzas in three categories : small, medium and large.",
      "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cGl6emF8ZW58MHwwfDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
      "status": True
    },
    {
      "title": "Extras",
      "description": "Breadsticks, dips, desserts and many more to compliment your delicious Pizza meal !!",
      "img": "https://images.unsplash.com/photo-1469648034646-7911874fe62b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8YXJsaWMlMjBicmVhZHxlbnwwfDB8MHx8&auto=format&fit=crop&w=500&q=60",
      "status": True
    },
    {
      "title": "Beverages",
      "description": "A wide range of hot and cold beverages to complete your perfect meal.",
      "img": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8YmV2ZXJhZ2VzfGVufDB8MHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
      "status": True
    }
  ]
  return jsonify(obj)

if __name__=="__main__":
    app.run(debug=True)