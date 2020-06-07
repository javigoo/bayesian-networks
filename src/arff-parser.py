#!/usr/bin/env python3

import csv
import pandas
import os
import sys

def divide_dataset(dataset):
    seed = 33543 # Ultimos 5 digitos del DNI de algun miembro del grupo

    atributos = "room_type,neighborhood,reviews,overall_satisfaction,accommodates,bedrooms,price,latitude,longitude"

    training = open(training_file, "w")
    training.write(atributos)
    training.write("Shared room,Eixample,27,4.5,10,1.0,264.0,41.391617,2.162516")
    training.close()

    validation = open(validation_file, "w")
    validation.write(atributos)
    validation.write("Shared room,Sants-Montjuïc,13,4.0,12,1.0,129.0,41.373267999999996,2.170138")
    validation.close()

    # Falta dividir dataset en 2, aletoriamente con la seed. 75% para training y 25% validation

def parse_to_arff(csv_dataset_file):
    # Falta trasformar atributos a valor discreto
    data = pandas.read_csv(csv_dataset_file)
    print("\n",data)

def main():
    divide_dataset(dataset_file)
    parse_to_arff(training_file)
    parse_to_arff(validation_file)

if __name__ == "__main__":
    # Temporal
    print("usage example: ./arff-parser.py barca.csv files-arff/training.arff files-arff/validation.arff")

    if len(sys.argv) < 4:
        sys.exit("Use: %s <csv-dataset-file> <arff-training-file> <arff-validation-file>" % sys.argv[0])

    if not os.path.isfile(sys.argv[1]):
        sys.exit("Error! %s not found" % sys.argv[1])

    dataset_file = os.path.abspath(sys.argv[1])
    training_file = sys.argv[2]
    validation_file = sys.argv[3]

    main()
