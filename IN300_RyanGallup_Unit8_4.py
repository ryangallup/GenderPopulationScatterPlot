import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV data into a DataFrame
data = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv")

# Extract the columns with corrected names for plotting
females = data["COUNT FEMALE"]  # Note the space
males = data["COUNT MALE"]  # Note the space

# Create the scatter plot
plt.scatter(males, females)

# Add labels and title
plt.xlabel("Male Population")
plt.ylabel("Female Population")
plt.title("Distribution of Male vs. Female Population by Zip Code")

# Show the plot
plt.show()
