games = [
    "Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
    "Fortnite Battle Royale 39 Million 2017",
    "Apex Legends 50 Million (1 Month) 2019",
    "Leauge of Legends (LOL) 27 Million 2009",
    "Counter Strike; Global Offensive 32 Million 2014",
    "Heartstone 29 Million 20120",
    "Minecraft 91 Million 2011",
    "DOTA 2 5 million 2015",
    "The Division 2 N/A 2019",
    "The Splatoon 2"
]

print("5: " + games[4])

print(len(games[7]))

print(f"Er zitten {len(games)} games in de lijst")

games.insert(1, "snake")

print(f"Helaas heeft de game {games[9]} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {games[9]}.")
games.remove("The Splatoon 2")

games[5].replace("20120", "2012")

print(games)

# ------------------------------------------------------------

computer_providers = (
    "Apple",
    "Asus",
    "Dell",
    "Lenovo",
    "Acer",
    "Samsung",
    "MSI",
    "Hewlett-Packard (HP)",
    "Toshiba",
    "Microsoft",
    "Chuwi",
    "Sony"
)

length = len(computer_providers)
print(f"De tuple bevat {length} computer leveranciers.")

print(computer_providers[9])


print(f"De naam van {computer_providers[7]} bestaat uit {len(computer_providers[7])} karakters.")

print(computer_providers[9])

print(computer_providers)

dictionary = {
    "The Simpsons": "636-555-3226",
    "Vegas Vacation": "555-0100",
    "Ghostbusters": "555-23678",
    "Billy Madison": "555-0840",
    "Swingers": "213-555-4679",
    "Bruce Almighty": "555-0123",
    "Seinfeld": "555-FILK",
    "Arrested Development": "555-0113",
    "Die Hard With a Vengeance": "555-0001",
    "The A-Team": "555-6162",
}

print(f"Het telefoonnummer van Bruce Almighty is {dictionary['Bruce Almighty']}.")

dictionary["Harry Potter"] = "605-475-6961"

print("het ")
dictionary.update({"Ghostbusters": "555-2368"})
# add a new item to the dictionary
dictionary.pop("Seinfeld")

print(len(dictionary.values()))