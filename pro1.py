
print("Available locations:")
print("nashik")
print("sukene")
print("niphad")
print("sinner")
print("pune")


nashik = 0
sukene = 60
niphad = 40
sinner = 70
pune = 90

location = str(input("Enter your start point: ")).lower()
destination = str(input("Enter your end point: ")).lower()

print("Your location is:", location)
print("Your destination is:", destination)

distances = {
    "nashik": nashik,
    "sukene": sukene,
    "niphad": niphad,
    "sinner": sinner,
    "pune": pune
}

if location in distances and destination in distances:
    totalkm = abs(distances[destination] - distances[location])
    print("The total km are:", totalkm)

    bikeavg = 50
    fuel_needed = totalkm / bikeavg
    print("Fuel needed (in liters) for the journey:", fuel_needed)
else:
    print("Invalid location or destination. Please check spelling.")
