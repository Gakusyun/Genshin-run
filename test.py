key={}
for i in input():
    try:
        key[i] +=1
    except:
        key[i] = 1
if key["启"] > 0 and key["动"] > 0:
    run = True
    if key["卸"] > 0 and key["载"] > 0:
        if key["启"]+key["启"]<key["卸"]+key["载"]:
            uninstall = True
            run = False
if key["卸"] > 0 and key["载"] > 0:
    uninstall = True
    if key["启"] > 0 and key["动"] > 0:
        if key["启"]+key["动"]>key["卸"]+key["载"]:
            run = True
            uninstall = False
if run == True and uninstall == True:
    print("启动牛魔大酬宾")
if run == True and uninstall == False:
    print("Run")
if run == False and uninstall == True:
    print("Uninstall")
if run == False and uninstall == False:
    print("Not Run and Not Uninstall")