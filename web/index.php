<html>
<?php
            set_error_handler(
	    function ($severity, $message, $file, $line) {
        	throw new ErrorException($message, $severity, $severity, $file, $line);
	    }
	    );

            require_once("env.php"); 

?>
    <head>
        <title>Books & Readers</title>
    </head>

    <body>
        <h1>Books & Readers</h1>
        <hr/>
 
        <h2>Books</h2>
            <?php
	    try {
            $json = file_get_contents($_ENV['URL_API_BOOKS']);
            $obj = json_decode($json,true);

		foreach ($obj as $index => $value)
		{
		 echo $obj[$index]["name"]; echo " / $"; echo $obj[$index]["price"];
		 echo "<br/>";
		 echo "<br/>";
		}
            } catch (Exception $e) {
		//echo 'Exceção capturada: ',  $e->getMessage(), "\n";
		//echo 'Algo de errado não está certo';	    
            }
            ?>

        <h2>Readers</h2>
            <?php            
	    try {
            $json = file_get_contents($_ENV['URL_API_READERS']);
            $obj = json_decode($json,true);

		foreach ($obj as $index => $value)
		{
		 echo $obj[$index]["name"];
		 echo "<br/>";
		}
            } catch (Exception $e) {
 		//echo 'Exceção capturada: ',  $e->getMessage(), "\n";
		//echo 'Algo de errado não está certo';
	    }
	    ?>
    </body>
<?php 
restore_error_handler();
?>
</html>
