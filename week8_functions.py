# week 8 function

def greet_user(firstname, lastname, age=18):
    print(f"Hello {firstname} {lastname}! {age}");
    
greet_user("Ramazan", "Asri")


def get_formatted_name(firstname, lastname):
    fullname=firstname + ' ' + lastname
    return fullname.title()
          
formatted_name = get_formatted_name("jimi","hendrix")
print(formatted_name)