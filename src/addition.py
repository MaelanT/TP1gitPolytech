def total(prix):
    """Additionne une liste de prix, avec remise d'ete de 10%."""
    somme = sum(prix)
    return round(somme * 0.9, 2)


if __name__ == "__main__":
    print(total([8, 16, 6]))
