def get_band_choice():
    print("Hey! I'm making a playlist of rock bands. Can you name a few of your favorites?")
    bands = []
    while True:
        band = input("Enter a band name (or 'done' to finish): ").strip()
        if band.lower() == 'done':
            break
        bands.append(band)
    return bands

def surprise_ticket(bands_entered, rock_bands_90s):
    matching_bands = [band for band in bands_entered if band in rock_bands_90s]
    if matching_bands:
        print(f"Surprise! I got you a ticket to see {matching_bands[0]} live!")
    else:
        print("You haven't mentioned any of the bands I had in mind...")
        surprise_band = random.choice(rock_bands_90s)
        print(f"But it's your lucky day! I'm surprising you with a ticket to see {surprise_band} live!")

import random

rock_en_espanol_bands_90s = [
    "Soda Stereo", "Caifanes", "Héroes del Silencio", "Maná", "La Ley",
    "Maldita Vecindad", "Los Fabulosos Cadillacs", "Los Auténticos Decadentes",
    "Café Tacvba", "Enanitos Verdes", "Los Pericos", "Jaguares",
    "Los Cafres", "Zoé", "Aterciopelados"
]

bands_entered = get_band_choice()
surprise_ticket(bands_entered, rock_en_espanol_bands_90s)

