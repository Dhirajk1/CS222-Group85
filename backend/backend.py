def signup():
    if(request.method == 'GET'):
        return render_template('signup.html')

    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()

        if user:
            flash('Email has already been used')
            return redirect(url_for('auth.signup'))

        new_user = User(email = email, name=name, password=password)

