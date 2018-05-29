cat $1 | sed 's/,\"htt/,htt/' | sed 's/\"$//' | sed 's/,htt/\,"htt/' | sed 's/$/\"/' > $2
#cat $1 | sed 's/\"$/$' > $2;