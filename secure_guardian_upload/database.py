def get_trusted_contanct():
    return{"name":"mom",
           "phone":"xxxxxxxxxxx"}
if __name__=="__main__":
    print("Database module ready.")
    contact=get_trusted_contanct()
    print("Trusted contact:",contact["name"],"-",contact["phone"])