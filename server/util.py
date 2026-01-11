import json
import pickle
import pandas as pd
import numpy as np

__data_columns = None
__districts = None
__directions = None
__balcony = None
__model = None

def get_district_names():
    return __districts

def get_direction_names():
    return __directions

def get_balcony_names():
    return __balcony

def load_saved_artifacts():

    print("Loading saved artifacts...")

    global __data_columns
    global __directions
    global __districts
    global __model
    global __balcony

    with open('/home/matcry/Documents/AI engineer roadmap/project vietnam housing/model/dataset_columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __districts = [i.replace("District_","") for i in __data_columns if "District_" in i]
        __directions = [i.replace("House direction_","") for i in __data_columns if "House direction_" in i]
        __balcony = [i.replace("Balcony direction_","") for i in __data_columns if "Balcony direction_" in i]

    with open('/home/matcry/Documents/AI engineer roadmap/project vietnam housing/model/vietnam_housing_price.pickle', 'rb') as f:
        __model = pickle.load(f)

    print("Success")
    #print(__balcony)

def get_estimated_price(area, frontage, access_road, floors, bedrooms, bathrooms, _direction, _balcony, _district):
    direction = "House direction_" + _direction
    district = "District_" + _district
    balcony = "Balcony direction_" + _balcony

    #district_index = np.where(X.columns == district)[0][0]
    #direction_index = np.where(X.columns == direction)[0][0]
    x_query = np.zeros(len(__data_columns))
    x_df = pd.DataFrame([x_query], columns=__data_columns)

    x_df['Area'] = area
    x_df['Frontage'] = frontage
    x_df['Access Road'] = access_road
    x_df['Floors'] = floors
    x_df['Bedrooms'] = bedrooms
    x_df['Bathrooms'] = bathrooms
    
    try:
        #district_index = __data_columns.index(district.lower())
        x_df[district] = 1
    except IndexError:
        print(f"Warning: '{district}' not found in training data. Ignoring.")

    try:
        #direction_index = __data_columns.index(direction.lower())
        x_df[direction] = 1
    except IndexError:
        print(f"Warning: '{direction}' not found in training data. Ignoring.")

    try:
        #balcony_index = __data_columns.index(balcony.lower())
        x_df[balcony] = 1
    except IndexError:
        print(f"Warning: '{balcony}' not found in training data. Ignoring.")
        
    
    return round(np.expm1(__model.predict(x_df)[0]), 2)

if __name__ == "__main__":
    load_saved_artifacts()

    print(get_estimated_price(5600, 5, 3, 7, 3, 5, 'Tây - Bắc', 'Nam', 'Đà Lạt'))
    #print(get_district_names())