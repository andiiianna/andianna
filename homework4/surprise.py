# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
for keys in targets: 
    print(keys)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_spectral_types(targets):
    for keys in targets:
        print(keys, targets[keys]["Spectral Type"])
print(print_spectral_types(targets))
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def conditional_mags(targets):
    for keys in targets:
        if targets[keys]["Magnitude"] > 0.1:
            print(keys)
print(conditional_mags(targets))
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Altair"] = {
    "RA": "19h 50m 47.0s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# def brightest_star(targets):
#     brightest = None 
#     smallest_difference = 100000
#     for keys in targets: 
#         dec = targets[keys]["Dec"] 
#         x = abs(dec - 20)

#         if x < smallest_difference:
#             smallest_difference = x
#             brightest = keys 
#     return brightest 
# print(brightest_star(targets))
# I cannot figure this one out lol, I keep getting the error "unsupported operand type(s) for -: 'str' and 'int'" 
# and I'm not sure how to chnage dec into an int, I tried looking it up, but it gave me a code of thigns I've never seen 
# before and I'd rather not put studd on here I don't undertsnad, sorryyy


# 6) What is your favorite constellation?
# Orion 