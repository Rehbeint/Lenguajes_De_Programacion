import json


def get_number_of_prizes_in_peace_cat():
    """Returns the number of prizes in the peace category, sum one per year

    returns
    -------
    int:
        Number of prizes in peace category

    """
    # -----------------
    # Start code
    # ----------------
    with open("prize.json", "r") as content:
        p = json.load(content)
        print(p.get("category"))


    # Aqui hay que hacer el recorrido del JSON y que busque las nominaciones a "peace"
    # Luego copiar, pegar y editar las variables para los def de abajo


    # -----------------
    # End code
    # ----------------


def get_number_of_prizes_in_literature():
    """Returns the number of prizes in the literature category, sum one per year

    returns
    -------
    int:
        Number of prizes in literature category

    """
    # -----------------
    # Start code
    # ----------------
    
    num = 11

    # -----------------
    # End code
    # ----------------


def get_oldest_prize():
    """Returns the year of the oldest prize

    returns
    -------
    int:
        the year of the oldest prize
    """
    # -----------------
    # Start code
    # ----------------
    pass
    # -----------------
    # End code
    # ----------------


def main():
    """Calls the methods"""
    num = get_number_of_prizes_in_peace_cat()
    print(f'{num} prizes in peace')
    num = get_number_of_prizes_in_literature()
    print(f'{num} prizes in literature')
    num = get_oldest_prize()
    print(f'{num} is the oldest year of the novel prizes')


if __name__ == "__main__":
    main()