from django.test import TestCase
from .models import Person
class PersonTestCase(TestCase):
    def createPerson(self):
        person = Person.objects.create(name="Person 1")
        self.assertEqual(person.name,"Person 1")

    
    def test_read_person(self):
        Person.objects.create(name="Chris")
        person1 = Person.objects.get(name="Chris")
        self.assertEqual(person1.name, "Chris")
    
    def test_update(self):
        Person.objects.create(name="Chris1")
        person1 = Person.objects.get(name="Chris1")
        person1.name = "Chris1update"
        person1.save()
        self.assertEqual(person1.name, "Chris1update")
    
    def test_delete(self):
        Person.objects.create(name="ChrisToBeDeleted")
        person = Person.objects.get(name="ChrisToBeDeleted")
        person.delete()

        with self.assertRaises(Person.DoesNotExist):
            Person.objects.get(name="ChrisToBeDeleted")
    
# Create your tests here.
