<!DOCTYPE html>
<html lang="en">
<head>
   <title>Fruit Service</title>
</head>
<body>
   <h1>Welcome to Nick's Fruit Shop</h1>
   <ul>
       <?php
           $json = file_get_contents('http://fruit-service');
           $obj = json_decode($json);
           $fruits = $obj->fruits;
           foreach ($fruits as $fruit){
               echo "<li>$fruit</li>";
           }
       ?>
   </ul>
</body>
</html>