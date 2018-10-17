from flask import Flask
from flask import request
import os
import subprocess

app = Flask(__name__)


@app.route('/api/blogrefresh', methods=['POST'])
def blogrefresh():
   print request.headers
   opt_param = request.headers.get("X-Github-Event")
   if opt_param is None:
      return "Argument not provided"
   else:
      print str(opt_param)
      if str(opt_param) == "push":
         script_path = "~/bin/jekyll_rebuild.sh"
         subprocess.call([os.path.expanduser(script_path)])
         print "success"
      else:
        print "invalid secret"
      return ""
   # script_path = "~/bin/jekyll_rebuild.sh"
   # subprocess.call([os.path.expanduser(script_path)])
   # return "blogrefresh"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


# jekyll_rebuild.sh
#——————————

#!/bin/bash
echo "Pulling latest from Git"
cd ~/ding-dong-app/ && git pull origin master

echo "Building Jekyll Site";
jekyll build --source ~/ding-dong-app/ --destination ~/ding-dong-app/_site/;
echo "Jekyll Site Built";

echo "Copying Site to /var/www/html/";
cp -rf ~/ding-dong-app/_site/* /var/www/html/;
echo "Site Rebuilt Successfully";