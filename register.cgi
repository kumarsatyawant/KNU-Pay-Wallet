#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser); 

# Output the HTTP header
print header ();

print<<EOP; 
	<html>
	<head><title>Account Creation Update</title>
	<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
	<link rel="stylesheet" href="design.css"></head>
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

$outf =  "register_1.out"; #account and user_name
$intf =  "register_2.out"; #user_name and password
$outf_1 =  "register_3.out"; #user_name and email
$intf_1 =  "register_4.out"; #user_name and name

$lgn = "home.htm";
$rgr = "register.htm";
$lk = "login.htm";

process_form();

sub process_form
{
  if ( validate_form () )
  {
	#Checking password and confirmation password both are same
	pass_match();
	
	#store the record in midterm-1.out
	store_record();
  }
}

sub validate_form
{
  #Fetching the form input
  $account_no = param("account_no");
  $userid = param("user_name");
  $pass = param("pass");
  $Cifmpassword = param("Cifmpassword");
  $email = param("email");
  $fname = param("fname");
  $lname = param("lname");
  
  $full_name = "";
  $full_name .= $fname." ".$lname;

  $error_message = "";
  
  #Checking whether the input field is empty or filled
  #if($account_no eq "" || $user_name eq "" || $password eq "" || $Cifmpassword eq "" || $email eq ""){
	#  $error_message .= "Incomplete Form Input<br>";
  #};
  
  #if ($account_no eq ""){$error_message .= "--Account NO<br>";}
  #if ($userid eq ""){$error_message .= "--User Name<br>";}
  #if ($pass eq ""){$error_message .= "--Password<br>";}
  #if ($Cifmpassword eq ""){$error_message .= "--Password confirmation<br>";}
  #if ($email eq ""){$error_message .= "--Email address<br>";}
  
  if ( $error_message )
  {
	#print error message if the input field is empty
	print<<EOP; 
		<head><title>Form Validation</title></head>
		<body><div class="content heading_new"><br> 
		<h2>Incomplete Input</h2>
		<p>You did not enter<br>
		<p style="color:red">$error_message</p>
		<p>Please <a href=$rgr>go back</a> and try again.</p></div>
EOP
    return 0;
  }
  else
  {
    # Form OK - return success
    return 1;
  }
}

#routine to check the password and confirmation password both are same
sub pass_match
{
	if($pass ne $Cifmpassword)
	{
		print<<EOP; 
		<head><title>Form Validation</title></head>
		<body><div class="content heading_new"><br>
		<h2>Failed password confirmation</h2>
		<p style="color:red">password - $pass configuration_password - $Cifmpassword</p>
		<p>Please <a href=$rgr>go back</a> and try again.</p></div>
EOP
		exit;
	}
}

sub store_record
{
	$count = 0;
	$cnt = 0;
	open(OUT,"$outf") || die "can't read to $outf";
	%hash = split(",", <OUT>);
	close(OUT);
	
	foreach $key (keys %hash) 
	{
		if($key eq $account_no)
		{
			$count++;
		}
	}
	
	foreach $value (values %hash) 
	{
		if($value eq $userid)
		{
			$cnt++;
		}
	}
	
	open(OUT,"$intf") || die "can't read to $intf";
	%hash_pass = split(",", <OUT>);
	close(OUT);
	
	open(OUT,"$outf_1") || die "can't read to $outf_1";
	%hash_email = split(",", <OUT>);
	close(OUT);
	
	open(OUT,"$intf_1") || die "can't read to $intf_1";
	%hash_name = split(",", <OUT>);
	close(OUT);
	
	#open(OUT,"$intf_1") || die "can't read to $intf_1";
	#%hash_pass = split(",", <OUT>);
	#%hash_email = split(",", <OUT>);
	#close(OUT);
	
	if($count > 0)
	{
		#print erroe message if the userid already exists
		print<<EOP; 
		<head><title>ID Validation</title></head>
		<body><div class="content heading_new"><br>
		<h2>Existing Account Numaber</h2>
		<p><b>$account_no</b> not available.</p>
		<p>Please <a href=$rgr>go back</a> and try again or <a href=$lk>Login</a> if already have an account.</div>
EOP
		exit;
	}
	elsif($cnt > 0)
	{
		#print erroe message if the userid already exists
		print<<EOP; 
		<head><title>ID Validation</title></head>
		<body><div class="content heading_new"><br>
		<h2>Existing User Name</h2>
		<p><b>$userid</b> not available.</p>
		<p>Please <a href=$rgr>go back</a> and try again or <a href=$lgn>Login</a>.</div>
EOP
		exit;
	}
	else{
		#Save the record and print confirmation messgae
		$hash{$account_no} = $userid;
		$hash_pass{$userid} = $pass;
		$hash_email{$userid} = $email;
		$hash_name{$userid} = $full_name;
		open(OUT,">$outf") || die "can't write to $outf";
		$, = ",";
		print OUT %hash;
		close(OUT);
		
		open(OUT,">$intf") || die "can't write to $intf";
		$, = ",";
		print OUT %hash_pass;
		close(OUT);
		
		open(OUT,">$outf_1") || die "can't write to $outf_1";
		$, = ",";
		print OUT %hash_email;
		close(OUT);
		
		open(OUT,">$intf_1") || die "can't write to $intf_1";
		$, = ",";
		print OUT %hash_name;
		close(OUT);
		
		print <<EOP;
		<html><head><title>Thank You</title></head>
		<body>
		<div class="content heading_new"><br>
		<h2>UserID Creation Confirmation</h2>
		<p>Congratulation, <b>$full_name!</b> You have successfully created your digital account.
		<p>Your User Name: <b>$userid!</b>.</p>
		<p><a href=$lk>Login</a></p></div>
		</body></html>
EOP
	}
}
