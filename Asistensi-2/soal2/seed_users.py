# Jalankan dari folder soal2:  python manage.py shell -c "exec(open('seed_users.py').read())"
from django.contrib.auth.models import Group, User

for name in ("regular", "editor", "owner"):
    user, _ = User.objects.get_or_create(username=name)
    user.set_password("aaaaa")
    user.save()
User.objects.get(username="editor").groups.add(Group.objects.get(name="Editor"))
User.objects.get(username="owner").groups.add(Group.objects.get(name="Owner"))
print("OK: regular, editor, owner (password aaaaa)")
