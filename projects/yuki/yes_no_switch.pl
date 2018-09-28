#!/usr/bin/env perl
use Switch;

sub yes_no {
    my ($question) = @_;

    while (1) {

	print $question;
	my $answer = <STDIN>;
	chomp $answer;
	$answer = lc $answer;
	
	switch ($answer) {
	    case ['y', "yep", "yes", "ya"]  {return true}
	    case ["n", "no", "nope", "nah"] {return false}
	}
	print "Not a valid input. Try again.\n";
    }
}

if ( yes_no("Does this work? ") ) {
    print("Yes\n");
} else {
    print("No\n");
}
