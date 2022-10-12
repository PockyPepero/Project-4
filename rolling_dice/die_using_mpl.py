import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
max_result = die_1.num_sides + die_2.num_sides 
frequencies = [results.count(value) for value in range(2, max_result+1)]
sums = ['2','3','4','5','6','7','8','9','10','11','12']

fig, ax = plt.subplots()
ax.bar(sums, frequencies)

# Set chart title and label axes
ax.set_title("Sums When Rolling 2 * D6s")
ax.set_xlabel("Possible Sums", fontsize=14)
ax.set_ylabel("Frequency of Sum", fontsize=14)

plt.show()
