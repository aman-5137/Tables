from flask import Flask, request, render_template
# Print the table of any number

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def Table():
    if request.method == 'POST':
        num = request.form.get('num')
        tableList = list()
        for i in range(1, 11):
            tableList.append(f"{num} X {i} = {int(num) * i}")
        return render_template('table.html', tableList = tableList)
    
    return render_template('table.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug = True)
