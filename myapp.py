from flask import Flask, render_template, request, escape

def searchletters(phrase:str,letters:str="aeoiu") -> set:
    return set(letters).intersection(set(phrase))
       

app = Flask(__name__)
# @app.route('/')
# def hello() -> str:
#  return redirect('/entry')

def log_request(req: 'flask_request', res: str) -> None:
 with open('vsearch.log', 'a') as log:
  print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
 

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(searchletters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
        the_title=title,
        the_phrase=phrase,
        the_letters=letters,
        the_results=results,)
    
@app.route('/entry')
@app.route('/')
def entry_page() -> 'html':
 return render_template('entry.html',
 the_title='DOS-07 my first flask application!')
 
@app.route('/viewlog')
def view_the_log() -> 'html':
  contents = []
  with open('vsearch.log') as log:
   for line in log:
    contents.append([])
    for item in line.split('|'):
     contents[-1].append(escape(item))
  titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
  return render_template('viewlog.html',
            the_title='View Log',
            the_row_titles=titles,
            the_data=contents,)

# def view_the_log() -> 'str':
#  contents = []
#  with open('vsearch.log') as log:
#   for line in log:
#    contents.append([])
#    for item in line.split('|'):
#     contents[-1].append(escape(item))
#  return str(contents)

# def view_the_log() -> str:
#  with open('vsearch.log') as log:
#   contents = log.readlines()
#   return escape(contents)

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')