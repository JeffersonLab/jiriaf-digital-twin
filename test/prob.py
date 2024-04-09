import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Define the cleanObservation, scalefactor, and sigma
cleanObservation = [1.0, 2.0, 3.0]
scalefactor = 1
sigma = 0.2

# Generate a range of x values
# x_values = np.linspace(min(cleanObservation) - 3*sigma, max(cleanObservation) + 3*sigma, 1000)
x_values = np.linspace(-3, 3, 50)

# Loop over each index
prob = []
for idx in range(len(cleanObservation)):
    # Calculate the mean of the normal distribution
    m = cleanObservation[idx] / scalefactor

    # Calculate the PDF for the x values
    pdf_values = norm.pdf(x_values, m, sigma/np.sqrt(scalefactor))

    # log the PDF values
    log_pdf_values = np.log(pdf_values)

    # exp the log PDF values
    log_pdf_values = np.exp(log_pdf_values)

    # Append the log PDF values to the prob list
    prob.append(log_pdf_values)

# Plot prob
plt.figure(figsize=(10, 6))
plt.plot(x_values, prob[0], label='Clean Observation 1')
plt.plot(x_values, prob[1], label='Clean Observation 2')
plt.plot(x_values, prob[2], label='Clean Observation 3')

# mark x_values on the plot
for x in x_values:
    plt.axvline(x=x, color='gray', alpha=0.1)



# Add a legend
plt.legend()

# Show the plot
plt.show()