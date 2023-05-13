<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "tamil";
#$time=date('h:i:00:00:a');
#echo $time;

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "SELECT * FROM tamil ";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    echo "<tr><td>".$row["word"]."</td></tr>";
  }
}
?>