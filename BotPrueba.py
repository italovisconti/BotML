from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

url = "https://www.pccomponentes.com/asus-geforce-gtx-1050-tis-4gb-gddr5"
url_coolmod = "https://articulo.mercadolibre.com.ve/MLV-718947014-carro-de-perros-caliente-y-hamburguesas-_JM#position=6&search_layout=stack&type=item&tracking_id=99e36af4-229a-42f8-88e4-5cca200a0bd7"

session = HTMLSession()

#no se ejecuta
def aviso_facil():
    while True:
        r = session.get(url)
        buy_zone = r.html.find("#btnsWishAddBuy")
        print(buy_zone)
        if len(buy_zone) > 0:
            print("HAY STOCK!!!")
            break
        else:
            print("Sigue sin haber stock :(")
        sleep(30)


def entrar_y_verificar():
    """HTML Session para obtener el codigo HTML"""
    product_page = session.get(url_coolmod)
    found = product_page.html.find("#ui-pdp-main-container")
    """Verificamos que exista el producto"""
    return found


def iniciar_sesion(driver):
    form = None
    """is_form_loaded = False

    while not is_form_loaded:
        try:
            form = driver.find_element_by_class_name("login100-form")
            is_form_loaded = True
        except NoSuchElementException:
            print("Puessss no esta el formulario...")"""

    email = driver.find_element(By.ID, value="user_id")
    email.send_keys("Prueba@hotmail.com")
    sleep(2)

    driver.find_element(By.CLASS_NAME, value="andes-button__content").click()

    """Hay Captcha, no se como resolverlo"""


def iniciar_compra(found):
    """Aca utilizamos el bot como tal"""
    if len(found):
        driver = webdriver.Firefox()
        driver.get(url_coolmod)
        sleep(3)
        print("Funcionando")
        """Debemos cerrar el Banner de Cookies"""
        driver.find_element(By.CLASS_NAME, value="cookie-consent-banner-opt-out__action.cookie-consent-banner-opt-out__action--primary.cookie-consent-banner-opt-out__action--key-accept").click()
        driver.find_element(By.CLASS_NAME, value="ui-pdp-actions").click()
        sleep(2)
        driver.find_element(By.CLASS_NAME, value="login-link.andes-button--large.andes-button--transparent").click()
        sleep(1)

        iniciar_sesion(driver)


def main():
    found = entrar_y_verificar()
    iniciar_compra(found)


if __name__ == "__main__":
    main()