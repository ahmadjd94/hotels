# hotels

make virtualenv 
```
virtualenv -p python3 env

source env/bin/activate
```

install python requirements 
```
pip3 install -r requirements.txt
```

after installing the requirements prepare the database 

```
cd hotels
python3 manage.py makemigrations hotels
python3 manage.py migrate
python3 manage.py runserver
```
the server will be ran at the port 8000 on local host



next you will need to create providers on the following endpoint

```127.0.0.1:8000/providers```

with the following body  
```
{
	"name":"Best"
}
```

next you you will need to create an hotel by using the following endpoint

```127.0.0.1:8000/providers/1/hotels ```


```
{
    "availability": "2018-10-13",
    "name": "tsest",
    "fare": 321,
    "city": "122",
    "rate": 5,
    "number_of_adults": 10,
    "discount": 0
}

```
create amenities 
```POST 127.0.0.1:8000/hotels/1/amenity
{"name":"new_amenity22"
}

```


you can now try the AvailableHotel,CrazyHotel and BestHotel APIs

```
   GET 127.0.0.1:8000/BestHotel?toDate=2019-01-01&fromDate=2018-01-01&city=JOR&numberOfAdults=2
   GET 127.0.0.1:8000/CrazyHotel?From=2012-01-01&To=2019-01-01&adultsCount=10&city=JOR
   GET 127.0.0.1:8000/AvailableHotel?toDate=2019-01-01&fromDate=2018-01-01&city=JOR&numberOfAdults=10
   ```
