Проект делался в PyCharm
1. Выбрать File -> Project from version control
   В открывшемся окне вставить в поле URL ссылку на репозиторий (https://github.com/RaZ3i/TestCase.git)
   В поле Directory выбрать место, куда клонируется репозиторий
2. Создать виртуальное окружение с помощью команды: python -m venv venv
3. Активровать окружение с помощью команды: venv/Scripts/activate
4. Установить зависимости с помощью команды: pip install -r requirements.txt
5. Запустить тесты с помощью команды: pytest -v

1. Для запуска тествого сервера необходимо выбрать интерпертатор.
2. Перейти в main.py, нажать на зеленую стрелочку -> Run 'main'
3. Перейти по ссылке http://127.0.0.1:8000/docs
