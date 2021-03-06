<html>


 <head>
  <title>Web Scraping Demo Server</title>
 </head>
 <body>
  <h1>SAP</h1>
  <p>Please enter a patient number to lookup</p>
  <p> - </p>

  <p>A link: <a href="http://www.redandgreen.co.uk"> Red and Green </a></p>
	<form action="" method="post">
	<input type="text" name="search">
	<input type="submit" name="submit" value="Search">
	</form>
	<?php
$search=$_POST["search"];
$con=new mysqli("localhost","user3","redandgreen","exampledb");
if($con->connect_error){
    echo 'Connection Failed: '.$con->connect_error;
    }else{
        $sql="select id, pat_num, claim, status FROM patients3 WHERE pat_num like '%{$search}%'";

        $res=$con->query($sql);

        while($row=$res->fetch_assoc()){
            echo 'Patient Number=:'.$row["pat_num"];
            echo "<br>";
            echo 'claim =:'.$row["claim"];
            echo "<br>";
            echo 'stat =:'.$row["status"];
            echo "<br>";
            echo 'id =:'.$row["id"];
 
            }       

        }
?>
 </body>
</html>




