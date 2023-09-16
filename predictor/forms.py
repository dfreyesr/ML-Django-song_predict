from django import forms

class PredictionForm(forms.Form):
    danceability = forms.FloatField(label='Danceability', min_value=0, max_value=1)
    energy = forms.FloatField(label='Energy', min_value=0, max_value=1)
    key = forms.IntegerField(label='Key', min_value=-1, max_value=11)
    loudness = forms.FloatField(label='Loudness', min_value=-60, max_value=0)
    mode = forms.ChoiceField(label='Mode', choices=[(0, 'Minor'), (1, 'Major')])
    speechiness = forms.FloatField(label='Speechiness', min_value=0, max_value=1)
    acousticness = forms.FloatField(label='Acousticness', min_value=0, max_value=1)
    instrumentalness = forms.FloatField(label='Instrumentalness', min_value=0, max_value=1)
    liveness = forms.FloatField(label='Liveness', min_value=0, max_value=1)
    valence = forms.FloatField(label='Valence', min_value=0, max_value=1)
    tempo = forms.FloatField(label='Tempo')
    time_signature = forms.IntegerField(label='Time Signature', min_value=3, max_value=7)
    duration_min = forms.FloatField(label='Duration (min)') 

    def clean(self):
        cleaned_data = super().clean()
        
        return cleaned_data
