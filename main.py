import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import streamlit as st 
db = pd.read_csv("Data/Housing_last.csv")
db.head()

db = db.dropna(axis = 0)
X = db.drop(["price", "basement"] , axis=1)
y = db["price"]

#model = GradientBoostingRegressor( n_estimators=200, learning_rate=0.05 , max_depth=3 , random_state=42)
model = LinearRegression()
X_train,X_test, y_train,y_test = train_test_split(X,y , test_size=0.2 , random_state= 10)

model.fit(X_train,y_train)


st.title("House Price Prediction Model ")
st.write("Enter the house detail and press the Predict buttonnnnn")

area    = st.text_input("Area(sq.feet): " , placeholder="Enter the Area")
bedroom = st.text_input("No Bedrooms:", placeholder="Enter the No of Bedrooms")
bathroom = st.text_input("No Batrhrooms:",placeholder="Enter the No of Bathrooms")
guestroom = st.text_input("No GuestRooms:",placeholder="Enter the No of Guestrooms")
parking = st.text_input("Parking:",placeholder="Enter the No of Parking")
furnishingstatus = st.text_input("Furnising(0,1,2):",placeholder="Enter the FurnishingStatus")

if st.button("Predict Price "):
    
    features = pd.DataFrame([[float(area),int(bedroom),int(bathroom),int(guestroom),int(parking),int(furnishingstatus)]],
    columns=[
    "area",
    "bedrooms",
    "bathrooms",
    "guestroom",
    "parking",
    "furnishingstatus"
    ])

    prediction = int(model.predict(features)[0])

    st.success(f"Predicted Price : {(prediction)}")