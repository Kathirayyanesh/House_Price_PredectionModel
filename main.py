import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import streamlit as st 
db = pd.read_csv("Data/Housing_last.csv")
db.head()

db = db.dropna(axis = 0)
X = db.drop("price" , axis=1)
y = db["price"]

#model = GradientBoostingRegressor( n_estimators=200, learning_rate=0.05 , max_depth=3 , random_state=42)
model = LinearRegression()
X_train,X_test, y_train,y_test = train_test_split(X,y , test_size=0.2 , random_state= 10)

model.fit(X_train,y_train)


st.title("House Price Prediction Model ")
st.write("Enter the house detail and press the Predict buttonnnnn")

area    = st.number_input("Area(sq.feet):")
bedroom = st.number_input("No Bedrooms:")
bathroom = st.number_input("No Batrhrooms:")
guestroom = st.number_input("No GuestRooms:")
basement = st.number_input("Basement:")
parking = st.number_input("Parking:")
furnishingstatus = st.number_input("Furnising(0,1,2):")

if st.button("Predict Price "):
    
    features = pd.DataFrame([[area,bedroom,bathroom,guestroom,basement,parking,furnishingstatus]],
    columns=[
    "area",
    "bedrooms",
    "bathrooms",
    "guestroom",
    "basement",
    "parking",
    "furnishingstatus"
    ])

    prediction = model.predict(features)

    st.success(f"Predicted Price : {(prediction)}")