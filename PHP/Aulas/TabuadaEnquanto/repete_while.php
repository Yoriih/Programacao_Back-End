<!DOCTYPE html>
<html lang="pt-br">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabuada com While - RESULTADO</title>
    </head>

    <body>
        
    <?php

    if (isset($_POST['numero'])) {

        $numero = $_POST['numero'];

        if (is_numeric($numero)) {
            
            print "<h2>Tabuada do número $numero (usando WHILE)</h2>";

            $i = 1;

            while ($i <= 10) {

                $resultado = $numero * $i;
                print "{$numero} * {$i} = {$resultado} <br>";
                $i++;
            }

        } else {
            print "<p style='color:red;'>Digite um número válido. </p>";
        }

    } else {
        print "<p style='color:red;'>Nenhum número foi enviado.</p>";
    }

    ?>

    </body>

</html>