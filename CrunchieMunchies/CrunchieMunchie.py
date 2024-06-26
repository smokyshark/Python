import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
#print(calorie_stats)

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
#print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

for i in range(len(calorie_stats_sorted)):
  if calorie_stats_sorted[i] > 60:
    #we have to add 1 to the nth_percentile cause array index is from 0
    nth_percentile = i + 1
    break
print(nth_percentile)
#nth_percentile = 4
more_calories = 100 - nth_percentile
print(more_calories)

percentage = np.mean(calorie_stats > 60)
print(percentage)

calorie_std = np.std(calorie_stats)
print(calorie_std)

print('The average calories is: ', average_calories)
print('The median of the calories is: ', median_calories)
print('The percentage of the ceraels that have more than 60 calories is: ', round(percentage * 100,2))
print('The standard deviation of calorie stats set is: ', calorie_std)
print('That means that the data spread is between ' + str(round(average_calories - calorie_std, 1)) + ' and ' +  str(round(average_calories + calorie_std, 1)) + ' calories.')