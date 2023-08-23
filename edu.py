f = open("portfolio.csv")
portfolio = []
for line in f:
    fields = line.split(",")
    name = fields[0]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name, shares, price)
    portfolio.append(stock)
print(portfolio)
