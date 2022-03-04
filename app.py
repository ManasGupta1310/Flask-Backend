from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/stores")
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

if __name__=="__main__":
    app.run(debug=True)