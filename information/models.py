from django.db import models

class Info(models.Model):
    Name_of_the_Board=models.CharField(max_length=2000)

    appeared_boys=models.IntegerField()
    appeared_girls=models.IntegerField()
    appeared_total=models.IntegerField(blank=True)

    passed_boys=models.IntegerField()
    passed_girls=models.IntegerField()
    passed_total=models.IntegerField(blank=True)

    sc_appeared_boys=models.IntegerField()
    sc_appeared_girls=models.IntegerField()
    sc_appeared_total=models.IntegerField(blank=True)

    sc_passed_boys=models.IntegerField()
    sc_passed_girls=models.IntegerField()
    sc_passed_total=models.IntegerField(blank=True)

    st_appeared_boys=models.IntegerField()
    st_appeared_girls=models.IntegerField()
    st_appeared_total=models.IntegerField(blank=True)

    st_passed_boys=models.IntegerField()
    st_passed_girls=models.IntegerField()
    st_passed_total=models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.id} --> {self.Name_of_the_Board}'
