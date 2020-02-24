import thorpy
import pygame
from money import money
from supplier import supplier
from store import store


def finishPurhcase():
    global amount
    global product
    global sellPrice
    global slider
    global slider1
    global togglable_pool
    amount = slider.get_value()
    sellPrice = slider1.get_value()
    product = togglable_pool.get_selected().get_full_txt()

    if amount.isdigit():
        if sellPrice.isdigit():
            if store.add(product, int(amount), supplier, int(sellPrice), money):
                print("amount", amount)
                print("sellPrice", sellPrice)
                print("product", product)
                successfulPurchase()
            else:
                unSuccessfulPurchase()
    begin()


def unSuccessfulPurchase():
    global product
    global amount
    background.unblit_and_reblit()

    thorpy.launch_blocking_alert(title="Error", text="Supplier does not have " + str(amount) + " " + product + " in stock", ok_text="ok", font_size=12, font_color=(0, 0, 0))
    begin()


def successfulPurchase():
    global product
    global amount
    background.unblit_and_reblit()

    thorpy.launch_blocking_alert(title="Success", text="purchased " + amount + " " + product, ok_text="ok", font_size=12, font_color=(0, 0, 0))
    begin()


def buyProduce():
    global slider
    global slider1
    global togglable_pool
    background.unblit_and_reblit()
    button1 = thorpy.make_button("purchase", func=finishPurhcase)
    button = thorpy.make_button("done", func=begin)
    title_element = thorpy.make_text("add item", 35, (255, 255, 0))
    slider = thorpy.Inserter(name="amount")
    slider1 = thorpy.Inserter(name="sell price")
    buttons = [thorpy.Togglable.make(str(i)) for i in supplier.availStockAsList()]
    togglable_pool = thorpy.TogglablePool(buttons, first_value=buttons[1], always_value=False)
    radio_and_toggable = buttons
    elements = [title_element] + radio_and_toggable + [slider, slider1, button, button1]
    central_box = thorpy.Box.make(elements=elements)
    central_box.fit_children(margins=(30, 30))
    central_box.center()
    central_box.add_lift()
    central_box.set_main_color((220, 220, 220, 180))

    thorpy.launch_blocking(central_box)


def checkInventory():
    background = thorpy.Background.make(image="./pictures/wholeChicken.png")
    background.unblit_and_reblit()
    thorpy.launch_blocking_alert(title="Inventory check", text=store.availStockAsText(), ok_text="ok", font_size=12, font_color=(255, 255, 255))
    begin()

def checkStock():
    background.unblit_and_reblit()
    thorpy.launch_blocking_alert(title="Supplier check", text=supplier.availStockAsText(), ok_text="ok", font_size=12, font_color=(255, 255, 255))
    begin()

def begin():
    thorpy.Background.remove_all_elements(background)
    background.unblit_and_reblit()
    choices = [("addItem", buyProduce), ("check store inventory", checkInventory), ("check supplier stock", checkStock)]
    thorpy.launch_blocking_choices("action selection", choices, parent=background)


screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
money = money(2000)
supplier = supplier()
store = store()
application = thorpy.Application((500, 500), "Grocery Store Simulator 2021")
button = thorpy.make_button("Begin game", func=begin)
background = thorpy.Background.make(image="./pictures/thick.png", elements=[button])
menu = thorpy.Menu(background)
product = ""
amount = 0
sellPrice = 0
slider = thorpy.SliderX(100, (12, 35), "amount")
slider1 = thorpy.SliderX(100, (12, 35), "sell price")
togglable_pool = 0
menu.play()

application.quit()
