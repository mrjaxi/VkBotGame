<?php
$servername = "localhost";
// Здесь указываем название БД
$dbname = "vkbotgame";
// Указываем имя пользователя
$username = "jordan";
// Указываем пароль
$password = "jordanpie";


 echo "Вы зашли";
// Рекомендуем не изменять данный API-ключ, он должен совпадать с ключом в скетче для платы
$api_key_value = "tPmAT5Ab3j7F9";
$card_id = $position = "";
$result = false;
$status = 0;
 echo "Вы зашлиeee";
  if(!empty($_POST["cardid"]) ){
			echo "1111111111111111";
			$card_id = $_POST["cardid"];
			$position = $_POST["position"];
			echo "222222222";
			 try {
				// Подключение к базе данных
				$db = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
				// Устанавливаем корректную кодировку
				$db->exec("set names utf8");
				// Собираем данные для запроса
				$data = array( 'card_id' => $card_id, 'position' => $position, 'status' => $status ); 
				
				
				$res = $db->query("SELECT count(*) FROM Card WHERE card_id=\"$card_id\"");
				$row = $res->fetch();
				$count = $row[0];
				 
				if($count == 0) {
					 // Подготавливаем SQL-запрос
					$query1 = $db->prepare("INSERT INTO Card (card_id, position, status) values (:card_id, :position, :status)");
					// Выполняем запрос с данными
					$query1->execute($data);	
				 
				}else { 
				// Подготавливаем SQL-запрос
					$query2 = "UPDATE Card SET  position = \"$position\", status = \"$status\" WHERE card_id = \"$card_id\"";
					// Выполняем запрос с данными
					
					$table = $db->prepare($query2);
					//Вставка данных
					$table->execute();
				}



				// Запишим в переменую, что запрос отрабтал
				$result = true;
			} catch (PDOException $e) {
				// Если есть ошибка соединения или выполнения запроса, выводим её
				print "Ошибка!: " . $e->getMessage() . "<br/>";
			}
		
			if ($result) {
					echo "Успех. Информация занесена в базу данных";
					http_response_code(200);
			}
  }



?>
