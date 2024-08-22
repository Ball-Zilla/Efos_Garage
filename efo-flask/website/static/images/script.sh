n=1
for file in *.jpg; do
    mv "$file" "img_$n.jpg"
    ((n++))
done
