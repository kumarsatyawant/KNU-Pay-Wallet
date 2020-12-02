#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$lgn = "adm_login.htm";

$userid = param("userid");
$passwd = param("pass");

$adm_id = "admin";
$adm_pass = "1234";

# Output the HTTP header
print header ();

print<<EOP; 
	<html>
	<head><title>Admin Login Validation</title>
	<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
	<link rel="stylesheet" href="design.css">
  </head>
	<body class="body_background">
	<div class="sidenav">
		<a href="home.htm">Home</a>
		<a href="contact.htm">Contact</a>
		<a href="services.htm">Services</a>
		<a href="about.htm">About</a> 
	</div>
	</body>
	</html>
EOP

if(($userid eq $adm_id) && ($passwd eq $adm_pass)){
	print<<EOP; 
	<div class="content">
		<h2 class="heading">Welcome to KNU Pay</h2><br>
		<div class="customer_login">
			<a href="adm_real_login.htm"><button class="button button1">Continue</button></a>
			<p>Press <b>Continue</b> button to proceed</p>
		</div>
	</div>
EOP
}
else{
	print<<EOP; 
	<head><title>Input field Validation</title></head>
	<body><div class="content heading_new">
	<h2 class="heading">Welcome to KNU Pay</h2><br> 
	<h2>Incorrect Input</h2>
	<p>Wrong <b>User id and Password</b> combination.</p>
    <p>Please <a href=$lgn>go back</a> and try again.</p></div>
EOP
    exit;
}