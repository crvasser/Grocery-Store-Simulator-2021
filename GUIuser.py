import pygame, thorpy
from supplier import supplier
from store import store
from money import money
from events import events
from random import randint
import math

layout = pygame.image.load("./pictures/Layout.PNG")
layout1 = pygame.image.load("./pictures/gss.png")
layout2 = pygame.image.load("./pictures/gssgameover.png")
songs = ["Groovy", "Futuristic", "background"]
songnum = randint(0, 2)
songname = songs[songnum]
pygame.mixer.init()
pygame.mixer.music.load("./Music/" + songname + ".wav")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(.5)


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


def doubleCheck(myFloat):
    try:
        num = float(myFloat)
    except ValueError:
        return False
    return True


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
    global flagNotEnoughMoney
    madePurchase = 1
    flagUnavail = 0
    flagInvalidPrice = 0
    flagInvalidAmount = 0
    amount = slider.get_value()
    sellPrice = slider1.get_value()
    if len(product) != 0:
        if amount.isdigit():
            if doubleCheck(sellPrice):
                if money.getMoney() > supplier.sellerItemPrice(product) * int(amount):
                    if store.add(product, int(amount), supplier, float(sellPrice), money):
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
                    product = " "
                    flagNotEnoughMoney = 1  # you don't have enough money
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
    button = thorpy.make_button("Show Menu", func=makeBox)
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
    screen.fill(white, (
        screen.get_width() // 3 + screen.get_width() // 3, screen.get_height() // 14, screen.get_width() // 3,
        screen.get_height()))
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
        supplierText = myfont.render("${0}".format(round(supplier.stock[i][2], 2)), 1, (0, 0, 0))
        screen.blit(supplierText, (start, beginY - 15))
        supplierText = myfont.render("x" + str(supplier.stock[i][1]), 1, (0, 0, 0))
        screen.blit(supplierText, (start + 15, beginY + 65))
        start = start + 75
        if start == 1300 + 75 * 8:
            beginY = beginY + 130
            start = 1300
    supplierCollisionList.draw(screen)
    screen.blit(layout, (screen.get_width() // 3, screen.get_height() // 3))
    supplierUpdate = 0


def drawStartShopping(shopper):
    global customerCollisionList1

    shopper.rect.x = shopper.rect.x + 1
    customerCollisionList1.add(shopper)
    customerCollisionList1.draw(screen)
    customerCollisionList1.remove(shopper)


def drawFailedShopping(shopper):
    global customerCollisionList2
    if shopper.rect.x > screen.get_width() // 3:
        shopper.rect.x = shopper.rect.x - 1
        customerCollisionList2.add(shopper)
    customerCollisionList2.draw(screen)
    customerCollisionList2.remove(shopper)


def drawSuccessfulShopping(shopper, purchase):
    global customerCollisionList2

    if shopper.rect.x > screen.get_width() // 3:
        shopper.rect.x = shopper.rect.x - 1
        purchase.rect.x = shopper.rect.x - 60
        if purchase.rect.x > screen.get_width() // 3:
            customerCollisionList2.add(purchase)
        purchase.rect.y = shopper.rect.y
        customerCollisionList2.add(shopper)
    customerCollisionList2.draw(screen)
    customerCollisionList2.remove(purchase)
    customerCollisionList2.remove(shopper)


# Method to draw out the store inventory
# Makes selected sprites (unused currently)
def drawStoreInventory():
    global storeUpdate
    global storeCollisionList
    storeCollisionList = pygame.sprite.Group()
    screen.fill(white, (0, screen.get_height() // 14, screen.get_width() // 3, screen.get_height()))
    storeText = myfont.render("Store Inventory", 1, (0, 0, 0))
    screen.blit(storeText, (150, 125))
    start = 5
    beginY = 160
    for i in range(len(store.inventory)):
        tempItem = Item(500, 500, store.inventory[i], store.inventory[i][0])
        tempItem.rect.x = start
        tempItem.rect.y = beginY
        storeCollisionList.add(tempItem)
        storeText = myfont.render("${0}".format(round(store.inventory[i][2], 2)), 1, (0, 0, 0))
        screen.blit(storeText, (start, beginY - 15))
        storeText = myfont.render("x" + str(store.inventory[i][1]), 1, (0, 0, 0))
        screen.blit(storeText, (start + 15, beginY + 65))
        start = start + 75
        if start == 5 + 75 * 8:
            beginY = beginY + 130
            start = 5
    storeCollisionList.draw(screen)
    screen.blit(layout, (screen.get_width() // 3, screen.get_height() // 3))
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
    global flagNotEnoughMoney
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
    elif flagNotEnoughMoney == 1:
        title_element = thorpy.make_text("You don't have enough money", 15, (255, 0, 0))
    flagNotEnoughMoney = 0
    flagUnavail = 0
    flagInvalidPrice = 0
    flagInvalidAmount = 0
    # Text inserter setup, madePurchase if statements ensures text won't be blanked out on event call
    if madePurchase == 0:
        oldSlider = slider.get_value()
    slider = thorpy.Inserter(name="Amount")
    if madePurchase == 0:
        slider.set_value(oldSlider)
    if madePurchase == 0:
        oldSlider1 = slider1.get_value()
    slider1 = thorpy.Inserter(name="Sell Price")
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
    central_box.set_topleft((screen.get_width() // 3, 80))
    central_box.blit()
    central_box.update()
    madePurchase = 0
    screen.blit(layout, (screen.get_width() // 3, screen.get_height() // 3))
    if len(text) != 0:
        screen.blit(eventText, (5, 60))
    storeUpdate = 1
    supplierUpdate = 1


def drawStartMenu():
    screen.blit(layout, (screen.get_width() // 3, screen.get_height() // 3))


def drawShopLifting(shoplifter):
    global shoplifterCollisionList
    shoplifter.rect.x = shoplifter.rect.x + 1
    shoplifterCollisionList.add(shoplifter)
    shoplifterCollisionList.draw(screen)
    shoplifterCollisionList.remove(shoplifter)


def drawRobbing(robber):
    global robberCollisionList
    if robber.rect.x < screen.get_width() / 3 + 200:
        robber.rect.x = robber.rect.x + 1
    else:
        if robber.rect.y < screen.get_height() / 3 + 370:
            robber.rect.y = robber.rect.y + 1
    robberCollisionList.add(robber)
    robberCollisionList.draw(screen)
    robberCollisionList.remove(robber)


def drawReturnRobbing(robber, stolenAmount):
    global robberCollisionList

    if robber.rect.y > screen.get_height() // 3 + 290:
        stolenString = "-$" + str(stolenAmount)
        stolenText = myfont.render(stolenString, 1, (0, 0, 0))
        screen.blit(stolenText, (robber.rect.x + 20, robber.rect.y))
    if robber.rect.x > screen.get_width() // 3:
        if robber.rect.y > screen.get_height() // 3 + 270:
            robber.rect.y = robber.rect.y - 1
        else:
            robber.rect.x = robber.rect.x - 1
        robberCollisionList.add(robber)
    robberCollisionList.draw(screen)
    robberCollisionList.remove(robber)


def drawReturnShoplifting(shoplifter):
    global shoplifterCollisionList
    if shoplifter.rect.x > screen.get_width() // 3:
        shoplifter.rect.x = shoplifter.rect.x - 1
        shoplifterCollisionList.add(shoplifter)
    shoplifterCollisionList.draw(screen)
    shoplifterCollisionList.remove(shoplifter)


flagNotEnoughMoney = 0
shopping = 0
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
inMenu = True
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
flagUnavail = 0
flagInvalidPrice = 0
flagInvalidAmount = 0
screen.fill((255, 255, 255))
rect = pygame.Rect((0, 0, 50, 50))
rect.center = screen.get_rect().center
clock = pygame.time.Clock()
red = (255, 0, 0)
score = 0
startShopping = 1
customer = events()
pygame.display.flip()
white = (255, 255, 255)
# declaration of some ThorPy elements ...
money = money(5000)
supplierUpdate = 1
storeUpdate = 1

shopSuccess = 0
shopFail = 0
supplierCollisionList = pygame.sprite.Group()
customerCollisionList1 = pygame.sprite.Group()
customerCollisionList2 = pygame.sprite.Group()
menuCollisionList = pygame.sprite.Group()
storeCollisionList = list()
# we regroup all elements on a menu, even if we do not launch the menu
screen.blit(layout, (screen.get_width() // 3, screen.get_height() // 3))
curTime = pygame.time.get_ticks()
curTime1 = pygame.time.get_ticks()
curTime2 = pygame.time.get_ticks()
shoplifterTime = pygame.time.get_ticks()
shoplifterCollisionList = pygame.sprite.Group()
robberTime = pygame.time.get_ticks()


songTime = pygame.time.get_ticks()
robberCollisionList = pygame.sprite.Group()
startClearing = 0
text = ""
amountMovex = 0
eventText = myfont.render("{0}".format(text), 1, (0, 0, 0))
playing_game = True
inExit = True
menuClock = pygame.time.Clock()

while inMenu:
    menuClock.tick(45)
    startButton = Item(500, 500, "start", "Apples")  # this should have start button image
    quitButton = Item(500, 500, "quit", "Bananas")  # this should have quit button image
    quitButton.rect.x = screen.get_width() // 3 + 400
    quitButton.rect.y = screen.get_height() // 3
    startButton.rect.y = screen.get_height() // 3
    startButton.rect.x = screen.get_width() // 3
    menuCollisionList.add(quitButton)
    menuCollisionList.add(startButton)
    menuCollisionList.draw(screen)
    pygame.event.pump()
    pygame.display.flip()
    screen.blit(layout1, (0, 0))  # this should have the actual title image
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked = [c for c in menuCollisionList if c.rect.collidepoint(pos)]
            if len(clicked) != 0:
                if clicked[0].name == "start":
                    inMenu = False
                    makeBox()
                if clicked[0].name == "quit":
                    inMenu = False
                    playing_game = False
                    inExit = False
                    pygame.mixer.music.stop()
        if event.type == pygame.QUIT:
            inMenu = False
            pygame.mixer.quit()
            playing_game = False
            inExit = False
stolen = False
startShopLifting = 0
firstShoplifter = 0
startRobbing = 0
firstRobber = 0
while playing_game:
    clock.tick(45)

    if songTime + 60000 < pygame.time.get_ticks():
        songTime = pygame.time.get_ticks()
        songnum = randint(0, 2)
        songname = songs[songnum]
        pygame.mixer.init()
        pygame.mixer.music.load("./Music/" + songname + ".wav")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(.5)

    pygame.display.flip()
    screen.blit(layout, (screen.get_width() // 3, screen.get_height() // 3))
    if startShopping == 1:
        newShopper = Item(500, 500, "customer", "Customer1")  # this will be customer sprite
        newShopper.rect.x = screen.get_width() // 3
        newShopper.rect.y = screen.get_height() // 3 + 270
        startShopping = 0
    drawStartShopping(newShopper)
    if shopSuccess == 1 and shopFail == 0:
        drawSuccessfulShopping(curShopper, purchase)
    if shopFail == 1 and shopSuccess == 0:
        drawFailedShopping(curShopper)
    if startShopLifting == 1:
        drawShopLifting(shoplifter)
    if startShopLifting == 0 and firstShoplifter == 1:
        drawReturnShoplifting(curShoplifter)  # stolen product would be added here
    if startRobbing == 1:
        drawRobbing(robber)
    if startRobbing == 0 and firstRobber == 1:
        drawReturnRobbing(curRobber, stolenAmount)
    # After 20000 ticks have a random event happen that affects the market
    if curTime2 + 20000 < pygame.time.get_ticks():
        curTime2 = pygame.time.get_ticks()
        text = customer.supplierRandomPriceChange(supplier)
        eventText = myfont.render("{0}".format(text), 1, (0, 0, 0))
        screen.fill(white, (0, 0, screen.get_width(), 100))
        storeUpdate = 1
        supplierUpdate = 1
        screen.blit(eventText, (5, 60))

    if shoplifterTime + 22000 < pygame.time.get_ticks() and startShopLifting == 0:  # change time added to shoplifting time for balance keep the 2k offset to avoid overlap
        firstShoplifter = 1
        shoplifterTime = pygame.time.get_ticks()
        shoplifter = Item(500, 500, "shoplifter", "Shoplifter")
        shoplifter.rect.x = screen.get_width() // 3
        shoplifter.rect.y = screen.get_height() // 3 + 270
        startShopLifting = 1
    if shoplifterTime + 10000 < pygame.time.get_ticks() and startShopLifting == 1:  # keep this as is

        shoplifterTime = pygame.time.get_ticks()
        stolen = customer.shoplifterStealProduct(store)
        if stolen:
            curShoplifter = Item(500, 500, "Shoplifter-1", "Shoplifter-1")
        else:
            curShoplifter = shoplifter
        curShoplifter.rect.x = shoplifter.rect.x
        curShoplifter.rect.y = shoplifter.rect.y
        startShopLifting = 0
        storeUpdate = 1
    if robberTime + 32000 < pygame.time.get_ticks() and startRobbing == 0:
        firstRobber = 1
        robberTime = pygame.time.get_ticks()
        robber = Item(500, 500, "robber", "Robber")
        robber.rect.x = screen.get_width() // 3
        robber.rect.y = screen.get_height() // 3 + 270
        startRobbing = 1
    if robberTime + 10000 < pygame.time.get_ticks() and startRobbing == 1:
        curRobber = robber
        robberTime = pygame.time.get_ticks()
        stolenAmount = customer.robberStealMoney(money)
        startRobbing = 0
    # After 500 ticks take away 10 dollars in taxes
    if curTime + 10000 < pygame.time.get_ticks():
        money.setMoney(money.getMoney() - ((money.getMoney() * 0.025) + 50))
        curTime = pygame.time.get_ticks()
    # After 10000 ticks have a customer come in and buy some random items
    if curTime1 + 10000 < pygame.time.get_ticks():
        shopFail = 0
        shopSuccess = 0
        startShopping = 1
        curShopper = newShopper
        curTime1 = pygame.time.get_ticks()
        if len(store.inventory) != 0:
            test = customer.customerBuyProduct(store, money)
            print("test = ", test)
            if test == 0:
                shopFail = 1
                shopSuccess = 0
            else:
                purchase = Item(500, 500, "customer", test)
                shopSuccess = 1
                shopFail = 0
            makeBox()
        else:
            shopFail = 1
            shopSuccess = 0
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
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            playing_game = False
            inExit = False
            break
        #        elif event.type == pygame.KEYDOWN:
        #            if event.key == pygame.K_LEFT:
        #                pygame.draw.rect(screen, (255,255,255), rect) #delete old
        #                pygame.display.update(rect)
        #               rect.move_ip((-5,0))
        #                pygame.draw.rect(screen, (255,0,0), rect) #drat new
        #                pygame.display.update(rect)
        menu.react(event)  # the menu automatically integrate your elements
        if len(supplier.inventory) == 0 and len(store.inventory) == 0:
            playing_game = False
exitClock = pygame.time.Clock()
exitCollisionList = pygame.sprite.Group()
screen.fill(white)
while inExit:
    exitClock.tick(45)
    quitButton = Item(500, 500, "quit", "Bananas")  # this should have quit button image
    quitButton.rect.x = screen.get_width() // 3 + 400
    quitButton.rect.y = screen.get_height() // 3
    exitCollisionList.add(quitButton)
    screen.blit(layout2, (0, 0))
    exitCollisionList.draw(screen)

    pygame.event.pump()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked = [c for c in exitCollisionList if c.rect.collidepoint(pos)]
            if len(clicked) != 0:
                if clicked[0].name == "quit":
                    inExit = False
        if event.type == pygame.QUIT:
            inExit = False

pygame.quit()
