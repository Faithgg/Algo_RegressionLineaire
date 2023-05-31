import data_preparation
import linear_regression
print ("Okay")

path_to_csv = "/Users/faithgotglin-dayi/Documents/Projet1_test_Data/number of travelers.csv"
objet = data_preparation.DataPreparation(path_to_csv)
x_train,y_train,x_test,y_test,y_train_ideal,moyenne_passagers,æ = objet.data_preparation()

donnee= linear_regression.LinearRegression(objet)
donnee.get_donnees(x_train,y_train,x_test,y_test  )
donnee.linear_regression()
donnee.entrainement (150000,0.00005)

donnee.visualisation(moyenne_passagers,æ  )
donnee.mse_visualisation()