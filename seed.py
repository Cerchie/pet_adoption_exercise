from app import db
from models import Pet

db.drop_all()
db.create_all()

p = Pet(name="Jane", photo_url="", available='True')
p2 = Pet(name="Janet", photo_url="https://assets.petco.com/petco/image/upload/f_auto,q_auto/cathp-092619-img-new-pet-adult-256w-256h-d", available="True")
p3 = Pet(name="Jan", photo_url="", available='False')
db.session.add(p)
db.session.add(p2)
db.session.add(p3)
db.session.commit()
