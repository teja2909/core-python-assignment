def taxi_fare(trips):
    total_fare=0
    for i in range(len(trips)):
        fare = trips[i]*10+50
        print(f"Trip{i+1}:${fare}")
        total_fare+=fare
    print(f"Total Fare: ${total_fare}")
print("Base fare: $50")
trips=list(map(int,input("Distances in km:").split(',')))
taxi_fare(trips)