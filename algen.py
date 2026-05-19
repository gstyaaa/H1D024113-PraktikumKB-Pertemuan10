import random

barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

kapasitas = 15

JUMLAH_POPULASI = 20
JUMLAH_GENERASI = 50


def fitness(kromosom):

    total_keuntungan = 0
    total_ukuran = 0

    for i in range(len(kromosom)):

        if kromosom[i] == 1:

            total_keuntungan += barang[i][1]
            total_ukuran += barang[i][2]

    if total_ukuran > kapasitas:
        return 0

    return total_keuntungan


def inisialisasi_populasi():

    populasi = []

    for _ in range(JUMLAH_POPULASI):

        individu = [

            random.randint(0, 1)

            for _ in range(len(barang))
        ]

        populasi.append(individu)

    return populasi


def selection(populasi, fitnesses):

    total = sum(fitnesses)

    if total == 0:
        return random.choice(populasi)

    r = random.uniform(0, total)

    current = 0

    for individu, fit in zip(populasi, fitnesses):

        current += fit

        if current >= r:
            return individu


def crossover(parent1, parent2):

    titik = random.randint(
        1,
        len(parent1)-1
    )

    anak1 = (
        parent1[:titik]
        + parent2[titik:]
    )

    anak2 = (
        parent2[:titik]
        + parent1[titik:]
    )

    return anak1, anak2


def mutation(kromosom):

    kromosom = kromosom.copy()

    i = random.randint(
        0,
        len(kromosom)-1
    )

    kromosom[i] = 1 - kromosom[i]

    return kromosom


populasi = inisialisasi_populasi()

best = None
best_fit = 0

for generasi in range(JUMLAH_GENERASI):

    fitnesses = [
        fitness(ind)
        for ind in populasi
    ]

    for i in range(len(populasi)):

        if fitnesses[i] > best_fit:

            best_fit = fitnesses[i]
            best = populasi[i]

    populasi_baru = []

    while len(populasi_baru) < JUMLAH_POPULASI:

        parent1 = selection(
            populasi,
            fitnesses
        )

        parent2 = selection(
            populasi,
            fitnesses
        )

        anak1, anak2 = crossover(
            parent1,
            parent2
        )

        anak1 = mutation(anak1)
        anak2 = mutation(anak2)

        populasi_baru.extend([
            anak1,
            anak2
        ])

    populasi = populasi_baru[:JUMLAH_POPULASI]

print("\n=== HASIL TERBAIK ===")
print("Kromosom:", best)
print("Keuntungan Maksimum:", best_fit)

print("\nBarang Terpilih:")

total_ukuran = 0

for i in range(len(best)):

    if best[i] == 1:

        print(
            f"{barang[i][0]}"
            f" | Keuntungan={barang[i][1]}"
            f" | Ukuran={barang[i][2]}"
        )

        total_ukuran += barang[i][2]

print("\nTotal Ukuran:", total_ukuran)