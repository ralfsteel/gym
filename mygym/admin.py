from django.contrib import admin
from mygym.models import Training, Activity

# Register your models here.
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('user','training_routine', 'date')
    list_filter = ('user', )


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('training','user_set','user_rep')


admin.site.register(Training, TrainingAdmin)
admin.site.register(Activity, ActivityAdmin)