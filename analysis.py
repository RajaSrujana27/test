import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

df['order_date'] = pd.to_datetime(df['order_date'])

user_total = df.groupby("user_id")["total_amount"].sum()

count_users = (user_total > 1000).sum()

print(count_users)

bins = [3.0, 3.5, 4.0, 4.5, 5.0]
labels = ["3.0–3.5", "3.6–4.0", "4.1–4.5", "4.6–5.0"]

df["rating_range"] = pd.cut(df["rating"], bins=bins, labels=labels)

print(df.groupby("rating_range")["total_amount"].sum())

gold_df = df[df["membership"] == "Gold"]

print(gold_df.groupby("city")["total_amount"].mean().sort_values(ascending=False))


gold_orders = df[df["membership"] == "Gold"].shape[0]

print("Total Gold Orders:", gold_orders)