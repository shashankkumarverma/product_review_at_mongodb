import pymongo

DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
DB_NAME = "Product_Review_assignment"
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

#create DB
database = client['Product_Review_assignment']

collection_name = "Reviewer_Product"
collection = database[collection_name]



Product_records = [
    {
        'Product_name': "delllaptop",
        "Reviewer_name": "Md Faiz Alam",
        'Rating': "5",
        "Comment_Heading": "Great product",
        "Comment": "It's awesome products"

    },
    {
        'Product_name': "delllaptop",
        "Reviewer_name": "Aditya Maddheshiya",
        'Rating': "5",
        "Comment_Heading": "Classy product",
        "Comment": "Best laptop , For studying"

    },
    {
        'Product_name': "delllaptop",
        "Reviewer_name": "Flipkart Customer",
        'Rating': "5",
        "Comment_Heading": "Terrific",
        "Comment": "Nice product I am sooooo happy ."

    },
    {
        'Product_name': "delllaptop",
        "Reviewer_name": "Priya Joseph",
        'Rating': "4",
        "Comment_Heading": "Wonderful",
        "Comment": "Very nice lappy...I gifted this to my hubby he was soo happy"
    }
]
collection.insert_many(Product_records)