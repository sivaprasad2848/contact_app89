def contact_write(contacts):
    fp=open("contact_details","a")
    for item in contacts:
        line=item[0]+"#"+item[1]+"#"+item[2]+"\n"
        fp.write(line)
    fp.close()