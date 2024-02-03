from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls) :
        cls.user = get_user_model().objects.create_user(
            username = "testUser" , email ='test@gmail.com' , password ="1234"
        )
        cls.post = Post.objects.create(
            title ='test',
            body = "hello world",
            author = cls.user,
        )
    def test_post_model(self):
        self.assertEqual(self.post.title , 'test')
        self.assertEqual(self.post.body , "hello world")
        self.assertEqual(self.post.author.username , "testUser")
        self.assertEqual(str(self.post),"test")
        self.assertEqual(self.post.get_absolute_url() , '/post/1')

    def tesT_url_exsist_at_current_location_listview(self):
        response = self.client.get("home")
        self.assertEqual(response.status_code , 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code , 200 )
        self.assertTemplateUsed(response , 'blog/home.html')
        self.assertContains(response , 'hello world')

    def tesT_url_exsist_at_current_location_detailview(self):
        response = self.client.get("post_detail")
        self.assertEqual(response.status_code , 200)   
    
    def test_post_detailview(self):
        response = self.client.get(reverse('post_detail' , kwargs={'pk':self.post.pk}))
        no_response = self.client.get("post/10000/")
        self.assertEqual(response.status_code ,200)
        self.assertEqual(no_response.status_code ,404)
        self.assertTemplateUsed(response , "blog/post_detail.html")
        self.assertContains(response , 'hello world')

    def test_post_create_view(self): 
        response = self.client.post(
        reverse("new"),
        {
            "title": "new title",
            "body": "new text",
            "author": self.user.id,
        },
        )
        self.assertEqual(response.status_code ,302)
        self.assertEqual(Post.objects.last().title , "new title")
        self.assertEqual(Post.objects.last().body , "new text")

    def test_post_update_view(self):
        response = self.client.post(reverse("update" , args='1'),{
            "title":"updated title",
            "body":"updated text",
        })
        self.assertEqual(response.status_code ,302)
        self.assertEqual(Post.objects.last().title , 'updated title')
        self.assertEqual(Post.objects.last().body , "updated text")

    def test_post_delete_view(self):
        response = self.client.post(reverse('delete' , args="1"))
        self.assertEqual(response.status_code,302)