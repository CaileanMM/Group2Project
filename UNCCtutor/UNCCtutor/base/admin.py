from django.contrib import admin

# Register your models here.
from .models import User
from .models import Classes
from .models import Review
from .models import Support

admin.site.register(User)

admin.site.register(Classes)

admin.site.register(Review)

admin.site.register(Support)