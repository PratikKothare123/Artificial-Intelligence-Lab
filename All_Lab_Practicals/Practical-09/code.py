# Bayes Theorem for Rain Prediction

# Given probabilities
P_rain = 0.3            # P(Rain)
P_cloud_given_rain = 0.8   # P(Cloud | Rain)
P_cloud = 0.5           # P(Cloud)

# Apply Bayes Theorem
P_rain_given_cloud = (P_cloud_given_rain * P_rain) / P_cloud

# Output
print("Probability of Rain given Clouds =", P_rain_given_cloud)

# Decision
if P_rain_given_cloud > 0.5:
    print("Prediction: Rain is likely")
else:
    print("Prediction: Rain is unlikely")
    
    
# Probability of Rain given Clouds = 0.48
# Prediction: Rain is unlikely