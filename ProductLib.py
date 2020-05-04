import pickle

class Product:
  def __init__(this, pid, pname, pcat, pprice):
    this.prodId = pid
    this.prodName = pname
    this.category = pcat
    this.price = pprice

class ProductOperations:
    def __init__(this):
        #this.products = []
        try:
            f = open("products.dat", "rb")
            this.products = pickle.load(f)
            f.close()
        except:
            this.products = []
        
    def addProduct(this, prod):
        this.products.append(prod)
        f = open("products.dat", "wb")
        pickle.dump(this.products, f)
        f.close()
    def getProductById(this, id):
        for prod in this.products:
            if(prod.prodId == id):
                return prod;
    def getAllProducts(this):
        return this.products;
    def updateProduct(this, id, prod):
        oldprod = this.getProductById(id)
        oldprod.prodName = prod.prodName
        oldprod.category = prod.category
        oldprod.price = prod.price
        f = open("products.dat", "wb")
        pickle.dump(this.products, f)
        f.close()
    def deleteProduct(this, id):
        prod = this.getProductById(id)
        this.products.remove(prod)
        f = open("products.dat", "wb")
        pickle.dump(this.products, f)
        f.close()
