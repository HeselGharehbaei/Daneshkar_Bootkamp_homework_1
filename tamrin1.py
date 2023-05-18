username = input("username=")
password = input("password=")
if username== '"admin"' and password == '"admin"':
    print('"Welcome"')
elif username == '"admin"':
    print('"Wrong Data"')
else:
    print('"Hello<', username, '>"', sep="")
