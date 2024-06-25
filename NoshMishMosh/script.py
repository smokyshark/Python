import noshmishmosh
import numpy as np

#get information about how many people visited the website
all_visitors = noshmishmosh.customer_visits
#get information about how many visitors bought the meals 
paying_visitors = noshmishmosh.purchasing_customers
total_visitor_count = len(noshmishmosh.customer_visits)
paying_visitor_count = len(noshmishmosh.purchasing_customers)

#get the baseline
baseline_percent = paying_visitor_count / total_visitor_count * 100
print('Baseline conversion rate: ', baseline_percent)

payment_history = noshmishmosh.money_spent
#print(payment_history)
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240 / average_payment)
#print(new_customer_needed)
percentage_point_increase = new_customers_needed / total_visitor_count * 100
print('Percentage point increase:', percentage_point_increase)

lift = round(percentage_point_increase / baseline_percent * 100, 2)
print('Minimum desired lift:', lift)

ab_sample_size = 472
print('Sample size:', ab_sample_size)