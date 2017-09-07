A simple test site for user gestures on the Web.

See [crbug.com/760848](https://crbug.com/760848) for the discussion around this.

# Usage

[Public test
site](https://mgiuca.github.io/user-gesture-testing/fetch-gesture.html): This
lets you use the basic test but the fetch handler will return ASAP, rather than
having a delay. To get a time-delayed response, you need to run a local server.

To run a local server, clone this repo, and run:

    $ python3 -m http.server --cgi 8080

Then point your browser at
[http://localhost:8080/fetch-gesture.html](http://localhost:8080/fetch-gesture.html).
