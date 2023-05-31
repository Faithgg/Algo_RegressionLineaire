import matplotlib.pyplot as plt
import numpy
class LinearRegression :
    def __init__(self, objet):
        self.donnees = objet
        self.a =0
        self.b =0

    def get_donnees (self,x_train,y_train,x_test,y_test) :
        self.x_train,self.y_train,self.x_test,self.y_test = x_train,y_train,x_test,y_test
      
    def linear_regression (self):
        self.predict = lambda x: self.a * x + self.b

        self.mse = lambda x,y : 1/len(x) * sum((self.predict(x_value) - y_value)**2 for x_value,y_value in zip (x,y))


    def entrainement (self,epoch,learning_rate) :
        self.epoch = epoch
        self.mse_values = []
        for i in range(epoch) :
            mse = self.mse (self.x_train,self.y_train)
            self.a = self.a - 2*learning_rate/len(self.x_train) * sum( (self.predict(x_value) - y_value)*x_value for x_value,y_value in zip (self.x_train,self.y_train))
            self.b = self.b - 2*learning_rate/len(self.x_train) * sum( (self.predict(x_value) - y_value) for x_value,y_value in zip (self.x_train,self.y_train))
            if i%5000 == 0 :
                self.mse_values.append(mse)
                print (f"{mse =}, {self.a =},  {self.b =}")


    
    def visualisation (self,moyenne_passagers,æ ) :
        y_ideal = (self.y_train*æ) + moyenne_passagers
        yyyy = (self.predict(self.x_train)*æ) + moyenne_passagers
        plt.figure(figsize=(15,6))
        plt.plot(self.x_train,y_ideal,"b.")
        plt.plot(self.x_train,yyyy,"y-")
        plt.show()
    def mse_visualisation (self ) :
        plt.figure(figsize=(15,6))
        plt.plot(numpy.arange(0,self.epoch,5000),self.mse_values,"r+")
        plt.show()
