#Functions with Outputs
def format_name(f_name, l_name):
  
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  name=formated_f_name+" "+ formated_l_name
  return name


z=format_name("shivam", "kumar")
print(z)