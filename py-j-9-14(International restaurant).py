

while True:
    menuinternational=input("1.chinese 2.italian 3.persian 4.Appetizers 5.drinks 6.exit:")
    while True:
        match menuinternational:
            case "1":
                chinesemenu=input("1.fried rice 500 2.chow mein 700 3.kung pao chicken 900 4.spring rolls 600 5.dumplings 600 6.sweet and sour chicken 900 7.hot and sour soup 400 8.peking duck 2000 9.mapo tofu 800  10.wonton soup 300  11.exit :")
                match chinesemenu:
                    case "1":
                        numfriedrice=int(input("enter number:"))
                        friedriceprice=1.1*500*numfriedrice
                        print(friedriceprice)
                    case "2":
                        numchowmein=int(input("enter number:"))
                        chowmeinprice=1.1*700*numchowmein
                        print(chowmeinprice)
                    case "3":
                        numkungpaochicken=int(input("enter number:"))
                        kungpaochickenprice=1.1*900*numkungpaochicken
                        print(kungpaochickenprice)
                    case "4":
                        numspringrolls=int(input("enter number:"))
                        springrollsprice=1.1*600*numspringrolls
                        print(springrollsprice)
                    case "5":
                        numdumplings=int(input("enter number:"))
                        dumplingsprice=1.1*600*numdumplings
                        print(dumplingsprice)
                    case "6":
                        numsweetandsourchicken=int(input("enter number:"))
                        sweetandsourchickenprice=1.1*900*numsweetandsourchicken
                        print(sweetandsourchickenprice)
                    case "7":
                        numhotandsoursoup=int(input("enter number:"))
                        hotandsoursoupprice=1.1*400*numhotandsoursoup
                        print(hotandsoursoupprice)
                    case "8":
                        numpekingduck=int(input("enter number:"))
                        pekingduckprice=1.1*2000*numpekingduck
                        print(pekingduckprice)
                    case "9":
                        nummapotofu=int(input("enter number:"))
                        mapotofuprice=1.1*800*nummapotofu
                        print(mapotofuprice)
                    case "10":
                        numwontonsoup=int(input("enter number:"))
                        wontonsoupprice=1.1*300*numchowmein
                        print(wontonsoupprice)
                    case "11":
                        break
            case "2":
                italianmenu=input("1.pizza 1000 2.lasagna 1000 3.spaghetti 800 4.alfredo 800 5.ravioli 900 6.risotto 700 7.carbonara 800 8.gnocchi 700 9.sandwich 900 10.tiramisu 500 11.exit :")
                match italianmenu:
                    case "1":
                        numpizza=int(input("enter number:"))
                        pizzaprice=1.1*1000*numpizza
                        print(pizzaprice)
                    case "2":
                        numlasagna=int(input("enter number:"))
                        lasagnaprice=1.1*1000*numlasagna
                        print(lasagnaprice)
                    case "3":
                        numspaghetti=int(input("enter number:"))
                        spaghettiprice=1.1*800*numspaghetti
                        print(spaghettiprice)
                    case "4":
                        numalfredo=int(input("enter number:"))
                        alfredoprice=1.1*800*numalfredo
                        print(alfredoprice)
                    case "5":
                        numravioli=int(input("enter number:"))
                        ravioliprice=1.1*900*numravioli
                        print(ravioliprice)
                    case "6":
                        numrisotto=int(input("enter number:"))
                        risottoprice=1.1*700*numrisotto
                        print(risottoprice)
                    case "7":
                        numcarbonara=int(input("enter number:"))
                        carbonaraprice=1.1*800*numcarbonara
                        print(carbonaraprice)
                    case "8":
                        numgnocchi=int(input("enter number:"))
                        gnocchiprice=1.1*700*numgnocchi
                        print(gnocchiprice)
                    case "9":
                        numsandwich=int(input("enter number:"))
                        sandwichprice=1.1*900*numsandwich
                        print(sandwichprice)
                    case "10":
                        numtiramisu=int(input("enter number:"))
                        tiramisuprice=1.1*500*numtiramisu
                        print(tiramisuprice)
                    case "11":
                        break
            case "3":
                persianmenu=input("1.kebab 1000 2.ghormeh sabzi 700 3.fesenjan 800 4.gheimeh 700 5.zereshk polo 600 6.baghali polo 900 7.tahchin 700 8.dizi 800 9.joojeh kebab 500 10.kotlet 700 11.exit :")
                match persianmenu:
                    case "1":
                        numkebab=int(input("enter number:"))
                        kebabprice=1.1*1000*numkebab
                        print(kebabprice)
                    case "2":
                        numghormehsabzi=int(input("enter number:"))
                        ghormehsabziprice=1.1*700*numghormehsabzi
                        print(ghormehsabziprice)
                    case "3":
                        numfesenjan=int(input("enter number:"))
                        fesenjanprice=1.1*800*numfesenjan
                        print(fesenjanprice)
                    case "4":
                        numgheimeh=int(input("enter number:"))
                        gheimehprice=1.1*700*numgheimeh
                        print(gheimehprice)
                    case "5":
                        numzereshkpolo=int(input("enter number:"))
                        zereshkpoloprice=1.1*600*numzereshkpolo
                        print(zereshkpoloprice)
                    case "6":
                        numbaghalipolo=int(input("enter number:"))
                        baghalipoloprice=1.1*900*numbaghalipolo
                        print(baghalipoloprice)
                    case "7":
                        numtahchin=int(input("enter number:"))
                        tahchinprice=1.1*700*numtahchin
                        print(tahchinprice)
                    case "8":
                        numdizi=int(input("enter number:"))
                        diziprice=1.1*800*numdizi
                        print(diziprice)
                    case "9":
                        numjoojehkebab=int(input("enter number:"))
                        joojehkebabprice=1.1*500*numjoojehkebab
                        print(joojehkebabprice)
                    case "10":
                        numkotlet=int(input("enter number:"))
                        kotletprice=1.1*700*numkotlet
                        print(kotletprice)
                    case "11":
                        break
            case "4":
                appetizersmenu=input("1.french fries 300 2.onion rings 300 3.caesar salad 800 4.greek salad 400 5.garlic bread 400 6.chicken wings 400 7.mozzarella sticks 500 8.bruschetta 500 9.hummus 600 10.soup 300 11.exit :")
                match appetizersmenu :
                    case "1":
                        numfrenchfries=int(input("enter number:"))
                        frenchfriesprice=1.1*300*numfrenchfries
                        print(frenchfriesprice)
                    case "2":
                        numonionrings=int(input("enter number:"))
                        onionringsprice=1.1*300*numonionrings
                        print(onionringsprice)
                    case "3":
                        numcaesarsalad=int(input("enter number:"))
                        caesarsaladprice=1.1*800*numcaesarsalad
                        print(caesarsaladprice)
                    case "4":
                        numgreeksalad=int(input("enter number:"))
                        greeksaladprice=1.1*400*numgreeksalad
                        print(greeksaladprice)
                    case "5":
                        numgarlicbread=int(input("enter number:"))
                        garlicbreadprice=1.1*400*numgarlicbread
                        print(garlicbreadprice)
                    case "6":
                        numchickenwings=int(input("enter number:"))
                        chickenwingsprice=1.1*400*numchickenwings
                        print(chickenwingsprice)
                    case "7":
                        nummozzarellasticks=int(input("enter number:"))
                        mozzarellasteaksprice=1.1*500*nummozzarellasticks
                        print(mozzarellasteaksprice)
                    case "8":
                        numbruschetta=int(input("enter number:"))
                        bruschettaprice=1.1*500*numbruschetta
                        print(bruschettaprice)
                    case "9":
                        numhummus=int(input("enter number:"))
                        hummusprice=1.1*600*numhummus
                        print(hummusprice)
                    case "10":
                        numsoup=int(input("enter number:"))
                        soupprice=1.1*300*numsoup
                        print(soupprice)
                    case "11":
                        break
            case "5":
                drinksmenu=input("1.water 30 2.coca-cola 100 3.fanta 100 4.orange juice 200 5.apple juice 200 6.tea 150 7.coffee 250 8.lemonade 300 9.milkshake 400 10.latte 300 11.exit :")
                match drinksmenu:
                    case "1":
                        numwater=int(input("enter number:"))
                        waterprice=1.1*30*numwater
                        print(waterprice)
                    case "2":
                        numcocacola=int(input("enter number:"))
                        cocacolaprice=1.1*100*numcocacola
                        print(cocacolaprice)
                    case "3":
                        numfanta=int(input("enter number:"))
                        fantaprice=1.1*100*numfanta
                        print(fantaprice)
                    case "4":
                        numorangejuice=int(input("enter number:"))
                        orangejuiceprice=1.1*200*numorangejuice
                        print(orangejuiceprice)
                    case "5":
                        numapplejuice=int(input("enter number:"))
                        applejuiceprice=1.1*200*numapplejuice
                        print(applejuiceprice)
                    case "6":
                        numtea=int(input("enter number:"))
                        teaprice=1.1*150*numtea
                        print(teaprice)
                    case "7":
                        numcoffee=int(input("enter number:"))
                        coffeeprice=1.1*250*numcoffee
                        print(coffeeprice)
                    case "8":
                        numlemonade=int(input("enter number:"))
                        lemonadeprice=1.1*300*numlemonade
                        print(lemonadeprice)
                    case "9":
                        nummilkshake=int(input("enter number:"))
                        milkshakeprice=1.1*400*nummilkshake
                        print(milkshakeprice)
                    case "10":
                        numlatte=int(input("enter number:"))
                        latteprice=1.1*300*numlatte
                        print(latteprice)
                    case "11":
                        break
            case "6":
                break
            
                                                        
                                                            
                                                            
                                                            
                                                            
                                                            
                                                                                            
                                                        
                                                            
                                                        
                                                        
                                                        
                                                            
                                                        
                                                        
                                                                                                         
                                            
                                            
                                            
                                            
                                            
                                            
                                                
                                            
                                                
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                                


                                            
                                            
                                            
                                            
                                                

                                            
                                            
                                                