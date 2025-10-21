<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 3 - PHP</title>
</head>
<body>
  
    <h1>Calculando a área de um círculo em PHP</h1>

    <?php
        $raio = 10;
        define("PI", 3.14);
        $area = PI * $raio * $raio;
        echo "A área do círculo de raio {$raio} é: {$area}";
    ?>
    
</body>
</html>
