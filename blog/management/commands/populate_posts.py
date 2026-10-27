from blog.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command inserts post data"

    titles = [
    "Introduction to Python",
    "Getting Started with Django",
    "HTML Basics for Beginners",
    "Mastering CSS Fundamentals",
    "JavaScript Essentials",
    "Understanding React",
    "Angular for Web Developers",
    "Introduction to MySQL",
    "Working with Django Models",
    "Python Object-Oriented Programming",
    "Understanding REST APIs",
    "Getting Started with Node.js",
    "Express.js Fundamentals",
    "MongoDB for Beginners",
    "Git and GitHub Basics",
    "Responsive Web Design",
    "Django Templates Explained",
    "Building Forms in Django",
    "Understanding Database Relationships",
    "Deploying Your First Web Application"
    ]

    contents = [
    "Python is a beginner-friendly programming language used for web development, automation, data analysis, and artificial intelligence. Learn about variables, data types, conditions, loops, and functions.",
    "Django is a powerful Python web framework that helps developers build secure and maintainable web applications. Explore project setup, applications, URLs, views, and settings.",
    "HTML provides the structure of web pages using elements such as headings, paragraphs, links, images, and forms. Learn how to create your first web page.",
    "CSS is used to style web pages with colors, spacing, typography, layouts, and animations. Discover selectors, the box model, Flexbox, and Grid.",
    "JavaScript makes websites interactive. Learn variables, functions, arrays, objects, events, DOM manipulation, and asynchronous programming.",
    "React is a JavaScript library for building user interfaces using reusable components. Explore JSX, props, state, hooks, and component rendering.",
    "Angular is a TypeScript-based framework for building dynamic web applications. Learn components, services, dependency injection, routing, and forms.",
    "MySQL is a relational database management system used to store and retrieve structured data. Learn SQL commands, tables, primary keys, and queries.",
    "Django models define the structure of application data and map Python classes to database tables. Learn fields, migrations, and database queries.",
    "Object-oriented programming organizes code using classes and objects. Explore inheritance, encapsulation, polymorphism, constructors, and methods in Python.",
    "REST APIs allow applications to exchange data over HTTP. Learn GET, POST, PUT, PATCH, DELETE, status codes, and JSON responses.",
    "Node.js enables JavaScript to run outside the browser. Discover modules, npm, file handling, asynchronous operations, and server creation.",
    "Express.js is a lightweight Node.js framework for building web servers and APIs. Learn routing, middleware, request handling, and error management.",
    "MongoDB is a document-oriented NoSQL database that stores information in flexible BSON documents. Learn collections, CRUD operations, filtering, and indexing.",
    "Git helps developers track code changes, create branches, and collaborate on projects. Learn commits, merges, pull requests, and essential GitHub workflows.",
    "Responsive web design helps websites adapt to different screen sizes. Explore media queries, flexible layouts, relative units, and mobile-first design.",
    "Django templates generate dynamic HTML pages using variables, tags, filters, and template inheritance. Learn how to pass data from views to templates.",
    "Django forms simplify user input collection and validation. Learn form classes, ModelForms, CSRF protection, error messages, and saving submitted data.",
    "Database relationships connect related records. Understand one-to-one, one-to-many, and many-to-many relationships using practical examples.",
    "Deploying a web application makes it accessible to users online. Learn about environment variables, production settings, static files, database configuration, and hosting."
    ]

    img_urls = [
        f"https://picsum.photos/id/{i}/200/300" for i in range(1, 21)
    ]

    def handle(self, *args, **options):
        for title, content, img_url in zip(self.titles, self.contents, self.img_urls):
            Post.objects.create(title=title, content=content, img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data"))