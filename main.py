import csv
import numpy as np
import matplotlib.pyplot as plt

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
 #print(headers)

survived = np.array(data[:,[0]], dtype=int).flatten()
fare = np.array(data[:,[7]], dtype=float).flatten()

# empty lists to hold data from the for loop
fare_survived = []
fare_not_survived = []

# for loop and if/else statements
for index in range(0, len(fare)):
  if survived[index] == 1:
    fare_survived.append(fare[index])
  else:
    fare_not_survived.append(fare[index])
    
# print lists
# print(f"The average fare of those who survived was: {round(np.mean(fare_survived), 2)}")
# print(f"The average fare of those who did not survive was: {round(np.mean(fare_not_survived), 2)}")

# print(f"The median fare of those who survived was: {round(np.median(fare_survived), 2)}")
# print(f"The median fare of those who did not survive was: {round(np.median(fare_not_survived), 2)}")

# create histogram to "see" data
bins = range(0,240,15)
plt.hist(fare_not_survived, bins, histtype="bar", color="red", alpha=0.5)
plt.hist(fare_survived, bins, histtype="bar", color="green", alpha=0.5)

plt.xticks(range(0,240,20))
plt.yticks(range(0,360,25))
plt.xlabel("Fare Amount Paid")
plt.ylabel("Number of Passengers")

plt.title("Titanic Passengers - compare survival against fare paid")
plt.gca().legend(("Did Not Survive", "Survived"))
plt.savefig("titanic_survival_fare.png")
