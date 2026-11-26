loads={"Laboratories":(3,10),"Hostels":(3,10),"Academic":(2,10),"Library":(1,10)}
for name,(demand,capacity) in loads.items():
    print(f"{name}: {demand} Gbps / {capacity} Gbps = {demand/capacity:.0%} utilisation")
