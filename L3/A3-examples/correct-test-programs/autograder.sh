# a=""

# for i in {0..21}
# do
# 	python 150050076-150050096.py t"$i"-correct.c > "$a"
# done

# cd temp

# for i in {0..21}
# do
	
# 	./Parser t"$i"-correct.c > "$a"
# done

# cd ..

for i in {0..21}
do
	diff t"$i"-correct.c.ast temp/t"$i"-correct.c.ast  
	diff t"$i"-correct.c.cfg temp/t"$i"-correct.c.cfg 
done
