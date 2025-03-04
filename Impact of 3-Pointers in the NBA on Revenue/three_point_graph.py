import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating a Line Plot for 3-Point Attempts Over Time
plt.figure(figsize=(8,5))
plt.plot(years, three_point_attempts, marker='o', linestyle='-', color='b', label='3PA per Game')
plt.xlabel('Year')
plt.ylabel('Average 3PA per Game')
plt.title('Increase in Three-Point Attempts Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Creating a Line Plot for NBA Revenue Over Time
plt.figure(figsize=(8,5))
plt.plot(years, revenues, marker='s', linestyle='-', color='g', label='NBA Revenue (Billion USD)')
plt.xlabel('Year')
plt.ylabel('Revenue (Billion USD)')
plt.title('NBA Revenue Growth Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Correlation Between 3-Point Attempts and Revenue
plt.figure(figsize=(8,5))
plt.scatter(three_point_attempts, revenues, color='r', label='Data Points')
plt.xlabel('Average 3PA per Game')
plt.ylabel('NBA Revenue (Billion USD)')
plt.title('Correlation Between Three-Point Attempts and Revenue')
plt.legend()
plt.grid(True)
plt.show()

# Trendline for Correlation
coeffs = np.polyfit(three_point_attempts, revenues, 1)
trendline = np.poly1d(coeffs)

plt.figure(figsize=(8,5))
plt.scatter(three_point_attempts, revenues, color='r', label='Data Points')
plt.plot(three_point_attempts, trendline(three_point_attempts), color='b', linestyle='--', label='Trendline')
plt.xlabel('Average 3PA per Game')
plt.ylabel('NBA Revenue (Billion USD)')
plt.title('Trend of Three-Point Attempts and Revenue')
plt.legend()
plt.grid(True)
plt.show()
