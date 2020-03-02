import pygame, thorpy
from supplier import supplier
from store import store
from money import money
def finishPurchase():
    global amount
    global product
    global sellPrice
    global slider
    global slider1
    amount = slider.get_value()
    sellPrice = slider1.get_value()
    product = ""
    if togglable_pool.get_selected():
        if amount.isdigit():
            if sellPrice.isdigit():
                if store.add(product, int(amount), supplier, int(sellPrice), money):
                    print("amount", amount)
                    print("sellPrice", sellPrice)
                    print("product", product)
                    successfulPurchase()
                else:
                    unSuccessfulPurchase()
    else:
        thorpy.launch_blocking_alert(title="No item selected",
                                     text="Please choose an item to purchase",
                                     ok_text="ok", font_size=12, font_color=(0, 0, 0))


def unSuccessfulPurchase():
    global product
    global amount

    thorpy.launch_blocking_alert(title="Error", text="Supplier does not have " + str(amount) + " " + product + " in stock", ok_text="ok", font_size=12, font_color=(0, 0, 0))

def checkStock():
    thorpy.launch_blocking_alert(title="Supplier check", text=supplier.availStockAsText(), ok_text="ok", font_size=12, font_color=(255, 255, 255))

def successfulPurchase():
    global product
    global amount
    thorpy.launch_blocking_alert(title="Success", text="purchased " + amount + " " + product, ok_text="ok", font_size=12, font_color=(0, 0, 0))

def checkInventory():
    #background = thorpy.Background.make(image="./pictures/wholeChicken.png")
    thorpy.launch_blocking_alert(title="Inventory check", text=store.availStockAsText(), ok_text="ok", font_size=12, font_color=(255, 255, 255))

money
amount = 0
product = ""
sellPrice = 0
supplier = supplier()
store = store()
pygame.init()
pygame.key.set_repeat(300, 30)
screen = pygame.display.set_mode((1000,1000))
screen.fill((255,255,255))
rect = pygame.Rect((0, 0, 50, 50))
rect.center = screen.get_rect().center
clock = pygame.time.Clock()

pygame.draw.rect(screen, (255,0,0), rect)
pygame.display.flip()

#declaration of some ThorPy elements ...
button1 = thorpy.make_button("purchase", func=finishPurchase)
button2 = thorpy.make_button("check Stock", func = checkStock)
button = thorpy.make_button("Check Inventory", func = checkInventory)
title_element = thorpy.make_text("add item", 35, (255, 255, 0))
slider = thorpy.Inserter(name="amount")
slider1 = thorpy.Inserter(name="sell price")
buttons = [thorpy.Togglable.make(str(i)) for i in supplier.availStockAsList()]
togglable_pool = thorpy.TogglablePool(buttons, first_value=buttons[0], always_value=True)
radio_and_toggable = buttons
elements = [title_element] + radio_and_toggable + [slider, slider1, button, button1, button2]
central_box = thorpy.Box.make(elements=elements)
central_box.fit_children(margins=(30, 30))
central_box.center()
central_box.add_lift()
central_box.set_main_color((220, 220, 220, 180))
#we regroup all elements on a menu, even if we do not launch the menu
menu = thorpy.Menu(central_box)
#important : set the screen as surface for all elements
for element in menu.get_population():
    element.surface = screen
#use the elements normally...
central_box.set_topleft((100,100))
central_box.blit()
central_box.update()

playing_game = True
while playing_game:
    clock.tick(45)
    for event in pygame.event.get():
        central_box.blit()
        central_box.update()
        if event.type == pygame.QUIT:
            playing_game = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, (255,255,255), rect) #delete old
                pygame.display.update(rect)
                rect.move_ip((-5,0))
                pygame.draw.rect(screen, (255,0,0), rect) #drat new
                pygame.display.update(rect)
        menu.react(event) #the menu automatically integrate your elements

pygame.quit()