# FIND:
# Keys
# Values
# Change Volvo 2021 -> 2022
# Add your favorite car too.
# Delete BMW


cars={"Audi":["R8",2022],
      "Volvo":["XC90",2021],
      "BMW":["I8",2020],
      "CHEVROLET":["IMPALA",1967]}

print(cars.keys())
print(cars.values())

cars["Volvo"][1]=2022
print(cars)

cars["AUDI"]=["RS7",2022]
print(cars)

cars.pop("BMW")
print(cars)