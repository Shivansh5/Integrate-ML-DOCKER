X = dataset["YearsExperience"]
X = X.values
X = X.reshape(-1,1)
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_tset = train_test_split(X,y,test_size=0.20,random_state=42)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

def sal_predict():
    exp = float(input("Enter the Exp : "))
    output = model.predict([[exp]])
    print("Predicted Salary is : " , output)

while True:
    choice = input("\n Please type  'Start' to continue to prediction or type 'leave' to end  the prediction: ")
    if choice == "Start":
            sal_predict()
    elif choice == "leave":
            print("Bye")
            break
    else:
            print("\n Please re enter the input")