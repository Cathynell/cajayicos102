
name_g = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna', 
          'Waje', 'Tola', 'Aisha', 'Latifa']
age_g = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
height_g = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
scores_g = [80, 85, 70, 60, 76,66, 87, 95, 50, 49]

name_b = ['Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola',
           'Kunle', 'Goerge', 'Thoma', 'Wesley']
age_b = [19,16,18,17,20,19,16,18,17,19]
height_b = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
scores_b = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

name = name_g + name_b
age = age_g + age_b
height = height_g + height_b
score = scores_g + scores_b

print("WELCOME TO STUDENT DATABASE!")

# Print table header
print(f"{'Name':<8} {'Age':<5} {'Height':<7} {'Score':<6}")
print("-" * 30)  # Print a separator line

# Print each student's data
for i in range(len(name)):  # Loop through the data using index
    print(f"{name[i]:<8} {age[i]:<5} {height[i]:<7} {score[i]:<6}")
