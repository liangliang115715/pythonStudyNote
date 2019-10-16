#_author:
#date:

#配置文件模块
import configparser

config = configparser.ConfigParser()
config["DEAFAULT"]={"ServeAliveInterval":"45",
                    "Compression":"yes",
                    "CompressionLevel":"9"
}
config["bitbucket.org"]={"user":"ll"}

config["topsecret.server.com"]={}
topsecret=config["topsecret.server.com"]
topsecret["Host Port"]="50022"
topsecret["Forwardxll"]="no"
config["DEAFAULT"]["Forwarxll"]="yes"

with open("example.ini","w") as configfile:
	config.write(configfile)
