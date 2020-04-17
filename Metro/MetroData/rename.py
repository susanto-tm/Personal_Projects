import os

year = 2009
count = 0
for filename in os.listdir("./"):
    if not filename.endswith(".py"):
        if count % 2 == 0:
            year += 1

        os.rename(filename, str(year)+f"_{count % 2 + 1}.csv")
        count += 1
