def profile(name, age=18, country="Pakistan"):
    return f"{name} - {age} - {country}"

print(profile("Ali"))
print(profile("Sara", 22))
print(profile("John", country="USA"))
print(profile("Muneeb", 30, "Dubai"))
