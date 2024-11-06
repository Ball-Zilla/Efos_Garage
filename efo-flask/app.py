from website import create_app  # Import the create_app function from the website package (__init__.py)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode on port 5000
