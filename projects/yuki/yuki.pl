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
	chomp $input;
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
	    return 0 if (leave());
	} else {
	    print "Test:$input:\n";
	    print "\nTry again: \n";
	}
    }
}

sub yes_no {
    my $question = shift;
    while(1) {
	print $question . "\n";
	my $input = <>;
	chomp $input;
	$input = lc $input;
#     I copied this off the internet, but I'm not sure how it works, or how to integrate it so. 
	if ($input =~ /^(y|yes|yep|ya|ye|yup|yeah)$/i) {
	    return 1;
	} elsif ($input =~ /^(n|no|nah|na|nope|neh)$/i) {
	    return 0;
	} else {
	    print "yes/no only, please\n"
	}
=begin comment
	if ($input eq "yes" || $input eq "yea" || $input eq "ye" || $input eq "yep" || $input eq "y" || $input eq "yeah" || $input eq "ya" || $input eq "yup") {
	    return 1;
	} elsif ($input eq "no" || $input eq "n" || $input eq "nope" || $input eq "nah" || $input eq "na" || $input eq "neh") {   
	    return 0;
	} else {
	    print "yes/no only, please";
	}
=end comment
=cut
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
	    speak_number::speak_number();
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
    print "It will be lonely without you here,\nbut if you must...";
    return yes_no("Must you?\n");
    if (1) {
	print "Goodbye then. I'm glad you stopped by.\nI hope I'll see you again soon.";
	exit;
    } else {
	print "I'm glad you can stay with me for a little longer.\nWhat would you like to do now?\n"
    }
    
}


