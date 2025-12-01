from selenium.webdriver.common.by import By
from .base_page import BasePage


class CrudPage(BasePage):
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com/"

   
    LIST_URL = BASE_URL + "contactList"
    ADD_URL = BASE_URL + "addContact"

    
    CONTACT_ROWS = (By.CSS_SELECTOR, ".contactTableBodyRow")
    ADD_BUTTON = (By.ID, "add-contact")  

   
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.ID, "submit")

    
    EDIT_BUTTON = (By.ID, "edit-contact")
    DELETE_BUTTON = (By.ID, "delete")
    RETURN_BUTTON = (By.ID, "return")  

  
    def open_page(self):
        """Abre la pantalla de lista de contactos."""
        self.open(self.LIST_URL)
        self.find_elements(self.CONTACT_ROWS)

    
    def contact_exists(self, email: str) -> bool:
        """Devuelve True si el email aparece en la tabla."""
        rows = self.find_elements(self.CONTACT_ROWS)
        return any(email.lower() in row.text.lower() for row in rows)

    def open_contact(self, email: str) -> None:
        """Hace clic en la fila del contacto que contiene ese email."""
        rows = self.find_elements(self.CONTACT_ROWS)
        for row in rows:
            if email.lower() in row.text.lower():
                row.click()
                return
        raise AssertionError(f"No se encontró el contacto con email {email}")

   
    def add_contact(self, first_name: str, last_name: str, email: str) -> None:
        """Crea un nuevo contacto."""
       
        self.open_page()
        self.click(self.ADD_BUTTON)

        
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.EMAIL_INPUT, email)

        
        self.click(self.SUBMIT_BUTTON)

        
        self.find_elements(self.CONTACT_ROWS)

    def edit_contact(self, new_first_name: str) -> None:
        """
        Edita el contacto actual (ya estamos en la pantalla de detalle).
        Cambiamos solo el nombre.
        """
       
        self.click(self.EDIT_BUTTON)

        
        self.type(self.FIRST_NAME_INPUT, new_first_name)

        
        self.click(self.SUBMIT_BUTTON)

        
        self.click(self.RETURN_BUTTON)
        self.find_elements(self.CONTACT_ROWS)

    def delete_contact(self) -> None:
        """
        Elimina el contacto actual (pantalla de detalle).
        La app muestra un alert de confirmación.
        """
        
        self.click(self.DELETE_BUTTON)

       
        alert = self.driver.switch_to.alert
        alert.accept()

        
        self.find_elements(self.CONTACT_ROWS)
