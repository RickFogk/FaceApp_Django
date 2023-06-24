from django.db import models

class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('other', 'Outros'),
    ]

    DISEASE_CHOICES = [
        ('sjs', 'Stevens-Johnson Syndrome (SJS)'),
        ('ten', 'Toxic Epidermal Necrolysis (TEN)'),
        ('agep', 'Acute Generalized Exanthematous Pustulosis (AGEP)'),
        ('dress', 'Drug Rash with Eosinophilia and Systemic Symptoms (DRESS)'),
        ('dile', 'Drug-induced Lupus Erythematosus (DILE)'),
        ('aad', 'Antibiotic-Associated Diarrhea'),
        ('dih', 'Drug-Induced Hepatitis'),
        ('din', 'Drug-Induced Nephrotoxicity'),
        ('dina', 'Drug-Induced Neutropenia/Agranulocytosis'),
        ('dit', 'Drug-Induced Thrombocytopenia'),
        ('dia', 'Drug-Induced Anemia'),
        ('dip', 'Drug-Induced Parkinsonism'),
        ('dips', 'Drug-Induced Psychosis'),
        ('oih', 'Opioid-Induced Hyperalgesia'),
    ]

    username = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    location = models.CharField(max_length=200)
    primary_disease = models.CharField(max_length=50, choices=DISEASE_CHOICES)
    primary_concern = models.CharField(max_length=200)
    symptom_duration = models.CharField(max_length=200)
    question = models.TextField()
    emotional_state = models.IntegerField()
    consent = models.BooleanField(default=False)
