runs={"Consulting rooms max":80,"Pharmacy":96,"Waiting hall AP":60,"Building backbone":420}
for name,m in runs.items():
    print(f"{name}: {m} m -> "+("within 90 m permanent-link limit" if m<=90 else "exceeds 90 m; redesign/use fibre"))
print("Copper channel maximum is 100 m including patch cords.")
