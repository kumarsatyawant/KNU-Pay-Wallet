#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser); 

$firstname = param("firstname");
$lastname = param("lastname");
$email = param("email");
$department = param("department");
$subject = param("subject");

print header ();

print<<EOP; 
<html>
<head><title>Contact</title>
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

print<<EOP; 
	<head><title>Contact Submission</title></head>
	<body><div class="content heading_new"><br>
	<h2>Thank You for contacting us!!</h2>
	<p>We have received your info successfully. Our team will get back to your query soon!!</p>
EOP