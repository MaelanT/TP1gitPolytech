def total(prix):
    """Additionne une liste de prix, TVA 20% incluse."""
    somme = sum(prix)
    return round(somme * 1.2, 2)


if __name__ == "__main__":
    print(total([8, 17, 11]))
