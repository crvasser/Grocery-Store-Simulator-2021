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
    global togglable_pool
    amount = slider.get_value()
    sellPrice = slider1.get_value()
    product = ""
    if togglable_pool.get_selected():
        product = togglable_pool.get_selected().get_text()
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



def successfulPurchase():
    global product
    global amount
    makeBox()

def hideMenu():
    global screen
    global white
    global hideMenuStat
    global central_box
    screen.fill(white)
    hideMenuStat = 1
    button = thorpy.make_button("show menu", func=makeBox)
    central_box = thorpy.Box.make(elements=[button])
    central_box.fit_children(margins=(30, 30))
    central_box.center()
    central_box.add_lift()
    central_box.set_main_color((220, 220, 220, 180))
    menu = thorpy.Menu(central_box)
    for element in menu.get_population():
        element.surface = screen
    central_box.set_topleft((100, 100))
    central_box.blit()
    central_box.update()


def makeBox():
    global central_box
    global menu
    global slider
    global slider1
    global togglable_pool
    global hideMenuStat
    global white
    global screen
    screen.fill(white)
    hideMenuStat = 0
    button0 = thorpy.make_button("hide menu", func=hideMenu)
    button1 = thorpy.make_button("purchase", func=finishPurchase)
    button3 = thorpy.make_button(text="store inventory\n" + store.availStockAsText())
    button4 = thorpy.make_button(text="supplier inventory\n" + supplier.availStockAsText())
    title_element = thorpy.make_text("Grocery Store Sim", 35, (255, 255, 0))
    slider = thorpy.Inserter(name="amount")
    slider1 = thorpy.Inserter(name="sell price")
    buttons = [thorpy.Togglable.make(str(i)) for i in supplier.availStockAsList()]
    togglable_pool = thorpy.TogglablePool(buttons, first_value=buttons[0], always_value=True)
    radio_and_toggable = buttons
    elements = [button0] + [title_element] + radio_and_toggable + [slider, slider1, button1, button3, button4]
    central_box = thorpy.Box.make(elements=elements)
    central_box.fit_children(margins=(30, 30))
    central_box.center()
    central_box.add_lift()
    central_box.set_main_color((220, 220, 220, 180))
    menu = thorpy.Menu(central_box)
    for element in menu.get_population():
        element.surface = screen
    central_box.set_topleft((100, 100))
    central_box.blit()
    central_box.update()

pygame.init()
myfont = pygame.font.SysFont("monospace", 16)
togglable_pool = 0
slider = 0
slider1 = 0
menu = 0
central_box = 0
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
score = 0
pygame.draw.rect(screen, (255,0,0), rect)
pygame.display.flip()
white = (255,255,255)
#declaration of some ThorPy elements ...
money = money(2000)
makeBox()
#we regroup all elements on a menu, even if we do not launch the menu


playing_game = True
while playing_game:
    clock.tick(45)
    pygame.display.flip()
    screen.fill(white, (0, 0, screen.get_width()//8, screen.get_height()//16))
    scoretext = myfont.render("Money {0}".format(money.getMoney()), 1, (0,0,0))
    screen.blit(scoretext, (5, 10))
    score += 1
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