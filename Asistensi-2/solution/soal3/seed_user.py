# Jalankan dari folder soal3:  python manage.py shell -c "exec(open('seed_user.py').read())"
from django.contrib.auth.models import User

user, _ = User.objects.get_or_create(username="regular")
user.set_password("aaaaa")
user.save()
print("OK: regular (password aaaaa)")
