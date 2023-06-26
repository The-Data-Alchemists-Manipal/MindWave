from django.shortcuts import render
import joblib
import numpy as np

# Create your views here.
def diabetes(request):
    return render(request, 'diabetes.html')

def result_diabetes(request):
    model = joblib.load('diabetes_model.sav')
    lis = []
    lis.append(request.POST['pregnancies'])
    lis.append(request.POST['glucose'])
    lis.append(request.POST['bloodpressure'])
    lis.append(request.POST['skinthickness'])
    lis.append(request.POST['insulin'])
    lis.append(request.POST['bmi'])
    lis.append(request.POST['diabetespedigreefunction'])
    lis.append(request.POST['age'])
    lis = np.array(lis)
    lis = lis.reshape(1, -1)
    ans = model.predict(lis)
    if ans[0] == 1:
        return render(request, 'result_diabetes.html', {'result': 'You have diabetes'})
    else:
        return render(request, 'result_diabetes.html', {'result': 'You do not have diabetes'})
 