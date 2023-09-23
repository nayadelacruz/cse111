import math

#introduce all the information form the cans we are going to use 
def main():
    can_name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#1 tall"
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#6Z"
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#10"
    radius = 15.75
    height = 17.78
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

    can_name = "303"
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    area = compute_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{can_name} {storage_efficiency:.2f}")

#compute volume
def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    area = 2 * math.pi *radius * (radius + height)
    return area
main()
    
