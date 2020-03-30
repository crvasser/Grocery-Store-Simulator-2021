import pygame, thorpy
from supplier import supplier
from store import store
from money import money
from events import events

layout = pygame.image.load("./pictures/Layout.PNG")
layout1 = pygame.image.load("./pictures/apple.png")


class Item(pygame.sprite.Sprite):
    def __init__(self, width, height, itemName, fileName):
        super().__init__()
        self.name = itemName
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        actualFileName = "./pictures/TSP/" + fileName + ".png"
        self.image = pygame.image.load(actualFileName).convert_alpha()
        self.rect = self.image.get_rect()


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
    if len(product) != 0:
        if amount.isdigit():
            if sellPrice.isdigit():
                if store.add(product, int(amount), supplier, int(sellPrice), money):
                    print("amount", amount)
                    print("sellPrice", sellPrice)
                    print("product", product)
                    product = ""
                    successfulPurchase()

                else:
                    product = ""
                    flagUnavail = 1  # supplier doesn't have enough of that item
                    makeBox()
            else:
                product = ""
                flagInvalidPrice = 1  # invalid price entered
                makeBox()
        else:
            product = ""
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
    global text
    global eventText
    screen.fill(white)
    button = thorpy.make_button("show menu", func=makeBox)
    central_box = thorpy.Box.make(elements=[button])
    central_box.fit_children(margins=(30, 30))
    central_box.center()
    central_box.add_lift()
    central_box.set_main_color((220, 220, 220, 180))
    menu = thorpy.Menu(central_box)
    screen.fill(white)
    if len(text) != 0:
        screen.blit(eventText, (5, 60))
    for element in menu.get_population():
        element.surface = screen
    central_box.set_topleft((100, 100))
    central_box.blit()
    central_box.update()
    screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))


# Method to draw out supplier invetory
# Creates clickable sprites
# Clicked sprites are assigned to the product value used when purchasing
def drawSupplierInventory():
    global supplierUpdate
    global supplierCollisionList
    supplierCollisionList = pygame.sprite.Group()
    supplierText = myfont.render("Supplier Inventory", 1, (0, 0, 0))
    screen.blit(supplierText, (1500, 125))
    start = 1300
    beginY = 160
    for i in range(len(supplier.stock)):
        tempItem = Item(500, 500, supplier.stock[i], supplier.stock[i][0])
        tempItem.rect.x = start
        tempItem.rect.y = beginY
        supplierCollisionList.add(tempItem)
        supplierText = myfont.render("$" + str(supplier.stock[i][2]), 1, (0, 0, 0))
        screen.blit(supplierText, (start, beginY - 15))
        supplierText = myfont.render("x" + str(supplier.stock[i][1]), 1, (0, 0, 0))
        screen.blit(supplierText, (start + 15, beginY + 65))
        start = start + 75
        if start == 1300 + 75 * 8:
            beginY = beginY + 130
            start = 1300
    supplierCollisionList.draw(screen)
    screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))
    supplierUpdate = 0


# Method to draw out the store inventory
# Makes selected sprites (unused currently)
def drawStoreInventory():
    global storeUpdate
    global storeCollisionList
    storeCollisionList = pygame.sprite.Group()
    storeText = myfont.render("store Inventory", 1, (0, 0, 0))
    screen.blit(storeText, (150, 125))
    start = 5
    beginY = 160
    for i in range(len(store.inventory)):
        tempItem = Item(500, 500, store.inventory[i], store.inventory[i][0])
        tempItem.rect.x = start
        tempItem.rect.y = beginY
        storeCollisionList.add(tempItem)
        storeText = myfont.render(str(store.inventory[i][2]) + "$", 1, (0, 0, 0))
        screen.blit(storeText, (start, beginY - 15))
        storeText = myfont.render("x" + str(store.inventory[i][1]), 1, (0, 0, 0))
        screen.blit(storeText, (start + 15, beginY + 65))
        start = start + 75
        if start == 5 + 75 * 8:
            beginY = beginY + 130
            start = 5
    storeCollisionList.draw(screen)
    screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))
    storeUpdate = 0


