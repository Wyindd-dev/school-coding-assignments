def kinetic_energy(mass, velocity):
    return 1/2 * mass * velocity ** 2

def main():
    mass = float(input("Enter the object's mass (in kilograms): "))
    velocity = float(input("Enter the object's velocity (in meters per second): "))
    print("The object has", kinetic_energy(mass, velocity), "joules of kinetic energy.")

main()