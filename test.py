from src.models.adminmodel import Admin
from src.settings.database import Database
Database().init_db()

username = 'us3wrer023'
password = 'admqr3in123'
email = 'tesrett32q@gmail.com'



admin = Admin.create(username, password, email)
print(admin)