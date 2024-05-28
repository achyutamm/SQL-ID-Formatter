from flask import Flask, render_template, request

app = Flask(__name__)

def format_ids_for_sql(input_ids: str) -> str:
    ids_list = input_ids.split()
    formatted_ids = ", ".join(f"'{id}'" for id in ids_list)
    return formatted_ids

@app.route('/sql_formate', methods=['GET', 'POST'])
def sql_formate():
    formatted_ids = None
    if request.method == 'POST':
        input_ids = request.form['input_ids']
        formatted_ids = format_ids_for_sql(input_ids)
    return render_template('index.html', formatted_ids=formatted_ids)

if __name__ == '__main__':
    app.run(debug=True)
