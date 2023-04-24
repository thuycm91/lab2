import ruamel.yaml as yaml
import json 

if __name__=="__main__":
    print("yaml working")

    with open ("user.yaml", "r") as stream :
        user_yaml=yaml.safe_load(stream)
    print("Print Type of user_yaml")
    print(type(user_yaml))

    print("-------------")

    for key in user_yaml:
        print (key)
    print("-------------")

    print ("value of key 'id'") 
    print (user_yaml["id"])
    #tuong duong: print ("value of key 'id'", user_yaml['id'])
    print("-------------")
    print ("print address")
    print (user_yaml["address"])
    
    print("-------------")
    adr=user_yaml["address"][0]
    print ("print city")
    print (adr["city"])

    print("--Convert--")
    user_json= json.dumps(user_yaml,default=str, indent=4)
    print("Structure JSON")
    print(user_json)

    file=open("user.json","w")
    file.write(user_json)
    file.close()




    
