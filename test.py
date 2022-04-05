from datetime import datetime
from travel.user import User
from travel.user import FrequentTraveller
from travel.booking import Booking
from travel.city import City

user1 = User()
user1.register('jill','iueo','jill@y.com')

su = FrequentTraveller()
su.register('jack','iituri', 'jack@x.com',123231)

brisbane = City('Brisbane', 'City in Queensland with a good weather')

st_date = datetime(2019,11,23)
end_date = datetime(2019,11,30)

booking = Booking(st_date,end_date,brisbane,user1)
