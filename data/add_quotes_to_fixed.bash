cat $1 | sed 's/l,\"/l,/' | sed 's/\"$//' | sed 's/\"/\"\"/' | sed 's/l,/l,\"/' | sed 's/$/\"/' > $2
#cat $1 | sed 's/\"$/$' > $2;