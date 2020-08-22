from forms import *

@app.route('/')
def index():
   form = ContactForm()
   return render_template('contact.html', form=form)


@app.route('/showall')
def showall():
   return render_template('show_all.html', students=students.query.all())



@app.route('/contact', methods=['GET', 'POST'])
def contact():
   form = ContactForm()
   if request.method == 'POST':
      if form.validate() == False:

         return render_template('contact.html', form=form)
      else:
         student = students(request.form['name'], request.form['Gender'],
                            request.form['Address'], request.form['email'], request.form['Age'], request.form['language'])
         db.session.add(student)


         db.session.commit()
         flash('Record was successfully added')
         return render_template('success.html')

   if request.method == 'GET':
      return render_template('contact.html', form=form)

@app.route('/email',methods=['GET', 'POST'])
def email():
   attachment = request.files['file']
   filename = attachment.filename
   print(filename)
   msg = Message('Hello', sender='kuldeep.tb.mali@gmail.com', recipients=['kuldeepmalikm41@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   msg.attach(filename, "image/png", attachment.read())
   mail.send(msg)
   return render_template('success.html')


if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)
