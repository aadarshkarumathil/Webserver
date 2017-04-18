<?php
session_start();
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
        <a href="about.php">About us</a>
      </li>
      <li>
        <a href="logout.php">Logout</a>
      </li>
    </ul>
  </div>
</nav>
<form method="post" action ="auth.php">
  <div class ="row">
    <div class = "input-field col s6">
     <label class = "active" >email:</label>
     <input type = "text" name="email", value="" /></p>
   </div>
    <div class = "input-field col s8">
      <label class = "active" >password:</label>
      <input type = "password" name="password", value="" /></p>
    </div>
  </div>
    <input class = "waves-effect waves-light btn" type="submit" value="SUBMIT" />
  </form>
</body>
</html>
