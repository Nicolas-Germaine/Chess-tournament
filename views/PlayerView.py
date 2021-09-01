"""Base view."""


class PlayerView:
    """Player game view."""

    def information_player(self):
        """Prompt for a name."""
        first_name = input("Tapez le prénom : ")
        last_name = input("Tapez le nom de famille : ")
        date_of_birth = input("Tapez la date de naissance (ex 12/02/1987) : ")
        gender = input("Sexe ? (H/F) : ")
        ranking = input("Son rang ? : ")

        return {first_name, last_name, date_of_birth, gender, ranking}