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
    amount = slider.get_value()
    sellPrice = slider1.get_value()
    print("amount = ", amount)
    print("sellprice = ", sellPrice)


def buyProduceApple():
    global slider
    global slider1
    background.unblit_and_reblit()
    slider = thorpy.SliderX(100, (0, 35), "amount")
    slider1 = thorpy.SliderX(100, (0, 35), "sell price")
    button1 = thorpy.make_button("purchase", func=finishPurhcase)
    button = thorpy.make_button("done", func=begin)
    title_element = thorpy.make_text("add item", 35, (255, 255, 0))
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
    background.unblit_and_reblit()
    thorpy.launch_blocking_alert(title="Inventory check", text=store.inventory, ok_text="ok", font_size=12, font_color=(255, 255, 255))
    begin()


def begin():
    background.unblit_and_reblit()
    choices = [("addItem", buyProduceApple), ("checkStock", checkInventory)]
    thorpy.launch_blocking_choices("action selection", choices, parent=background)


screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
money = money(2000)
supplier = supplier()
store = store()
application = thorpy.Application((500, 500), "Launching alerts")
button = thorpy.make_button("Begin game", func=begin)
background = thorpy.Background.make(image=thorpy.style.EXAMPLE_IMG, elements=[button])
menu = thorpy.Menu(background)
product = ""
amount = 0
sellPrice = 0
slider = thorpy.SliderX(100, (12, 35), "amount")
slider1 = thorpy.SliderX(100, (12, 35), "sell price")

menu.play()

application.quit()
