import pygame, thorpy
from supplier import supplier
from store import store
from money import money
from events import events

layout = pygame.image.load("./pictures/Layout.PNG")


# method called when purchase is made
# attempts to buy items from the supplier based on amounts entered
# returns with flags set for any errors that occurred
def finishPurchase():
    global amount
    global product
    global sellPrice
    global slider
    global slider1
    global togglable_pool
    global flagUnavail
    global flagInvalidPrice
    global flagInvalidAmount
    global madePurchase
    madePurchase = 1
    flagUnavail = 0
    flagInvalidPrice = 0
    flagInvalidAmount = 0
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
                    flagUnavail = 1  # supplier doesn't have enough of that item
                    makeBox()
            else:
                flagInvalidPrice = 1  # invalid price entered
                makeBox()
        else:
            flagInvalidAmount = 1  # invalid amount entered
            makeBox()


# called when item is actually brought from supplier
# and moved into store inventory
# updates box
def successfulPurchase():
    makeBox()


# hides menu
# makes new box to show menu
def hideMenu():
    global screen
    global white
    global central_box
    global menu
    screen.fill(white)
    button = thorpy.make_button("show menu", func=makeBox)
    central_box = thorpy.Box.make(elements=[button])
    central_box.fit_children(margins=(30, 30))
    central_box.center()
    central_box.add_lift()
    central_box.set_main_color((220, 220, 220, 180))
    menu = thorpy.Menu(central_box)
    screen.fill(white)
    for element in menu.get_population():
        element.surface = screen
    central_box.set_topleft((100, 100))
    central_box.blit()
    central_box.update()
    screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))


# Main GUI setup
# Makes box with title of game, buttons to select items from store inventory,
# Text boxes to add amount and cost of item, and a purchase button
# Error messages are displayed in red text below title when they occur
def makeBox():
    global central_box
    global button3
    global menu
    global slider
    global slider1
    global togglable_pool
    global white
    global screen
    global flagUnavail
    global flagInvalidPrice
    global flagInvalidAmount
    global madePurchase
    screen.fill(white)
    button0 = thorpy.make_button("Hide menu", func=hideMenu)
    button1 = thorpy.make_button("Purchase", func=finishPurchase)
    # make store inventory and supplier inventory buttons if they are needed
    if len(store.availStockAsText()) != 0:
        button3 = thorpy.make_button(text="Store inventory\n" + store.availStockAsText())
    else:
        button3 = thorpy.make_button(text="Store inventory empty")
    if len(supplier.availStockAsText()) != 0:
        button4 = thorpy.make_button(text="Supplier inventory\n" + supplier.availStockAsText())
    else:
        button4 = thorpy.make_button(text="Supplier inventory empty")
    title_element0 = thorpy.make_text("Grocery Store Sim 2021", 25, (255, 255, 0))
    title_element = thorpy.make_text("123", 0, (255, 255, 0))
    # updates error msg based on flag received when purchasing
    if flagUnavail == 1:
        title_element = thorpy.make_text("Supplier Does not have enough", 15, (255, 0, 0))
    elif flagInvalidPrice == 1:
        title_element = thorpy.make_text("Invalid price entered", 15, (255, 0, 0))
    elif flagInvalidAmount == 1:
        title_element = thorpy.make_text("Invalid amount entered", 15, (255, 0, 0))
    flagUnavail = 0
    flagInvalidPrice = 0
    flagInvalidAmount = 0
    # Text inserter setup, madePurchase if statements ensures text won't be blanked out on event call
    if madePurchase == 0:
        oldSlider = slider.get_value()
    slider = thorpy.Inserter(name="amount")
    if madePurchase == 0:
        slider.set_value(oldSlider)
    if madePurchase == 0:
        oldSlider1 = slider1.get_value()
    slider1 = thorpy.Inserter(name="sell price")
    if madePurchase == 0:
        slider1.set_value(oldSlider1)
    buttons = [thorpy.Togglable.make(str(i)) for i in supplier.availStockAsList()]
    if len(buttons) == 0:
        buttons = [thorpy.Togglable.make("No Supplier stock")]
    togglable_pool = thorpy.TogglablePool(buttons, first_value=buttons[0], always_value=True)
    radio_and_toggable = buttons
    elements = [title_element0] + [button0] + [title_element] + radio_and_toggable + [slider, slider1, button1, button3,
                                                                                      button4]
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
    madePurchase = 0
    screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))


madePurchase = 1
button3 = 0
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
screen = pygame.display.set_mode((1000, 1000))
flagUnavail = 0
flagInvalidPrice = 0
flagInvalidAmount = 0
screen.fill((255, 255, 255))
rect = pygame.Rect((0, 0, 50, 50))
rect.center = screen.get_rect().center
clock = pygame.time.Clock()
score = 0
customer = events()
pygame.display.flip()
white = (255, 255, 255)
# declaration of some ThorPy elements ...
money = money(2000)
makeBox()
# we regroup all elements on a menu, even if we do not launch the menu
screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))
curTime = pygame.time.get_ticks()
curTime1 = pygame.time.get_ticks()
playing_game = True
while playing_game:
    clock.tick(45)
    pygame.display.flip()
    # After 500 ticks take away 10 dollars in taxes
    if curTime + 500 < pygame.time.get_ticks():
        money.setMoney(money.getMoney() - 10)
        curTime = pygame.time.get_ticks()
    # After 10000 ticks have a customer come in and buy some random items
    if curTime1 + 10000 < pygame.time.get_ticks():
        curTime1 = pygame.time.get_ticks()
        if len(store.inventory) != 0:
            customer.customerBuyProduct(store, money)
            makeBox()
    # After 60000 ticks have a random event happen that affects the market
    if curTime1 + 60000 < pygame.time.get_ticks():
        eventText = myfont.render(customer.supplierRandomPriceChange(supplier), False, (0, 0, 0))
        screen.blit(eventText, (50, 10))
    screen.fill(white, (0, 0, screen.get_width() // 8, screen.get_height() // 16))
    scoretext = myfont.render("Money {0}".format(round(money.getMoney(), 2)), 1, (0, 0, 0))
    screen.blit(scoretext, (5, 10))
    # When money hits 0, game over
    if money.getMoney() < 0:
        playing_game = False
    # Mostly unused event handler, keeping it as reference
    for event in pygame.event.get():
        central_box.blit()
        central_box.update()
        if event.type == pygame.QUIT:
            playing_game = False
            break
        #        elif event.type == pygame.KEYDOWN:
        #            if event.key == pygame.K_LEFT:
        #                pygame.draw.rect(screen, (255,255,255), rect) #delete old
        #                pygame.display.update(rect)
        #               rect.move_ip((-5,0))
        #                pygame.draw.rect(screen, (255,0,0), rect) #drat new
        #                pygame.display.update(rect)
        menu.react(event)  # the menu automatically integrate your elements
pygame.quit()
