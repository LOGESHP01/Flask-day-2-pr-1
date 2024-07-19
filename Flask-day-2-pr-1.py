#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<h1>JUST FUN</h1><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat delectus expedita officia maxime, magnam perferendis nulla natus illum minus. Quasi quibusdam sequi voluptatum distinctio tempore aperiam quo odit saepe! Animi tempora veritatis reiciendis impedit error ipsa cupiditate numquam laborum. Error dolorum reiciendis nulla maiores corrupti, inventore eum obcaecati officia laborum maxime debitis quod cumque, blanditiis, deleniti alias sit distinctio nisi quos accusamus. Atque delectus dignissimos distinctio voluptatum velit autem accusamus ratione veniam. Placeat hic saepe non debitis officia repudiandae obcaecati reiciendis, aliquam corrupti cupiditate sunt eligendi? Perferendis dolor, aut consequatur consequuntur voluptatibus cum fugiat adipisci explicabo quas nisi id ullam?</p>"

if __name__=='__main__':
    app.run(debug=True)