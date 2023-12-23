import colorgram

rgb_colors = []
colors = colorgram.extract("raja.jpg", 30)
print(colors)
for item in colors:
     rgb_colors.append(item.rgb)
print(rgb_colors)