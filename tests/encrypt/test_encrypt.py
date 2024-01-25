import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    mensage = "teste"

    # Caso 1: key is a number odd
    assert encrypt_message(mensage, 3) == "set_et"

    # Caso 2: key is a number even
    assert encrypt_message(mensage, 2) == "ets_et"

    # Caso 3: error key is not a number
    with pytest.raises(TypeError):
        encrypt_message(mensage, "2")

    # Caso 4: error message is not a string
    with pytest.raises(TypeError):
        encrypt_message(2, 2)

    # Caso 5: key is not in range
    assert encrypt_message(mensage, 5) == "etset"
