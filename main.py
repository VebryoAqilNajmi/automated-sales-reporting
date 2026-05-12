import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Read dataset
df = pd.read_csv("train.csv")

# Total sales
total_sales = round(df["Sales"].sum(), 2)

# Top category
top_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

# Top region
top_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

print("=== SALES SUMMARY ===")
print("Total Sales:", total_sales)
print("Top Category:", top_category)
print("Top Region:", top_region)

summary_df = pd.DataFrame({
    "Metric": ["Total Sales", "Top Category", "Top Region"],
    "Value": [total_sales, top_category, top_region]
})

summary_df.to_excel("sales_summary.xlsx", index=False)

print("✅ Excel report generated!")

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_box = driver.find_element(By.NAME, "my-text")

text_box.send_keys(f"Total Sales: {total_sales}")

time.sleep(5)

driver.quit()