from rest_framework.response import Response
from rest_framework.decorators import api_view
import joblib
from django.conf import settings
from django.shortcuts import render
from .forms import PredictionForm

model = joblib.load(settings.MODEL_PATH)

@api_view(['POST'])
def predict_success(request):
    data = request.data
    
    features = [
        data['danceability'], 
        data['energy'], 
        data['key'], 
        data['loudness'], 
        data['mode'], 
        data['speechiness'],
        data['acousticness'], 
        data['instrumentalness'], 
        data['liveness'], 
        data['valence'], 
        data['tempo'], 
        data['time_signature'], 
        data['duration_min']
    ]
    
    prediction = model.predict([features])
    return Response({"success_potential": prediction[0]})

def predict_form(request):
    form = PredictionForm()
    prediction = None

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = [data[feature] for feature in form.fields]
            prediction = model.predict([features])[0]

    return render(request, 'predict_form.html', {'form': form, 'prediction': prediction})

