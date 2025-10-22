<!DOCTYPE html>
<html lang="pt-br">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RESULTADO</title>
    </head>

    <body style="background-color: burlywood;">
        
        <?php

            $numero1 =$_POST['numero1'];
            $numero2 =$_POST['numero2'];
            $operacao =$_POST['operacao'];

            switch ($operacao) {
                
                case "+":
                    $resultado = $numero1 + $numero2;
                    break;

                case "-":
                    $resultado = $numero1 - $numero2;
                    break;

                case "*":
                    $resultado = $numero1 * $numero2;
                    break;

                case "/":
                    $resultado = $numero1 / $numero2;
                    break;    

            }
            
            echo "============== RESULTADO ==============<br><br>";
            echo "O RESULTADO É: " .$resultado. '<br>';
            echo "==========================================";
            
        ?>
        
        
    </body>

</html>