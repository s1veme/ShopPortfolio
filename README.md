# ShopPortfolio

## Информация

Данный интернет-магазин был написан только для практики. 
В разраработке использовался Django и Vue. 

***

## Установка

Копируем данный репозиторий и переходим в него:
```
git clone https://github.com/s1veme/ShopPortfolio.git
cd ShopPortfolio
```

Устанавливаем `virtualenv` и активируем виртуальное окружение: 
```
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
```

Устанавливаем библиотеки: 
```
pip install -r requirements.txt
```

Далее переходил в папку с Vue и устанавливаем нужне модули:
```
cd frontend
npm install
```

Запускаем Vue в отдельном терминале:
```
npm run serve
```

Возвращаемся в корень проекта и делаем миграции:
```
python manage.py migrate
```

Теперь можно запустить и сам backend:
```
python manage.py runserver
```
