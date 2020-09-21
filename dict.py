products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
newproduct = input('Enter product name')
if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
