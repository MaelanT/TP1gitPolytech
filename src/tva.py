def ttc(prix_ht, taux=0.10):
    """Prix TTC avec la TVA restauration (10 %)."""
    return round(prix_ht * (1 + taux), 2)


if __name__ == "__main__":
    print(ttc(18))
