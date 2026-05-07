def app(environ, start_response):
    method = environ.get("REQUEST_METHOD", "GET")

    if method == "POST":
        try:
            size = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(size).decode()
            data = body.split("=")[1] if "=" in body else ""

            nums = list(map(int, data.replace("+", " ").split()))
            nums.sort()

            response = f"""
            <html>
            <body>
                <h3>Sorted Numbers:</h3>
                <p>{nums}</p>
                <a href="/">Go back</a>
            </body>
            </html>
            """
        except:
            response = """
            <html>
            <body>
                <h3>Invalid input</h3>
                <a href="/">Go back</a>
            </body>
            </html>
            """

    else:
        response = """
        <html>
        <body>
            <h2>Enter numbers (space separated)</h2>
            <form method="POST">
                <input name="numbers" placeholder="e.g. 5 2 9 1">
                <button type="submit">Sort</button>
            </form>
        </body>
        </html>
        """

    start_response("200 OK", [("Content-Type", "text/html")])
    return [response.encode()]


# For local run or GAE entry
if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8080, app)
    print("Running on http://0.0.0.0:8080")
    server.serve_forever()
