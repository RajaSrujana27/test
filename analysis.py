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
# 3.0–3.5    1881754.57
# 3.6–4.0    1717494.41
# 4.1–4.5    1960326.26
# 4.6–5.0    2197030.75

gold_df = df[df["membership"] == "Gold"]

print(gold_df.groupby("city")["total_amount"].mean().sort_values(ascending=False))

gold_orders = df[df["membership"] == "Gold"].shape[0]
print("Total Gold Orders:", gold_orders)

# Total Gold Orders: 4987
combo_revenue = df.groupby(["membership", "cuisine"])["total_amount"].sum()

print(combo_revenue.sort_values(ascending=False))
# membership  cuisine
# Regular     Mexican    1072943.30
#             Italian    1018424.75
# Gold        Mexican    1012559.79
#             Italian    1005779.05
# Regular     Indian      992100.27
# Gold        Indian      979312.31
#             Chinese     977713.74
# Regular     Chinese     952790.91

df["quarter"] = df["order_date"].dt.quarter
quarter_revenue = df.groupby("quarter")["total_amount"].sum()

print(quarter_revenue)
# quarter
# 1    2010626.64
# 2    1945348.72
# 3    2037385.10
# 4    2018263.66

# Orders where rating >= 4.5
high_rating_orders = df[df["rating"] >= 4.5].shape[0]

print(high_rating_orders)
# 3374
print(df.shape[0]) 
# 10000
