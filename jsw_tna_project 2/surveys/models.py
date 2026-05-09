from django.db import models
from .competencies import ROLE_CHOICES, FUNCTION_CHOICES


class TNAFHQResponse(models.Model):
    """Functional Head Questionnaire — importance + desired proficiency per competency."""
    employee_name = models.CharField(max_length=200)
    employee_code = models.CharField(max_length=100)
    role = models.CharField(max_length=10, default='FH')
    function = models.CharField(max_length=50, choices=FUNCTION_CHOICES)
    designation = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    # JSON: {comp_code: {name, importance, desired_get, desired_mt}}
    competency_ratings = models.JSONField(default=dict)
    # Open questions
    q_critical = models.TextField(blank=True)
    q_gap_risk = models.TextField(blank=True)
    q_ojt = models.TextField(blank=True)
    q_alp = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'FHQ Response'

    def __str__(self):
        return f"{self.employee_name} — {self.get_function_display()} [{self.submitted_at.date()}]"


class TNASelfAssessmentResponse(models.Model):
    """GET / MT Self-Assessment — current proficiency per competency."""
    employee_name = models.CharField(max_length=200)
    employee_code = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    function = models.CharField(max_length=50, choices=FUNCTION_CHOICES)
    date = models.DateField()
    # JSON: {comp_code: {name, current_level}}
    competency_ratings = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Self-Assessment Response'

    def avg_rating(self):
        vals = [v.get('current_level', 0) for v in self.competency_ratings.values() if v.get('current_level')]
        return round(sum(vals) / len(vals), 2) if vals else 0

    def __str__(self):
        return f"{self.employee_name} ({self.role}) — {self.get_function_display()} [{self.submitted_at.date()}]"
