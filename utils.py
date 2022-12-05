import settings

def height_prct(percentage):
    return (settings.height/100)*percentage

# test
# print(height_prct(25))

def width_prct(percentage):
    return (settings.width/100)*percentage