from django.shortcuts import render
from .models import HealthPrediction
from .ml_model import health_agent


def health_predict(request):

    prediction = None
    confidence = None

    if request.method == "POST":

        age = int(request.POST.get("age"))

        gender = request.POST.get("gender")

        height = float(request.POST.get("height"))

        weight = float(request.POST.get("weight"))

        blood_pressure = float(
            request.POST.get("blood_pressure")
        )

        cholesterol = float(
            request.POST.get("cholesterol")
        )


        prediction, confidence = health_agent.predict(
            age,
            gender,
            height,
            weight,
            blood_pressure,
            cholesterol
        )


        HealthPrediction.objects.create(

            age=age,

            gender=gender,

            height=height,

            weight=weight,

            blood_pressure=blood_pressure,

            cholesterol=cholesterol,

            prediction=prediction,

            confidence=confidence

        )


    return render(
        request,
        "healthPredict.html",
        {
            "prediction": prediction,
            "confidence": confidence
        }
    )