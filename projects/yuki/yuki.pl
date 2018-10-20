#!/usr/bin/env perl
#This is Yuki. She's here to help.
#Please be patient, she's learning.
#girlingoggles made this.
use strict;
use warnings;
use lib "../speak_number/";
use speak_number;


main();


sub main {

    print "Hello\n";
    print "My name is Yuki. I'm here to help.\n";
    # pretty sure perl boolean true is lowercase. or '1'
    # coding convention: add space before {
    while (1) {
	print "Would you like to: \n";
	print "chat\n";
	print "affirmation\n";
	print "math\n";
	print "cake\n";
	print "music\n";
	print "leave\n";
	print "Please choose one: \n";
	my $input = <>;
	$input = lc $input;
    
	if ($input eq "chat") {
	    have_chat();
	} elsif ($input eq "affirmation") {
	    affirmation();
	} elsif ($input eq "math") {
	    do_math();
	} elsif ($input eq "cake") {
	    cake();
	} elsif ($input eq "music") {
	    music();
	} elsif ($input eq "leave") {
	    leave();
	} else {
	    print "\nTry again: \n"
	}
    }
}

sub yes_no {
    while(1) {
	my $input = <>;
	chomp $input;
	$input = lc $input;
```     I copied this off the internet, but I'm not sure how it works, or how to integrate it so. 
	if (/^(y|yes|yep|ya|ye|yup|yeah)$/i) {
	    return 1;
	} elsif (/^(n|no|nah|na|nope|neh)$/i) {
	    return 0;
	} else {
	    print "yes/no only, please\n"
	}
```
	if ($input eq "yes" || $input eq "yea" || $input eq "ye" || $inpute eq "yep" || $input eq "y" || $input eq "yeah" || $input eq "ya" || $input eq "yup") {
	    return 1;
	} elsif ($input eq "no" || $input eq "n" || $input eq "nope" || $input eq "nah" || $input eq "na" || $input eq "neh") {   
	    return 0;
	} else {
	    print "yes/no only, please";
	}
    }
}

sub do_math {
    while (1) {
	print "You can: \n0. go back\n1. do basic math\n2. tell me your favourite number\n3. say a number\nPlease choose 0-3: \n";
	my $input = <>;

#	if ($input eq "1") or ($input eq "1.") or ($input eq "1. "); {
	if (parse_menu_number(1, $input)) {
	    basic_math();
	} elsif ($input eq "2" || $input eq "2." || $input eq "2. ") {
	    favourite_num();
	} elsif ($input eq "3" || $input eq "3." || $input eq "3. ") {
	    speak_number::main();
	    #	   import  speak_number here
	} elsif ($input eq "0" || $input eq "4." || $input eq "4. "){
	    return;
	} else {
	    print "Please choose a number:\n";
	}
	    
    }
}

sub parse_menu_number { 
    my ($num, $input) = @_;
    chomp $input;
    if ($input eq $num || $input eq "$num.") {
	return 1;
    } else {
	return 0;
    }
}
    
sub basic_math {

}

sub favourite_num {

}

sub number_loop {

}

sub have_chat {

}

sub affirmation {

}

sub leave {

}

