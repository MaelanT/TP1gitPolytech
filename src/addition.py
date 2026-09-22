def total(prix):
    """Additionne une liste de prix."""
    somme = 0
    for p in prix:
        somme += p
    return somme


if __name__ == "__main__":
    print(total([7, 18, 8]))
