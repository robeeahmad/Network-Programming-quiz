L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
d = {x:y for x,y in zip(L1, L2)}
print(d)