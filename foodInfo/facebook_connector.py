import fb 

token = "CAACEdEose0cBADrxvLwXZCZAObH78mMqYutLgVsbg1I5sbo18MtKMYJaKzZAlczWC3Atsx7vsViDZCUvaO8g9cn1WCrQlDSsMXlQxJUKlfJgZBEyosZCujtc3uS3Qx48W1BDcaJWMq3aa0iwbQIDLmK25eUky9XvLH0HQi3rKiRmsCdDxC8TNcbZCzyWE9Jhp7ZAklQY6EcTOwZDZD"
facebook=fb.graph.api(token)

data=facebook.get_object(cat="single", id="129511477069092", fields=[ 'events'] )