# Main GUI setup
# Makes box with title of game, buttons to select items from store inventory,
# Text boxes to add amount and cost of item, and a purchase button
# Error messages are displayed in red text below title when they occur
def makeBox():
    global central_box
    global product
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
    global storeUpdate
    global supplierUpdate
    global text
    global eventText
    screen.fill(white)
    if len(text) != 0:
        screen.blit(eventText, (5, 60))
    button0 = thorpy.make_button("Hide menu", func=hideMenu)
    button1 = thorpy.make_button("Purchase", func=finishPurchase)
    button2 = thorpy.make_text("Please Select an Item to Purchase", 15, (0, 0, 0))
    if len(product) != 0:
        button2 = thorpy.make_text(product + " Selected", 15, (0, 0, 0))
    title_element0 = thorpy.make_text("Supplier Purchase Menu", 25, (255, 255, 0))
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
    elements = [title_element0] + [button0] + [title_element] + [button2, slider, slider1, button1,
                                                                 ]
    central_box = thorpy.Box.make(elements=elements)
    central_box.fit_children(margins=(30, 30))
    central_box.center()
    central_box.set_main_color((220, 220, 220, 180))
    menu = thorpy.Menu(central_box)
    for element in menu.get_population():
        element.surface = screen
    central_box.set_topleft((screen.get_width() / 3, 80))
    central_box.blit()
    central_box.update()
    madePurchase = 0
    screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))
    if len(text) != 0:
        screen.blit(eventText, (5, 60))
    storeUpdate = 1
    supplierUpdate = 1

text = ""
madePurchase = 1
button3 = 0
pygame.init()
myfont = pygame.font.SysFont("monospace", 16)
eventFont = pygame.font.SysFont("monospace", 12)
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
screen = pygame.display.set_mode((1920, 1080))
flagUnavail = 0
flagInvalidPrice = 0
flagInvalidAmount = 0
screen.fill((255, 255, 255))
rect = pygame.Rect((0, 0, 50, 50))
rect.center = screen.get_rect().center
clock = pygame.time.Clock()
red = (255, 0, 0)
score = 0
customer = events()
pygame.display.flip()
white = (255, 255, 255)
# declaration of some ThorPy elements ...
money = money(2000)
supplierUpdate = 1
storeUpdate = 1
makeBox()
supplierCollisionList = pygame.sprite.Group()
storeCollisionList = list()
# we regroup all elements on a menu, even if we do not launch the menu
screen.blit(layout, (screen.get_width() / 3, screen.get_height() / 3))
curTime = pygame.time.get_ticks()
curTime1 = pygame.time.get_ticks()
curTime2 = pygame.time.get_ticks()
text = ""
eventText = myfont.render("{0}".format(text), 1, (0, 0, 0))
playing_game = True
while playing_game:
    clock.tick(45)
    pygame.display.flip()
    # After 60000 ticks have a random event happen that affects the market
    if curTime2 + 60000 < pygame.time.get_ticks():
        curTime2 = pygame.time.get_ticks()
        text = customer.supplierRandomPriceChange(supplier)
        eventText = myfont.render("{0}".format(text), 1, (0, 0, 0))
        screen.fill(white)
        screen.blit(eventText, (5, 60))

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
    screen.fill(white, (0, 0, screen.get_width() // 8, screen.get_height() // 20))
    scoretext = myfont.render("Money {0}".format(round(money.getMoney(), 2)), 1, (0, 0, 0))
    screen.blit(scoretext, (5, 10))
    if supplierUpdate == 1:
        drawSupplierInventory()
    if storeUpdate == 1:
        drawStoreInventory()
    # When money hits 0, game over
    if money.getMoney() < 0:
        playing_game = False

    # Mostly unused event handler, keeping it as reference
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked = [c for c in supplierCollisionList if c.rect.collidepoint(pos)]
            if len(clicked) != 0:
                print("clicked = ", clicked[0].name)
                product = clicked[0].name[0]
                makeBox()
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
