from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
# def result(request):
#     data = pd.read_csv(r"E:\Diabetic prediction 2\diabetes.csv")
#     X = data.drop("Outcome", axis=1)
#     Y = data['Outcome']
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#     model = LogisticRegression()
#     model.fit(X_train, Y_train)

#     val1 = float(request.GET['n1'])
#     val2 = float(request.GET['n2'])
#     val3 = float(request.GET['n3'])
#     val4 = float(request.GET['n4'])
#     val5 = float(request.GET['n5'])
#     val6 = float(request.GET['n6'])
#     val7 = float(request.GET['n7'])
#     val8 = float(request.GET['n8'])

#     pared = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

#     result1 = ""
#     if pared == [1]:
#         result1 = "Positive"
#     elif pared == [0]:
#         result1 = 'Negative'

#     return render(request, "predict.html", {"result2": result1})
def result(request):
    try:
        data = pd.read_csv(r"E:\Diabetic prediction 2\diabetes.csv")
        X = data.drop("Outcome", axis=1)
        Y = data['Outcome']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        model = LogisticRegression()
        model.fit(X_train, Y_train)

        val1 = float(request.GET.get('n1', 0))
        val2 = float(request.GET.get('n2', 0))
        val3 = float(request.GET.get('n3', 0))
        val4 = float(request.GET.get('n4', 0))
        val5 = float(request.GET.get('n5', 0))
        val6 = float(request.GET.get('n6', 0))
        val7 = float(request.GET.get('n7', 0))
        val8 = float(request.GET.get('n8', 0))

        pared = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

        result1 = ""
        if pared == [1]:
            result1 = "Positive"
        elif pared == [0]:
            result1 = 'Negative'

        return render(request, "predict.html", {"result2": result1})
    except ValueError:
        error_message = "Invalid input. Please make sure all fields are filled with numeric values."
        return render(request, "predict.html", {"error_message": error_message})
