import os
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('/templates'))
template = env.get_template('template.conf')
conf = template.render(NGINX_SSL=os.environ['NGINX_SSL'],
                       DOMAIN=os.environ['DOMAIN'])

with open('/etc/nginx/conf.d/default.conf', 'w') as f:
    f.write(conf)
