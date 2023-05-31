import pandas
import numpy
class DataPreparation :
    def __init__(self,path_to_csv) :
        self.data = pandas.read_csv(path_to_csv)
        self.data["index_time"] =  numpy.arange(0,len(self.data) ,1)

    def data_preparation(self) :
        split = int(len(self.data)*0.7)
        moyenne_passagers = numpy.mean(self.data["passengers"])
        æ = numpy.std(self.data["passengers"])
        y_train_ideal =  self.data ["passengers"][: split]
        self.data["passengers"] = (self.data["passengers"] - moyenne_passagers) / æ
        x_train = self.data ["index_time"][: split]
        y_train = self.data ["passengers"][: split]

        x_test = self.data ["index_time"][split :]
        y_test = self.data ["passengers"][split :]
        return x_train,y_train,x_test,y_test,y_train_ideal,moyenne_passagers,æ       
        #print (self.data["passengers"].head())


    