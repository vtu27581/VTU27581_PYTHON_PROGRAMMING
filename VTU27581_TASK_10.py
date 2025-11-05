import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

Sales_A= (200,250, 300,280, 350, 400)

sales-B=(150, 180, 200,220, 260,300)

sales-C=(100, 150, 180, 200, 230, 250)

Plt. plot (months, sales-A, Label='product A')

plt.plot (months, sales-B, label ='product B')

plt plot (months, sales-C, label= 'product c')

plt.title('monthly sales (line chart)')

PH. Xlabel ('months')

plt. ylabel('sales in units)')

plt. lengd()

plt.grid (True)

plt.show()

products=['product A', 'product B', 'product C')

total-sales-(sum (sales_A), sum(sales- B), sum (sales-c))

Plt. bar (products, total-sales, (Dlor= ('bule', 'green', 'red'))

plt.title('total sales (Bar (chart)')

plt .Xlabel ('products')

plt. Ylabel (' Total sales')

plt.show()

plt .pie (total-sales, labels = products, autoplt = ('%\.if%%.')

Plt.title ('sales percentage (pie chart)')

plt.show()
