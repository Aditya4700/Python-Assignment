from datetime import datetime

def DateInRange(sdate, date, edate):
    sdate = datetime.strptime(sdate, "%Y-%m-%d")
    date = datetime.strptime(date, "%Y-%m-%d")
    edate = datetime.strptime(edate, "%Y-%m-%d")
    return sdate <= date <= edate
sdate = "2023-01-01" #start date
date = "2023-01-26"
edate = "2023-12-31" #end date
print(DateInRange(sdate, date, edate))  
