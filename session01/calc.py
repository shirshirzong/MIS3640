#question 1:2562s
print(42*60+42)
#question 2:6.21miles
print(10/1.61)
#question 3:
first=42*60+4
second=10/1.61
#time per mile in seconds:406.364
print(first/second)
#time per mile in minutes:6.772
third=first/second
print(third/60)
#average speed in miles per hour: 8.859
fourth=first/60/60
print(second/fourth)

# Exercise 1 9/4
# question 1:
import math
print(math.pi)
volume = 4 / 3 * math.pi * 5 ** 3
print('The volume of a sphere with radius 5 is ${:.2f}'.format(volume))

#question 2:
total_cover_price = 60 * 24.95 * (1 - 0.4)
total_shipping_cost = 3 + 0.75 * (60 - 1)
total_cost = total_cover_price + total_shipping_cost
print('The total wholesale cost for 60 copies is {:.2f}'.format(total_cost))

# question 3:
leave = (6 * 60 + 52) * 60
easy = (8 * 60 + 15) * 2
tempo = (7 * 60 + 12) * 3
arrive_hour = (leave + easy + tempo) / (60*60)
arrive_rd = (leave + easy + tempo) // (60*60)
arrive_minute = (arrive_hour - arrive_rd) * 60
print ('The time I get home for breakfast is {:d}:{:d}'.format(int(arrive_hour), int(arrive_minute)))

# question 4:
change = (89 - 82)/82
percentage_change = change * 100
print ('The percentage increase is {:.1f}%'.format(percentage_change))