eth_in_pool=100
solid_in_pool=100

total_eth_in_wallet=0
total_solid_in_wallet=100
window=0.1
while(1):
    price=eth_in_pool/solid_in_pool
    print("current_price: "+str(price)+" eth/solid",end=" ")
    
    eth_in_pool-=1/window
    total_eth_in_wallet+=1/window
    print(str(1/window)+" eth bought",end=" ")
    
    solid_in_pool+=(1/price)/window
    total_solid_in_wallet-=(1/price)/window
    print(str(1/price/window)+" solid sold\n")

    if(total_solid_in_wallet)<=0:
        break

print("total eth in wallet: "+str(total_eth_in_wallet))
print("total solid in wallet: "+str(total_solid_in_wallet))
