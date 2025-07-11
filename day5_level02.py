# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted:", ages)
print("Min:", min_age)
print("Max:", max_age)

# 2
ages.extend([min_age, max_age])
print("Extended:", ages)

# 3
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Median:", median)

# 4
average = sum(ages) / len(ages)
print("Average:", average)

# 5
range_ages = max_age - min_age
print("Range:", range_ages)

# 6
print("Min - Avg:", abs(min_age - average))
print("Max - Avg:", abs(max_age - average))

# 7
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)
mid = n // 2
print("Middle country/countries:", countries[mid] if n % 2 != 0 else countries[mid-1:mid+1])

# 8
first_half = countries[:mid+1] if n % 2 != 0 else countries[:mid]
second_half = countries[mid+1:] if n % 2 != 0 else countries[mid:]
print("First half:", first_half)
print("Second half:", second_half)

# 9
c1, c2, c3, *scandic_countries = countries
print("First 3:", c1, c2, c3)
print("Scandic countries:", scandic_countries)

