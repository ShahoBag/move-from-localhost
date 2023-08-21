from encodings import utf_8
import re

# Paste the path to your exported file in open function
with open("D:\\wc-product-export.csv", 'r', encoding="utf_8") as f:
    my_csv_text = f.read()

# In my example I'm moving localhost
find_str = 'http://localhost/example'
replace_str = 'https://example.com'

# Substituting the needed strings
new_csv_str = re.sub(find_str, replace_str, my_csv_text)

# Saving the outcome in a new csv file
new_csv_path = 'D:\\new.csv'
with open(new_csv_path, 'w', encoding="utf8") as f:
    f.write(new_csv_str)

# Now you can import the new.csv file in your wordpress website!