from flask import Flask, render_template, request

app = Flask(__name__)

def format_ids_for_sql(input_ids: str) -> str:
    ids_list = input_ids.split()
    formatted_ids = ", ".join(f"'{id}'" for id in ids_list)
    return formatted_ids

@app.route('/', methods=['GET', 'POST'])
@app.route('/sql_format', methods=['GET', 'POST'])
def sql_format():
    formatted_ids = None
    soql_query = None
    input_ids = ''
    custom_query = ''
    
    if request.method == 'POST':
        input_ids = request.form.get('input_ids', '')
        custom_query = request.form.get('custom_query', '')
        if input_ids and custom_query:
            formatted_ids = format_ids_for_sql(input_ids)
            soql_query = custom_query.replace("()", f"({formatted_ids})")
            
    return render_template('index.html', input_ids=input_ids, custom_query=custom_query, soql_query=soql_query)

if __name__ == '__main__':
    app.run(debug=True)
