# name of student: Ali Goutsal 
# number of student: 1
# purpose of program: Zo zie je hoeveel munten je van een bepaalde muntsoort moet uitkeren  
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # Vraag aan de gebruiker hoeveel hij moet betalen en zet het bedrag om naar een int
paid = int(float(input('Paid amount: ')) * 100) # Het bedrag dat is betaalt en in een int omgezet is
change = paid - toPay # Wisselgeld
coin500 = 0
coin300 = 0
coin200 = 0 
coin100 = 0
coin50 = 0
coin20 = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0

if change > 0: # Als het wisselgeld groter is dan 0
  coinValue = 500 # Het variabele CoinValue krijgt de waarde 500 cent
  
  while change > 0 and coinValue > 0: # Terwijl de wisselgeld groter is dan 0 en de CoinValue groter is dan 0
    nrCoins = change // coinValue # De wisselgeld delen door het coinValue en de uitkomst afronden

    if nrCoins > 0: # Als het aantal munten groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Laat zien hoeveel muntjes je moet uitkeren
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Vul hoeveel muntjes je hebt uitgekeerd
      change -= nrCoinsReturned * coinValue # Het bedrag die overblijft die nog uitgekeerd moet worden

# comment on code below: 
    if coinValue == 500:
      coin500 = nrCoinsReturned
      coinValue = 300
    elif coinValue == 300:
      coin300 = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      coin200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      coin100 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      coin50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      coin20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      coin10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      coin5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      coin2 = nrCoinsReturned
      coinValue = 1
    #elif coinValue == 1:
     # coin1 = nrCoinsReturned
    else:
      coinValue = 0
if change > 0: # Het bedrag dat overblijft en niet uitgekeerd is
    print('Change not returned: ', str(change) + ' cents')
else:
  if coin500 > 0:
    print("U heeft",coin500, "munten van 500 centen gekregen")
  if coin300 > 0:
    print("U heeft",coin300, "munten van 300 centen gekregen")
  if coin200 > 0:
    print("U heeft",coin200, "munten van 200 centen gekregen")
  if coin100 >0:
    print("U heeft",coin100, "munten van 200 centen gekregen")
  if coin50 > 0:
    print("U heeft",coin50, "munten van 50 centen gekregen")
  if coin20 > 0:
    print("U heeft",coin20, "munten van 20 centen gekregen")
  if coin10 > 0: 
    print("U heeft",coin10, "munten van 10 centen gekregen")
  if coin5 > 0: 
    print("U heeft",coin5, "munten van 5 centen gekregen")
  if coin2 > 0:  
    print("U heeft",coin2, "munten van 2 centen gekregen")
 # if coin1 > 0:
  #  print("U heeft",coin1, "munten van 1 centen gekregen")
    print('done')