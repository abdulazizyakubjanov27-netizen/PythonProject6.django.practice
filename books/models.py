from django.db import models


class BookType(models.TextChoices):
    STANDARD = 'standard'
    BADIIY = 'badiiy'
    ILMIY = 'ilmiy'


class Author(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'authors'
        ordering = ['-birth_date']


# id -> primary key-serial,title->varchar(255),description->text,author-varchar,type-> varchar
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=BookType.choices, default=BookType.STANDARD)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'books'
        ordering = ['-created_time']


# CRUD -> INSERT,SELECT,UPDATE,DELETE

"""
sql

insert into authors (first_name, last_name, birth_date) VALUES ("sasas", "sasasa", "2024-2-1");

SELECT * from authors;

UPDATE authors SET first_name = ?, last_name = ?, birth_date = ? where id = ?;

DELETE from authors where id = ?;
"""

"""
python manage.py shell

CRUD

python code -> ORM -> sql ogirib cursor.excute() (database ga yoziladi)
python code SELECT: -> ORM -> sql  cursor.excute()
python object  <- ORM <- sql
"""


class BaseQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db).filter(is_deleted=False)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    objects = DeletedManager()

def delete(self, *args, **kwargs):
    self.is_deleted = True
    self.save()

class AllManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)

