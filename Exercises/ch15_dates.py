from datetime import datetime
import datedelta as dd
import datetime as dt

while True:
    start_date = input("""Enter subscription start date 
(dd/mm/yyyy or enter 'today' if applicable): """)
    if start_date == "today":
        start_date = dt.date.today()
    else: 
        start_date = datetime.strptime(start_date, "%d/%m/%Y")

    subs_dur = input("Enter subscription duation (Xw, Xm, Xy): ")
    duration_num = int(subs_dur[:-1])
    duration_units = subs_dur[-1]
    
    if duration_units == 'w':
        duration_num = dd.datedelta(days=(duration_num*7))
    elif duration_units == 'm':
        duration_num = dd.datedelta(months=duration_num)
    elif duration_units == 'y':
        duration_num = dd.datedelta(years=duration_num)
    
    end_date = start_date + duration_num
    print(f"Subscription ends: {end_date}")

    more = input("Would you like to continue? y/n: ")
    if more == 'n':
        break