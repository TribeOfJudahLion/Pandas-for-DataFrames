import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Sample data generation
def generate_sales_data(num_records):
    data = {
        'SaleID': range(1, num_records + 1),
        'Product': [f'Product{chr(65 + i % 3)}' for i in range(num_records)],
        'Quantity': [i % 5 + 1 for i in range(num_records)],
        'Price': [100 + i % 20 for i in range(num_records)],
        'SaleDate': [datetime.now() - timedelta(days=i % 10) for i in range(num_records)]
    }
    return pd.DataFrame(data)

# Business logic for processing sales data
def process_sales_data(sales_data):
    # Calculate total sales per product
    total_sales = sales_data.groupby('Product').apply(lambda x: (x['Quantity'] * x['Price']).sum()).reset_index(
        name='TotalSales')

    # Apply a 10% discount to ProductB
    total_sales['TotalSales'] = total_sales.apply(
        lambda row: row['TotalSales'] * 0.9 if row['Product'] == 'ProductB' else row['TotalSales'], axis=1)

    return total_sales

# Generate a summary report
def generate_report(total_sales):
    print("Sales Summary Report")
    print("====================")
    print(total_sales)
    print("====================")
    total_revenue = total_sales['TotalSales'].sum()
    print(f"Total Revenue: ${total_revenue:.2f}")
    print("====================")

# Advanced representation: Visualization
def visualize_data(total_sales, sales_data):
    # Set the style
    sns.set(style="whitegrid")

    # Plotting total sales per product
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Product', y='TotalSales', data=total_sales)
    plt.title('Total Sales Per Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.show()

    # Time series of sales
    sales_data['SaleDate'] = pd.to_datetime(sales_data['SaleDate']).dt.date
    sales_data['TotalSale'] = sales_data['Quantity'] * sales_data['Price']
    time_series = sales_data.groupby('SaleDate').agg({'TotalSale': 'sum'}).reset_index()

    plt.figure(figsize=(14, 7))
    sns.lineplot(x='SaleDate', y='TotalSale', data=time_series)
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    num_records = 1000  # Number of sales records to simulate
    print(f"Generating {num_records} sales records...")
    sales_data = generate_sales_data(num_records)

    print("Processing sales data...")
    total_sales = process_sales_data(sales_data)

    print("Generating sales summary report...")
    generate_report(total_sales)

    print("Visualizing sales data...")
    visualize_data(total_sales, sales_data)

if __name__ == "__main__":
    main()
