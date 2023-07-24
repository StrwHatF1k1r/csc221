from math import ceil

# Step 1: Read input values
wall_height = float(input("Enter the wall height: "))
wall_width = float(input("Enter the wall width: "))
cost_per_can = float(input("Enter the cost of one paint can: "))

# Step 2: Calculate wall area
wall_area = wall_height * wall_width

# Step 3: Calculate paint needed and number of cans
paint_needed = wall_area / 350.0
cans_needed = ceil(paint_needed)

# Step 4: Calculate paint cost, sales tax, and total cost
paint_cost = cost_per_can * cans_needed
sales_tax = paint_cost * 0.07
total_cost = paint_cost + sales_tax

# Step 5: Output wall area
print(f"Wall area: {wall_area:.1f} sq ft")

# Step 6: Output paint needed
print(f"Paint needed: {paint_needed:.3f} gallons")

# Step 7: Output number of cans needed
print(f"Cans needed: {cans_needed} can(s)")

# Step 8: Output paint cost
print(f"Paint cost: ${paint_cost:.2f}")

# Step 9: Output sales tax
print(f"Sales tax: ${sales_tax:.2f}")

# Step 10: Output total cost
print(f"Total cost: ${total_cost:.2f}")
