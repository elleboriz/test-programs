x_file = (open("C:\\Users\\gmb\\Documents\\mix.txt").read()).replace("\n", ",").split(",")
damain = "@wanadoo.fr"
f_email = lambda email: damain in email
xdomain_email = list(filter(f_email, x_file))
output = []
new_file = open(f"C:\\Users\\gmb\\Documents\\new{damain}.txt", "w")
for i in xdomain_email:
    i = i + '\n'
    output = new_file.write(i)

print("done")






