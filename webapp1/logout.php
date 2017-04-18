<?php
$servername = "localhost";
$username = "root";
$password = "passw0rd";
$db="MICROBLOG";
$sessionid = $_SERVER["SESSION_ID"];
$conn=mysqli_connect($servername, $username, $password, $db);

if(!$conn){
  die("Connection failed: ".mysqli_connect_error());
}
$query = "DELETE FROM session where session_hash = '$sessionid';";
mysqli_query($conn,$query);
?>
<html>
<head>
  <title> MircoBlog </title>
  <!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/css/materialize.min.css">
<link rel="stylesheet" type="text/css" href="main.css"/>
<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/js/materialize.min.js"></script>
</head>
<body>
  <nav>
  <div class ="nav-wrapper">
    <a href="#" class="brand-logo right">MicroBlog</a>
    <ul id = "nav-mobile" class = "left hide-on-med-and-down">
      <li>
        <a href="home.php">Home</a>
      </li>
      <li>
        <a href="help.php">Help</a>
      </li>
      <li>
        <a href="about.php">About us</a>
      </li>
      <li>
        <a href="login.php">Login</a>
      </li>
      <li>
        <a href="register.php">Register</a>
      </li>
    </ul>
  </div>
</nav>
Successfully logged out
</body>
</html>
