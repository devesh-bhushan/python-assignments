"""
program to concatinate the given dictionary
"""
d1 = {1: 100, 2: 200}
d2 = {3: 300, 4: 400}
d3 = {5: 500, 6: 600}
print(d2)
print(d1)
print(d3)
d2.update(d3)
d1.update(d2)
for k, v in d1.items():
    print(f"keys - {k} ->value -  {v}")