Django signals are a powerful feature that allows decoupled applications to get notified when certain actions occur elsewhere in the framework. They are especially useful for executing some logic in response to certain events, such as saving a model instance, deleting a model instance, or changing a field value.

### Common Use Cases for Django Signals
- Automatically updating related models.
- Sending notifications or emails after certain events.
- Logging or auditing actions.
- Caching updates.

### Built-in Signals

Django provides several built-in signals, such as:

- `pre_save` and `post_save`: Sent before or after a model's `save` method is called.
- `pre_delete` and `post_delete`: Sent before or after a model's `delete` method is called.
- `m2m_changed`: Sent when a ManyToManyField is changed.
- `request_started` and `request_finished`: Sent when an HTTP request is started or finished.

### Example: Using Django Signals

Here’s a step-by-step example demonstrating how to use Django signals:

#### 1. Setting Up the Project

First, ensure you have a Django project set up. If not, you can create one:

```bash
django-admin startproject myproject
cd myproject
django-admin startapp myapp
```

Add the app to your `INSTALLED_APPS` in `settings.py`:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'myapp',
]
```

#### 2. Defining the Models

Create a simple model in `models.py`:

```python
# myapp/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Run the migrations to create the model in the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 3. Creating Signals

Create a file named `signals.py` in your app to define your signal handlers:

```python
# myapp/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Book

@receiver(pre_save, sender=Book)
def before_saving_book(sender, instance, **kwargs):
    print(f"About to save book: {instance.title}")

@receiver(post_save, sender=Book)
def after_saving_book(sender, instance, created, **kwargs):
    if created:
        print(f"Book created: {instance.title}")
    else:
        print(f"Book updated: {instance.title}")
```

#### 4. Connecting Signals

To ensure your signals are connected when the application starts, import the signals module in your app's `apps.py`:

```python
# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals
```

Update the `__init__.py` file to include the AppConfig:

```python
# myapp/__init__.py
default_app_config = 'myapp.apps.MyappConfig'
```

#### 5. Testing Signals

To test the signals, you can use the Django shell:

```bash
python manage.py shell
```

In the shell, create and update some `Book` instances:

```python
from myapp.models import Author, Book

author = Author.objects.create(name='Author 1')
book = Book.objects.create(title='Book 1', author=author)
book.title = 'Updated Book 1'
book.save()
```

You should see the output from the signal handlers in the console.

### Summary

Django signals are a powerful tool for decoupled applications to react to events. This example covers the basics of setting up, defining, and using Django signals to perform actions before and after saving a model instance. Signals can be extended and customized for various use cases, making them a versatile feature in Django development.
