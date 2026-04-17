# ISA relationship (Inheritance)
isa = {
    "Bird": "Animal",
    "Dog": "Animal",
    "Sparrow": "Bird"
}

# HAS-A relationship (Property)
has = {
    "Animal": "Cells"
}

# CAN relationship (Ability)
can = {
    "Bird": "Fly",
    "Dog": "Bark"
}

# Function to check ISA relationship
def check_isa(x, y):
    while x in isa:
        if isa[x] == y:
            return True
        x = isa[x]
    return False

# Function to check HAS-A property with inheritance
def check_has(x, property):
    if x in has and has[x] == property:
        return True

    while x in isa:
        x = isa[x]
        if x in has and has[x] == property:
            return True

    return False

# Function to check CAN ability with inheritance
def check_can(x, ability):
    if x in can and can[x] == ability:
        return True

    while x in isa:
        x = isa[x]
        if x in can and can[x] == ability:
            return True

    return False


# Driver Code
print("Sparrow ISA Bird :", check_isa("Sparrow", "Bird"))
print("Dog ISA Animal :", check_isa("Dog", "Animal"))

print("Sparrow HAS Cells :", check_has("Sparrow", "Cells"))

print("Bird CAN Fly :", check_can("Bird", "Fly"))
print("Dog CAN Bark :", check_can("Dog", "Bark"))


# Sparrow ISA Bird : True
# Dog ISA Animal : True
# Sparrow HAS Cells : True
# Bird CAN Fly : True
# Dog CAN Bark : True