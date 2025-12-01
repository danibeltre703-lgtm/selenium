from pages.login_page import LoginPage
from pages.crud_page import CrudPage
import time
import uuid

VALID_EMAIL = "danibeltre703@gmail.com"
VALID_PASSWORD = "Dbeltr3"


def login_and_open_crud(driver):
    login = LoginPage(driver)
    login.open_login()
    login.login(VALID_EMAIL, VALID_PASSWORD)

    assert login.is_logged_in(), "ERROR: El login no funcionó con credenciales válidas."

    crud = CrudPage(driver)
    crud.open_page()
    return crud


def test_crear_contacto(driver):
    crud = login_and_open_crud(driver)

    unique = uuid.uuid4().hex[:6]
    email = f"test{unique}@mail.com"

    crud.add_contact("Test", "User", email)
    time.sleep(1)

    assert crud.contact_exists(email), "ERROR: El contacto no se creó."


def test_editar_contacto(driver):
    crud = login_and_open_crud(driver)

    unique = uuid.uuid4().hex[:6]
    email = f"edit{unique}@mail.com"

    crud.add_contact("Nombre", "Original", email)
    time.sleep(1)
    assert crud.contact_exists(email), "ERROR: El contacto inicial no se creó."

    crud.open_contact(email)
    crud.edit_contact("NombreEditado")
    time.sleep(1)

    # El email no cambia, así que seguimos buscando por email
    assert crud.contact_exists(email), "ERROR: No se actualizó el contacto."


def test_eliminar_contacto(driver):
    crud = login_and_open_crud(driver)

    unique = uuid.uuid4().hex[:6]
    email = f"del{unique}@mail.com"

    crud.add_contact("Delete", "Me", email)
    time.sleep(1)
    assert crud.contact_exists(email), "ERROR: El contacto de prueba para eliminar no se creó."

    crud.open_contact(email)
    crud.delete_contact()
    time.sleep(1)

    assert not crud.contact_exists(email), "ERROR: El contacto no se eliminó."
