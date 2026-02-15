import matplotlib.pyplot as plt

# Sample data
price = [100, 200, 300, 400, 500, 600]
discount = [5, 10, 15, 20, 25, 30]

# Create scatter plot
plt.scatter(price, discount)

# Labels and title
plt.xlabel("Price Range")
plt.ylabel("Discount (%)")
plt.title("Relationship Between Price and Discount")

# Show plot
plt.show()