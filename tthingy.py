import colormap

hex  = "#c03730"
hex =  "#008ce0"

rgb = colormap.hex2rgb(hex)

print(rgb)
print(hex)

av = round((rgb[0] + rgb[1] + rgb[2])/3)

t  = []
for i in range(1, 4):
    t.append(av)

h =  colormap.rgb2hex(t[0], t[1], t[2])

print(h[1:])