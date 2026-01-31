import pandas as pd
import sqlite3


orders = pd.read_csv("orders.csv")
users = pd.read_json("users.json")


conn = sqlite3.connect("restaurants.db")
conn.execute("DROP TABLE IF EXISTS restaurants")
with open("restaurants.sql", "r") as file:
    sql_script = file.read()
conn.executescript(sql_script)

restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)
print("Orders Columns:", orders.columns)
print("Users Columns:", users.columns)
print("Restaurants Columns:", restaurants.columns)

orders_users = pd.merge(
    orders,
    users,
    on="user_id",
    how="left"
)

final_df = pd.merge(
    orders_users,
    restaurants,
    on="restaurant_id",
    how="left"
)

if "restaurant_name_x" in final_df.columns:
    final_df = final_df.drop(columns=["restaurant_name_x"])
    final_df = final_df.rename(columns={"restaurant_name_y": "restaurant_name"})


final_df.to_csv("final_food_delivery_dataset.csv", index=False)
print("✅ Final Dataset Created Successfully!")


conn.close()
