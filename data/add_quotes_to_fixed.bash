cat $1 | sed 's/l,\"/l,/' | sed 's/JS,\"/JS,/' | sed 's/json,\"/json,/' | sed 's/\"$//' | sed 's/\"/\"\"/g' | sed 's/l,/l,\"/' | sed 's/JS,/JS,\"/' | sed 's/json,/json,\"/' | sed 's/$/\"/' > $2
