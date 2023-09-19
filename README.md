# Инструкция по сборке приожения в контейнер:
<ul>
  <li>Клонировать этот репозиторий - <code>git clone https://github.com/BgPyt/HR_365.git</code></li>
  <li>Создание образа - <code>docker image build -t {name}:{tag} {path dockerfile}</code></li>
  <li>Создание контейнера и запуск - <code>docker run --name {name_container} -p 8000:8000 -d {name_image} </code></li>
</ul>
