rand_alpha()
{
    cat /dev/urandom | tr -dc 'a-zA-Z' | fold -w ${1:-32} | head -n 1
}

rand_num()
{
    cat /dev/urandom | tr -dc '0-9' | fold -w ${1:-32} | head -n 1
}

rand_alphanum()
{
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w ${1:-32} | head -n 1
}

rand_date()
{
	printf "%0.2d/%0.2d/%0.2d\n" $((1 + RANDOM%29)) $((1 + RANDOM%12)) $((1990 + RANDOM%26))
	#printf "%0.2d/%0.2d/%0.2d\n" $((1 + RANDOM%12)) $((1 + RANDOM%29)) $((1990 + RANDOM%26))
}
