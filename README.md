# Инструкция по сборке приожения в контейнер:
<ul>
  <li>Клонировать этот репозиторий - <code>git clone https://github.com/BgPyt/HR_365.git</code></li>
  <li>Создание образа - <code>docker image build -t {name}:{tag} {path dockerfile}</code></li>
  <li>Создание контейнера и запуск - <code>docker run --name {name_container} -p 8000:8000 -d {name_image} </code></li>
</ul>

# Документация API (currency_api)
<h3>Request:</h3><code>- http://0.0.0.0:8000/api/rates?from_of={Валюта_из}&to={Валюта_в}&value={Значение}</code><br>



<br>
curl -X 'GET'

'http://0.0.0.0:8000/api/rates?from_of=USD&to=RUB&value=4'<br>
-H 'accept: application/json'

<h3>Responce:</h3>
Response code: 200

Responce body: 

<code>{
  "result": 384.08
}
</code>
<hr>
Response code: 400

Responce body: 

<code>{
  "error": "Bad request"
}
</code>
<h3>Input parameters:</h3>
<table>
<tr><th>№</th><th>Параметр</th><th>Тип данных</th><th>Обязательный</th><th>Описание</th><th>Варианты значений</th></tr> 
<tr><td>1</td><td>from_of</td><td>str</td><td>True</td><td>Валюта из</td><td><code>https://api.coingate.com/v2/rates</code> <-- все курсы валют описаны здесь</td></tr> 
<tr><td>2</td><td>to</td><td>str</td><td>True</td><td>Валюта в</td><td><code>https://api.coingate.com/v2/rates</code> <-- все курсы валют описаны здесь</td></tr> 
<tr><td>2</td><td>value</td><td>int</td><td>True</td><td>Значение</td><td>[1, 2, 3, ...]</td></tr> 
</table>
  


  
