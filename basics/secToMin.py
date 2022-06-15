t = int(input("Time in seconds:- "))
secs = t % 60
mins = (t -secs)/60

print(mins, " mins ", secs,"secs")